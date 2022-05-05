from .oper import *

from bin_types.list import List

from funcs.exceptions import binarian_assert
from funcs.blocks_parser import parse_lists

def get_args(lexic, state) -> Oper:
    """
    Parses literal, variable or expression and returns list of Oper object 
    """

    binarian_assert(" ".join(lexic).count("[") != " ".join(lexic).count("]"), 'Lists must have start and finish matched with "[" and "]"', state)

    ret = []
    lexic = parse_lists(lexic)

    for var in lexic:
        if var[0] == "[": # list parsing
            elems = get_args(var[1:-1].split(), state)
            ret.append(Oper(OpIds.value, List(elems)))
        elif var.isdigit() or (var[0] == "-" and var[1:].isdigit()): # int parsing
            ret.append(Oper(OpIds.value, int(var) if var[0] != "-" else -int(var[1:])))
        elif var.replace(".", "").isdigit() or (var[0] == "-" and var[1:].replace(".", "").isdigit()): # float parsing
            ret.append(Oper(OpIds.value, float(var) if var[0] != "-" else -float(var[1:])))
        else:
            ret.append(Oper(OpIds.variable, var))

    return ret