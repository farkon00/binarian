from funcs.exceptions import binarian_assert
from funcs.utils import check_args
from bin_types.list import List
from parsing.oper import Oper

def index_keyword(op : Oper, state, local : dict[str : object]):
    list, index = check_args(op, [(List, str), int], state, local)

    binarian_assert(index >= len(list) if index > 0 else abs(index) > len(list), "Index out of range.", state)

    if state.is_expr:
        return list[index]

def setindex_keyword(op : Oper, state, local : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    list, index, val = check_args(op, [List, int, object], state, local)

    binarian_assert(abs(index) -1 if index < 0 else index >= len(list), "Index out of range.", state)

    list[index] = val

def len_keyword(op : Oper, state, local : dict[str : object]):
    _list = check_args(op, [(List, str)], state, local)

    if state.is_expr:
        return len(_list)

def append_keyword(op : Oper, state, local : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    _list, _object = check_args(op, [List, object], state, local)

    _list.append(_object)