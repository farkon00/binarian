from bin_types.list import List
from .blocks_parser import parse_lists
from .exceptions import *
from .convert_type import *

def get_var(var : str, full_vars : dict[str : object], state, _type : type = object, error = "Variable"):
    if var[0] != "[":
        binarian_assert(var not in full_vars, f"{error} is not found : {var}", state)

        ret = full_vars[var]
    else:
        binarian_assert(var.count("[") != var.count("]"), 'Lists must have start and finish matched with "[" and "]"', state)

        elems = parse_lists(var[1:-1].split())
        ret = List([get_var(j, full_vars, state) for j in elems])

    if not isinstance(ret, _type):
        # Makes better strs for types e. g. <class 'int'> -> int
        type1 = type_to_str(_type)
        type2 = type_to_str(type(ret))

        throw_exception(f"Unexpected type, {type1} was expected, {type2} was given", state)

    return ret