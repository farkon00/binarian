from get_var import get_var

def if_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]):
    if "(" not in " ".join(lexic):
        raise SyntaxError(f'Blocks must have starts and finishes matched with "(" and ")". Line : {i + 1}')

    cond = get_var(lexic[1], i, full_vars, int)
    state.allowed_blocks += cond

    state.opened_ifs.append((bool(cond), state.opened_blocks))

def else_keyword(lexic : list[str], i : int, state):
    if "(" not in " ".join(lexic):
        raise SyntaxError(f'Blocks must have starts and finishes matched with "(" and ")". Line : {i + 1}')

    for j in state.opened_ifs:
        if j[1] == state.opened_blocks:
            if_ = j
            state.opened_ifs.remove(j)
            break
    else:
        raise SyntaxError(f"If operator for else was not found. Line : {i + 1}")

    if not if_[0]:
        state.allowed_blocks += 1