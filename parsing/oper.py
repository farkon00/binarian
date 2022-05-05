from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Iterable

class OpIds(Enum):
    operation = auto()
    value = auto()
    variable = auto()
    var = auto()
    drop = auto()
    input = auto()
    output = auto()
    convert = auto()
    and_ = auto()
    or_ = auto()
    not_ = auto()
    index = auto()
    setindex = auto()
    len = auto()
    append = auto()
    zip = auto()
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
    def __init__(self, id: OpIds, args: list[Oper | object] = None, oper: list[Oper] = None):
        if args is None:
            args = []
        elif not isinstance(args, list | tuple):
            args = [args]
        if oper is None:
            oper = []
        self.id = id
        self.args = args
        self.oper = oper

    def __str__(self):
        new = "\n"
        return\
f"""(
    "id": {self.id.name},
    "args": {new.join([str(i) for i in self.args])}
    "oper": {new.join([str(i) for i in self.oper])}
),"""