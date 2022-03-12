class List(list):
    """List in binarian"""
    def __str__(self):
        return f"[{' '.join([str(i) for i in self])}]"

    def __int__(self):
        """Converts binarian list from binary to decimal int"""
        return sum([2 ** j * i for j, i in enumerate(self[::-1])])