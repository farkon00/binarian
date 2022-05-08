from bin_types.list import List
from funcs.exceptions import binarian_assert
from funcs.utils import check_args, type_to_str
from parsing.oper import Oper

def execute_oper(op : Oper, state, local : dict[str : object]):
    operation = op.args[0]
    orig_args = op.args
    op.args = op.args[1:]
    types = (int, float, str, List)
    arg1, arg2 = check_args(op, [types, types], state, local)
    op.args = orig_args

    if isinstance(arg1, str | List) or isinstance(arg2, str | List):
        binarian_assert(type(arg1) != type(arg2) and op.args[0] not in state.diff_types_operations, 
            f"Cant perform operation with different types : {type_to_str(type(arg1))} and {type_to_str(type(arg2))}", state
        )
        binarian_assert(operation not in state.iter_operations, 
            f"Cant perform \"{operation}\" on {type_to_str(type(arg1))} and {type_to_str(type(arg2))}", state
        )

    match operation:
        case "+":  return     arg1 + arg2 if not isinstance(arg1, List) else List(arg1 + arg2)
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