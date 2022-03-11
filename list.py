class List(list):
    """List in binarian"""
    def __str__(self):
        return f"[{' '.join([str(i) for i in self])}]"