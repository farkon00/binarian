from bin_types.list import List
from funcs.exceptions import binarian_assert
from funcs.utils import type_to_str
from parsing.oper import *

def tc_line2(op : Oper, state):
    """Executes 2 stage of type checking for 1 keyword"""
    is_func = bool(state.opened_function)
    local = state.opened_function.locals if is_func else {}
    full_vars = {**state.vars, **local}

    state.current_line = op.line

    match op.id:
        case OpIds.value:
            return type(op.args[0])
        
        case OpIds.variable:
            if op.args[0] not in full_vars: 
                state.warnings += 1
                return object

            return full_vars[op.args[0]]

        case OpIds.operation:
            exp_type = type_to_str((float, int))
            arg1 = tc_line2(op.args[1], state)
            arg2 = tc_line2(op.args[2], state)

            if arg1 not in (object, None) and op.args[0] not in state.iter_operations:
                binarian_assert(not issubclass(arg1, float | int),
                f"Unexpected operation argument type, {exp_type} was expected, {type_to_str(arg1)} found.", state
                )
            if arg2 not in (object, None) and op.args[0] not in state.iter_operations:
                binarian_assert(not issubclass(arg2, float | int),
                f"Unexpected operation argument type, {exp_type} was expected, {type_to_str(arg2)} found.", state
                )

            if issubclass(arg1, str | List) or issubclass(arg2, str | List):
                binarian_assert(arg1 != arg2 and op.args[0] not in state.diff_types_operations and\
                    arg1 not in (object, None) and arg2 not in (object, None),
                    f"Cant perform operation with different types : {type_to_str(arg1)} and {type_to_str(arg2)}", state
                )
                binarian_assert(op.args[0] not in state.iter_operations, 
                    f"Cant perform \"{op.args[0]}\" on {type_to_str(arg1)} and {type_to_str(arg2)}", state
                )

            # Returns type
            if op.args[0] in state.int_operations:
                return int
            elif op.args[0] in state.float_operations:
                return float
            elif arg1 not in (object, None) and issubclass(arg1 if arg1 else object, float):
                return float
            elif arg2 not in (object, None) and issubclass(arg2 if arg2 else object, float):
                return float
            elif issubclass(tc_line2(op.args[1], state), str) or\
            issubclass(tc_line2(op.args[2], state), str) and\
            op.args[0] in state.iter_operations:
                return str
            elif issubclass(tc_line2(op.args[1], state), List) or\
            issubclass(tc_line2(op.args[2], state), List) and\
            op.args[0] in state.iter_operations:
                return List
            else:
                return int

        case OpIds.var:
            exp = tc_line2(Oper(OpIds.variable, state, op.args[0]), state)
            got = tc_line2(op.args[1], state)
            if exp not in (object, None) and got not in (object, None):
                binarian_assert(not issubclass(got, exp),
                 f"Unmatching types, {type_to_str(exp)} was expected, {type_to_str(got)} found.", state
                )

        case OpIds.convert:
            return op.args[1]

        case OpIds.if_ | OpIds.else_ | OpIds.elif_ | OpIds.while_:
            for i in op.oper:
                tc_line2(i, state)

        case OpIds.for_:
            if is_func:
                local[op.args[0]] = object
            else:
                state.vars[op.args[0]] = object
                
            for i in op.oper:
                tc_line2(i, state)

        case OpIds.func:
            state.opened_function = state.functions[op.args[0]]
            for i in state.opened_function.oper:
                tc_line2(i, state)
            state.opened_function = None

        case OpIds.return_:
            binarian_assert(not is_func, 'Keyword "return" is restricted out of functions.', state)
            exp = state.opened_function.ret
            got = tc_line2(op.args[0], state)
            if exp not in (object, None) and got not in (object, None):
                binarian_assert(
                    not issubclass(got, exp),
                    f"Unexpected return type, {type_to_str(exp)} was expected, {type_to_str(got)} found", state
                )

        case OpIds.call:
            func = op.args[0].args[0]
            if func not in state.functions:
                state.warnings += 1
                return object
            binarian_assert(len(state.functions[func].args) != len(op.args) - 1,
                f"{func} takes {len(state.functions[func].args)} arguments", state)
            for j, i in enumerate(state.functions[func].args):
                exp = i[1]
                got = tc_line2(op.args[j+1], state)
                if exp not in (object, None) and got not in (object, None):
                    binarian_assert(
                        not issubclass(got, exp),
                        f"Unexpected argument type for {i[0]}, {type_to_str(exp)} was expected, {type_to_str(got)} found", state
                    )
            return state.functions[func].ret

        case _:
            if op.id.name in state.keywords:
                keyword = state.keywords[op.id.name]

                for j, i in enumerate(keyword[1:]):
                    exp = i
                    got = tc_line2(op.args[j], state) if exp not in (None, object) else None
                    if exp not in (object, None) and got not in (object, None):
                        binarian_assert(
                            not issubclass(got, exp),
                            f"Unexpected argument type, {type_to_str(exp)} was expected, {type_to_str(got)} found", state
                        )

                return keyword[0]

            state.warnings += 1