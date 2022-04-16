from bin_types.list import List

def get_type(var : str, state, full_vars : dict[str : object]):
    """Returns type of variable or type of literal e. g. int, float, list etc."""
    if var[0] == "[":
        return List
    elif var.isdigit() or (var[0] == "-" and var[1:].isdigit()):
        return int
    elif var.replace(".", "").isdigit() or (var[0] == "-" and var[1:].replace(".", "").isdigit()):
        return float
    elif var in state.types:
        return state.types[var]
    elif var not in full_vars:
        return object

    return full_vars[var]