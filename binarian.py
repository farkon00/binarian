import sys

from code_preparer import prepare_code

from keywords.log_oper import *
from keywords.set_keyw import *
from keywords.io_keyw import *
from keywords.func_keyw import *

from Function import Function

global block_indexes
global code
vars = {}
code : str = None
block_indexes = []

def execute_line(lexic : list[str], i : int, local : dict[str : Function] = None, is_expr=False) -> int | None:

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
            if is_expr:
                raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

            func_keyword(lexic, i, code, local if is_func else vars, block_indexes)
        
        case "call":
            return call_keyword(lexic, i, full_vars)

        case "return":
            return return_keyword(lexic, i, is_func)


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
    global block_indexes
    global code

    try:
        code = open(sys.argv[1], "r", encoding="utf-8").read()
    except:
        raise FileExistsError("File does not exist.")

    code, executable_code, block_indexes = prepare_code(code)

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