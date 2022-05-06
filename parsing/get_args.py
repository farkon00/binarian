from .oper import *

from bin_types.list import List

from funcs.exceptions import binarian_assert
from funcs.brackets_parser import parse_lexic

def get_args(lexic, state) -> Oper:
    """
    Parses literal, variable or expression and returns list of Oper object 
    """

    ret = []
    lexic = parse_lexic(lexic, state)

    for var in lexic:
        if var[0] == "[": # list parsing
            elems = get_args(var[1:-1].split(), state)
            ret.append(Oper(OpIds.value, state.current_line, [List(elems)]))
        elif var[0] == '"': 
            ret.append(Oper(OpIds.value, state.current_line, [var[1:-1]]))
        elif var.isdigit() or (var[0] == "-" and var[1:].isdigit()): # int parsing
            ret.append(Oper(OpIds.value, state.current_line, int(var) if var[0] != "-" else -int(var[1:])))
        elif var.replace(".", "").isdigit() or (var[0] == "-" and var[1:].replace(".", "").isdigit()): # float parsing
            ret.append(Oper(OpIds.value, state.current_line, float(var) if var[0] != "-" else -float(var[1:])))
        elif var[0] == "(":
            ret.append(state.GLOBAL_FUNCS["parse_line"](var[1:-1], state))
        else:
            ret.append(Oper(OpIds.variable, state.current_line, var))

    return ret