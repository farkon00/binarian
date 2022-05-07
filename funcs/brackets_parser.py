from .exceptions import *

def parse_lexic(lexic : list[str], state) -> list[str]:
    """Finds [ and ] in lexic and combines all lexic beetween them"""
    arrays_opened = 0
    expr_opened = 0
    is_string_opened = False

    line = " ".join(lexic)
    res = [""]

    for i in range(len(line)):
        symb = line[i]

        if symb == "\"":
            is_string_opened = not is_string_opened

        if not is_string_opened:
            match symb:
                case " ": 
                    if not arrays_opened and not expr_opened: 
                        res.append("")

                case "[": arrays_opened += 1
                case "]": arrays_opened -= 1
                case "(": expr_opened += 1
                case ")": expr_opened -= 1
                case "{": symb = ""
                case "}": symb = ""

        res[-1] += symb

    for i in range(len(res)):
        res[i] = res[i].strip()
        if res[i] == "":
            del res[i]

    """for i in range(len(lexic)):
        now_lex = lexic[i-merged]

        if not is_string_opened:
            lexic[i-merged] = lexic[i-merged].replace("{", "").replace("}", "")
            if lexic[i-merged].strip() == "":
                del lexic[i-merged]
                merged += 1
                continue

        if arrays_opened > 0 or expr_opened > 0 or is_string_opened:
            lexic[i-1-merged] += " " + now_lex
            del lexic[i-merged]
            merged += 1
            
        if lexic[i-merged].startswith('"'):
            is_string_opened = True

        if not is_string_opened:
            arrays_opened += now_lex.count("[")
            arrays_opened -= now_lex.count("]")

            expr_opened += now_lex.count("(")
            expr_opened -= now_lex.count(")")

        if lexic[i-merged].endswith('"'):
            is_string_opened = False"""

    binarian_assert(expr_opened != 0, 'Expression must have start and finish matched with "(" and ")".', state)
    binarian_assert(arrays_opened != 0, 'Lists must have start and finish matched with "[" and "]".', state)
    binarian_assert(is_string_opened, 'String must be opened and closed with ".', state)

    return res