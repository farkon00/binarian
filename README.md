# Binarian
# Content
  * [Global info](#global-info)
  * [Basic syntax](#basic-syntax)
   * [Expressions](#expressions)
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
  
  All files with code on binarian have extension .bino.

  Exe file will be released when stable version of python 3.10 is released.
  
  I have 2 version of conpilers high level and main compiler. 
  High level contains additional keywords(xor, xnor, nor, nand).
  Main compiler contains onle base keywords.
  
  To run your code, run python file(compiler.py or high_level.py). Also you can add debug after file name to see variable in the end of executing.
  
  Examples :
  ```
  python compiler.py your_file.bino
  python3 high_level.py your_file.bino
  python3.10 high_level.py your_file.bino debug
  python3 compiler.py other_file.bino debug
  ```

# Basic syntax
  All syntax is based on keywords and arguments. 
  ```
  keyword1 arg1 arg2(not for all keywords)
  keyword2 arg1 arg2(not for all keywords)
  keyword3 arg1
  ```
  All keywords except [not](#not) and [input](#input) takes second argument. This 2 keywords take only 1 argument.
  
  To reference variable you must type name of it. 
  
  To write comments use '//'. All symbols in line after '//' will be matched as comments.
  
  ## Expressions
   Expressions is lines in lines. But logical operators not make auto output, they will be replaced by result. Also you can't use set, input and output in expressions.
   Syntax : 
   ```
   keyword {keyword arg {keyword arg arg}} arg
   ```
   
   Example :
   ```
   input var1
   input var2
   output {and var1 {not var2}}
   ```
  
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
   
   Boolean logical operator or.

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
   
   Boolean logical operator not.

   Value must be 1 or 0.
   If keyword using in expression, expression will replaced by result. Else in console will be printed keyword output.
   
   Example : 
   ```
   input i1
   input i2
   not i1
   set var1 {not {or i1 i2}} // nor analogue
   ```
  ## Additional keywords
   ### nand 
   Syntax : `nand val1 val2`
   
   Boolean logical operator nand.

   Values must be 1 or 0.
   If keyword using in expression, expression will replaced by result. Else in console will be printed keyword output.
   
   Example : 
   ```
   input i1
   input i2
   nand i1 i2
   set var1 {nand i1 1}
   ```
 
   ### nor
   Syntax : `nor val1 val2`
   
   Boolean logical operator nor.

   Values must be 1 or 0.
   If keyword using in expression, expression will replaced by result. Else in console will be printed keyword output.
   
   Example : 
   ```
   input i1
   input i2
   nor i1 i2
   set var1 {nor i1 i2}
   ```
 
   ### xor
   Syntax : `xor val1 val2`
   
   Boolean logical operator xor.

   Values must be 1 or 0.
   If keyword using in expression, expression will replaced by result. Else in console will be printed keyword output.
   
   Example : 
   ```
   input i1
   input i2
   xor i1 i2
   set var1 {xor i1 i2}
   ```
 
   ### xnor
   Syntax : `xnor val1 val2`
   
   Boolean logical operator xnor.

   Values must be 1 or 0.
   If keyword using in expression, expression will replaced by result. Else in console will be printed keyword output.
   
   Example : 
   ```
   input i1
   input i2
   xnor i1 i2
   set var1 {xnor i1 i2}
   ```
