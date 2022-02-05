from .check_args import check_args

def and_keyword(lexic : list[str], i : int, state) -> int:
    if len(lexic) <= 2:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

    check_args((lexic[1], lexic[2]), i)

    if not state.is_expr:
        print(f"AND output : {int(int(lexic[1]) and int(lexic[2]))}. Line : {i + 1}")
    else:
        return int(int(lexic[1]) and int(lexic[2]))

def or_keyword(lexic : list[str], i : int, state) -> int:
    if len(lexic) <= 2:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

    check_args((lexic[1], lexic[2]), i)

    if not state.is_expr:
        print(f"OR output : {int(int(lexic[1]) or int(lexic[2]))}. Line : {i + 1}")
    else:
        return int(int(lexic[1]) or int(lexic[2]))

def not_keyword(lexic : list[str], i : int, state) -> int:
    if len(lexic) <= 1:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

    check_args((lexic[1]), i)
    
    if not state.is_expr:
        print(f"NOT output : {int(not int(lexic[1]))}. Line : {i + 1}")
    else:
        return int(not int(lexic[1]))