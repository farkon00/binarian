from funcs.exceptions import *
from funcs.get_var import get_var
from type_checking.get_type import get_type
from funcs.utils import type_to_str

def convert_keyword(op : list[str], state, local : dict[str : object]):
    original = state.GLOBAL_FUNCS['execute_line'](op.args[0], state, local)
    end_type = op.args[1]
    try:
        final = end_type(original)
    except Exception:
        throw_exception(f"Can`t convert to type {type_to_str(end_type)}", state)

    if state.is_expr:
        return final