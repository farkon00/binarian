def check_args(args : tuple[str], i : int) -> None:
    if any(map(lambda x : x not in ("0", "1"), args)):
        raise NameError(f"Variable is not found. Line : {i + 1}")