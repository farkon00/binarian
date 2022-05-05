from .oper import *
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

    match lexic[0]:
        case "drop":
            binarian_assert(len(lexic) != 2, "Drop must have one argument.", state)
            return Oper(OpIds.drop, lexic[1])

        case "input":
            binarian_assert(len(lexic) != 2, "Input must have one argument.", state)
            return Oper(OpIds.input, lexic[1])

        case "break":
            binarian_assert(len(lexic) != 1, "Break must have no arguments.", state)
            return Oper(OpIds.break_)
        
        case "continue":
            binarian_assert(len(lexic) != 1, "Continue must have no arguments.", state)
            return Oper(OpIds.continue_)