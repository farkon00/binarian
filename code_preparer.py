def delete_comments(code : str) -> str:
    while "//" in code:
        comm_start = code.find("//")

        if comm_start != -1:
            code = code[:comm_start]

    return code