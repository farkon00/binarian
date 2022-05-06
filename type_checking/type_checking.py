from bin_types.list import List
from bin_types.function import Function
from .tc_types import *
from .stage1 import *
from .stage2 import *

def type_check(opers : list, state):
    """
    Type check program from state
    Runs two stages of type checking
    """
    state = TypeCheckingState(state)

    # Stage 1(type)
    for op in opers:
        tc_line1(op, state)

    stage1_warn = state.warnings
    print(f"First stage of type checking completed successfully with {stage1_warn} warnings")
    state.reset()

    # Stage 2(check)
    for op in opers:
        tc_line2(op, state)
        
        state.current_line += 1

    print(f"Second stage of type checking completed successfully with {state.warnings - stage1_warn} warnings")
    print(f"Type checking completed successfully with {state.warnings} warnings\n")
