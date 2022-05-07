from time import time

from funcs.exceptions import binarian_assert, throw_exception

def input_keyword(op : list[str], state) -> None | str:
    input_start_time = time()
    inp = input()
    state.input_time += time() - input_start_time

    if state.is_expr:
        return inp

def output_keyword(op : list[str], state, local : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    print(f"{op.args[1]} : {state.GLOBAL_FUNCS['execute_line'](op.args[0], state, local)}")