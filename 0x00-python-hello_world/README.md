# 0x00. Python - Hello, World

In this project, I learned about the basics of Python, the creator of Python, ```Guido van Rossum```, the ```Zen of Python```, the use of ```pycodestyle```, and the use of Python interpreter. I also learned basics of working with strings and string slicing.

### 0. Run Python file
- [0-run](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/0-run) - a Shell script that runs a Python script.
  - The Python file name will be saved in the environment variable ```$PYFILE```

### 1. Run inline
- [1-run_inline](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/1-run_inline) - a Shell script that runs Python code.
  - The Python code will be saved in the environment variable ```$PYCODE```
  
### 2. Hello, print
- [2-print.py](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/2-print.py) - a Python script that prints exactly ```"Programming is like building a multilingual puzzle```, followed by a new line.

### 3. Print integer
- [3-print_number.py](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/3-print_number.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable ```number```, followed by ```Battery street```, followed by a new line.
  - The output of the script should be:
    - the ```number```, followed by ```Battery street```,
    - followed by a new line
  - You are not allowed to cast the variable number into a string
  - Your code must be 3 lines long
  - You have to use ```f-strings```

### 4. Print float
- [4-print_float.py](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/4-print_float.py) - Complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable ```number``` with a precision of 2 digits.
  - The output of the program should be:
    - ```Float:```, followed by the float with only 2 digits
    - followed by a new line
  - You are not allowed to cast ```number``` to string
  - You have to use f-strings
  
### 5. Print string
- [5-print_string.py](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/5-print_string.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
  - The output of the program should be:
    - 3 times the value of ```str```
    - followed by a new line
    - followed by the 9 first characters of ```str```
    - followed by a new line
  - You are not allowed to use any loops or conditional statement
  - Your program should be maximum 5 lines long

### 6. Play with strings
- [6-concat.py](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/6-concat.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print ```Welcome to Holberton School!```
  - You are not allowed to use any loops or conditional statements.
  - You have to use the variables ```str1``` and ```str2``` in your new line of code
  - Your program should be exactly 5 lines long
  
### 7. Copy - Cut - Paste
- [7-edges.py](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/7-edges.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
  - You are not allowed to use any loops or conditional statements
  - Your program should be exactly 8 lines long
  - ```word_first_3``` should contain the first 3 letters of the variable ```word```
  - ```word_last_2``` should contain the last 2 letters of the variable ```word```
  - ```middle_word``` should contain the value of the variable ```word``` without the first and last letters

### 8. Create a new sentence
- [8-concat_edges.py](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/8-concat_edges.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print ```object-oriented programming with Python```, followed by a new line.
You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals

### 9. Easter Egg
- [9-easter_egg.py](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/9-easter_egg.py) - a Python script that prints “```The Zen of Python```”, by ```TimPeters```, followed by a new line.
  - Your script should be maximum 98 characters long
  
### 10. Linked list cycle
- [10-check_cycle.c](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-check_cycle.c) - a function in C that checks if a singly linked list has a cycle in it.
  - Use [lists.h](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/lists.h), [10-linked_lists.c](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-linked_lists.c) and [10-main.c](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-main.c) to test your code.
  - To compile: ```gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle```

### 11. Hello, write
- [100-write.py](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/100-write.py) - a Python script that prints exactly ```and that piece of art is useful - Dora Korpar, 2015-10-19```, followed by a new line.
  - Use the function ```write``` from the ```sys``` module
  - You are not allowed to use ```print```
  - Your script should print to ```stderr```
  - Your script should exit with the status code ```1```

### 12. Compile
- [101-compile](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/101-compile) - a script that compiles a Python script file.
  - The Python file name will be stored in the environment variable ```$PYFILE```
  - The output filename has to be ```$PYFILEc```
  
### 
- [102-magic_calculation.py](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x00-python-hello_world/102-magic_calculation.py) -  the Python function ```def magic_calculation(a, b):``` that does exactly the same as the following Python bytecode:
  ```
   3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
  ```
  - Read [Python bytecode](https://docs.python.org/3.4/library/dis.html)
