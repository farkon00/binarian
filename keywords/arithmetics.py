from funcs.exceptions import binarian_assert
from funcs.get_var import *

def arithmetics(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(len(lexic) < 3, "Not enought arguments for arithmetical operation", state)
    arg1 = get_var(lexic[1], full_vars, state, _type=(int, float))
    arg2 = get_var(lexic[2], full_vars, state, _type=(int, float))

    if lexic[0] == "+":
        return arg1 + arg2

    elif lexic[0] == "-":
        return arg1 - arg2

    elif lexic[0] == "*":
        return arg1 * arg2

    elif lexic[0] == "/":
        return arg1 / arg2