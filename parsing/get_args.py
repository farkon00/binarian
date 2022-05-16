from .oper import *

from bin_types.list import List

from funcs.exceptions import binarian_assert, throw_exception
from funcs.brackets_parser import parse_lexic

def get_args(lexic, state) -> Oper:
    """
    Parses literal, variable or expression and returns list of Oper object 
    """

    ret = []
    lexic = parse_lexic(lexic, state)

    for var in lexic:
        if var[0] == "[": # list parsing
            elems = get_args(var[1:-1].split(), state)
            ret.append(Oper(OpIds.value, state.current_line, [List(elems)]))
        elif var[0] == '"': 
            ret.append(Oper(OpIds.value, state.current_line, [parse_string(var, state)]))
        elif var.lower().startswith("0x") or var.lower().startswith("-0x"): # Hex numbers
            binarian_assert(any(i not in "0123456789abcdef" for i in var[2:].lower()),
             f"Invalid hexadecimal litteral: {var}", state)
            ret.append(Oper(OpIds.value, state.current_line, [int(var, 16)]))
        elif var.lower().startswith("0b") or var.lower().startswith("-0b"): # Binary numbers
            binarian_assert(any(i not in "01" for i in var[2:].lower()),
             f"Invalid binary litteral: {var}", state)
            ret.append(Oper(OpIds.value, state.current_line, [int(var, 2)]))
        elif var.lower().startswith("0o") or var.lower().startswith("-0b"): # Octal numbers
            binarian_assert(any(i not in "01234567" for i in var[2:].lower()),
             f"Invalid octal litteral: {var}", state)
            ret.append(Oper(OpIds.value, state.current_line, [int(var, 8)]))
        elif var.isdigit() or (var[0] == "-" and var[1:].isdigit()): # int parsing
            ret.append(Oper(OpIds.value, state.current_line, int(var) if var[0] != "-" else -int(var[1:])))
        elif var.replace(".", "").isdigit() or (var[0] == "-" and var[1:].replace(".", "").isdigit()): # float parsing
            ret.append(Oper(OpIds.value, state.current_line, float(var) if var[0] != "-" else -float(var[1:])))
        elif var[0] == "(":
            ret.append(state.GLOBAL_FUNCS["parse_line"](var[1:-1], state))
        else:
            ret.append(Oper(OpIds.variable, state.current_line, var))

    return ret

def parse_string(var : str, state) -> str:
    res = ""
    escaped = False
    for i in var[1:-1]:
        if escaped:
            match i:
                case "n": char = "\n"
                case "t": char = "\t"
                case "r": char = "\r"
                case "\"": char = "\""
                case "\\": char = "\\"
                case _: throw_exception(f"Unknown escape sequence: \\{i}", state)
            escaped = False
        elif i == "\\":
            escaped = True
            char = ""
        else:
            char = i

        res += char

    return res