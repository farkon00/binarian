def get_var(var : str, i : int, full_vars : dict[str : int], _type : type = object):
    if var not in full_vars:
        raise NameError(f"Variable is not found. Line : {i + 1}")

    ret = full_vars[var]

    if _type:
        if not isinstance(ret, _type):
            raise TypeError(f"Unexpected type, {_type} was expected, {type(ret)} was given. Line : {i + 1}")

    return ret