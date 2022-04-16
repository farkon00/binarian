from funcs.exceptions import binarian_assert
from funcs.get_var import *

def execute_oper(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(len(lexic) < 3, "Not enought arguments for operation", state)
    arg1 = get_var(lexic[1], full_vars, state, _type=(int, float))
    arg2 = get_var(lexic[2], full_vars, state, _type=(int, float))

    match lexic[0]:
        case "+":  return     arg1 + arg2
        case "-":  return     arg1 - arg2
        case "*":  return     arg1 * arg2
        case "/":  return     arg1 / arg2  
        case "**": return     arg1 ** arg2
        case "%":  return     arg1 % arg2
        case "==": return int(arg1 == arg2)
        case "!=": return int(arg1 != arg2)
        case ">":  return int(arg1 > arg2)
        case "<":  return int(arg1 < arg2)
        case ">=": return int(arg1 >= arg2)
        case "<=": return int(arg1 <= arg2)

    assert False, "Unreachable, operation not found"