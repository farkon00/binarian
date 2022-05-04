from funcs.blocks_parser import *
from funcs.exceptions import binarian_assert
from funcs.utils import *
from .get_type import get_type
from .tc_types import TypeCheckedFunction

def tc_line1(lexic : list[str], state):
    """Executes 1 stage of type checking for 1 keyword"""
    is_func = bool(state.opened_function)
    local = state.opened_function.locals if is_func else {}
    full_vars = {**state.vars, **local}

    line = parse_blocks(" ".join(lexic), state)
    lexic = line.split()
    lexic = parse_lists(lexic)

    if state.opened_function:
        if state.opened_blocks <= state.function_blocks - 1:
            state.opened_function = None
            state.function_blocks = None

    if len(lexic) <= 0:
        return None

    if lexic[0] in state.operations:
        if lexic[0] in state.int_operations:
            return int
        elif lexic[0] in state.float_operations:
            return float
        elif issubclass(get_type(lexic[1], state, full_vars), float) or\
         issubclass(get_type(lexic[2], state, full_vars), float):
            return float
        else:
            return int

    match lexic[0]:
        case "set":
            if is_func:
                if len(lexic) >= 4:
                    binarian_assert(lexic[1] not in state.types, f"Type is not found : {lexic[1]}", state)
                    local[lexic[2]] = state.types[lexic[1]]
                elif lexic[1] not in local:
                    local[lexic[1]] = get_type(lexic[2], state, full_vars)
            else:
                if len(lexic) >= 4:
                    binarian_assert(lexic[1] not in state.types, f"Type is not found : {lexic[1]}", state)
                    state.vars[lexic[2]] = state.types[lexic[1]]

                    if lexic[3] in state.functions:
                        state.functions[lexic[2]] = lexic[3]

                else:
                    if lexic[1] not in state.vars:
                        state.vars[lexic[1]] = get_type(lexic[2], state, full_vars)

                    if lexic[2] in state.functions:
                        state.functions[lexic[1]] = lexic[2]

        case "input":
            if is_func:
                local[lexic[1]] = int
            else:
                state.vars[lexic[1]] = int

        case "func":
            parts = " ".join(lexic).split(":", 1)
            if len(parts[0].split()) >= 3:
                ret = parts[0].split()[1]
                binarian_assert(ret not in state.types, f"Type is not found : {lexic[1]}", state)
                ret = state.types[ret]
                name = parts[0].split()[2]
            else:
                ret = object
                name = parts[0].split()[1]

            args = []
            if len(parts) >= 2:
                args_text = parts[1].split()
                for i in args_text:
                    if ":" in i:
                        arg_splited = i.split(":")
                        binarian_assert(arg_splited[1] not in state.types, f"Type is not found : {arg_splited[1]}", state)
                        args.append((arg_splited[0], state.types[arg_splited[1]]))
                    else:
                        args.append((i, object))

            func = TypeCheckedFunction(args[:-1], ret)
            state.functions[name] = func
            state.opened_function = func
            state.function_blocks = state.opened_blocks

        case _:
            if lexic[0] in state.keywords:
                keyword = state.keywords[lexic[0]]

                return keyword[0]

            if lexic[0] in state.functions:
                return state.functions[lexic[0]].ret

            state.warnings += 1


def tc_expr1(line : str, state):
    """Executes 1 stage of type checking for expession"""
    indexes = parse_brackets(line, ("(", ")"), state)

    if not indexes:
        return
    start_ind, end_ind = indexes

    lexic = line[start_ind+1:end_ind].split()

    return line[:start_ind] + type_to_str(tc_line1(lexic, state)) + line[end_ind+1:]