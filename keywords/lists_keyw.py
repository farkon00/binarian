from get_var import get_var
from exceptions import *
from list import List

def index_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(len(lexic) <= 2, "You didn`t give enough arguments.", state)

    index = int(get_var(lexic[2], full_vars, state, List))
    list = get_var(lexic[1], full_vars, state, List)

    binarian_assert(index >= len(list), "Index out of range.", state)

    if not state.is_expr:
        print(f"INDEX output : {list[index]}. Line : {state.current_line + 1}")
    else:
        return list[index]

def len_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(len(lexic) <= 1, "You didn`t give enough arguments.", state)

    _list = get_var(lexic[1], full_vars, state, List)
    _len = List(list(bin(len(_list)).replace('0b', '')))

    if not state.is_expr:
        print(f"LEN output : {_len}. Line : {state.current_line + 1}")
    else:
        return _len

def append_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) <= 2, "You didn`t give enough arguments.", state)

    _list = get_var(lexic[1], full_vars, state, List)
    _object = get_var(lexic[2], full_vars, state,)

    _list.append(_object)