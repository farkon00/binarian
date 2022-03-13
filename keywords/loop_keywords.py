from get_var import get_var
from exceptions import throw_exception
from list import List

def for_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    if state.is_expr:
        throw_exception(f"This operation is unavailable in expressions.", state)
    if len(lexic) <= 3:
        throw_exception(f"You didn`t give enough arguments.", state)
    if lexic[1] in state.RESTRICTED_NAMES:
        throw_exception(f"Variable name is unavailable.", state)
    if "(" not in " ".join(lexic):
        throw_exception(f'Blocks must have starts and finishes matched with "(" and ")".', state)
    get_var(lexic[2], full_vars, state, List) # Checks for errors in list

    state.opened_loops.append([state.current_line, state.opened_blocks, [], 0])

def execute_for(loop : list[int, int, list[str]], state, full_vars : dict[str : object], local : dict[str : object] = None):
    loop_lexic = state.lines[loop[0]].split()
    loop_lexic = state.GLOBAL_FUNCS["parse_lists"](loop_lexic)

    for loop_iter in get_var(loop_lexic[2], full_vars, state, List):
        if local != None:
                local[loop_lexic[1]] = loop_iter
        else:
            state.vars[loop_lexic[1]] = loop_iter

        state.current_line = loop[0]

        for line in loop[2]:
            state.current_line += 1

            # Expressions executing
            if line.count("{") != line.count("}"):
                throw_exception('Expression must have start and finish matched with "{" and "}".', state)

            if state.opened_blocks <= state.allowed_blocks:
                while "{" in line:
                    line = state.GLOBAL_FUNCS["execute_expr"](line, state, local=local)
                
            
            lexic = line.split()
            if len(lexic) <= 0:
                continue

            state.GLOBAL_FUNCS["execute_line"](lexic, state, local=local)

    if local != None:
        del local[loop_lexic[1]]
    else:
        del state.vars[loop_lexic[1]]

def while_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    if state.is_expr:
        throw_exception(f"This operation is unavailable in expressions.", state)
    if len(lexic) <= 2:
        throw_exception(f"You didn`t give enough arguments.", state)
    if "(" not in " ".join(lexic):
        throw_exception(f'Blocks must have starts and finishes matched with "(" and ")".', state)

    state.opened_loops.append([state.current_line, state.opened_blocks, [], 1])

def execute_while(loop : list[int, int, list[str]], state, full_vars : dict[str : object], local : dict[str : object] = None):
    loop_cond = state.lines[loop[0]].split()[1:-1]
    loop_cond = state.GLOBAL_FUNCS["parse_lists"](loop_cond)

    while get_var(state.GLOBAL_FUNCS["execute_expr"](" ".join(loop_cond), state, local=local).replace("{", "").replace("}", ""), full_vars, state, int):
        state.current_line = loop[0]

        for line in loop[2]:
            state.current_line += 1

            # Expressions executing
            if line.count("{") != line.count("}"):
                throw_exception('Expression must have start and finish matched with "{" and "}".', state)

            if state.opened_blocks <= state.allowed_blocks:
                while "{" in line:
                    line = state.GLOBAL_FUNCS["execute_expr"](line, state, local=local)
                
            
            lexic = line.split()
            if len(lexic) <= 0:
                continue

            state.GLOBAL_FUNCS["execute_line"](lexic, state, local=local)

        full_vars = {**state.vars, **(local if local != None else {})}