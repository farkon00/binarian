from dataclasses import dataclass

from binarian.blocks_parser import *
from binarian.get_var import get_var
from binarian.exceptions import *

@dataclass
class Function:
    """Class that represents function in binarian"""

    args : list[str]
    start_line : int

    def execute(self, args : list[str], state, full_vars : dict[str : object]):
        starter_blocks = state.opened_blocks

        is_expr_before = state.is_expr
        state.is_expr = False

        local = {self.args[j] : get_var(args[j], full_vars, state) for j in range(len(args))}
        for line in state.lines[self.start_line+1:]:
            state.current_line += 1

            # Expressions executing
            binarian_assert(line.count("{") != line.count("}"), 'Expression must have start and finish matched with "{" and "}".', state)

            if state.opened_blocks <= state.allowed_blocks:
                while "{" in line:
                    line = state.GLOBAL_FUNCS["execute_expr"](line, state, local=local)
            
            lexic = line.split()

            opened_blocks, _ = parse_blocks(line, state, ret=True)
            if opened_blocks <= starter_blocks - 1:
                state.opened_blocks -= 1
                state.allowed_blocks -= 1
                state.is_expr = is_expr_before
                
                return 0

            state.GLOBAL_FUNCS["execute_line"](lexic, state, local=local)

            if state.last_return != None:
                state.opened_blocks -= 1
                state.allowed_blocks -= 1
                state.is_expr = is_expr_before

                ret = state.last_return
                state.last_return = None

                return ret

        state.is_expr = is_expr_before

    def __str__(self):
        return f"<function : {' '.join(self.args)}>"