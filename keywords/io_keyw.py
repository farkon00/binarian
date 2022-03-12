from time import time

from get_var import get_var
from exceptions import throw_exception

def input_keyword(lexic : list[str], in_vars : dict[str : int], state) -> None:
    if state.is_expr:
        throw_exception(f"This operation is unavailable in expressions.", state)

    # Error handeling
    if len(lexic) >= 2:
        if lexic[1] not in state.RESTRICTED_NAMES:
            input_start_time = time()
            inp = input(f"{lexic[1]} : ")
            state.input_time += time() - input_start_time
            if inp not in ("0", "1"): 
                throw_exception(f"Value must be 0 or 1.", state)
        else:
            throw_exception(f"Variable name is unavailable.", state)
    else:
        throw_exception(f"You didn`t provide a variable name.", state)
    
    inp = int(inp)

    in_vars[lexic[1]] = inp

def output_keyword(lexic : list[str], state, full_vars : dict[str : int]):
    if state.is_expr:
        throw_exception(f"This operation is unavailable in expressions.", state)

    # Error handeling
    if len(lexic) < 3:
        throw_exception(f"You didn`t give enough arguments.", state)

    print(f"{' '.join(lexic[2:])} : {get_var(lexic[1], full_vars, state)}")