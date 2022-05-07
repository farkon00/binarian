# Standart library
# Table of contents
* [Operators](#operators)
  * [xor](#xor)
* [Input/Output](#inputoutput)
  * [print](#print)
  * [try_input_int](#try_input_int)
* [Math](#math)
  * [ceil](#ceil)
  * [math_to_int](#to_int)
* [Type convertions shortcuts](#type-convertions-shortcuts)
  * [to_int](#to_int)
  * [to_float](#to_float)
  * [to_str](#to_str)
  * [to_list](#to_list)
* [Str functions](#str-functions)
  * [join](#join)
  * [is_numeric](#is_numeric)
* [List functions](#list-function)
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
  ## print
  Return type : int(always 0)
  
  Writes object, converted to str, to stdout and puts \n at the end.

  Arguments :
  * value : obejct

  ## try_input_int
  Return type : list(always length 2)
  
  Inputs integer from user, before input outputs `tip`. Returns list of two integers, first integer represents was converting to intger successful(1 if was successful, if not 0) and parsed integer, 0 if parsing wasnt successful.

  Arguments :
  * tip : str

# Math
  ## ceil
  Return type : int
  
  Return the ceiling of x, the smallest integer greater than or equal to x.

  Arguments :
  * val : object

  ## math_to_int
  Return type : int
  
  Regular to_int works like floor, this funtion uses standart mathematical way to round number with decimal point to integer.

  Arguments :
  * val : object

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

# Str functions
  ## join
  Return type : str
  
  Joins list of elements to one string with `sep` beetwen elements. All elements are converted to str.

  Arguments :
  * list_ : list
  * sep : str

  ## is_numeric
  Return type : int
  
  Returns 1 if str can be converted to integer.

  Arguments :
  * string : str

# List function
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