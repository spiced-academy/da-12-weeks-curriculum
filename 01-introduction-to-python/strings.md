---
title: "Strings"
weight: 20
---

![Strings exercise](/images/strings.png)
{{% credits %}}
Photo by Dr. Kristian Rother on [Academis](https://www.academis.eu/posts/python_basics/data_structures/strings.md).
{{% /credits %}}

{{% notice warmup "Warmup: Strings" %}}

- Open a Terminal in Visual Studio Code.
- Type in `ipython` to start the interactive python shell.
- Create the variable `s` as indicated in the middle of the diagram above.
- Find out what the expressions on the diagram do to the string!
{{% /notice %}}


## Key Concepts

Text values are called strings. In Python, strings are defined by single quotes `'...'`, double quotes `"..."`, triple-single or triple-double-quotes `"""..."""`.


Concept  |  description
---|---|
`input()`               |     a function reading text from the keyboard
`"Hello" + "Spiced"`    |     combines two (or more) strings into a single string
`text = "Hello Spiced"` |     a variable that contains a string (text) 
`text[2:4]`             |     extract the third and fourth character from a string
`text.upper()`          |     convert the string to UPPERCASE
`str()`                 |     function to convert another python object to a string
`f'Hello {name}'`       |     a formatted string to combine text and variables


## Substrings

Substrings can be formed by applying square brackets with two numbers inside separated by a colon (slices). The index *starts at zero* and the second number is *not* included in the substring itself.

```
"E m i l y   S m i t h"
 0 1 2 3 4 5 6 7 8 9 10
```

What is the result of the following substring operations?

```python
name = 'Emily Smith'
name[0:5]
name[1:4]
name[6:11]
name[:3]
name[-4]
name[-4:]
name[2]
```

## String Methods

Every string in Python brings a list of functions to work with it. As the functions are contained within the string they are also called methods. They are used by adding the `.` to the string variable followed by the method name.

#### Changing Case

```python
name = 'Manipulating Strings \n'
name.upper()
name.lower()
```

#### Removing whitespace at both ends

```python
name.strip()
```

{{% notice info "Special Characters" %}}

Some characters in Python require special attention:

- `\n` - Newline character
- `\t` - Tabulator
- `\"` - literal double quote
- `\\` - Normal, single backslash

Example: `print("Hello! What\'s up? How are you?\nI\'m doing fine.")`

Additionally, Python 3 encodes Unicode characters including German Umlauts, Chinese and Arab alphabets by default. However, they may not be interpreted in the same way in different environments. Just be a bit careful when using them.

{{% /notice %}}

#### Replacing substrings

```python
name.replace('Strings','text')
```

Can you replace the newline character with something else?

## f-strings

Variables and strings can be combined, using f-strings. f-strings contain placeholders with variable names. Here are some examples:

```python
name = 'Roger'
number = 42

print(f'Hello {name}')
print(f'Result: {number}')
print(f'Hi {name}, you are {number} years old!')
```

{{% notice info "How to save the result of a string operation?" %}}

By extracting substrings from a string or applying a method the original string is not changed!
To save the result of such an operation just overwrite the original variable or store the result 
in a new variable:

```python
text = "hi spiced"
text.upper()              
print(text)               # text did not change!
text = text.upper()       # overwrite the old variable
print(text)
```

{{% /notice %}}

## `input()`

The programmer can get information from the user with the `input()` function. This function asks the user to enter a value. Beware that any data from the input function will be saved as a string. So if in order to transform the data to an integer use `int()`. Here is  an example:

```python
number = input('Please enter a number: ')
print(f'The datatype of the entered number is: {type(number)}')

# transform using int()
number = int(number)
print(f'After putting it through the int() function it is now: {type(number)}')
``` 
When the above code is executed the user will first see the following in the terminal:
``` 
Please enter a number:
``` 
Then the user can enter a number and the results of the f-string print statements will be rendered:
``` 
Please enter a number: 8
The datatype of the entered number is: <class 'str'>
After putting it through the int() function it is now: <class 'int'>
```





## Exercises: Your first program

In this walk-through you will write your first python program, fix bugs and 
output results on the terminal.

### Step 1: Your first program

Create a new file `name.py` in the text editor and enter the following instructions:

```python
name = input("What is your name? ")
print("Hello", name)
```

Open a terminal window and execute the program by typing in `python name.py`.

### Step 2: Break the program!

When programming, it is inevitable that you make mistakes. Errors can be simple typos or complicated errors in the logical structure. One of the most important skills in programming is to find the cause of a bug in a program and fix it. You can practice this by intentionally breaking the program and seeing what happens.

Try the following programs with errors one by one and try to understand the error message:

```python
name = input("What is your name? ")
pront("Hello", name)

name = input("What is your name? "
print("Hello", name)

name = input("What is your name? ")
print(Hello , name)

x = input("What is your name? ")
print("Hello", x)
```

How can you find out what is going on?

### Step 3: input

Which of the following input commands work? Try them one by one.

```python
name input("enter your name: ")
name = input("enter a number: ")
name = input(enter your name)
name = input()
```

### Step 4: Debugging

The following program should output a song by Bob Marley. It contains three bugs. Find and fix them.

```python
part1 = "Don't worry about a thing"
part2 = "Cause every little thing"
part3 = gonna be all right

text = "part1 + part2 + part3"
print(text
```

### Step 5: Extend your program

- Write a program that asks for your first and last name
- Output both in uppercase letters
- Also ask for your age
- Combine the output using a f-string


## Project Challenges

{{% notice challenge "Improve your text-adventure" %}}

The player of your game has a starting location. 

1. Define a variable that contains the current location:

      ```python
      room = "hometown"
      ```

2. Give the user some information about where she is using the `print()` function to add depth to the story.
3. Using the `input()` function to ask the user for a new location to enter.
4. Display the new location and some information about the new room the player has entered.

{{% /notice %}}

## Reading


{{% notice reading "Reading" %}}

- [In-depth tutorial about strings](https://realpython.com/python-strings/)
- [In-depth guide about f-strings](https://realpython.com/python-f-strings/)

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Kristian Rother, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of 

- http://www.academis.eu/python_basics/reference/strings.html

by Dr. Kristian Rother, used under CC-BY-SA 4.0. 
{{% /notice %}}