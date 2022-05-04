from bin_types.list import List

class TypeCheckedFunction:
    """
    Class, that represents function while type checking
    Contains types for all arguments, local variables and return type
    """
    def __init__(self, args, ret=object):
        self.args : list[tuple[str:type]] = args
        self.ret : type = ret

        self.locals : dict[str : type] = {i : j for i, j in args}

class TypeCheckingState:
    """Class that contains all data about type checking state"""
    def __init__(self, state):
        self.vars : dict[str : type] = {}
        self.functions : dict[str : TypeCheckedFunction] = {}

        self.reset()

        self.warnings : int = 0

        self.code : str = state.code
        self.lines : list[str] = state.lines
        self.std_lines : int = state.std_lines

        self.call_stack : list[tuple[str, int]] = [] # For throw_exception function to work, unused anywhere else

        self.types : dict[str : type] = state.types

        # (return, *arguments)
        # None  - not typechecked(e. g. name of var)
        self.keywords : dict[str : tuple[type]] = {
            "drop" : (None,),
            "input" : (None, None),
            "output" : (None, object, None),
            "convert" : (object, object, None),
            "and" : (int, object, object),
            "or" : (int, object, object),
            "not" : (int, object),
            "index" : (object, List, int),
            "setindex" : (None, List, int, object),
            "len" : (int, List),
            "append" : (None, List, object),
            "zip" : (List, List, List),
            "if" : (None, object),
            "for" : (None, None, List),
            "while" : (None, object),
            "func" : (None,),
            "return" : (None, object),
        }

        self.operations : tuple[str] = (
            "+", "-", "*", "/", "**", "%", ">", "<", ">=", "<=", "==", "!="
        )
        self.int_operations : tuple[str] = (">", "<", ">=", "<=", "==", "!=")
        self.float_operations : tuple[str] = ("/")

    def reset(self):
        """Resets data beetween two stages of type checking"""
        self.opened_function : TypeCheckedFunction = None
        self.function_blocks : int = None

        self.current_line : int = 0
        self.opened_blocks : int = 0
        self.allowed_blocks : int = 0 # For parse_blocks function to work, unused anywhere else