def get_var(var : str, i : int, full_vars : dict[str : int], _type : type = object):
    if var not in full_vars:
        raise NameError(f"Variable is not found. Line : {i + 1}")

    ret = full_vars[var]

    if not isinstance(ret, _type):
        # Makes better strs for types e. g. <class 'int'> -> int s
        type1 = str(_type)[str(_type).find("'")+1:str(_type).rfind("'")].split(".")[-1] 
        type2 = str(type(ret))[str(type(ret)).find("'")+1:str(type(ret)).rfind("'")].split(".")[-1]

        raise TypeError(f"Unexpected type, {type1} was expected, {type2} was given. Line : {i + 1}")

    return ret