from funcs.utils import check_args
from funcs.exceptions import binarian_assert
from parsing.oper import Oper

def if_keyword(op : Oper, state, local : dict[str, object] | None):
    cond = bool(check_args(op, [object], state, local)[0])

    if cond:
        state.GLOBAL_FUNCS["execute_opers"](op.oper, state, local)

    state.opened_ifs.append(cond)

def else_keyword(op : Oper, state, local : dict[str, object] | None):
    binarian_assert(len(state.opened_ifs) <= 0, f"If operator for else was not found.", state)

    if_ = state.opened_ifs[-1]
    del state.opened_ifs[-1]

    if not if_:
        state.GLOBAL_FUNCS["execute_opers"](op.oper, state, local)

def elif_keyword(op : Oper, state, local : dict[str, object] | None):
    binarian_assert(len(state.opened_ifs) <= 0, f"If operator for else was not found.", state)

    if_ = state.opened_ifs[-1]
    del state.opened_ifs[-1]

    cond = bool(check_args(op, [object], state, local)[0])

    if cond and not if_:
        state.GLOBAL_FUNCS["execute_opers"](op.oper, state, local)

    state.opened_ifs.append(True if if_ else cond)  