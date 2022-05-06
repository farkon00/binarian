from funcs.exceptions import binarian_assert
from funcs.utils import check_args
from bin_types.list import List

def index_keyword(op : list[str], state, local : dict[str : object]):
    list, index = check_args(op, [List | str, int], state, local)

    binarian_assert(index >= len(list) if index > 0 else abs(index) > len(list), "Index out of range.", state)

    if state.is_expr:
        return list[index]

def setindex_keyword(op : list[str], state, local : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    list, index, val = check_args(op, [List, int, object], state, local)

    binarian_assert(abs(index) -1 if index < 0 else index >= len(list), "Index out of range.", state)

    list[index] = val

def len_keyword(op : list[str], state, local : dict[str : object]):
    _list = check_args(op, [List | str], state, local)

    if state.is_expr:
        return len(_list)

def append_keyword(op : list[str], state, local : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    _list, _object = check_args(op, [List, object], state, local)

    _list.append(_object)

def zip_keyword(op : list[str], state, local : dict[str : object]):
    list1, list2 = check_args(op, [List, List], state, local)

    list1 = List(list1 + [0] * (len(list2) - len(list1)))
    list2 = List(list2 + [0] * (len(list1) - len(list2)))

    if state.is_expr:
        return List([List(i) for i in zip(list1, list2)])