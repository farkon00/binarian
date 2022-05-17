from funcs.exceptions import binarian_assert

def type_to_str(_type : type | tuple, sep : str =" or "):
    """
    Converts type or tuple of types to string
    e. g. <class 'bin_types.functions.Function'> -> function
    For tuples will separate types with argument sep, standard sep is " or "
    """
    
    if isinstance(_type, tuple):
        types = []
        for i in _type:
            types.append(type_to_str(i))

        return sep.join(types)

    if _type is None:
        return "none"

    res = str(_type)
    main_part = str(_type).find("'")+1
    end_main_part = str(_type).rfind("'")
    res = res[main_part:end_main_part]
    res = res.split(".")[-1] # removes modules names

    return res.lower()

def check_args(op, types : list[type], state, local) -> list | object:
    ret = []
    for i, type_ in zip(op.args, types + [object] * (len(op.args) - len(types))):
        res = state.GLOBAL_FUNCS['execute_line'](i, state, local)
        binarian_assert(not isinstance(res, type_), 
            f"Unexpected argument type {type_to_str(type_)} was expected, {type_to_str(type(res))} found.", state)
        ret.append(res)

    if len(ret) > 1:
        return ret
    binarian_assert(len(ret) < 1, "No arguments were given", state)
    return ret[0]

def is_name_unavailable(name : str, state):
    """
    Checks if name of variable or function is unavailiable
    Not checks if its taken, just checks, that name isnt any literal or keyword etc.
    """
    # 1 line - name is keyword
    # 2 line - name is integer
    # 3-4 line - name is float
    # 5 line - name includes brackets
    return ((name in state.RESTRICTED_NAMES) or\
        (name.isdigit() or (name[0] == "-" and name[1:].isdigit())) or\
        (name.replace(".", "").isdigit() or\
         (name[0] == "-" and name[1:].replace(".", "").isdigit())) or\
        any([(i in name) for i in state.BRACKETS])
    )