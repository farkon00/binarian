from .exceptions import *

def parse_lists_and_expr(lexic : list[str]) -> list[str]:
    """Finds [ and ] in lexic and combines all lexic beetween them"""
    arrays_opened = 0
    expr_opened = 0
    merged = 0
    
    for i in range(len(lexic)):
        now_lex = lexic[i-merged]
        
        if arrays_opened > 0 or expr_opened > 0:
            lexic[i-1-merged] += " " + now_lex
            del lexic[i-merged]
            merged += 1

        arrays_opened += now_lex.count("[")
        arrays_opened -= now_lex.count("]")

        expr_opened += now_lex.count("(")
        expr_opened -= now_lex.count(")")

    return lexic