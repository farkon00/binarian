from time import time

from parsing.oper import Oper

def input_keyword(op : Oper, state) -> str:
    input_start_time = time()
    inp = input()
    state.input_time += time() - input_start_time

    return inp