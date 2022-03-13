from get_var import get_var
from exceptions import throw_exception
from list import List

def for_keyword(lexic : list[str], state, full_vars : dict[str  : object]):
    if state.is_expr:
        throw_exception(f"This operation is unavailable in expressions.", state)
    if len(lexic) <= 3:
        throw_exception(f"You didn`t give enough arguments.", state)
    if lexic[1] in state.RESTRICTED_NAMES:
        throw_exception(f"Variable name is unavailable.", state)
    if "(" not in " ".join(lexic):
        throw_exception(f'Blocks must have starts and finishes matched with "(" and ")".', state)
    get_var(lexic[2], full_vars, state, List) # Checks for errors in list

    state.opened_fors.append([state.current_line, state.opened_blocks, []])