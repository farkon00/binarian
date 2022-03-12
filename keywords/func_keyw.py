from Function import Function
from get_var import get_var
from exceptions import throw_exception

def func_keyword(lexic : list[str], state, in_vars : dict[str : int]):
    if state.is_expr:
        throw_exception(f"This operation is unavailable in expressions.", state)
    if lexic[1] in state.RESTRICTED_NAMES:
        throw_exception(f"Function name is unavailable.", state)
    if "(" not in " ".join(lexic):
        throw_exception(f'Blocks must have starts and finishes matched with "(" and ")".', state)

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

def call_keyword(lexic : list[str], state, full_vars : dict[str : int]):
    args = lexic[2:]

    func = get_var(lexic[1], full_vars, state, Function, error="Function")


    if len(func.args) != len(args):
        throw_exception(f"You didn`t give enough arguments.", state)

    call_line = state.current_line

    state.call_stack.append((lexic[1], state.current_line))
    state.current_line = func.start_line

    ret = func.execute(args, state, full_vars)

    del state.call_stack[-1]
    state.current_line = call_line

    return ret

def return_keyword(lexic : list[str], state, is_func : bool, full_vars : dict[str : int]):
    # Error handeling
    if not is_func:
        throw_exception(f'Keyword "return" is restricted out of functions.', state)

    return get_var(lexic[1], full_vars, state)