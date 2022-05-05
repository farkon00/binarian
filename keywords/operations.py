from funcs.utils import check_args
from funcs.get_var import *

def execute_oper(op : list[str], state, local : dict[str : object]):
    operation = op.args[0]
    orig_args = op.args
    op.args = op.args[1:]
    arg1, arg2 = check_args(op, [int | float, int | float], state, local)
    op.args = orig_args

    match operation:
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