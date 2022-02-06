from get_var import get_var

def set_keyword(lexic : list[str], i : int, state, in_vars : dict[str : int], full_vars) -> None:
    if state.is_expr:
        raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

    # Error handeling
    if len(lexic) >= 3:
        if lexic[1] in state.RESTRICTED_NAMES:
            raise NameError(f"Variable name is unavailable. Line : {i + 1}")
    else:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")
    
    in_vars[lexic[1]] = get_var(lexic[2], i, full_vars, int)

def drop_keyword(lexic : list[str], i : int, state, in_vars : dict[str : int]):
    if state.is_expr:
        raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")
    if lexic[1] not in in_vars:
        raise NameError(f"Variable is not found. Line : {i + 1}")

    del in_vars[lexic[1]]