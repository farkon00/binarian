from time import time

from binarian.get_var import get_var
from binarian.exceptions import binarian_assert

def input_keyword(lexic : list[str], in_vars : dict[str : object], state) -> None:
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) < 2, "You didn`t provide a variable name.", state)
    binarian_assert(lexic[1] in state.RESTRICTED_NAMES, "Variable name is unavailable.", state)

    input_start_time = time()
    inp = input(f"{lexic[1]} : ")
    state.input_time += time() - input_start_time
    binarian_assert(inp not in ("0", "1"), "Value must be 0 or 1.", state)
    
    inp = int(inp)

    in_vars[lexic[1]] = inp

def output_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) < 3, "You didn`t give enough arguments.", state)

    print(f"{' '.join(lexic[2:])} : {get_var(lexic[1], full_vars, state)}")