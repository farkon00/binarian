from bin_types.function import Function
from funcs.get_var import get_var
from funcs.exceptions import binarian_assert
from funcs.utils import is_name_unavailable, check_args

def func_keyword(lexic : list[str], state, in_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert("{" not in " ".join(lexic), 'Blocks must have starts and finishes matched with "{" and "}".', state)

    parts = " ".join(lexic).split(":", 1)

    if (len(parts[0].split()) >= 3 and len(parts) >= 2) or (len(parts[0].split()) >= 4 and len(parts) == 1):
        binarian_assert(parts[0].split()[1] not in state.types, f"Type is not found : {parts[0].split()[1]}", state)
        func_name = parts[0].split()[2]
    else:
        func_name = parts[0].split()[1]

    binarian_assert(is_name_unavailable(func_name, state), "Function name is unavailable.", state)

    try:
        args = parts[1].split(",")
    except:
        args = []

    temp = []
    for i in args:
        i = i.replace("{", "")
        i = i.replace("}", "")
        i = i.strip()

        if ":" in i:
            arg = i.split(":")
            arg = [arg[0].strip(), arg[1].strip()]
            binarian_assert(arg[1] not in state.types, f"Type is not found : {arg[1]}", state)

            temp.append(arg[0])
        else:
            temp.append(i)

        binarian_assert(is_name_unavailable(temp[-1], state), f"Argument name is unavailable : {temp[-1]}", state)

    args = temp
    del temp


    if "{" in args: args.remove("{")
    if "}" in args: args.remove("}")
    if "{}" in args: args.remove("{}")

    in_vars[func_name] = Function(args, state.current_line)

def call_keyword(op : list[str], state, local : dict[str : object]):
    func = check_args(op, [Function], state, local)
    args = func[1:]
    func = func[0]

    binarian_assert(len(func.args) > len(args), f"You didn`t give enough arguments, {len(func.args)} was expected.", state)
    binarian_assert(len(func.args) < len(args), f"You gave too much arguments, {len(func.args)} was expected.", state)

    call_line = state.current_line

    state.call_stack.append((op[0], state.current_line))
    state.current_line = func.start_line

    ret = func.execute(args, state)

    del state.call_stack[-1]
    state.current_line = call_line

    return ret

def return_keyword(op : list[str], state, is_func : bool, local : dict[str : object]):
    binarian_assert(not is_func, 'Keyword "return" is restricted out of functions.', state)

    state.last_return = check_args(op, [object], state, local)