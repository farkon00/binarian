from sys import argv

from code_preparer import *
from blocks_parser import *

from keywords.log_oper import *
from keywords.set_keyw import *
from keywords.io_keyw import *
from keywords.func_keyw import *

from Function import Function

vars = {}

code : str = ""

def execute_line(lexic : list[str], i : int, opened_blocks : int, allowed_blocks : int, local : dict[str : Function] = None, is_expr=False) -> tuple[int, int, int] | tuple[int, int]:

    if opened_blocks > allowed_blocks:
        opened_blocks, allowed_blocks = parse_blocks(" ".join(lexic), opened_blocks, allowed_blocks)
        return opened_blocks, allowed_blocks

    is_func = local != None
    full_vars = {**vars, **(local if is_func else {})}

    for j in range(len(lexic)):
        if lexic[j] in full_vars.keys():
            if not isinstance(full_vars[lexic[j]], Function):
                lexic[j] = str(full_vars[lexic[j]])

    opened_blocks, allowed_blocks = parse_blocks(" ".join(lexic), opened_blocks, allowed_blocks)

    if is_func and opened_blocks < 0:
        opened_blocks = allowed_blocks = 0
        return opened_blocks, allowed_blocks

    match lexic[0]:
        case "set":
            set_keyword(lexic, i, local if is_func else vars, is_expr, is_func)
            return opened_blocks, allowed_blocks

        case "input":
            input_keyword(lexic, i, local if is_func else vars, is_expr, is_func)
            return opened_blocks, allowed_blocks

        case "output":
            output_keyword(lexic, i, is_expr)
            return opened_blocks, allowed_blocks

        case "and":
            return opened_blocks, allowed_blocks, and_keyword(lexic, i, is_expr)

        case "or":
            return opened_blocks, allowed_blocks, or_keyword(lexic, i, is_expr)

        case "not":
            return opened_blocks, allowed_blocks, not_keyword(lexic, i, is_expr)

        case "func":
            func_keyword(lexic, i, code, local if is_func else vars, is_expr)
            return opened_blocks, allowed_blocks
        
        case "call":
            opened_blocks += 1
            allowed_blocks += 1
            return call_keyword(lexic, i, code, opened_blocks, allowed_blocks, full_vars)

        case "return":
            return opened_blocks, allowed_blocks, return_keyword(lexic, i, is_func)


        case _:
            raise NameError(f"Keyword did not found. Line : {i + 1}")


def execute_expr(line : str, i : int, opened_blocks : int, allowed_blocks : int, local : dict[str : Function] = None) -> str:
    global vars

    indexes = parse_expr(line, i)

    if not indexes:
        return line

    start_ind, end_ind = indexes

    lexic = line[start_ind+1:end_ind].split()

    opened_blocks, allowed_blocks, replacement = execute_line(lexic, i, opened_blocks, allowed_blocks, is_expr=True, local=local)

    return opened_blocks, allowed_blocks, line.replace(line[start_ind:end_ind] + "}",
    str(replacement))

def main():
    global code

    try:
        code = open(argv[1], "r", encoding="utf-8").read().lower()
    except:
        raise FileExistsError("File does not exist.")

    #code, executable_code, block_indexes = prepare_code(code) # TODO : remove this after implomenting new brackets parsing algorithm 
    code = delete_comments(code)
    opened_blocks = allowed_blocks = 0

    for i in range(len(code.split("\n"))):

        line = code.split("\n")[i]

        # Expressions executing
        if line.count("{") != line.count("}"):
            raise SyntaxError('Expression must have start and finish matched with "{" and "}". Line : ' + str(i + 1))

        if opened_blocks <= allowed_blocks:
            while "{" in line:
                opened_blocks, allowed_blocks, line = execute_expr(line, i, opened_blocks, allowed_blocks)
            
        
        lexic = line.split()
        if len(lexic) <= 0:
            continue

        opened_blocks, allowed_blocks = execute_line(lexic, i, opened_blocks, allowed_blocks)[:2]


    if "-d" in argv:
        print("\n" + str(vars))

    print("\nFinished")
        

if __name__ == "__main__":
    main()