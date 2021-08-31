import sys

vars = {}

def get_var(name, i):
    try:
        return vars[name]
    except:
        raise NameError(f"Variable did not found or value isn`t 0 or 1. Line : {i + 1}")

def expr_read(line, i):
    end_ind = line.find("}")
    if end_ind != -1:
        for j in range(end_ind, 0, -1):
            if line[j] == "{":
                start_ind = j
                break

    lexic = line[start_ind+1:end_ind].split()

    match lexic[0]:
        case "and":
            args = []
            if lexic[1] != '0' and lexic[1] != '1':
                args.append(get_var(lexic[1], i))
            else:
                args.append(int(lexic[1]))
            if lexic[2] != '0' and lexic[2] != '1':
                args.append(get_var(lexic[2], i))
            else:
                args.append(int(lexic[2]))
            line = line.replace(line[start_ind:end_ind] + '}', str(int(args[0] and args[1])))

        case "or":
            args = []
            if lexic[1] != '0' and lexic[1] != '1':
                args.append(get_var(lexic[1], i))
            else:
                args.append(int(lexic[1]))
            if lexic[2] != '0' and lexic[2] != '1':
                args.append(get_var(lexic[2], i))
            else:
                args.append(int(lexic[2]))
            line = line.replace(line[start_ind:end_ind] + '}', str(int(args[0] or args[1])))

        case "not":
            args = []
            if lexic[1] != '0' and lexic[1] != '1':
                args.append(get_var(lexic[1], i))
            else:
                args.append(int(lexic[1]))

            line = line.replace(line[start_ind:end_ind] + '}', str(int(not args[0])))

    
        # Unavailable keywords check
        case "set":
            raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")
        case "input":
            raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")
        case "output":
            raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")

        case _:
            raise NameError(f"Keyword did not found. Line : {i + 1}")
            
    return line


try:
    code = open(sys.argv[1], 'r', encoding="utf-8").read()
except:
    raise FileExistsError("File does not exist.")

for i in range(len(code.split('\n'))):
    line = code.split('\n')[i]

    comm_start = line.find("//")

    if comm_start != -1:
        line = line[:comm_start]

    while '{' in line:
        if line.count('{') == line.count('}'):
            line = expr_read(line, i)
        else:
            raise SyntaxError("Expression must have start and finish matched with '{' and '}'. Line : " + str(i + 1))
    
    lexic = line.split()
    if len(lexic) <= 0:
        continue

    match lexic[0]:
        case "set":
            if len(lexic) >= 3:
                try:
                    set_val = int(lexic[2])
                except ValueError:
                    raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
                if set_val == 0 or set_val == 1:
                    vars[lexic[1]] = set_val
                else:
                    raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
            else:
                raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

        case "input":
            if len(lexic) >= 2:
                try:
                    inp = int(input(f'{lexic[1]} : '))
                except ValueError:
                    raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
                if inp == 0 or inp == 1:
                    vars[lexic[1]] = inp
                else:
                    raise ValueError(f"Value must be 0 or 1. Line : {i + 1}")
            else:
                raise ValueError(f"You didn`t provide a variable name. Line : {i + 1}")

        case "output":
            if lexic[1] != '0' and lexic[1] != '1':
                print(f"{lexic[2]} : {get_var(lexic[1], i)}")
            else:
                print(f"{lexic[2]} : {lexic[1]}")


        case "and":
            args = []
            if lexic[1] != '0' and lexic[1] != '1':
                args.append(get_var(lexic[1], i))
            else:
                args.append(int(lexic[1]))
            if lexic[2] != '0' and lexic[2] != '1':
                args.append(get_var(lexic[2], i))
            else:
                args.append(int(lexic[2]))

            print(f"AND output : {int(args[0] and args[1])}. Line : {i + 1}")

        case "or":
            args = []
            if lexic[1] != '0' and lexic[1] != '1':
                args.append(get_var(lexic[1], i))
            else:
                args.append(int(lexic[1]))
            if lexic[2] != '0' and lexic[2] != '1':
                args.append(get_var(lexic[2], i))
            else:
                args.append(int(lexic[2]))

            print(f"OR output : {int(args[0] and args[1])}. Line : {i + 1}")

        case "not":
            args = []
            if lexic[1] != '0' and lexic[1] != '1':
                args.append(get_var(lexic[1], i))
            else:
                args.append(int(lexic[1]))

            print(f"NOT output : {int(not args[0])}. Line : {i + 1}")
        case _:
            raise NameError(f"Function or keyword did not found. Line : {i + 1}")


try:
    if sys.argv[2] == "debug":
        print("\n" + str(vars), "\n\nFinished")
except:
    print("Finished")