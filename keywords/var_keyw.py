from funcs.get_var import get_var
from funcs.exceptions import binarian_assert

def set_keyword(lexic : list[str], state, in_vars : dict[str : object], full_vars : dict[str : object]) -> None:
    # Error handeling
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) < 3, "You didn`t give enough arguments.", state)
    binarian_assert(lexic[1] in state.RESTRICTED_NAMES, "Variable name is unavailable.", state)
    
    in_vars[lexic[1]] = get_var(lexic[2], full_vars, state)

def drop_keyword(lexic : list[str], state, in_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(lexic[1] not in in_vars, "Variable is not found.", state)

    del in_vars[lexic[1]]