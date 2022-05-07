from time import time

from funcs.exceptions import binarian_assert
from funcs.utils import check_args
from parsing.oper import Oper

def input_keyword(op : Oper, state) -> None | str:
    input_start_time = time()
    inp = input()
    state.input_time += time() - input_start_time

    if state.is_expr:
        return inp

def output_keyword(op : Oper, state, local : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    text = check_args(op, [str], state, local)

    print(text, end="")