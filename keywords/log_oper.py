from funcs.utils import check_args

def and_keyword(op : list[str], state, local : dict[str : object]) -> int:
    arg1, arg2 = check_args(op, [object, object], state, local)

    if state.is_expr:
        return int(arg1 and arg2)

def or_keyword(op : list[str], state, local : dict[str : object]) -> int:
    arg1, arg2 = check_args(op, [object, object], state, local)

    if state.is_expr:
        return int(arg1 or arg2)

def not_keyword(op : list[str], state, local : dict[str : object]) -> int:
    arg = check_args(op, [object], state, local)

    if state.is_expr:
        return int(not arg)