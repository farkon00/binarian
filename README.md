[![Test](https://github.com/farkon00/binarian/actions/workflows/main.yml/badge.svg)](https://github.com/farkon00/binarian/actions/workflows/main.yml)
![](https://img.shields.io/github/commit-activity/m/farkon00/binarian)
# Binarian
# Content
  * [Global info](#global-info)
  * [How to compile](#how-to-compile)
  * [Standart library](#standart-library)
  * [Types](#types)
  * [Basic syntax](#basic-syntax)
    * [Expressions](#expression)
    * [Operations](#operations)
    * [Functions](#functions)
  * [Keywords](#keywords)
    * [Special keywords](#special-keywords)
      * [var](#var)
      * [drop](#drop)
      * [input](#input)
      * [output](#output)
      * [convert](#convert)
      * [pyeval](#pyeval)
    * [Conditional operators](#conditional-operators)
      * [if](#if)
      * [else](#else)
      * [elif](#elif)
    * [Loops](#loops)
      * [for](#for)
      * [while](#while)
      * [break](#break)
      * [continue](#continue)
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
  
  Usage: `binarian <file> [options]`

    Options:

      -d          Debug mode, outputs variables values at the end of execution. 

      -tc         Type check code before executing, will output all errors found.

      -no-std     Disables std library.

      -cache      Caches parsed code to file. 

      -load-cache Sets mode to loading cached file.

      -opers      Outputs file parsed to operations before execution. Will print all std operations too.

      --help      Show help message.
  
# How to compile
 If you want to compile binarian intepreter yourself for tests of your modifications, updating std.bino or other reasons. Pyinstaller is recomended.

 Command for creating executable in current version is `pyinstaller binarian.py --paths "<path to source code directory>" --onefile --add-data "std.bino;."`

# Standart library
  Latest version of standart library is stored in github repo in std.bino file, if you want new features from standart library and stay with old version, use old source code of intepreter and new std.bino in directory with source code. New versions of standart library can work incorrectly on older versions. Look to [How to compile](#how-to-compile) for more information about creating executable.  

  Standart library includes useful functions like sum, list-eq, xor. Documentation for standart library is available in github repo in std_docs.md file.

  Use -no-std flag in command to not include it while execution. If std.bino is not found warning will be displayed and execution will continue without including standart library.

# Basic syntax  
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
   
  ## Operations
  Operations can be performed on int, float, str, list. But some types are limited. 
  
  List of operations :
  * -, *, /, %, \*\*, &gt;, &lt;, &gt;=, &lt;= - can only be performed between floats and ints.
  * \+ - can be performed on any types mentioned above, but you can only add lists to lists, strings to strings and int or float to int or float.
  * ==, != - can be performed beetwen any two objects.
   
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
  Most common type in binarian, represents any integer. In binarian also takes place of boolean. Examples : `0 -69 420`

  There is int litterals in other bases: octal, binary and hexadecimal. Binarian uses prefixes to recognize alternative bases.
  Examples : 
  ```
  0x12  // Hexadecimal, 18
  0b010 // Binary, 2
  0o10  // Octal, 8
  ```

  ## float
  Number with floating decimal point, has slower arithmetics operation then int. But you can have fractions with it. Examples : `420.69 -24.0000 96.0001`
  
  ## str
  String of characters, matched only with ". Str can contain escape characters new line, tab etc., to use them put \ before character e. g. "\\", "\n" "\"". Examples : `"Hellow world\n" "\tBrackets : [] {} ()"`

  ## list
  List can contain any objects of any other types. Look to [Lists](#lists) for more details. Examples : `[6 9 "420" [420.69]]`

  ## function
  Type representing function usually defined by [func](#func) keyword.

  ## object
  Object is basically every possible value in binarian. So if type of something is object it can be anything.
  
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
  Syntax : `input`
  
  This keyword uses to input data from keyboard. Keyword returns user input as str.
  
  Example : 
  ```
  output (input) // echo
  ```
  
  ### output
  Syntax : `output str`
  
  This keyword uses to output data to user.
 
  You can't use this keyword in expression.
  
  Example : 
  ```
  var val1 = 1
  output val1
  output "some string"
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

  ### pyeval
  Syntax : `pyeval code imports exports`
  Executes python code joins first argument with new line, imports values to code with name, returns list of variables with names from exports.

  **Using this keyword isnt recomended std library may have features, that you need or at least use functions for generic features**

  Example :
  ```
  func object get_attr : obj: object, attr: str {
    return (index (pyeval [(+ "ret = obj." attr)] [["obj" obj]] ["ret"]) 0)
  }
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

  ## elif
  Synatax :
  ``` 
  if condition {
    code
  }
  elif condition {
    code
  }
  ...
  else {
    code
  }
  ```
  Conditional operator elif, executes code in block if condition of previous if operator is false(mostly it means, that value is "empty") and it's condition is true(mostly it means, that value isnt "empty").
  
  Not required for every if.
  
  Elif must go right after if.

  You can chain as much elifs as you want and else isnt required after last elif.
      
  Example :
  ```
  input a
  input b
  
  if a {
    output a a
  }
  elif b {
    output b b
  }
  else {
    input c
    output c c
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

  ### break
  Synatax :
  ``` 
  while condition {
    code
    break
  }
  for var list {
    code 
    break
  }
  ```
  Stops `while` or `for` loop. Mostly used with conditions.
      
  Example :
  ```
  for i [0 0 1 0] {
    if i {
      break
    }
    output i i
  }
  ```

  ### continue
  Synatax :
  ``` 
  while condition {
    code
    continue
  }
  for var list {
    code 
    continue
  }
  ```
  Stops current `while` or `for` loop iteration and starts the next one. Mostly used with conditions.
      
  Example :
  ```
  for i [0 0 1 0] {
    if i {
      continue
    }
    output i cont
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
