from bin_types.function import Function
from bin_types.list import List
from parsing.oper import OpIds, Oper
from .tc_types import TypeCheckedFunction

def tc_line1(op : Oper, state):
    """Executes 1 stage of type checking for 1 keyword"""
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
            if op.args[0] in state.int_operations:
                return int
            elif op.args[0] in state.float_operations:
                return float
            elif issubclass(tc_line1(op.args[1], state), float) or\
            issubclass(tc_line1(op.args[2], state), float):
                return float
            elif issubclass(tc_line1(op.args[1], state), str) or\
            issubclass(tc_line1(op.args[2], state), str) and\
            op.args[0] in state.iter_operations:
                return str
            elif issubclass(tc_line1(op.args[1], state), List) or\
            issubclass(tc_line1(op.args[2], state), List) and\
            op.args[0] in state.iter_operations:
                return List
            else:
                return int

        case OpIds.var:
            if is_func:
                if op.types:
                    local[op.args[0]] = op.types[0]
                elif local.get(op.args[0], None) in (None, object):
                    local[op.args[0]] = tc_line1(op.args[1], state)
            else:
                if op.types:
                    state.vars[op.args[0]] = op.types[0]
                elif state.vars.get(op.args[0], None) in (None, object):
                    state.vars[op.args[0]] = tc_line1(op.args[1], state)

        case OpIds.convert:
            return op.args[1]

        case OpIds.if_ | OpIds.else_ | OpIds.elif_ | OpIds.while_:
            for i in op.oper:
                tc_line1(i, state)

        case OpIds.for_:
            if is_func:
                local[op.args[0]] = object
            else:
                state.vars[op.args[0]] = object

            for i in op.oper:
                tc_line1(i, state)

        case OpIds.func:
            func = TypeCheckedFunction(op.oper, list(zip(op.args[1:], op.types[1:])), op.types[0])
            state.functions[op.args[0]] = func
            full_vars[op.args[0]] = Function
            state.opened_function = func
            for i in op.oper:
                tc_line1(i, state)
            state.opened_function = None

        case OpIds.call:
            func = op.args[0].args[0]
            if func not in state.functions:
                state.warnings += 1
                return object
            return state.functions[func].ret

        case _:
            if op.id.name in state.keywords:
                keyword = state.keywords[op.id.name]

                return keyword[0]

            state.warnings += 1