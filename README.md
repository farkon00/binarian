[![Test](https://github.com/farkon00/binarian/actions/workflows/main.yml/badge.svg)](https://github.com/farkon00/binarian/actions/workflows/main.yml)
# Binarian
# Content
  * [Global info](#global-info)
  * [How to compile](#how-to-compile)
  * [Standart library](#standart-library)
  * [Types](#types)
  * [Basic syntax](#basic-syntax)
    * [Expressions](#expression)
    * [Lists](#lists)
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
    * [Loops](#loops)
      * [for](#for)
      * [while](#while)
    * [List keywords](#list-keywords)
      * [index](#index)
      * [setindex](#setindex)
      * [len](#len)
      * [append](#append)
    * [Functions keywords](#functions-keywords)
      * [func](#func)
      * [return](#return)

# Global info
  Original interpreters are written in CPython 3.10.
  
  All files with binarian source code have extension .bino.
  
  To run your code, run python file(binarian.py) or executable(binarian.exe). 
  
  Also you can add -d flag after file name to see variable in the end of execution. Or -no-std flag to not include standart library.
  
  Examples :
  ```
  python binarian.py your_file.bino
  python3 binarian.py your_file.bino
  python3.10 binarian.py your_file.bino -d
  python3 binarian.py other_file.bino -d
  binarian.exe your_file.bino -no-std
  ```
  
# How to compile
 If you want to compile binarian intepreter yourself for tests of your modifications, updating std.bino or other reasons. Pyinstaller is recomended.

 Command for creating executable in current version is `pyinstaller binarian.py --paths "<path to source code directory>" --onefile --add-data "std.bino;."`

# Standart library
  Latest version of standart library is stored in github repo in std.bino file, if you want new features from standart library and stay with old version, use old source code of intepreter and new std.bino in directory with source code. New versions of standart library can work incorrectly on older versions. Look to [How to compile](#how-to-compile) for more information about creating executable.  

  Standart library includes useful functions like sum, list-eq, xor. Documentation for standart library is available in github repo in std_docs.md file.

  Use -no-std flag in command to not include it while execution. If std.bino is not found warning will be displayed and execution will continue without including standart library.

# Basic syntax
  All syntax is based on keywords and arguments. 
  ```
  keyword1 arg1 arg2...
  keyword2 arg1 arg2...
  keyword3 arg1
  ```
  
  To reference variable you must type name of it. 
  
  To write comments use '//'. All symbols in line after '//' will be marked as comments.
  
  ## Expression
   Expressions is lines in lines, but while execution they will be replaced with returns of keywords or functions. Also you can't use set, input and output etc. in expressions.
   Syntax : 
   ```
   keyword (keyword arg (keyword arg arg)) arg
   ```
   
   Example :
   ```
   input var1
   input var2
   output (and var1 (not var2))
   ```

  ## Lists
  Lists in binarian can contain any object and isn't staticlly typed. Multidimensional lists are also supported.
  To create list in binarian use square brackets : `[0 1 [1 1]]`.

  Check [List keywords](#list-keywords) for all possible keywords related to lists.
   
  ## Functions
  To create function use [func](#func) keyword is global scope.
  To call function use function name as keyword, than put all needed arguments after function name. To get return value of function put call in expression.
  To return value use [return](#return) keyword. If fucntion don\`t return any value, it will return 0.
  
  If any variable was registred in function, it will become local. So it\`s unavailable in global scope, other functions and other functions calls. Arguments is local too.
  
  Example :
  ```
  func name : arg1, arg2 {
    not arg1
    
    input inp1
    output (and inp1 arg1) output
    
    return (and arg1 arg2)
  }
  ```

# Types
There are 6 types in binarian, one of them isnt recomended to use and was added for techinical porpuses.

  ## int
  Most common type in binarian, represents any integer from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,808(64 bits limits). In binarian also takes place of boolean.

  ## float
  Number with floating decimal point, has slower arithmetics operation then int and range of values are smaller. But you can have fractions with it. 

  ## list
  List can contain any objects of any other types(except none). Look to [Lists](#lists) for more details.

  ## function
  Type representing function usually defined by [func](#func) keyword.

  ## object
  Object is basically every possible value in binarian. So if type of something is object it can be anything.

  ## none
  Just not type checked type, very unrecomended to use. Was added for keywords that not return any value.
  
# Keywords
  ## Special keywords
  ### var
  Syntax = : `var var_name = value; var type = var_name value`
  
  This keyword uses to assign or change value of variables. Typing is optional. While type checking type may be figured out by value, if type isnt provided.
  
  You can't use this keyword in expression.
  Variable name can\`t be same as keyword or have brackets in them. 
  
  Example : 
  ```
  var var1 = 1
  var var2 = 1
  and var1 var2
  or 0 var1
  ```
  
  ### drop
  Syntax : `drop var_name`
  
  This keyword uses to delete variable from memory.
  
  Variable need to be assigned before droping.
  You can't use this keyword in expression.
  Variable name can\`t be same as keyword or have brackets in them. 
  
  Example : 
  ```
  var var1 = 1
  var var2 = 1
  drop var1
  and var1 var2 // Will throw exception
  ```
  
  ### input
  Syntax : `input var_name`
  
  This keyword uses to input data from keyboard. In console user will see `var_name : <user input here>`. Keyword assign variable with name var_name.
  
  You can't use this keyword in expression.
  Variable name can\`t be same as keyword or have brackets in them. 
  Input must be valid integer.
  
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
 
  User tip cannot contain spaces.
 
  You can't use this keyword in expression.
  
  Example : 
  ```
  var val1 = 1
  output val1 Hi! // Hi! : 1
  output 0 Its_zero // Its_zero : 0
  ```

  ### convert
  Syntax : `convert value type`
  
  Converts value to type `type`, if cant convert(for example converting int to list) throws exception.

  If keyword used in expression, expression will replaced by result. 

  Type must be lowercase, written same as specified in [Types](#types).
  
  Example : 
  ```
  input inp
  var a = (convert inp float)  // Type cheking will automatically set type of variable to float,
                               // but wont check if type can be converted to specified type
  ```

  ## Logical operators keywords
  ### and
  Syntax : `and val1 val2`
  
  Boolean logical operator and.

  If keyword used in expression, expression will replaced by result.
  
  Example : 
  ```
  input i1
  input i2
  and i1 i2
  var var1 = (and i1 1)
  ```
  
  ### or
  Syntax : `or val1 val2`
  
  Boolean logical operator or.

  If keyword used in expression, expression will replaced by result.
  
  Example : 
  ```
  input i1
  input i2
  or i1 i2
  var var1 = (or i1 i2)
  ```
  
  ### not
  Syntax : `not val`
  
  Boolean logical operator not.

  If keyword used in expression, expression will replaced by result.
  
  Example : 
  ```
  input i1
  input i2
  not i1
  var var1 = (not (or i1 i2))
  ```
  
  ## Conditional operators
  ### if  
  Synatax :
  ``` 
  if condition {
    code
  }
  ```
  Conditional operator if, executes code in block if condition is true(mostly it means, that value isnt "empty").
      
  Example :
  ```
  input a
  if a {
    output a _a
  }
  ```
  
  ### else 
  Synatax :
  ``` 
  if condition {
    code
  }
  else {
    code
  }
  ```
  Conditional operator else, executes code in block if condition of previous if operator is false(mostly it means, that value is "empty").
  
  Not required for every if.
  
  Else must go right after if.
      
  Example :
  ```
  input a
  
  if a {
    output a _a
  }
  else {
    input b
    output b _b
  }
  ```

  ## Loops
  ### for
  Synatax :
  ``` 
  for variable list {
    code
  }
  ```
  For loop, aka foreach. Iterates throw `list`, every iteration executes code inside, sets `variable` to next value in list.
  After last loop iteration finished, `variable` is droped, so you can`t access it any more.
      
  Example :
  ```
  var list = [[0 1] [1 0]]

  for i list {
    output i pretty list

    for j i {
      output j pretty sub-list
    }
  }
  ```

  ### while
  Synatax :
  ``` 
  while condition {
    code
  }
  ```
  While loop. Repeats code inside, while condition is true(mostly it means, that value isnt "empty").
      
  Example :
  ```
  // This code will just output hi there : 1
  var name = 1

  while name {
    output 1 hi_there
    var name = 0
  }
  ```
 
  ## List keywords
  ### index
  Synatax : `index list index`

  Gets list element with index `index`.

  If keyword used in expression, expression will replaced by result.

  Example :
  ```
  var list = [0 1 0]
  output (index list 2) 3rd // Prints 0
  ```

  ### setindex
  Synatax : `setindex list index value`

  Sets list element with index `index` to `value`.

  You can't use this keyword in expression.

  Example :
  ```
  var list_ = [0 1 0]
  setindex list_ 2 1 // [0 1 1]
  ```

  ### len
  Synatax : `len list`

  Returns length of list.

  If keyword used in expression, expression will replaced by result.

  Example :
  ```
  set list [0 1 0]
  output (len list) len // Prints 3
  ```

  ### append
  Synatax : `append list element`

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
  func name : arg1, arg2... {
    code
  }
  func ret_type name : arg1:type, arg2... {
    code
  }
  ```

  Function declaration keyword. Typing is optional and mixing up typed and not typed arguments is allowed. 
  
  ":" is not needed if no args used in function.
      
  Example :
  ```
  func int nor : arg1:int, arg2 {
    return (not (or arg1 arg2))
  }
  ```
      
      
  ### return
  Synatax : `return value`

  Returns value for function.
      
  Keyword need to be used in function.
  
      
  Example : 
  ```
  func nor : arg1, arg2 {
    return (not (or arg1 arg2))
  }
  ```
