from __future__ import annotations

class List(list):
    """List in binarian"""
    @staticmethod
    def convert_lists(lst : list | List) -> list | List:
        res = []
        if isinstance(lst, List):
            for i in lst:
                if isinstance(i, List):
                    res.append(List.convert_lists(i))
                else:
                    res.append(i)
            return res
        else:
            for i in lst:
                if isinstance(i, list):
                    res.append(List.convert_lists(i))
                else:
                    res.append(i)
            return List(res) 

    def __str__(self) -> str:
        res = "["
        for i in self:
            if not isinstance(i, str):
                res += str(i) + " "
            else:
                res += f"\"{i}\"" + " "
        return res[:-1] + "]"