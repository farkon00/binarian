from funcs.exceptions import binarian_assert
from parsing.oper import Oper

def var_keyword(op : Oper, state, in_vars : dict[str : object], local : dict[str : object]) -> None:
    # Error handeling
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    in_vars[op.args[0]] = state.GLOBAL_FUNCS["execute_line"](op.args[1], state, local)

def drop_keyword(op : Oper, state, in_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    if op.args[0] in in_vars:
        del in_vars[op.args[0]]