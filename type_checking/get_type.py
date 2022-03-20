from bin_types.list import List

def get_type(var, state, full_vars):
    if var in state.types:
        return state.types[var]
    if var not in full_vars:
        return object
    if var[0:] == "[":
        return List

    return full_vars[var]