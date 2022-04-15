from funcs.get_var import get_var
from funcs.exceptions import binarian_assert
from funcs.utils import is_name_unavailable

def set_keyword(lexic : list[str], state, in_vars : dict[str : object], full_vars : dict[str : object]) -> None:
    # Error handeling
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) < 3, "You didn`t give enough arguments.", state)

    if len(lexic) >= 4:
        binarian_assert(lexic[1] not in state.types, f"Type is not found : {lexic[1]}", state)
        binarian_assert(is_name_unavailable(lexic[2], state), "Variable name is unavailable.", state) 

        in_vars[lexic[2]] = get_var(lexic[3], full_vars, state)
        return

    binarian_assert(is_name_unavailable(lexic[1], state), "Variable name is unavailable.", state)
        
    in_vars[lexic[1]] = get_var(lexic[2], full_vars, state)

def drop_keyword(lexic : list[str], state, in_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    if lexic[1] in in_vars:
        del in_vars[lexic[1]]