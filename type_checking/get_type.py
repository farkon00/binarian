from bin_types.list import List

def get_type(var, state, full_vars):
    if var[0] == "[":
        return List
    if var in state.types:
        return state.types[var]
    if var not in full_vars:
        return object

    return full_vars[var]