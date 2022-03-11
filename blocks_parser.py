def parse_brackets(line : str, i : int, mode : tuple[str, str], error : str = "Expression") -> tuple[int, int] | None:
    """Finds brackets indexes"""

    end_ind = line.find(mode[1])
    if end_ind != -1:
        start_ind = line[:end_ind].rfind(mode[0])
        if start_ind == -1:
            raise SyntaxError(f'{error} must have start and finish matched with "{mode[0]}" and "{mode[1]}". Line : {i + 1}')
        return start_ind, end_ind

def parse_arrays(lexic : list[str]):
    arrays_opened = 0
    
    for j, i in enumerate(lexic):
        if arrays_opened > 0:
            lexic[j-1] += " " + i
            del lexic[j]

        if i[0] == "[":
            arrays_opened += 1
        if i[0] == "]":
            arrays_opened -= 1

    return lexic


def parse_blocks(line : str, state, ret : bool = False) -> str | tuple[int, int]:
    """Counts opened blocks"""

    opened_blocks, allowed_blocks = state.opened_blocks, state.allowed_blocks

    closings = line.count(")")

    if opened_blocks <= allowed_blocks:
        allowed_blocks -= closings

    opened_blocks += line.count("(")
    opened_blocks -= closings

    if ret:
        return opened_blocks, allowed_blocks

    state.opened_blocks = opened_blocks
    state.allowed_blocks = allowed_blocks
    
    return line.replace(")", "")