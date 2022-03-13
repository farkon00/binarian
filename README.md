# Binarian
# Content
  * [Global info](#global-info)
  * [Basic syntax](#basic-syntax)
    * [Expressions](#expression)
    * [Lists](#lists)
      * [Lists as integers](#lists-as-integers)
    * [Functions](#functions)
  * [Keywords](#keywords)
    * [Special keywords](#special-keywords)
      * [set](#set)
      * [drop](#drop)
      * [input](#input)
      * [output](#output)
    * [Logical operators keywords](#logical-operators-keywords)
      * [and](#and)
      * [or](#or)
      * [not](#not)
    * [Conditional operators](#conditional-operators)
      * [if](#if)
      * [else](#else)
    * [List keywords](#list-keywords)
      * [index](#index)
      * [len](#len)
      * [append](#append)
    * [Functions keywords](#functions-keywords)
      * [func](#func)
      * [return](#return)

# Global info
  Original compilers are written in python 3.10.
  
  All files with binarian source code have extension .bino.
  
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

  ## Lists
  Lists in binarian can contain any object and isn't staticlly typed. Multidimensional lists are also supported.
  To create list in binarian use square brackets : `[0 1 [1 1]]`.

  Check [List keywords](#list-keywords) for all possible keywords related to lists.

  ### Lists as integers
  Keywords and in future standart functions use lists as integers. Format of integer lists is just a positive binary number. 
  Check [wiki](https://en.wikipedia.org/wiki/Binary_number#Representation) for more details.
  E.g. `[1 1 0]` is 6, `[0 1 1 1]` is 7. Zero in second example is optional, but you can put infinite number of zeros before number and nofing will be changed.
   
  ## Functions
  To create function use [func](#func) keyword is global scope. Inline functions are unavaliable for now.
  To call function use function name as keyword, than put all needed arguments after function name. To get return value of function put call in expression.
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
  
  ### drop
  Syntax : `drop var_name`
  
  This keyword uses to delete variable from memory.
  
  Variable need to be assigned before droping.
  You can't use this keyword in expression.
  Variable name can\`t be same as keyword. 
  
  Example : 
  ```
  set var1 1
  set var2 1
  drop var1
  and var1 var2 // Will throw exception
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
 
  User tip can contain spaces, everything after value will be considered tip.
 
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
  If keyword using in expression, expression will replaced by result. Otherwise keyword output will be printed in console.
  
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
  If keyword using in expression, expression will replaced by result. Otherwise keyword output will be printed in console.
  
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
  If keyword using in expression, expression will replaced by result. Otherwise keyword output will be printed in console.
  
  Example : 
  ```
  input i1
  input i2
  not i1
  set var1 {not {or i1 i2}}
  ```
  
  ## Conditional operators
  ### if  
  Synatax :
  ``` 
  if condition (
    code
  )
  ```
  Conditional operator if, execute code in block if condition is 1.
  
  Condition must be 0 or 1.
      
  Example :
  ```
  input a
  if a (
    output a _a
  )
  ```
  
  ### else 
  Synatax :
  ``` 
  if condition (
    code
  )
  else (
    code
  )
  ```
  Conditional operator else, execute code in block if condition of previous if operator is 0.
  
  Not required for every if.
  
  Else must go right after if.
      
  Example :
  ```
  input a
  
  if a (
    output a _a
  )
  else (
    input b
    output b _b
  )
  ```
 
  ## List keywords
  ### index
  Synatax : `index list index`

  Gets list element with index `index`. Index is also a list, check [Lists as integers](#lists-as-integers) for more details.

  If keyword using in expression, expression will replaced by result. Otherwise keyword output will be printed in console.

  Example :
  ```
  set list [0 1 0]
  index list [1 0] // Prints 0
  ```

  ### len
  Synatax : `len list`

  Returns length of list. Lenght is also a list, check [Lists as integers](#lists-as-integers) for more details.

  If keyword using in expression, expression will replaced by result. Otherwise keyword output will be printed in console.

  Example :
  ```
  set list [0 1 0]
  len list // Prints [1 1]
  ```

  ### append
  Synatax : `len list element`

  Appends element to end of the list.

  You can't use this keyword in expression.

  Example :
  ```
  set list [0 1 0]
  append list 1 // List becomes [0 1 0 1]
  ```
  
  ## Functions keywords
  ### func
  Synatax :
  ```
  func name : arg1 arg2... (
    code
  )
  ```

  Function declaration keyword.
  
  ":" is not needed if no args used in function.
      
  Example :
  ```
  func nor : arg1 arg2 (
    return {not {or arg1 arg2}}
  )
  ```
      
      
  ### return
  Synatax : `return value`

  Returns value for function.
      
  Keyword need to be used in function.
  
      
  Example : 
  ```
  func nor : arg1 arg2 (
    return {not {or arg1 arg2}}
  )
  ```
