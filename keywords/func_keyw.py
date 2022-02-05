import sys
sys.path.append(".")

from Function import Function

from .check_args import check_args

def func_keyword(lexic : list[str], i : int, state, in_vars : dict[str : int]):
    if state.is_expr:
        raise SyntaxError(f"This operation is unavailable in expressions. Line : {i + 1}")
    if lexic[1] in state.RESTRICTED_NAMES:
        raise NameError(f"Function name is unavailable. Line : {i + 1}")

    parts = " ".join(lexic).split(":")

    func_name = parts[0].split()[1]
    try:
        args = parts[1].split()
    except:
        args = []

    if "(" in args: args.remove("(")
    if ")" in args: args.remove(")")
    if "()" in args: args.remove("()")

    in_vars[func_name] = Function(args, i)

def call_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]):
    args = lexic[2:]
    check_args(args, i)

    # Error handeling
    if lexic[1] in full_vars.keys():
        if isinstance(full_vars[lexic[1]], Function):
            if len(full_vars[lexic[1]].args) != len(args):
                raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")
        else:
            raise TypeError(f"This object is not callable. Line : {i + 1}")
    else:
        raise NameError(f"Function is not found. Line : {i + 1}")

    return full_vars[lexic[1]].execute(args, i, state)

def return_keyword(lexic : list[str], i : int, is_func : bool):
    check_args((lexic[1]), i)

    # Error handeling
    if not is_func:
        raise SyntaxError(f'Keyword "return" is restricted out of functions. Line : {i + 1}')

    return int(lexic[1])