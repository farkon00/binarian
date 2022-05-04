from bin_types.list import List
from funcs.exceptions import binarian_assert

def get_type(var : str, state, full_vars : dict[str : object], only_name : bool = False):
    """Returns type of variable or type of literal e. g. int, float, list etc."""
    if var[0] == "[" and not only_name:
        return List
    elif var.isdigit() or (var[0] == "-" and var[1:].isdigit()) and not only_name:
        return int
    elif var.replace(".", "").isdigit() or (var[0] == "-" and var[1:].replace(".", "").isdigit()) and not only_name:
        return float
    elif var in state.types or only_name:
        binarian_assert(var not in state.types, f"Unknown type: {var}", state)
        return state.types[var]
    elif var not in full_vars:
        return object

    return full_vars[var]