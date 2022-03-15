import sys
from time import time

from .code_preparer import *
from .blocks_parser import *
from .exceptions import *

from .keywords import *

class ExecutionState:
    """Class that contains all data about execution state and constants for execution"""
    def __init__(self, code : str) -> None:
        self.vars : dict[str : object] = {"0" : 0, "1" : 1}
        self.is_expr : bool = False

        self.current_line = -1

        self.opened_blocks : int = 0
        self.allowed_blocks : int = 0
        self.opened_ifs : list[tuple[bool, int]] = [] # condition, opened_blocks
        self.opened_loops : list[list[int, int, list[str], int]] = [] # line, opened_block, lines, type
        # Types :
        # 0 - for
        # 1 - while

        self.call_stack : list[tuple[str, int]] = [] # func_name, line
        self.last_return : object = None 

        self.code : str = code
        self.lines : list[str] = code.split("\n")
        self.std_lines : int = 0 # Shold be setted to right value in main 
        self.std_lib_vars : dict[str : object] = {} 

        self.input_time : int = 0

        self.RESTRICTED_NAMES = (
            "0", "1", "and", "or", "not", "set", "drop", "input", "output", "func",
            "return", "call", "index", "len", "append", "zip", "for", "while", "(",
            ")", "[", "]", "{", "}"
        )
        self.GLOBAL_FUNCS = {
            "execute_line" : execute_line,
            "execute_expr" : execute_expr,
            "parse_blocks" : parse_blocks,
            "parse_lists" : parse_lists
        }

def execute_line(lexic : list[str], state : ExecutionState, local : dict[str : object] = None) -> int | None:
    """Executes one keyword"""

    is_func = local != None
    full_vars = {**state.vars, **(local if is_func else {})}

    allowed = state.allowed_blocks
    opened = state.opened_blocks

    line = parse_blocks(" ".join(lexic), state)

    for i in state.opened_loops.copy():
        i[2].append(" ".join(lexic))
        if i[1] > state.opened_blocks:
            state.opened_loops.remove(i)
            if i[3] == 0:
                execute_for(i, state, full_vars, local if is_func else None)
            else:
                execute_while(i, state, full_vars, local if is_func else None)

    if opened > allowed:
        return None

    if len(lexic) <= 0:
        return None

    lexic = line.split()
    lexic = parse_lists(lexic)

    if len(lexic) <= 0:
        return None

    if lexic[0] != "else":
        for j in state.opened_ifs:
            if j[1] == state.opened_blocks + 1:
                state.opened_ifs.remove(j)
                break

    match lexic[0]:
        case "set":
            set_keyword(lexic, state, local if is_func else state.vars, full_vars)

        case "drop":
            drop_keyword(lexic, state, local if is_func else state.vars)

        case "input":
            input_keyword(lexic, local if is_func else state.vars, state)

        case "output":
            output_keyword(lexic, state, full_vars)

        case "and":
            return and_keyword(lexic, state, full_vars)

        case "or":
            return or_keyword(lexic, state, full_vars)

        case "not":
            return not_keyword(lexic, state, full_vars)

        case "index":
            return index_keyword(lexic, state, full_vars)

        case "setindex":
            return setindex_keyword(lexic, state, full_vars)

        case "len":
            return len_keyword(lexic, state, full_vars)

        case "append":
            return append_keyword(lexic, state, full_vars)

        case "zip":
            return zip_keyword(lexic, state, full_vars)

        case "if":
            if_keyword(lexic, state, full_vars)

        case "else":
            else_keyword(lexic, state)

        case "for":
            for_keyword(lexic, state, full_vars)

        case "while":
            while_keyword(lexic, state, full_vars)

        case "func":
            func_keyword(lexic, state, local if is_func else state.vars)

        case "return":
            return return_keyword(lexic, state, is_func, full_vars)


        case _:
            if lexic[0] in full_vars:
                state.opened_blocks += 1
                state.allowed_blocks += 1
                return call_keyword(lexic, state, full_vars)

            throw_exception(f"Keyword or function wasn`t found.", state)


def execute_expr(line : str, state : ExecutionState, local : dict[str : object] = None) -> str:
    """Execute one expression"""
    state.is_expr = True

    indexes = parse_brackets(line, ("{", "}"), state)

    if not indexes:
        state.is_expr = False
        return line

    start_ind, end_ind = indexes

    lexic = line[start_ind+1:end_ind].split()

    ret = line[:start_ind] + str(execute_line(lexic, state, local=local)) + line[end_ind+1:]

    state.is_expr = False

    return ret

def main(test_argv=None):
    start_time = time()

    if test_argv:
        argv = test_argv
    else:
        argv = sys.argv

    try:
        code = open(argv[1], "r", encoding="utf-8").read().lower()
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist.")

    if "-no-std" not in argv:
        try:
            std_lib = open("\\".join(__file__.split("\\")[:-1]) + "\\std.bino", "r", encoding="utf-8").read().lower()
        except FileNotFoundError:
            from .std_lib_code import std_lib_code
            std_lib = std_lib_code.lower()
    else:
        std_lib = ""
        

    code = delete_comments(std_lib + "\n" + code)
    state = ExecutionState(code)
    state.std_lines = std_lib.count("\n") + 1

    binarian_assert(code.count("(") != code.count(")"), 'Blocks must have starts and finishes matched with "(" and ")".', state, display_line=False)

    for i in range(len(state.lines)):
        state.current_line += 1

        if state.current_line == state.std_lines:
            state.std_lib_vars = state.vars.copy()

        line = state.lines[i]

        # Expressions executing
        binarian_assert(line.count("{") != line.count("}"), 'Expression must have start and finish matched with "{" and "}".', state)

        if state.opened_blocks <= state.allowed_blocks:
            while "{" in line:
                line = execute_expr(line, state)

        lexic = line.split()

        execute_line(lexic, state)


    if "-d" in argv:
        debug_vars = list(state.vars.items())
        for i in state.std_lib_vars.items():
            debug_vars.remove(i)
        
        print("\n" + str({i : str(j) for i, j in debug_vars}))

    print(f"\nFinished in {time() - start_time - state.input_time} sec")
        

if __name__ == "__main__":
    main()