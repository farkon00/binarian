from funcs.get_var import get_var
from funcs.exceptions import binarian_assert
from funcs.utils import is_name_unavailable

def var_keyword(lexic : list[str], state, in_vars : dict[str : object], full_vars : dict[str : object]) -> None:
    # Error handeling
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert("=" not in " ".join(lexic), '"=" not found in var', state)

    parts = [None, None]
    for j, i in enumerate(lexic):
        if "=" in i:
            spl = i.find("=")
            parts[0] = lexic[:j] + [i[:spl]]
            parts[1] = [i[spl + 1:]] + lexic[j + 1:]
    binarian_assert(not len(parts[1]), 'Nothing was found after "=" in var', state)
    if not parts[0][-1]: parts[0] = parts[0][:-1]
    if not parts[1][0]: parts[1] = parts[1][1:]

    if len(parts[0]) >= 3:
        binarian_assert(parts[0][1].strip() not in state.types, f"Type is not found : {lexic[1]}", state)
        binarian_assert(is_name_unavailable(parts[0][2].strip(), state), "Variable name is unavailable.", state) 

        in_vars[parts[0][2].strip()] = get_var(parts[1][0].strip(), full_vars, state)
        return

    binarian_assert(is_name_unavailable(parts[0][1].strip(), state), "Variable name is unavailable.", state)
        
    in_vars[parts[0][1].strip()] = get_var(parts[1][0].strip(), full_vars, state)

def drop_keyword(lexic : list[str], state, in_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)

    if lexic[1] in in_vars:
        del in_vars[lexic[1]]