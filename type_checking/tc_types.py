from bin_types.list import List

class TypeCheckedFunction:
    """
    Class, that represents function while type checking
    Contains types for all arguments, local variables and return type
    """
    def __init__(self, oper, args, ret=object):
        self.args : list[tuple[str:type]] = args
        self.ret : type = ret
        self.oper = oper

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
            "input" : (str,),
            "output" : (None, str),
            "convert" : (object, object, None),
            "and_" : (int, object, object),
            "or_" : (int, object, object),
            "not_" : (int, object),
            "index" : (object, (List, str), int),
            "setindex" : (None, List, int, object),
            "len" : (int, (List, str)),
            "append" : (None, List, object),
            "zip" : (List, List, List),
            "if_" : (None, object),
            "else_" : (None,),
            "for_" : (None, None, (List, str)),
            "while_" : (None, object),
            "break_" : (None,),
            "continue_" : (None,),
            "func" : (None,),
            "return_" : (None, object),
        }

        self.operations : tuple[str] = (
            "+", "-", "*", "/", "**", "%", ">", "<", ">=", "<=", "==", "!="
        )
        self.int_operations : tuple[str] = (">", "<", ">=", "<=", "==", "!=")
        self.float_operations : tuple[str] = ("/")
        self.iter_operations : tuple[str] = state.iter_operations
        self.diff_types_operations : tuple[str] = state.diff_types_operations

    def reset(self):
        """Resets data beetween two stages of type checking"""
        self.opened_function : TypeCheckedFunction = None

        self.current_line : int = 0