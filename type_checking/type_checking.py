from bin_types.list import List
from bin_types.function import Function
from .tc_types import *
from .stage1 import *
from .stage2 import *

def type_check(state):
    """
    Type check program from state
    Runs two stages of type checking
    """
    state = TypeCheckingState(state)

    # Stage 1(type)
    for line in state.lines:
        while "(" in line:
            line = tc_expr1(line, state)

        lexic = line.split()
        tc_line1(lexic, state)
        
        state.current_line += 1

    stage1_warn = state.warnings
    print(f"First stage of type checking completed successfully with {stage1_warn} warnings")
    state.reset()

    # Stage 2(check)
    for line in state.lines:
        while "(" in line:
            line = tc_expr2(line, state)

        lexic = line.split()
        tc_line2(lexic, state)
        
        state.current_line += 1

    print(f"Second stage of type checking completed successfully with {state.warnings - stage1_warn} warnings")
    print(f"Type checking completed successfully with {state.warnings} warnings\n")
