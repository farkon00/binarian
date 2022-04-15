from bin_types.list import List

def get_type(var, state, full_vars):
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