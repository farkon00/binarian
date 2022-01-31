from http.server import executable


def delete_comments(code):
    while "//" in code:
        comm_start = code.find("//")

        if comm_start != -1:
            code = code[:comm_start]

    return code

def blocks_finder(code):
    ret = []

    if "*" in code:
        raise UnicodeEncodeError('Character "*" is restricted in binarian code')

    temp = code
    executable_code = code

    if code.count("(") != code.count(")"):
        raise SyntaxError('Functions must have start and finish matched with "(" and ")".')

    while "(" in temp:
        end_ind = temp.find(")")
        if end_ind != -1:
            start_ind = temp[:end_ind].rfind("(")

            if start_ind == -1:
                raise SyntaxError('Functions must have start and finish matched with "(" and ")".')

            temp = temp[:start_ind]  + "{" + temp[start_ind+1:]
            temp = temp[:end_ind]  + "}" + temp[end_ind+1:]

            new_line_count = executable_code[start_ind:end_ind].count("\n")

            executable_code = executable_code[:start_ind] + "*" * (end_ind - start_ind + 1) + executable_code[end_ind+1:]
            executable_code = executable_code[:end_ind] + "\n" * new_line_count + executable_code[end_ind:]

            ret.append((start_ind, end_ind))  

    executable_code = executable_code.replace("*", "")

    return (executable_code, ret)

def prepare_code(code):
    prep1 = delete_comments(code)
    return (prep1,) + blocks_finder(prep1)