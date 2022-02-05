from .check_args import check_args

def set_keyword(lexic : list[str], i : int, state, in_vars : dict[str : int]) -> None:
    if state.is_expr:
        raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

    # Error handeling
    if len(lexic) >= 3:
        if lexic[1] not in ("0", "1", "and", "or", "not", "set", "input", "output"): # TODO : Move this tuple to constant
            try:
                set_val = int(lexic[2])
            except ValueError:
                raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")

            if set_val not in (0, 1):
                raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
        else:
            raise NameError(f"Variable name is unavailable. Line : {i + 1}")
    else:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")
    
    in_vars[lexic[1]] = int(lexic[2])