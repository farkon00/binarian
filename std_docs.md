# Standard library
# Table of contents
* [Operators](#operators)
  * [xor](#xor)
* [Input/Output](#inputoutput)
  * [output](#output)
  * [print](#print)
  * [try_input_int](#tryinputint)
  * [Variables](#variables)
* [Math](#math)
  * [ceil](#ceil)
  * [math_to_int](#mathtoint)
  * [Variables](#variables-1)
* [Type convertions shortcuts](#type-convertions-shortcuts)
  * [to_int](#toint)
  * [to_float](#tofloat)
  * [to_str](#tostr)
  * [to_list](#tolist)
  * [to_tuple](#totuple)
* [Pyeval](#pyeval)
  * [execute_method](#executemethod)
  * [execute_function](#executefunction)
  * [get_module](#getmodule)
  * [get_attr](#getattr)
  * [set_attr](#setattr)
  * [has_attr](#hasattr)
  * [safe_get_attr](#safegetattr)
  * [throw_exception](#throwexception)
  * [assert](#assert)
  * [is_instance](#isinstance)
  * [type_of](#typeof)
  * [open](#open)
  * [read](#read)
  * [write](#write)
  * [close](#close)
  * [random](#random)
  * [random_range](#randomrange)
  * [exit](#exit)
  * [Variables](#variables-2)
* [Str functions](#str-functions)
  * [join](#join)
  * [is_numeric](#isnumeric)
* [List functions](#list-function)
  * [len](#len)
  * [in](#in)
  * [sum](#sum)

# Operators
  ## xor
  Return type : int
  
  Logical xor operator.

  Arguments :
  * num1 : int
  * num2 : int

# Input/Output
  ## output
  Return type : int
  
  Writes str to stdout. Returns how many characters was written.

  Arguments :
  * text : str

  ## print
  Return type : int

  Writes object, converted to str, to stdout and puts \n at the end. Returns how many characters was printed.

  Arguments :
  * value : obejct

  ## try_input_int
  Return type : list(always length 2)
  
  Inputs integer from user, before input outputs `tip`. Returns list of two integers, first integer represents was converting to intger successful(1 if was successful, if not 0) and parsed integer, 0 if parsing wasnt successful.

  Arguments :
  * tip : str

  ## Variables
  sys
  ---
  Python sys library

  stdout
  ---
  Standard output, can be changed to any writable object(mostly file), so [output](#output) will write to this stdout.

# Math
  ## ceil
  Return type : int
  
  Return the ceiling of x, the smallest integer greater than or equal to x.

  Arguments :
  * val : object

  ## math_to_int
  Return type : int
  
  Regular to_int works like floor, this funtion uses standard mathematical way to round number with decimal point to integer.

  Arguments :
  * val : object

  ## Variables
  math
  ---
  Math module from python. Check [Pyeval](#pyeval) for more details.

  pi
  ---
  Float pi number

# Type convertions shortcuts
  ## to_int
  Return type : int
  
  Shortcut for `(convert val int)`.

  Arguments :
  * val : object

  ## to_float
  Return type : float
  
  Shortcut for `(convert val float)`.

  Arguments :
  * val : object

  ## to_str
  Return type : str
  
  Shortcut for `(convert val str)`.

  Arguments :
  * val : object

  ## to_list
  Return type : list
  
  Shortcut for `(convert val list)`.

  Arguments :
  * val : object

  ## to_tuple
  Return type : object
  
  Converts list top python tuple.

  Arguments :
  * val : list

# Pyeval
  ## execute_method
  Return type : object
  
  Executes python method with name `method` on `obj` with args(unpacks list as args). Returns return of method, if returned None, returs 0.

  Arguments :
  * obj : object
  * method : str
  * args : list

  ## execute_function
  Return type : object
  
  Executes python function with name `func_` with args(unpacks list as args). Returns return of function, if returned None, returs 0.

  Arguments :
  * func_ : str
  * args : list

  ## get_module
  Return type : object
  
  Imports and returns module with name `module` 

  Arguments :
  * module : str

  ## get_attr
  Return type : object
  
  Returns attribute with name `attr` of object `obj`, will give python error if attribute was not found.

  Arguments :
  * obj : object
  * attr : str

  ## set_attr
  Return type : None
  
  Sets attribute with name `attr` of object `obj` to `value`.

  Arguments :
  * obj : object
  * attr : str
  * value : object

  ## has_attr
  Return type : int
  
  Returns 1 if `obj` has attribute with name `attr`, else returns 0.

  Arguments :
  * obj : object
  * attr : str

  ## safe_get_attr
  Return type : object
  
  Returns attribute with name `attr` of object `obj`, if there is attribute with name `attr` on object `obj`, will return -1, if attribute was not found.

  Arguments :
  * obj : object
  * attr : str

  ## throw_exception 
  Return type : int
  
  Throws regular binarian exception with message `message`. 

  Arguments :
  * message : str

  ## assert
  Return type : int
  
  Throws regular binarian exception with message `message` if condition is 1. Retunrs condition.

  Arguments :
  * condition : int
  * message : str

  ## is_instance
  Return type : int
  
  Returns 1 if `obj` is of type with name `type`(names will be processed with python). 

  Arguments :
  * obj : object
  * type : str

  ## type_of
  Return type : object
  
  Returns type of obj.

  Arguments :
  * obj : object

  ## construct
  Return type : object
  
  Creates object of type `type_` and returns its instance. Gives arguments args to constructor.

  Arguments :
  * type_ : object
  * args : list

  ## open
  Return type : object
  
  Returns file object with name `file`.

  Arguments :
  * file : str
  * mode : str
  
  ## write
  Return type : int
  
  Writes to file with mode "a" or "w". Returns number of characters written.

  Arguments :
  * file : object
  * str_ : str

  ## read
  Return type : int
  
  Returns all text in file with mode "r".

  Arguments :
  * file : object

  ## close
  Return type : int
  
  Closes file.

  Arguments :
  * file : object

  ## random
  Return type : float
  
  Returns pseudo-random float beetwen 0 and 1.

  **This function shouldnt be used for cryptography**

  ## random_range
  Return type : int
  
  Returns pseudo-random float beetwen `min` and `max` including only first endpoint.

  **This function shouldnt be used for cryptography**

  Arguments :
  * min : int
  * max : int

  ## exit
  Return type : int
  
  Exits with exit code `code`

  Arguments :
  * code : int

  ## Variables
  None/null
  ---
  Function epresenting None from python. **This works really bad with return**

# Str functions
  ## join
  Return type : str
  
  Joins list of elements to one string with `sep` beetwen elements. All elements are converted to str.

  Arguments :
  * list_ : list
  * sep : str

  ## replace
  Return type : str
  
  Replaces all `old` characters with `new` string in string `str_` and returns it. Old mush be 0-1 characters string.

  Arguments :
  * str_ : str
  * old : str
  * new : str

  ## is_numeric
  Return type : int
  
  Returns 1 if str can be converted to integer.

  Arguments :
  * string : str

# List function
  ## len
  Return type : int
  
  Returns length of str/list.

  Arguments :
  * iter : object

  ## map
  Return type : list
  
  Returns new list, where all elements are return values of function `callback` with 1st argument as element of list.

  Arguments :
  * list_ : list
  * callback : function

  ## filter
  Return type : list
  
  Returns new list, where all elements, will return true if you call `callback` with 1st argument as element of list. Other elements are elemenated from new list.

  Arguments :
  * list_ : list
  * callback : function

  ## in
  Return type : int
  
  Returns 1 if element is in list.

  Arguments :
  * val : object
  * _list : list

  ## sum
  Return type : int
  
  Sums all numbers in list, in list format. Returns sum of them in list format.

  Arguments :
  * num1 : list
  * num2 : list
