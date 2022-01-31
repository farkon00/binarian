import sys
from dataclasses import dataclass

from keywords.log_oper import *
from keywords.set_keyw import *
from keywords.io_keyw import *
from keywords.func_keyw import *

from Function import Function

global vars
global block_indexes
global code
vars = {}
code : str = None
block_indexes = []



def execute_line(lexic : list[str], i : int, local : dict[str : Function] = None, is_expr=False) -> int | None:
    global vars
    global code

    full_vars = vars.copy()
    is_func = local != None

    if is_func:
        full_vars |= local

    for j in range(len(lexic)):
        if lexic[j] in full_vars.keys():
            if not isinstance(full_vars[lexic[j]], Function):
                lexic[j] = str(full_vars[lexic[j]])

    match lexic[0]:
        case "set":
            set_keyword(lexic, i, local if is_func else vars, is_expr, is_func)

        case "input":
            input_keyword(lexic, i, local if is_func else vars, is_expr, is_func)

        case "output":
            output_keyword(lexic, i, is_expr)

        case "and":
            return and_keyword(lexic, i, is_expr)

        case "or":
            return or_keyword(lexic, i, is_expr)

        case "not":
            return not_keyword(lexic, i, is_expr)

        case "func":
            parts = " ".join(lexic).split(":")

            func_name = parts[0].split()[1]
            args = parts[1].split()

            func_index = len("\n".join(code.split("\n")[:i+1]))-1

            # Finding nearest block for tha function
            block = block_indexes[0]
            for j in block_indexes:
                if func_index > j[0]:
                    if j[0] < block[0]:
                        block = j

            if not code[func_index:block[1]].split():
                raise SyntaxError(f"Between nearest block and function declaration code was found. Line : {i+1}")

            func_code = code[block[0]:block[1]]

            if is_func:
                local.append(Function(args, func_code))

            vars[func_name] = Function(args, func_code)
        
        case "call":
            return call_keyword(lexic, i, full_vars)

        case "return":
            check_args((lexic[1]), i)

            # Error handeling
            if not is_func:
                raise SyntaxError(f'Keyword "return" is restricted out of functions. Line : {i + 1}')

            return int(lexic[1])


        case _:
            raise NameError(f"Keyword did not found. Line : {i + 1}")


def expr_read(line : str, i : int, local : dict[str : Function] = None) -> str:
    global vars

    end_ind = line.find("}")
    if end_ind != -1:
        for j in range(end_ind, 0, -1):
            if line[j] == "{":
                start_ind = j
                break
        else: # If for ends without break. That means "}" located before "{"
            raise SyntaxError('Expression must have start and finish matched with "{" and "}". Line : ' + str(i + 1))

    lexic = line[start_ind+1:end_ind].split()
            
    return line.replace(line[start_ind:end_ind] + "}", str(execute_line(lexic, i, is_expr=True, local=local)))

def main():
    global vars
    global block_indexes
    global code

    try:
        code = open(sys.argv[1], "r", encoding="utf-8").read()
    except:
        raise FileExistsError("File does not exist.")

    while "//" in code:
        comm_start = code.find("//")

        if comm_start != -1:
            code = code[:comm_start]

    if "*" in code:
        raise UnicodeEncodeError('Character "*" is restricted in binarian code')

    # Blocks indexes search and deleting non-global scope code from executable
    temp = code
    executable_code = code
    deleted = 0

    if code.count("(") != code.count(")"):
        raise SyntaxError('Functions must have start and finish matched with "(" and ")".')

    while "(" in temp:
        end_ind = temp.find(")")
        if end_ind != -1:
            start_ind = temp[:end_ind].rfind("(")

            if start_ind == -1:
                raise SyntaxError('Functions must have start and finish matched with "(" and ")".')

            temp = temp[:start_ind]  + "{" + temp[start_ind+1:]
            temp = temp[:end_ind]  + "}" + temp[end_ind+1:]

            new_line_count = executable_code[start_ind:end_ind].count("\n")

            executable_code = executable_code[:start_ind] + "*" * (end_ind - start_ind + 1) + executable_code[end_ind+1:]
            executable_code = executable_code[:end_ind] + "\n" * new_line_count + executable_code[end_ind:]

            block_indexes.append((start_ind, end_ind))  

    executable_code = executable_code.replace("*", "")      

    for i in range(len(executable_code.split("\n"))):

        line = executable_code.split("\n")[i].lower()

        while "{" in line:
            if line.count("{") == line.count("}"):
                line = expr_read(line, i)
            else:
                raise SyntaxError('Expression must have start and finish matched with "{" and "}". Line : ' + str(i + 1))
        
        lexic = line.split()
        if len(lexic) <= 0:
            continue

        execute_line(lexic, i)


    if "-d" in sys.argv:
        print("\n" + str(vars))

    print("\nFinished")
        

if __name__ == "__main__":
    main()