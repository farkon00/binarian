def parse_expr(line : str, i : int) -> tuple[int, int] | None:
    """Finds expression indexes"""

    end_ind = line.find("}")
    if end_ind != -1:
        for j in range(end_ind, 0, -1):
            if line[j] == "{":
                start_ind = j
                return start_ind, end_ind
        else: # If for ends without break. That means "}" located before "{"
            raise SyntaxError('Expression must have start and finish matched with "{" and "}". Line : ' + str(i + 1))
    else:
        pass

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