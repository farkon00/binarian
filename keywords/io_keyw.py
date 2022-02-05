from time import time

from .check_args import check_args

def input_keyword(lexic : list[str], i : int, in_vars : dict[str : int], state) -> None:
    if state.is_expr:
        raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

    # Error handeling
    if len(lexic) >= 2:
        if lexic[1] not in ("0", "1", "and", "or", "not", "set", "input", "output"):
            input_start_time = time()
            inp = input(f"{lexic[1]} : ")
            state.input_time += time() - input_start_time
            if inp not in ("0", "1"): 
                raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
        else:
            raise NameError(f"Variable name is unavailable. Line : {i + 1}")
    else:
        raise ValueError(f"You didn`t provide a variable name. Line : {i + 1}")
    
    inp = int(inp)

    in_vars[lexic[1]] = inp

def output_keyword(lexic : list[str], i : int, state):
    if state.is_expr:
        raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

    check_args((lexic[1]), i)

    # Error handeling
    if len(lexic) < 3:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

    print(f"{lexic[2]} : {int(lexic[1])}")