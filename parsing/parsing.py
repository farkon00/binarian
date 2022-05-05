from .oper import *
from .get_args import *
from funcs.exceptions import binarian_assert

def parse_to_ops(state):
    opers = []
    for line_index, i in enumerate(state.lines):
        # For skiping, that was already parsed inside blocks 
        if state.current_line > line_index + 1:
            continue

        state.current_line += 1
        line = state.lines[state.current_line]
        line = line.replace("}", "")

        binarian_assert(line.count("(") != line.count(")"), 'Expression must have start and finish matched with "(" and ")".', state)

        op = parse_line(line, state)
        if op:
            opers.append(op)

    return opers

def parse_line(line, state):
    lexic = line.split()

    if len(lexic) <= 0:
        return

    if lexic[0] in state.operations:
        op = Oper(OpIds.operation, lexic[0:1] + get_args(lexic[1:], state)) 
        binarian_assert(len(op.args) != 2, "Operation must have two argument.", state)
        return op

    match lexic[0]:
        case "drop":
            binarian_assert(len(lexic) != 2, "Drop must have one argument.", state)
            return Oper(OpIds.drop, lexic[1])

        case "input":
            binarian_assert(len(lexic) != 2, "Input must have one argument.", state)
            return Oper(OpIds.input, lexic[1])

        case "and" | "or":
            op = Oper(type.__getattribute__(OpIds, lexic[0] + "_"), get_args(lexic[1:], state))
            binarian_assert(len(op.args) != 2, f"{lexic[0][0].upper() + lexic[0][1:]} must have two argument.", state)
            return op

        case "index" | "append" | "zip":
            op = Oper(type.__getattribute__(OpIds, lexic[0]), get_args(lexic[1:], state))
            binarian_assert(len(op.args) != 2, f"{lexic[0][0].upper() + lexic[0][1:]} must have two argument.", state)
            return op

        case "not":
            op = Oper(OpIds.not_, get_args(lexic[1:], state))
            binarian_assert(len(op.args) != 1, "Not must have one argument.", state)
            return op

        case "setindex":
            op = Oper(OpIds.setindex, get_args(lexic[1:], state))
            binarian_assert(len(op.args) != 3, "Setindex must have three argument.", state)
            return op

        case "len":
            op = Oper(OpIds.len, get_args(lexic[1:], state))
            binarian_assert(len(op.args) != 1, "Len must have one argument.", state)
            return op

        case "break" | "continue":
            binarian_assert(len(lexic) != 1, "Break must have no arguments.", state)
            return Oper(type.__getattribute__(OpIds, lexic[0] + "_"))