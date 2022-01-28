from argparse import ArgumentError
import sys

global vars
vars = {}

def check_args(arg1, i, arg2="0"):
    if arg1 not in ("0", "1") and arg2 not in ("0", "1"):
        raise NameError(f"Variable is not found. Line : {i + 1}")

def expr_read(line, i):
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

    match lexic[0]:
        case "and":
            check_args(lexic[0], i, arg2=lexic[1])

            line = line.replace(line[start_ind:end_ind] + "}", str(int(int(lexic[1]) and int(lexic[2]))))

        case "or":
            check_args(lexic[0], i, arg2=lexic[1])

            line = line.replace(line[start_ind:end_ind] + "}", str(int(int(lexic[1]) or int(lexic[2]))))

        case "not":
            check_args(lexic[0], i)

            line = line.replace(line[start_ind:end_ind] + "}", str(int(not int(lexic[1]))))

    
        # Unavailable keywords check
        case "set" | "input" | "output":
            raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

        case _:
            raise NameError(f"Keyword did not found. Line : {i + 1}")
            
    return line


try:
    code = open(sys.argv[1], "r", encoding="utf-8").read()
except:
    raise FileExistsError("File does not exist.")

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

    for j in range(len(lexic)):
        if lexic[j] in vars.keys():
            lexic[j] = str(vars[lexic[j]])

    match lexic[0]:
        case "set":
            if len(lexic) >= 3:
                if lexic[1] not in ["0", "1", "and", "or", "not", "set", "input", "output"]:
                    try:
                        set_val = int(lexic[2])
                    except ValueError:
                        raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
                    if set_val == 0 or set_val == 1:
                        vars[lexic[1]] = set_val
                    else:
                        raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
                else:
                    raise NameError(f"Variable name is unavailable. Line : {i + 1}")
            else:
                raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

        case "input":
            if len(lexic) >= 2:
                if lexic[1] not in ["0", "1", "and", "or", "not", "set", "input", "output"]:
                    inp = input(f"{lexic[1]} : ")
                    if inp in ("0", "1"): 
                        inp = int(inp)
                        vars[lexic[1]] = inp
                    else:
                        raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
                else:
                    raise NameError(f"Variable name is unavailable. Line : {i + 1}")
            else:
                raise ValueError(f"You didn`t provide a variable name. Line : {i + 1}")

        case "output":
            if len(lexic) < 3:
                raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")
            if lexic[1] not in ("0", "1"):
                raise NameError(f"Variable is not found. Line : {i + 1}")
            else:
                print(f"{lexic[2]} : {int(lexic[1])}")


        case "and":
            check_args(lexic[0], i, arg2=lexic[1])

            print(f"AND output : {int(int(lexic[1]) and int(lexic[2]))}. Line : {i + 1}")

        case "or":
            check_args(lexic[0], i, arg2=lexic[1])

            print(f"OR output : {int(int(lexic[1]) or int(lexic[2]))}. Line : {i + 1}")

        case "not":
            check_args(lexic[0], i)

            print(f"NOT output : {int(not int(lexic[1]))}. Line : {i + 1}")
        case _:
            raise NameError(f"Keyword did not found. Line : {i + 1}")


try:
    if sys.argv[2] == "debug":
        print("\n" + str(vars), "\n\nFinished")
except:
    print("Finished")