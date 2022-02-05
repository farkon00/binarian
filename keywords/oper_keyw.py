from .check_args import check_args

def if_keyword(lexic : list[str], i : int, state):
    check_args(lexic[1], i)
    if "(" not in " ".join(lexic):
        raise SyntaxError(f'Blocks must have starts and finishes matched with "(" and ")". Line : {i + 1}')

    state.allowed_blocks += int(lexic[1])