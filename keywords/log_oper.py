from exceptions import throw_exception
from get_var import get_var

def and_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]) -> int:
    if len(lexic) <= 2:
        throw_exception(f"You didn`t give enough arguments.", state)

    if not state.is_expr:
        print(f"AND output : {int(get_var(lexic[1], i, full_vars, state, int) and get_var(lexic[2], i, full_vars, state, int))}. Line : {i + 1}")
    else:
        return int(get_var(lexic[1], i, full_vars, state, int) and get_var(lexic[2], i, full_vars, state, int))

def or_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]) -> int:
    if len(lexic) <= 2:
        throw_exception(f"You didn`t give enough arguments.", state)

    if not state.is_expr:
        print(f"OR output : {int(get_var(lexic[1], i, full_vars, state, int) or get_var(lexic[2], i, full_vars, state, int))}. Line : {i + 1}")
    else:
        return int(get_var(lexic[1], i, full_vars, state, int) or get_var(lexic[2], i, full_vars, state, int))

def not_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]) -> int:
    if len(lexic) <= 1:
        throw_exception(f"You didn`t give enough arguments.", state)
    
    if not state.is_expr:
        print(f"NOT output : {int(not get_var(lexic[1], i, full_vars, state, int))}. Line : {i + 1}")
    else:
        return int(not get_var(lexic[1], i, full_vars, state, int))