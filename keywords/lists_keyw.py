from get_var import get_var
from list import List

def index_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]):
    if len(lexic) <= 2:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

    index = int(get_var(lexic[2], i, full_vars, List))
    list = get_var(lexic[1], i, full_vars, List)
    if index >= len(list):
        raise IndexError(f"Index out of range. Line : {i + 1}")

    if not state.is_expr:
        print(f"INDEX output : {list[index]}. Line : {i + 1}")
    else:
        return list[index]

def len_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]):
    if len(lexic) <= 1:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

    _list = get_var(lexic[1], i, full_vars, List)
    _len = List(list(bin(len(_list)).replace('0b', '')))

    if not state.is_expr:
        print(f"LEN output : {_len}. Line : {i + 1}")
    else:
        return _len

def append_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]):
    if state.is_expr:
        raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

    if len(lexic) <= 2:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

    _list = get_var(lexic[1], i, full_vars, List)
    _object = get_var(lexic[2], i, full_vars)

    _list.append(_object)