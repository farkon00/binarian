from dataclasses import dataclass
import traceback

@dataclass
class Function:
    args : list[str]
    start_line : int

    def execute(self, args : list[int], i : int, code : str, opened_blocks : int, allowed_blocks : int):
        import binarian
        local = {self.args[j] : args[j] for j in range(len(args))}
        for line in code.split("\n")[self.start_line+1:]:
            
            # Expressions executing
            if line.count("{") != line.count("}"):
                raise SyntaxError('Expression must have start and finish matched with "{" and "}". Line : ' + str(i + 1))

            if opened_blocks <= allowed_blocks:
                while "{" in line:
                    line = binarian.execute_expr(line, i, opened_blocks, allowed_blocks, local=local)[-1]
            
            lexic = line.split()
            if len(lexic) <= 0:
                continue

            ret = binarian.execute_line(lexic, i, opened_blocks, allowed_blocks, local=local)
            opened_blocks, allowed_blocks = ret[:2]

            try:
                if ret[2] != None:
                    return opened_blocks, allowed_blocks, ret[-1]
            except:
                #traceback.print_exc()
                None

        return opened_blocks, allowed_blocks, 0