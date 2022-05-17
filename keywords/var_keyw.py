from funcs.exceptions import binarian_assert
from parsing.oper import Oper

def var_keyword(op : Oper, state, in_vars : dict[str, object] | None, local : dict[str, object] | None) -> None:
    # Error handeling
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    in_vars[op.args[0]] = state.GLOBAL_FUNCS["execute_line"](op.args[1], state, local)

def drop_keyword(op : Oper, state, in_vars : dict[str, object] | None):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(op.args[0] not in in_vars, f"Variable to drop was not found : {op.args[0]}", state)

    del in_vars[op.args[0]]