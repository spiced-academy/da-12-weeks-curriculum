---
title: "Data Types and Operators"
weight: 19
---

![An intro image](/images/calculator.jpg)
{{< credits >}}
Photo by Charles Deluvio on Unsplash
{{< /credits >}}

{{% notice warmup "Warmup: Calculator" %}}

Open a terminal window and type in `ipython`. You should see the following prompt:

```bash
In [1]: 
```

Execute a few calculations in Python. Insert the missing symbols into the gaps:

```bash
In [1]: 1 + ___
Out[1]: 3

In [2]: 12 ___ 8
Out[2]: 4

In [3]: ___ * 5
Out[3]: 20

In [4]: 21 / 7
Out[4]: ___

In [5]: ___ ** 2
Out[5]: 81
```

Do not enter the first part (`In [1]` etc.). It appears automatically. Close the IPython shell by typing in `exit()`


{{% /notice %}}


## Key Concepts


concept  |  example | description
---|---| ---
variable    | `x=345` | For saving numbers, text, results of calculations and other values.
operator     | `2+4` | For performing calculations on variables or values.
comments       | `# hello`| Descriptions that explain your code. Ignored by the Python interpreter.
float         | `4.0`, `2.3`| Built-in type for real numbers.
int           | `4`, `100`, `-45`| Built-in type for integer numbers.
str           | `"spiced"`, `'unicorn'`| Built-in type for text.
`print`    | `print('hi')` | Function that prints out the content of variables as text on the terminal.
`type`      | `type(34)`| Function that prints out the type of a variable on the terminal


## Examples

Enter them in the console and examine the result.

### Division

What is the difference between the following instructions? 

```python
10 / 4
10.0 / 4
10.0 / 4.0
10 // 4
10 * 0.25
```

### More Operators

Which operations result in 8?

```python
0 + 8
4 - -4
65 // 8
17 % 9
2 * 4
64 ** 0.5
```

{{% notice info "Modulo and Floor division" %}}

`//` is the floor division operator. The result of a floor division is always an `int` value:

- `10 // 3 = 3` 
- `6 // 4 = 1`

`%` is the modulo operator. It returns the remainder that is left after doing a floor division:

- `10 % 3 = 1`
- `6 % 4 = 2`

{{% /notice %}}



### Variables

Fill the gaps:

```bash
In [1]: apples = 25
In [2]: bananas = 7
In [4]: apples
Out[4]: ______
In [5]: bananas + 1
Out[5]: ______
In [6]: 3 * apples
Out[6]: ______
In [7]: fruits = apples + bananas
In [8]: fruits
Out[8]: ______
```

### Assignments

Which variable assignments are correct?

```python
a = 1 * 2
2 = 1 + 1
5 + 6 = y
seven = 3 * 4
```


### Variable Names 

Try which of the following names of Python variables are valid:

```python
# the following code will produce errors!
YODA = 'jedi'
darth vader = 'sith'
luke99 = 'jedi' = 'sith'
2000imperator = 'sith'
obi_wan_kenobi = 'jedi'
darth.maul = 'sith'
```

{{% notice info "Variable Names" %}}

A variable can have any name as long as it follows the rules. Be creative but 
try to be as precise as possible! When naming things, please stick to these guidelines:

- Only use letters
- Write everything in lowercase
- Separate words with the underscore character `_`

{{% /notice %}}

### Type

Guess the type!

```bash
In [1]: apples = 25
In [2]: bananas = 7.0
In [3]: type(apples)
Out[3]: ______
In [4]: type(bananas)
Out[4]: ______
In [5]: type('hello')
Out[5]: ______
```


### Strings and numbers

What is the difference between the following values? 

```python
"2.0"
2.0
"2"
'2'
2
```

Use the `type()` function to check the values' type!

### String Concatenation

We can also use the `+` operator with strings! 

```python
first_word = 'hello'
second_word = 'spiced!'
sentence = first_word + second_word
print(sentence)
```

Can you use other operators, like `*`? 

### Printing

Which of the following print commands work? Try them one by one.

```python
name = "Spiced"
print "Hello"
print("Hello", name, name)
print("Hello" + name)
print("Hello name")
print(name)
```

## Exercises


### Task 1 - White Rabbits

In April you have 10 white rabbits:

```python
rabbits = 10
```

The rabbits constantly multiply. Every month, their number grows by 20%. In May you already have 12 rabbits. **How many rabbits will you have in December?**

### Task 2 - Debugging

Find and solve all bugs in this code!

```python
'spiced' = word
x = 345
print(y)
y = '12'
z = x + y
print(word)*5
```

## Project Challenges


{{% notice challenge "Start your text adventure!" %}}

##### Step 1: Setup

- Create a new python file `adventure.py` and save it in the project folder.
- To edit the file, open it within Visual Studio Code.

##### Step 2: The Basic Structure

Make the program produce a welcoming message. You could use an output with multiple lines:

```python
print("""
Find the Dragon Egg
===================

Your quest starts.
""")
```

At the end, the program congratulates the player to success:

```python
print("""
On a hidden clearing you discover the dragon egg.

Your quest has been successful!
""")
```

During the project, you will insert more code between these two instructions.

##### Step 3: Run it

Execute the program and make sure it works.

- Open a terminal window.
- Type in `python adventure.py` to run the file.

{{% /notice %}}

## Reading

{{% notice reading "Reading" %}}

- [Python Data Types](https://realpython.com/python-data-types/)
- [Python Data Types Quiz](https://realpython.com/quizzes/python-data-types/)

{{% /notice %}}

<br>

{{% notice copyright "Kristian Rother, Malte Bonart" %}}
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of 


- http://www.academis.eu/python_basics/first_steps/hello.html
- http://www.academis.eu/python_basics/reference/basics.html
- http://www.academis.eu/python_basics/reference/type_conversions.html

by Dr. Kristian Rother, used under CC-BY-SA 4.0. 
{{% /notice %}}
