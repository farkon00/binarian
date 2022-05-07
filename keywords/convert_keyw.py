from funcs.exceptions import throw_exception
from funcs.utils import type_to_str
from parsing.oper import Oper

def convert_keyword(op : Oper, state, local : dict[str : object]):
    original = state.GLOBAL_FUNCS['execute_line'](op.args[0], state, local)
    end_type = op.args[1]
    try:
        final = end_type(original)
    except Exception:
        throw_exception(f"Can`t convert to type {type_to_str(end_type)}", state)

    if state.is_expr:
        return final