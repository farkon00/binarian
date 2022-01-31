import sys
sys.path.append( '.' )

from Function import Function

from .check_args import check_args

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