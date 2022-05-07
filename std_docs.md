# Standart library
# Table of contents
* [Operators](#operators)
  * [xor](#xor)
* [Input/Output](#inputoutput)
  * [print](#print)
* [Type convertions shortcuts](#type-convertions-shortcuts)
  * [to_int](#to_int)
  * [to_float](#to_float)
  * [to_str](#to_str)
  * [to_list](#to_list)
* [Additional functions](#additional-functions)
  * [join](#join)
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

# Additional functions
  ## sum
  Return type : int
  
  Sums all numbers in list, in list format. Returns sum of them in list format.

  Arguments :
  * num1 : list
  * num2 : list

  ## join
  Return type : str
  
  Joins list of elements to one string with `sep` beetwen elements. All elements are converted to str.

  Arguments :
  * list_ : list
  * sep : str