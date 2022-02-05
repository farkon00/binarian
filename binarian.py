from sys import argv

from code_preparer import *
from blocks_parser import *

from keywords.log_oper import *
from keywords.set_keyw import *
from keywords.io_keyw import *
from keywords.func_keyw import *

from Function import Function

class ExecutionState:
    def __init__(self, code : str) -> None:
        self.vars = {}
        self.is_expr : bool = False

        self.opened_blocks : int = 0
        self.allowed_blocks : int = 0

        self.code : str = code
        self.lines : list[str] = code.split("\n")

        self.global_funcs = {
            "execute_line" : execute_line,
            "execute_expr" : execute_expr
        }

def execute_line(lexic : list[str], i : int, state : ExecutionState, local : dict[str : Function] = None) -> int | None:

    if state.opened_blocks > state.allowed_blocks:
        parse_blocks(" ".join(lexic), state)
        return None

    is_func = local != None
    full_vars = {**state.vars, **(local if is_func else {})}

    for j in range(len(lexic)):
        if lexic[j] in full_vars.keys():
            if not isinstance(full_vars[lexic[j]], Function):
                lexic[j] = str(full_vars[lexic[j]])

    parse_blocks(" ".join(lexic), state)

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

        case "func":
            func_keyword(lexic, i, state, local if is_func else state.vars)
        
        case "call":
            state.opened_blocks += 1
            state.allowed_blocks += 1
            return call_keyword(lexic, i, state, full_vars)

        case "return":
            return return_keyword(lexic, i, is_func)


        case _:
            print("")

            raise NameError(f"Keyword did not found. Line : {i + 1}")


def execute_expr(line : str, i : int, state : ExecutionState, local : dict[str : Function] = None) -> str:
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
    try:
        code = open(argv[1], "r", encoding="utf-8").read().lower()
    except:
        raise FileExistsError("File does not exist.")

    code = delete_comments(code)
    state = ExecutionState(code)

    if code.count("(") != code.count(")"):
        raise SyntaxError('Blcoks must have starts and finishes matched with "(" and ")". Line : ')

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

    print("\nFinished")
        

if __name__ == "__main__":
    main()