from get_var import get_var
from exceptions import throw_exception

def set_keyword(lexic : list[str], state, in_vars : dict[str : int], full_vars) -> None:
    if state.is_expr:
        throw_exception(f"This operation is unavailable in expressions.", state)

    # Error handeling
    if len(lexic) >= 3:
        if lexic[1] in state.RESTRICTED_NAMES:
            throw_exception(f"Variable name is unavailable.", state)
    else:
        throw_exception(f"You didn`t give enough arguments.", state)
    
    in_vars[lexic[1]] = get_var(lexic[2], full_vars, state)

def drop_keyword(lexic : list[str], state, in_vars : dict[str : int]):
    if state.is_expr:
        throw_exception(f"This operation is unavailable in expressions.", state)
    if lexic[1] not in in_vars:
        throw_exception(f"Variable is not found.", state)

    del in_vars[lexic[1]]