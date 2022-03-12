from blocks_parser import parse_brackets
from list import List
from blocks_parser import parse_lists

def get_var(var : str, i : int, full_vars : dict[str : int], _type : type = object):
    if var[0] != "[":
        ret = full_vars[var]

        if var not in full_vars:
            raise NameError(f"Variable is not found. Line : {i + 1}")
    else:
        temp = var

        if temp.count("[") != temp.count("]"):
            raise SyntaxError(f'Arrays must have start and finish matched with "[" and "]". Line : {i + 1}')

        while "[" in temp:
            start_ind, end_ind = parse_brackets(temp, i, ("[", "]"), error="List")
            elems = parse_lists(temp[start_ind+1:end_ind].split())
            ret = List([get_var(j, i, full_vars) for j in elems])
            temp = temp[:start_ind] + temp[end_ind+1:]

    if not isinstance(ret, _type):
        # Makes better strs for types e. g. <class 'int'> -> int
        type1 = str(_type)[str(_type).find("'")+1:str(_type).rfind("'")].split(".")[-1] 
        type2 = str(type(ret))[str(type(ret)).find("'")+1:str(type(ret)).rfind("'")].split(".")[-1]

        raise TypeError(f"Unexpected type, {type1} was expected, {type2} was given. Line : {i + 1}")

    return ret