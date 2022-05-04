# Standart library
# Table of contents
* [Operators](#operators)
  * [xor](#xor)
  * [list-eq](#list-eq)
* [Additional functions](#additional-functions)
  * [floor](#floor)
  * [sum](#sum)

# Operators
  ## xor
  Return type : int
  
  Logical xor operator.

  Arguments :
  * num1 : int
  * num2 : int

  ## list-eq
  Return type : int
  
  Returns 1 if all elements in `list1` is the same at in `list2`, else returns 0.

  Arguments :
  * list1: list
  * list2: list

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