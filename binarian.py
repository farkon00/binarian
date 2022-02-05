from sys import argv
from time import time

from code_preparer import *
from blocks_parser import *

from keywords import *

from Function import Function

class ExecutionState:
    """Class that contains all data about execution state and constants for execution"""
    def __init__(self, code : str) -> None:
        self.vars = {}
        self.is_expr : bool = False

        self.opened_blocks : int = 0
        self.allowed_blocks : int = 0
        self.opened_ifs : list[tuple[bool, int]] = []

        self.code : str = code
        self.lines : list[str] = code.split("\n")

        self.input_time : int = 0

        self.RESTRICTED_NAMES = ("0", "1", "and", "or", "not", "set", "input", "output", "func", "return", "call")
        self.GLOBAL_FUNCS = {
            "execute_line" : execute_line,
            "execute_expr" : execute_expr
        }

def execute_line(lexic : list[str], i : int, state : ExecutionState, local : dict[str : Function] = None) -> int | None:
    """Executes one keyword"""

    if state.opened_blocks > state.allowed_blocks:
        parse_blocks(" ".join(lexic), state)
        return None

    is_func = local != None
    full_vars = {**state.vars, **(local if is_func else {})}

    for j in range(len(lexic)):
        if lexic[j] in full_vars.keys():
            if not isinstance(full_vars[lexic[j]], Function):
                lexic[j] = str(full_vars[lexic[j]])

    line = parse_blocks(" ".join(lexic), state)
    lexic = line.split()

    if len(lexic) <= 0:
        return None

    if lexic[0] != "else":
        for j in state.opened_ifs:
            if j[1] == state.opened_blocks + 1:
                state.opened_ifs.remove(j)
                break

    match lexic[0]:
        case "set":
            set_keyword(lexic, i, state, local if is_func else state.vars)

        case "input":
            input_keyword(lexic, i, local if is_func else state.vars, state)

        case "output":
            output_keyword(lexic, i, state)

        case "and":
            return and_keyword(lexic, i, state)

        case "or":
            return or_keyword(lexic, i, state)

        case "not":
            return not_keyword(lexic, i, state)

        case "if":
            if_keyword(lexic, i, state)

        case "else":
            else_keyword(lexic, i , state)

        case "func":
            func_keyword(lexic, i, state, local if is_func else state.vars)
        
        case "call":
            state.opened_blocks += 1
            state.allowed_blocks += 1
            return call_keyword(lexic, i, state, full_vars)

        case "return":
            return return_keyword(lexic, i, is_func)


        case _:
            raise NameError(f"Keyword did not found. Line : {i + 1}")


def execute_expr(line : str, i : int, state : ExecutionState, local : dict[str : Function] = None) -> str:
    """Execute one expression"""
    state.is_expr = True

    indexes = parse_expr(line, i)

    if not indexes:
        return line

    start_ind, end_ind = indexes

    lexic = line[start_ind+1:end_ind].split()

    ret = line[:start_ind] + str(execute_line(lexic, i, state, local=local)) + line[end_ind+1:]

    state.is_expr = False

    return ret

def main():
    start_time = time()

    try:
        code = open(argv[1], "r", encoding="utf-8").read().lower()
    except:
        raise FileExistsError("File does not exist.")

    code = delete_comments(code)
    state = ExecutionState(code)

    if code.count("(") != code.count(")"):
        raise SyntaxError('Blocks must have starts and finishes matched with "(" and ")".')

    for i in range(len(state.lines)):

        line = state.lines[i]

        # Expressions executing
        if line.count("{") != line.count("}"):
            raise SyntaxError('Expression must have start and finish matched with "{" and "}". Line : ' + str(i + 1))

        if state.opened_blocks <= state.allowed_blocks:
            while "{" in line:
                line = execute_expr(line, i, state)
            
        
        lexic = line.split()
        if len(lexic) <= 0:
            continue

        execute_line(lexic, i, state)


    if "-d" in argv:
        print("\n" + str(state.vars))

    print(f"\nFinished in {time() - start_time - state.input_time} sec")
        

if __name__ == "__main__":
    main()