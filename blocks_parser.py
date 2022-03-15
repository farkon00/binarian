from exceptions import *

def parse_brackets(line : str, mode : tuple[str, str], state, error : str = "Expression") -> tuple[int, int] | None:
    """Finds brackets indexes"""

    end_ind = line.find(mode[1])
    if end_ind != -1:
        start_ind = line[:end_ind].rfind(mode[0])
        binarian_assert(start_ind == -1, f'{error} must have start and finish matched with "{mode[0]}" and "{mode[1]}".', state)
        return start_ind, end_ind

def parse_lists(lexic : list[str]):
    arrays_opened = 0
    merged = 0
    
    for i in range(len(lexic)):
        now_lex = lexic[i-merged]
        
        if arrays_opened > 0:
            lexic[i-1-merged] += " " + now_lex
            del lexic[i-merged]
            merged += 1

        arrays_opened += now_lex.count("[")
        arrays_opened -= now_lex.count("]")

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