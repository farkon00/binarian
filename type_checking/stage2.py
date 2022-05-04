from funcs.blocks_parser import *
from funcs.exceptions import binarian_assert
from funcs.utils import *
from .get_type import get_type

def tc_line2(lexic : str, state):
    """Executes 2 stage of type checking for 1 keyword"""
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
        # Check types
        exp_type = type_to_str((float, int))

        if get_type(lexic[1], state, full_vars) not in (object, None):
            binarian_assert(not issubclass(get_type(lexic[1], state, full_vars), float | int),
f"Unexpected operation argument type, {exp_type} was expected, \
{type_to_str(get_type(lexic[1], state, full_vars))} found.", state
            )
        if get_type(lexic[2], state, full_vars) not in (object, None):
            binarian_assert(not issubclass(get_type(lexic[2], state, full_vars), float | int),
f"Unexpected operation argument type, {exp_type} was expected, \
{type_to_str(get_type(lexic[2], state, full_vars))} found.", state
            )

        # Returns type
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
        case "var":
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
                binarian_assert(parts[0][1] not in state.types, f"Type is not found : {lexic[1]}", state)
                if (get_type(parts[1][0], state, full_vars) and get_type(parts[0][2], state, full_vars)) and\
                object not in (get_type(parts[1][0], state, full_vars), get_type(parts[0][2], state, full_vars)):
                    binarian_assert(
                        not issubclass(get_type(parts[1][0], state, full_vars), get_type(parts[0][2], state, full_vars)),
f"Unmatching types, {type_to_str(get_type(parts[0][2], state, full_vars))} was expected, \
{type_to_str(get_type(parts[1][0], state, full_vars))} found.",
                        state
                    )
            else:
                if get_type(parts[1][0], state, full_vars) and get_type(parts[0][1], state, full_vars) and\
                object not in (get_type(parts[1][0], state, full_vars), get_type(parts[0][1], state, full_vars)):
                    binarian_assert(
                        not issubclass(get_type(parts[1][0], state, full_vars), get_type(parts[0][1], state, full_vars)),
f"Unmatching types, {type_to_str(get_type(parts[0][1], state, full_vars))} was expected, \
{type_to_str(get_type(parts[1][0], state, full_vars))} found.",
                        state
                    )

        case "convert":
            binarian_assert(len(lexic) < 3, "Not enought arguments for convert", state)
            return get_type(lexic[2], state, {}, True)

        case "func":
            parts = " ".join(lexic).split(":", 1)
            if len(parts[0].split()) >= 3:
                name = parts[0].split()[2]
            else:
                name = parts[0].split()[1]

            state.opened_function = state.functions[name]
            state.function_blocks = state.opened_blocks

        case "return":
            binarian_assert(not is_func, 'Keyword "return" is restricted out of functions.', state)
            if get_type(lexic[1], state, full_vars) and state.opened_function.ret and\
                object not in (get_type(lexic[1], state, full_vars), state.opened_function.ret):
                binarian_assert(
                    not issubclass(get_type(lexic[1], state, full_vars), state.opened_function.ret),
f"Unexpected return type, {type_to_str(state.opened_function.ret)} was expected, \
{type_to_str(get_type(lexic[1], state, full_vars))} found",
                    state
                )

        case _:
            if lexic[0] in state.keywords:
                keyword = state.keywords[lexic[0]]

                for j, i in enumerate(keyword[1:]):
                    if not i or not get_type(lexic[j+1], state, full_vars) or object in (i, get_type(lexic[j+1], state, full_vars)):
                        continue
                    binarian_assert(
                        not issubclass(get_type(lexic[j+1], state, full_vars), i),
f"Unexpected argument type, {type_to_str(i)} was expected, \
{type_to_str(get_type(lexic[j+1], state, full_vars))} found.",
                        state
                    ) 

                return keyword[0]

            if lexic[0] in state.functions:
                for j, i in enumerate(state.functions[lexic[0]].args):
                    if not i or not get_type(lexic[j+1], state, full_vars) or object in (i, get_type(lexic[j+1], state, full_vars)):
                        continue
                    binarian_assert(
                        not issubclass(get_type(lexic[j+1], state, full_vars), i[1]),
f"Unexpected argument type for {i[0]}, {type_to_str(i[1])} was expected, \
{type_to_str(get_type(lexic[j+1], state, full_vars))} found.",
                        state
                    ) 

                return state.functions[lexic[0]].ret

            state.warnings += 1

def tc_expr2(line : str, state):
    """Executes 2 stage of type checking for expression"""
    indexes = parse_brackets(line, ("(", ")"), state)

    if not indexes:
        return
    start_ind, end_ind = indexes

    lexic = line[start_ind+1:end_ind].split()

    return line[:start_ind] + type_to_str(tc_line2(lexic, state)) + line[end_ind+1:]