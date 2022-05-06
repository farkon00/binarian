class List(list):
    """List in binarian"""
    def __str__(self) -> str:
        res = "["
        for i in self:
            if not isinstance(i, str):
                res += str(i) + " "
            else:
                res += f"\"{i}\"" + " "
        return res[:-1] + "]"