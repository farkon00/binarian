from dataclasses import dataclass

from blocks_parser import *
from get_var import get_var

@dataclass
class Function:
    """Class that represents function in binarian"""

    args : list[str]
    start_line : int

    def execute(self, args : list[str], i : int, state, full_vars : dict[str : int]):
        starter_blocks = state.opened_blocks
        state.is_expr = False

        local = {self.args[j] : get_var(args[j], i, full_vars, int) for j in range(len(args))}
        for line in state.lines[self.start_line+1:]:
            
            # Expressions executing
            if line.count("{") != line.count("}"):
                raise SyntaxError('Expression must have start and finish matched with "{" and "}". Line : ' + str(i + 1))

            if state.opened_blocks <= state.allowed_blocks:
                while "{" in line:
                    line = state.GLOBAL_FUNCS["execute_expr"](line, i, state, local=local)
            
            lexic = line.split()
            if len(lexic) <= 0:
                continue

            opened_blocks, _ = parse_blocks(line, state, ret=True)
            if opened_blocks <= starter_blocks - 1:
                state.opened_blocks -= 1
                state.allowed_blocks -= 1
                return 0

            ret = state.GLOBAL_FUNCS["execute_line"](lexic, i, state, local=local)

            if ret != None and lexic[0] == "return":
                state.opened_blocks -= 1
                state.allowed_blocks -= 1
                return ret