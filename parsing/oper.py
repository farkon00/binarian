from __future__ import annotations

from enum import Enum, auto

class OpIds(Enum):
    operation = auto()
    value = auto()
    variable = auto()
    var = auto()
    drop = auto()
    input = auto()
    output = auto()
    convert = auto()
    pyeval = auto()
    and_ = auto()
    or_ = auto()
    not_ = auto()
    index = auto()
    setindex = auto()
    append = auto()
    if_ = auto()
    else_ = auto()
    elif_ = auto()
    for_ = auto()
    while_ = auto()
    break_ = auto()
    continue_ = auto()
    func = auto()
    return_ = auto()
    call = auto()

class Oper:
    def __init__(self, id: OpIds, line: int, args: list[Oper | object] = None,
     oper: list[Oper] = None, types : list[type] = None):
        if args is None:
            args = []
        elif not isinstance(args, list | tuple):
            args = [args]
        if oper is None:
            oper = []
        if types is None:
            types = []
        elif not isinstance(types, list | tuple):
            types = [types]

        self.id = id
        self.args = args
        self.oper = oper
        self.types = types
        self.line = line

    def __str__(self):
        new = "\n"
        return\
f"""(
    "id": {self.id.name},
    "args": {new.join([str(i) for i in self.args])}
    "oper": {new.join([str(i) for i in self.oper])},
    "types": {self.types}
),"""