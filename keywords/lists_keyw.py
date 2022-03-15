from funcs.get_var import get_var
from funcs.exceptions import binarian_assert
from bin_types.list import List

def index_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(len(lexic) <= 2, "You didn`t give enough arguments.", state)

    index = int(get_var(lexic[2], full_vars, state, List))
    list = get_var(lexic[1], full_vars, state, List)

    binarian_assert(index >= len(list), "Index out of range.", state)

    if not state.is_expr:
        print(f"INDEX output : {list[index]}. Line : {state.current_line - state.std_lines + 1}")
    else:
        return list[index]

def setindex_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) <= 3, "You didn`t give enough arguments.", state)

    list = get_var(lexic[1], full_vars, state, List)
    index = int(get_var(lexic[2], full_vars, state, List))
    val = get_var(lexic[3], full_vars, state)

    binarian_assert(index >= len(list), "Index out of range.", state)

    list[index] = val

def len_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(len(lexic) <= 1, "You didn`t give enough arguments.", state)

    _list = get_var(lexic[1], full_vars, state, List)
    _len = List(list(bin(len(_list)).replace('0b', ''))[::-1])

    if not state.is_expr:
        print(f"LEN output : {_len}. Line : {state.current_line - state.std_lines + 1}")
    else:
        return _len

def append_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) <= 2, "You didn`t give enough arguments.", state)

    _list = get_var(lexic[1], full_vars, state, List)
    _object = get_var(lexic[2], full_vars, state,)

    _list.append(_object)

def zip_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(len(lexic) <= 2, "You didn`t give enough arguments.", state)

    list1 = get_var(lexic[1], full_vars, state, List)
    list2 = get_var(lexic[2], full_vars, state, List)

    list1 = List(list1 + [0] * (len(list2) - len(list1)))
    list2 = List(list2 + [0] * (len(list1) - len(list2)))

    if state.is_expr:
        return List([List(i) for i in zip(list1, list2)])