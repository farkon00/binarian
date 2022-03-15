from .types.list import List
from .blocks_parser import parse_lists
from .exceptions import *

def get_var(var : str, full_vars : dict[str : object], state, _type : type = object, error = "Variable"):
    if var[0] != "[":
        binarian_assert(var not in full_vars, f"{error} is not found : {var}", state)

        ret = full_vars[var]
    else:
        binarian_assert(var.count("[") != var.count("]"), 'Arrays must have start and finish matched with "[" and "]"', state)

        elems = parse_lists(var[1:-1].split())
        ret = List([get_var(j, full_vars, state) for j in elems])

    if not isinstance(ret, _type):
        # Makes better strs for types e. g. <class 'int'> -> int
        type1 = str(_type)[str(_type).find("'")+1:str(_type).rfind("'")].split(".")[-1] 
        type2 = str(type(ret))[str(type(ret)).find("'")+1:str(type(ret)).rfind("'")].split(".")[-1]

        throw_exception(f"Unexpected type, {type1} was expected, {type2} was given", state)

    return ret