from dataclasses import dataclass
import sys
from types import NoneType

global vars
vars = {}

@dataclass
class Function:
    args : list[str]
    lines : list[list[str]] # List contains lexic lists

    def execute(self):
        pass

def execute_line(lexic : list[str], i : int, local : list[int | Function] | NoneType = None, is_expr=False) -> int:
    global vars

    full_vars = vars
    is_func = local != None

    if is_func:
        full_vars += local

    for j in range(len(lexic)):
        if lexic[j] in vars.keys():
            lexic[j] = str(full_vars[lexic[j]])

    match lexic[0]:
        case "set":
            if is_expr:
                raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

            # Error handeling
            if len(lexic) >= 3:
                if lexic[1] not in ("0", "1", "and", "or", "not", "set", "input", "output"):
                    try:
                        set_val = int(lexic[2])
                    except ValueError:
                        raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")

                    if set_val not in (0, 1):
                        raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
                else:
                    raise NameError(f"Variable name is unavailable. Line : {i + 1}")
            else:
                raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")
            
            if is_func:
                local[lexic[1]] = set_val
            else:
                vars[lexic[1]] = set_val
                

        case "input":
            if is_expr:
                raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

            # Error handeling
            if len(lexic) >= 2:
                if lexic[1] not in ["0", "1", "and", "or", "not", "set", "input", "output"]:
                    inp = input(f"{lexic[1]} : ")
                    if inp not in ("0", "1"): 
                        raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
                else:
                    raise NameError(f"Variable name is unavailable. Line : {i + 1}")
            else:
                raise ValueError(f"You didn`t provide a variable name. Line : {i + 1}")

            inp = int(inp)

            if is_func:
                local[lexic[1]] = inp
            else:
                vars[lexic[1]] = inp

        case "output":
            if is_expr:
                raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

            # Error handeling
            if len(lexic) < 3:
                raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")
            if lexic[1] not in ("0", "1"):
                raise NameError(f"Variable is not found. Line : {i + 1}")

            print(f"{lexic[2]} : {int(lexic[1])}")


        case "and":
            check_args(lexic[0], i, arg2=lexic[1])

            if not is_expr:
                print(f"AND output : {int(int(lexic[1]) and int(lexic[2]))}. Line : {i + 1}")

            return int(int(lexic[1]) and int(lexic[2]))

        case "or":
            check_args(lexic[0], i, arg2=lexic[1])

            if not is_expr:
                print(f"OR output : {int(int(lexic[1]) or int(lexic[2]))}. Line : {i + 1}")

            return int(int(lexic[1]) or int(lexic[2]))

        case "not":
            check_args(lexic[0], i)
            
            if not is_expr:
                print(f"NOT output : {int(not int(lexic[1]))}. Line : {i + 1}")

            return int(not int(lexic[1]))


        case _:
            raise NameError(f"Keyword did not found. Line : {i + 1}")

def check_args(arg1 : str, i : int, arg2="0") -> None:
    if arg1 not in ("0", "1") and arg2 not in ("0", "1"):
        raise NameError(f"Variable is not found. Line : {i + 1}")

def expr_read(line : str, i : int) -> str:
    global vars

    end_ind = line.find("}")
    if end_ind != -1:
        for j in range(end_ind, 0, -1):
            if line[j] == "{":
                start_ind = j
                break

    lexic = line[start_ind+1:end_ind].split()

    for j in range(len(lexic)):
        if lexic[j] in vars.keys():
            lexic[j] = str(vars[lexic[j]])
            
    return line.replace(line[start_ind:end_ind] + "}", str(execute_line(lexic, i, is_expr=True)))


try:
    code = open(sys.argv[1], "r", encoding="utf-8").read()
except:
    code = open("test.bino", "r", encoding="utf-8").read()
    #raise FileExistsError("File does not exist.")

for i in range(len(code.split("\n"))):
    line = code.split("\n")[i].lower()

    comm_start = line.find("//")

    if comm_start != -1:
        line = line[:comm_start]

    while "{" in line:
        if line.count("{") == line.count("}"):
            line = expr_read(line, i)
        else:
            raise SyntaxError('Expression must have start and finish matched with "{" and "}". Line : ' + str(i + 1))
    
    lexic = line.split()
    if len(lexic) <= 0:
        continue

    execute_line(lexic, i)


try:
    if sys.argv[2] == "debug":
        print("\n" + str(vars), "\n\nFinished")
except:
    print("Finished")