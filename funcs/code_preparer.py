def delete_com_line(line : str) -> str:
    """Deletes comments from line"""

    comm_start = line.find("//")

    if comm_start != -1:
        line = line[:comm_start]

    return line

def delete_comments(code : str) -> str:
    lines = code.split("\n")
    for i in range(len(lines)):
        lines[i] = delete_com_line(lines[i])

    return "\n".join(lines)