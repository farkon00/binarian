def type_to_str(_type):
    return str(_type)[str(_type).find("'")+1:str(_type).rfind("'")].split(".")[-1].lower() if _type != None else "none"