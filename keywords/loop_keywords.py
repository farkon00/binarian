from get_var import get_var
from exceptions import *
from list import List

def for_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) < 3, "You didn`t give enough arguments.", state)
    binarian_assert(lexic[1] in state.RESTRICTED_NAMES, "Variable name is unavailable.", state)
    binarian_assert("(" not in " ".join(lexic), 'Blocks must have starts and finishes matched with "(" and ")".', state)
    get_var(lexic[2], full_vars, state, List) # Checks for errors in list

    state.opened_loops.append([state.current_line, state.opened_blocks, [], 0])

def execute_for(loop : list[int, int, list[str]], state, full_vars : dict[str : object], local : dict[str : object] = None):
    state.current_line = loop[0]
    
    loop_line = state.lines[loop[0]]
    while "{" in loop_line:
        loop_line = state.GLOBAL_FUNCS["execute_expr"](loop_line, state, local=local)

    loop_lexic = loop_line.split()
    loop_lexic = state.GLOBAL_FUNCS["parse_lists"](loop_lexic)

    for loop_iter in get_var(loop_lexic[2], full_vars, state, List):
        if local != None:
                local[loop_lexic[1]] = loop_iter
        else:
            state.vars[loop_lexic[1]] = loop_iter

        state.current_line = loop[0]
        state.opened_blocks += 1
        state.allowed_blocks += 1

        for line in loop[2]:
            state.current_line += 1

            # Expressions executing
            binarian_assert(line.count("{") != line.count("}"), 'Expression must have start and finish matched with "{" and "}".', state)

            if state.opened_blocks <= state.allowed_blocks:
                while "{" in line:
                    line = state.GLOBAL_FUNCS["execute_expr"](line, state, local=local)
                
            
            lexic = line.split()
            if len(lexic) <= 0:
                continue

            state.GLOBAL_FUNCS["execute_line"](lexic, state, local=local)

            if state.last_return != None:
                return None

    try:
        if local != None:
            del local[loop_lexic[1]]
        else:
            del state.vars[loop_lexic[1]]
    except KeyError:
        pass

def while_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert(state.is_expr, "This operation is unavailable in expressions.", state)
    binarian_assert(len(lexic) < 2, "You didn`t give enough arguments.", state)
    binarian_assert("(" not in " ".join(lexic), 'Blocks must have starts and finishes matched with "(" and ")".', state)

    state.opened_loops.append([state.current_line, state.opened_blocks, [], 1])

def execute_while(loop : list[int, int, list[str]], state, full_vars : dict[str : object], local : dict[str : object] = None):
    state.current_line = loop[0]
    loop_cond = " ".join(state.lines[loop[0]].split()[1:-1])

    while True:
        state.current_line = loop[0]
        
        temp_loop_cond = loop_cond
        while "{" in temp_loop_cond:
            temp_loop_cond = state.GLOBAL_FUNCS["execute_expr"](temp_loop_cond, state, local=local)
        temp_loop_cond = get_var(temp_loop_cond, full_vars, state, int)
        if not temp_loop_cond:
            break
        del temp_loop_cond
        
        for line in loop[2]:
            state.current_line += 1

            # Expressions executing
            binarian_assert(line.count("{") != line.count("}"), 'Expression must have start and finish matched with "{" and "}".', state)

            if state.opened_blocks <= state.allowed_blocks:
                while "{" in line:
                    line = state.GLOBAL_FUNCS["execute_expr"](line, state, local=local)
                
            
            lexic = line.split()
            if len(lexic) <= 0:
                continue

            state.GLOBAL_FUNCS["execute_line"](lexic, state, local=local)

            if state.last_return != None:
                return None

        full_vars = {**state.vars, **(local if local != None else {})}