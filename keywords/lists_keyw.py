from get_var import get_var
from list import List

def index_keyword(lexic : list[str], i : int, state, full_vars : dict[str : int]):
    if len(lexic) <= 2:
        raise SyntaxError(f"You didn`t give enough arguments. Line : {i + 1}")

    index = int(get_var(lexic[2], i, full_vars, List))
    list = get_var(lexic[1], i, full_vars, List)
    if index >= len(list):
        raise IndexError(f"Index out of range. Line : {i + 1}")

    if not state.is_expr:
        print(f"INDEX output : {list[index]}. Line : {i + 1}")
    else:
        return list[index]