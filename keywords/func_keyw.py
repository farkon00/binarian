import sys
sys.path.append( '.' )

from Function import Function

from .check_args import check_args

def func_keyword(lexic : list[str], i : int, code : str, in_vars : dict[str : int], block_indexes : list[tuple[int, int]]):
    parts = " ".join(lexic).split(":")

    func_name = parts[0].split()[1]
    try:
        args = parts[1].split()
    except:
        args = []

    func_index = len("\n".join(code.split("\n")[:i+1]))-1

    # Finding nearest block for tha function
    block = block_indexes[0]
    for j in block_indexes:
        if func_index > j[0]:
            if j[0] < block[0]:
                block = j

    if not code[func_index:block[1]].split():
        raise SyntaxError(f"Between nearest block and function declaration code was found. Line : {i+1}")

    func_code = code[block[0]:block[1]]

    in_vars[func_name] = Function(args, func_code)

def call_keyword(lexic : list[str], i : int, full_vars : dict[str : int]):
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

    return full_vars[lexic[1]].execute(args, i)

def return_keyword(lexic : list[str], i : int, is_func : bool):
    check_args((lexic[1]), i)

    # Error handeling
    if not is_func:
        raise SyntaxError(f'Keyword "return" is restricted out of functions. Line : {i + 1}')

    return int(lexic[1])