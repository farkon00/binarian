from typing import Iterable
from bin_types.function import Function
from funcs.get_var import get_var
from funcs.exceptions import binarian_assert
from funcs.utils import is_name_unavailable, check_args

def func_keyword(op : list[str], state, in_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    in_vars[op.args[0]] = Function(op)

def call_keyword(op : list[str], state, local : dict[str : object]):
    func = check_args(op, [Function], state, local)
    if isinstance(func, Iterable):
        args = func[1:]
        func = func[0]
    else:
        args = []

    binarian_assert(len(func.args) > len(args), f"You didn`t give enough arguments, {len(func.args)} was expected.", state)
    binarian_assert(len(func.args) < len(args), f"You gave too much arguments, {len(func.args)} was expected.", state)

    call_line = state.current_line

    state.call_stack.append((func.name, state.current_line))

    ret = func.execute(args, state)

    del state.call_stack[-1]
    state.current_line = call_line

    return ret

def return_keyword(op : list[str], state, is_func : bool, local : dict[str : object]):
    binarian_assert(not is_func, 'Keyword "return" is restricted out of functions.', state)

    state.last_return = check_args(op, [object], state, local)