def type_to_str(_type):
    return str(_type)[str(_type).find("'")+1:str(_type).rfind("'")].split(".")[-1].lower() if _type != None else "none"

def is_name_unavailable(name, state):
    # 1 line - name is keyword
    # 2 line - name is integer
    # 3 line - name includes brackets
    return ((name in state.RESTRICTED_NAMES) or\
        (name.isdigit() or (name[0] == "-" and name[1:].isdigit())) or\
        any([(i in name) for i in state.BRACKETS])
    )