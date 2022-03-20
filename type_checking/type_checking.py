from bin_types.list import List
from bin_types.function import Function
from .tc_types import *
from .stage1 import *

def type_check(state):
    state = TypeCheckingState(state)

    for line in state.lines:
        while "{" in line:
            line = tc_expr1(line, state)

        lexic = line.split()
        tc_line1(lexic, state)
        
        state.current_line += 1

    print(f"First stage of type checking completed successfully with {state.warnings} warnings")
