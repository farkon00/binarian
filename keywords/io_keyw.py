from time import time

from funcs.get_var import get_var
from funcs.exceptions import binarian_assert, throw_exception
from funcs.utils import is_name_unavailable

def input_keyword(lexic : list[str], in_vars : dict[str : object], state) -> None:
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) < 2, "You didn`t provide a variable name.", state)
    binarian_assert(is_name_unavailable(lexic[1], state), "Variable name is unavailable.", state)

    input_start_time = time()
    try:
        inp = int(input(f"{lexic[1]} : "))
    except:
        throw_exception("This is not an integer.", state)
    state.input_time += time() - input_start_time

    in_vars[lexic[1]] = inp

def output_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) < 3, "You didn`t give enough arguments.", state)

    print(f"{' '.join(lexic[2:])} : {get_var(lexic[1], full_vars, state)}")