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

def parse_blocks(line : str, state) -> None:
    """Counts opened blocks"""

    closings = line.count(")")

    if state.opened_blocks <= state.allowed_blocks:
        state.allowed_blocks -= closings

    state.opened_blocks += line.count("(")
    state.opened_blocks -= closings