"""
If you are using Pylance in VS Code I strongly
recomend to disable showing missing imports in settings.
Pylance is a little bit stupid and does not understand complicated imports.

Just add this to settings.json :
"python.analysis.diagnosticSeverityOverrides": { 
    "reportMissingImports" : "none",
}
"""

from .log_oper import *
from .var_keyw import *
from .io_keyw import *
from .func_keyw import *
from .oper_keyw import *
from .lists_keyw import *
from .loop_keywords import *