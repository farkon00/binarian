def type_to_str(_type, sep=" or "):
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

def is_name_unavailable(name, state):
    # 1 line - name is keyword
    # 2 line - name is integer
    # 3 line - name includes brackets
    return ((name in state.RESTRICTED_NAMES) or\
        (name.isdigit() or (name[0] == "-" and name[1:].isdigit())) or\
        any([(i in name) for i in state.BRACKETS])
    )