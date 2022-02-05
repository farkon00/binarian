from dataclasses import dataclass

from blocks_parser import *

@dataclass
class Function:
    args : list[str]
    start_line : int

    def execute(self, args : list[int], i : int, state):
        starter_blocks = state.opened_blocks
        state.is_expr = False

        local = {self.args[j] : args[j] for j in range(len(args))}
        for line in state.lines[self.start_line+1:]:
            
            # Expressions executing
            if line.count("{") != line.count("}"):
                raise SyntaxError('Expression must have start and finish matched with "{" and "}". Line : ' + str(i + 1))

            if state.opened_blocks <= state.allowed_blocks:
                while "{" in line:
                    line = state.global_funcs["execute_expr"](line, i, state, local=local)
            
            lexic = line.split()
            if len(lexic) <= 0:
                continue

            parse_blocks(line, state)
            if state.opened_blocks <= starter_blocks - 1:
                return 0

            ret = state.global_funcs["execute_line"](lexic, i, state, local=local)

            if ret != None and lexic[0] == "return":
                return ret