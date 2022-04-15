from bin_types.list import List

class TypeCheckedFunction:
    def __init__(self, args, ret=object):
        self.args : list[tuple[str:type]] = args
        self.ret = ret

        self.locals = {i : j for i, j in args}

class TypeCheckingState:
    def __init__(self, state):
        self.vars : dict[str : type] = {}
        self.functions : dict[str : TypeCheckedFunction] = {}

        self.reset()

        self.warnings : int = 0

        self.code : str = state.code
        self.lines : list[str] = state.lines
        self.std_lines : int = state.std_lines

        self.call_stack = [] # For throw_exception function to work, unused anywhere else

        self.types : dict[str : type] = state.types

        # (return, *arguments)
        # None  - not typechecked(e. g. name of var)
        self.keywords : dict[str : tuple[type]] = {
            "drop" : (None,),
            "input" : (None, None),
            "output" : (None, object, None),
            "and" : (object, object, int),
            "or" : (object, object, int),
            "not" : (object, int),
            "index" : (object, List, List),
            "setindex" : (None, List, List, object),
            "len" : (List, List),
            "append" : (None, List, object),
            "zip" : (List, List, List),
            "if" : (None, int),
            "for" : (None, None, List),
            "while" : (None, int),
            "func" : (None,),
            "return" : (None, object),
        }

        self.operations = ("+", "-", "*", "/", "**", "%")
        self.int_operations = ()
        self.float_operations = ("/")

    def reset(self):
        self.opened_function = None
        self.function_blocks : int = None

        self.current_line : int = 0
        self.opened_blocks : int = 0
        self.allowed_blocks : int = 0 # For parse_blocks function to work, unused anywhere else