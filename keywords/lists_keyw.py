from get_var import get_var
from exceptions import throw_exception
from list import List

def index_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]):
    if len(lexic) <= 2:
        throw_exception(f"You didn`t give enough arguments.", state)

    index = int(get_var(lexic[2], i, full_vars, state, List))
    list = get_var(lexic[1], i, full_vars, state, List)
    if index >= len(list):
        throw_exception(f"Index out of range.", state)

    if not state.is_expr:
        print(f"INDEX output : {list[index]}. Line : {i + 1}")
    else:
        return list[index]

def len_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]):
    if len(lexic) <= 1:
        throw_exception(f"You didn`t give enough arguments.", state)

    _list = get_var(lexic[1], i, full_vars, state, List)
    _len = List(list(bin(len(_list)).replace('0b', '')))

    if not state.is_expr:
        print(f"LEN output : {_len}. Line : {i + 1}")
    else:
        return _len

def append_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]):
    if state.is_expr:
        throw_exception(f"This operation is unavailable in expressions.", state)

    if len(lexic) <= 2:
        throw_exception(f"You didn`t give enough arguments.", state)

    _list = get_var(lexic[1], i, full_vars, state, List)
    _object = get_var(lexic[2], i, full_vars, state,)

    _list.append(_object)