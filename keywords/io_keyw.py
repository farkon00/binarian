from time import time

from funcs.exceptions import binarian_assert, throw_exception

def input_keyword(op : list[str], in_vars : dict[str : object], state) -> None:
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    input_start_time = time()
    try:
        inp = int(input(f"{op.args[0]} : "))
    except:
        throw_exception("This is not an integer.", state)
    state.input_time += time() - input_start_time

    in_vars[op.args[0]] = inp

def output_keyword(op : list[str], state, local : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    print(f"{op.args[1]} : {state.GLOBAL_FUNCS['execute_line'](op.args[0], state, local)}")