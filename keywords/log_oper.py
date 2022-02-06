from get_var import get_var

def and_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]) -> int:
    if len(lexic) <= 2:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

    if not state.is_expr:
        print(f"AND output : {int(get_var(lexic[1], i, full_vars, int) and get_var(lexic[2], i, full_vars, int))}. Line : {i + 1}")
    else:
        return int(get_var(lexic[1], i, full_vars, int) and get_var(lexic[2], i, full_vars, int))

def or_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]) -> int:
    if len(lexic) <= 2:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

    if not state.is_expr:
        print(f"OR output : {int(get_var(lexic[1], i, full_vars, int) or get_var(lexic[2], i, full_vars, int))}. Line : {i + 1}")
    else:
        return int(get_var(lexic[1], i, full_vars, int) or get_var(lexic[2], i, full_vars, int))

def not_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]) -> int:
    if len(lexic) <= 1:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")
    
    if not state.is_expr:
        print(f"NOT output : {int(not get_var(lexic[1], i, full_vars, int))}. Line : {i + 1}")
    else:
        return int(not get_var(lexic[1], i, full_vars, int))