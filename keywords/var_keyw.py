from funcs.exceptions import binarian_assert
from parsing.oper import Oper

def var_keyword(op : Oper, state, in_vars : dict[str, object], local : dict[str, object] | None) -> None:
    # Error handeling
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    in_vars[op.values[0]] = state.GLOBAL_FUNCS["execute_line"](op.args[0], state, local)

def drop_keyword(op : Oper, state, in_vars : dict[str, object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(op.values[0] not in in_vars, f"Variable to drop was not found : {op.values[0]}", state)

    del in_vars[op.values[0]]