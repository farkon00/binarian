# Binarian
# Content
  * [Global info](#global-info)
  * [Basic syntax](#basic-syntax)
    * [Expressions](#expression)
    * [Functions](#functions)
  * [Keywords](#keywords)
    * [Special keywords](#special-keywords)
      * [set](#set)
      * [input](#input)
      * [output](#output)
    * [Logical operators keywords](#logical-operators-keywords)
      * [and](#and)
      * [or](#or)
      * [not](#not)
    * [Functions keywords](#functions-keywords)
      * [func](#func)
      * [call](#call)
      * [return](#return)

# Global info
  Original compilers are written in python 3.10.
  
  All files with code on binarian have extension .bino.
  
  To run your code, run python file(binarian.py) or executable(binarian.exe). Also you can add -d flag after file name to see variable in the end of execution.
  
  Examples :
  ```
  python compiler.py your_file.bino
  python3 compiler.py your_file.bino
  python3.10 compiler.py your_file.bino -d
  python3 compiler.py other_file.bino -d
  binarian.exe your_file.bino
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
  
  To write comments use '//'. All symbols in line after '//' will be marked as comments.
  
  ## Expression
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
   
  ## Functions
  To create function use [func](#func) keyword is global scope. Inline functions are unavaliable for now.
  To call function use [call](#call) keyword. To get return value of function put call in expression.
  To return value use [return](#return) keyword. If fucntion don\`t return any value, it will return 0.
  
  If any variable was registred in function, it will become local. So it\`s unavailable in global scope, other functions and other functions calls. Arguments is local too.
  
  Example :
  ```
  func name : arg1 arg2 (
    not arg1
    
    input inp1
    output {and inp1 arg1} output
    
    return {and arg1 arg2}
  )
  ```
  
# Keywords
  ## Special keywords
   ### set
   Syntax : `set var_name value`
   
   This keyword uses to assign or change value of variables.
   
   Value must be 1 or 0.
   var_name writing without " or '.
   You can't use this keyword in expression.
   Variable name can\`t be same as keyword. 
   
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
   Variable name can\`t be same as keyword. 
   
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
  ## Logical operators keywords
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
   set var1 {not {or i1 i2}}
   ```
 ## Functions keywords
   ### func
   Synatax : ```func name : arg1 arg2... (
     <code>
   )```
 
   Function declaration keyword.
   ":" is not needed if no args used in function
      
   Example : ```
      func nor : arg1 arg2 (
        return {not {or arg1 arg2}}
      )
   ```
      
      
   ### call
   Synatax : `call func_name arg1 arg2...`
 
   Function call keyword.
   To get return value of function put it in expression.
      
   Second argument must be function.
   Count of arguments given for function must equal to count of arguments that function acceptes.
   
      
   Example : ```
      <nor fucntion decalration with 2 args>
      
      call nor 1 0 // Returns 0
      
      input inp1
      input inp2
      
      output {call nor inp1 inp2} nor_result // Outputs "nor_result : <function return value>"
   ```
       
       
   ### return
   Synatax : `return value`
 
   Returns value for function.
      
   Keyword need to be used in function.
   
      
   Example : ```
      func nor : arg1 arg2 (
        return {not {or arg1 arg2}}
      )
   ``
 
   
