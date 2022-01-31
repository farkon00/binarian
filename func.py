from dataclasses import dataclass

import binarian

@dataclass
class Function:
    args : list[str]
    lines : str

    def execute(self, args, i):
        local = {self.args[j] : args[j] for j in range(len(args))}
        for line in map(lambda x : x.lower(), self.lines.split("\n")[1:-1]):
            while "{" in line:
                if line.count("{") == line.count("}"):
                    line = binarian.expr_read(line, i, local=local)
                else:
                    raise SyntaxError('Expression must have start and finish matched with "{" and "}". Line : ' + str(i + 1))
            
            lexic = line.split()
            if len(lexic) <= 0:
                continue

            ret = binarian.execute_line(lexic, i, local=local)

            if ret != None:
                return ret

        return "0"