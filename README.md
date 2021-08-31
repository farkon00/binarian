# Binarian
# Content
  * [Global info](#global-info)
  * [Basic syntax](#basic-syntax)
  * [Keywords](#keywords)
    * [Base keywords](#base-keywords)
      * [set](#set)
      * [input](#input)
      * [output](#output)
      * [and](#and)
      * [or](#or)
      * [not](#not)

# Global info
  Original compilers are written in python 3.10rc1. I or other peoples will update compilers to new versions of python.

  Exe file will be released when stable version of python 3.10 is released.
  
  I have 2 version of conpilers high level and main compiler. 
  High level contains additional keywords(xor, xnor, nor, nand).
  Main compiler contains onle base keywords.

# Basic syntax
  All syntax is based on keywords and arguments. 
  ```
  keyword arg1 arg2(not for all keywords)
  ```
  All keywords except [not](#not) and [input](#input) takes second argument. This 2 keywords take only 1 argument.
  
  To reference variable you must type name of it. 
  
# Keywords
  ## Base keywords
   ### set
   Syntax : `set var_name value`
   
   This keyword uses to assign or change value of variables.
   
   value must be 1 or 0.
   var_name writing without " or '.
   You can't use this keyword in expression.
   
   Example : 
   ```
   set var1 1
   set var2 1
   and var1 var2
   or 0 var1
   ```
   
   ### input
   Syntax : `input var_name`
   
   This keyword uses to input data from keyboard. In console user will see 'var_name : <user input here>'. Keyword assign variable with name var_name.
  
   Inputed value must be 1 or 0.
   var_name writing without " or '.
   You can't use this keyword in expression.
   
   Example : 
   ```
   input inp0
   input some_name
   or inp0 some_name
   ```
  
   ### output
   Syntax : `output value user_tip`
   
   This keyword uses to output data to user. In console user will see 'user_tip : value'.

   user_tip writing without " or '.
   You can't use this keyword in expression.
   
   Example : 
   ```
   set val1 1
   output val1 Hi! // Hi! : 1
   output 0 Its_zero // Its_zero : 0
   ```
  
   ### and
   Syntax : `and val1 val2`
   
   Boolean logical operator and.

   Values must be 1 or 0.
   If keyword using in expression, expression will replaced by result. Else in console will be printed keyword output.
   
   Example : 
   ```
   input i1
   input i2
   and i1 i2
   set var1 {and i1 1}
   ```
  
   ### or
   Syntax : `or val1 val2`
   
   Boolean logical or operator.

   Values must be 1 or 0.
   If keyword using in expression, expression will replaced by result. Else in console will be printed keyword output.
   
   Example : 
   ```
   input i1
   input i2
   or i1 i2
   set var1 {or i1 i2}
   ```
  
   ### not
   Syntax : `not val`
   
   Boolean logical or operator.

   Value must be 1 or 0.
   If keyword using in expression, expression will replaced by result. Else in console will be printed keyword output.
   
   Example : 
   ```
   input i1
   input i2
   not i1
   set var1 {not {or i1 i2}} // nor analogue
   ```
  

