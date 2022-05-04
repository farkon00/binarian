from funcs.exceptions import *
from funcs.get_var import get_var
from type_checking.get_type import get_type
from funcs.utils import type_to_str

def convert_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(len(lexic) < 3, "Not enought arguments for opeartion", state)
    original = get_var(lexic[1], full_vars, state)
    end_type = get_type(lexic[2], state, {}, True)
    try:
        final = end_type(original)
    except Exception:
        throw_exception(f"Can`t convert to type {type_to_str(end_type)}", state)

    if state.is_expr:
        return final