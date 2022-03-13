from Function import Function
from get_var import get_var
from exceptions import *

def func_keyword(lexic : list[str], state, in_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(lexic[1] in state.RESTRICTED_NAMES, "Function name is unavailable.", state)
    binarian_assert("(" not in " ".join(lexic), 'Blocks must have starts and finishes matched with "(" and ")".', state)

    parts = " ".join(lexic).split(":")

    func_name = parts[0].split()[1]
    try:
        args = parts[1].split()
    except:
        args = []

    if "(" in args: args.remove("(")
    if ")" in args: args.remove(")")
    if "()" in args: args.remove("()")

    in_vars[func_name] = Function(args, state.current_line)

def call_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    args = lexic[1:]

    func = get_var(lexic[0], full_vars, state, Function, error="Function")


    binarian_assert(len(func.args) != len(args), "You didn`t give enough arguments.", state)

    call_line = state.current_line

    state.call_stack.append((lexic[0], state.current_line))
    state.current_line = func.start_line

    ret = func.execute(args, state, full_vars)

    del state.call_stack[-1]
    state.current_line = call_line

    return ret

def return_keyword(lexic : list[str], state, is_func : bool, full_vars : dict[str : object]):
    binarian_assert(not is_func, 'Keyword "return" is restricted out of functions.', state)

    return get_var(lexic[1], full_vars, state)