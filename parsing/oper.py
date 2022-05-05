from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto

class OpIds(Enum):
    operation = auto()
    value = auto()
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
    len_ = auto()
    append = auto()
    zip_ = auto()
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

@dataclass
class Oper:
    id: auto
    args: list[Oper | object] # object is for value operation
    oper: list[Oper] = []