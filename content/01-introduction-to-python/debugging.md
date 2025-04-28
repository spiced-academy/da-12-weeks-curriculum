---
title: "Debugging"
weight: 60
---

![the first computer bug 1945](/images/bug.jpg)
{{< credits >}}
Courtesy of the Naval Surface Warfare Center, Dahlgren, VA., 1988. - U.S. Naval Historical Center Online Library
{{< /credits >}}

{{% notice warmup "Warmer: Debugging" %}}

How do you debug code? Collect some ideas and thoughts!

{{% /notice %}}

## 10+1 Debugging Strategies

```bash
In [1]: x = 'hi'
In [2]: x.split(3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-19-2408812e0c33> in <module>
----> 1 x.split(3)

TypeError: must be str or None, not int
```

1. save the file and rerun the code
2. read the error message
3. read through the traceback to find out where the error happened
4. include `print` statements for variables
5. identify and fix typos
6. search the internet for your error message (stackoverflow)
7. look up the documentation and usage examples 
8. break down the problem into smaller pieces
9. *code review*: explain/ talk about the problem to others
10. ask for help (stackoverflow, teachers, team members)
11. take a break


## 🐛 SyntaxErrors

Syntax error are raised *before* the code runs. Not a single line gets executed! The most common Syntax errors are:

- missing or wrong indention
- missing colons `:`
- missing whitespace or too much whitespace
- missing or wrong quotation marks (`""`, `''`)
- missing or wrong brackets (`{}`, `()`, `[]`)


What is the problem here?

```python
x = 7 
while x > 5
   x = x-1
print('hi')
```

Syntax errors are easy to spot and to fix. 


## 🐛🐛 Runtime Errors

Runtime errors happen while the program is already running. The code executes but it crashes at some point.

```python
x = ['outside', 'castle', 'forrest']
print(x[0])
print(x[4])
```

Common runtime errors are:

- `IndexError`: accessing elements of a list that don't exist
- `KeyError`: accessing elements of a dictionary that don't exist
- `TypeError`: performing unsupported operations on values (e.g. subtracting strings)
- `ValueError`: performing an unsupported type conversion (e.g. `int('+')`)
- Spelling mistakes in variable or function names
- Wrong file paths


## 🐛🐛🐛 Semantic Errors 

Also called logic errors. The programs runs through and no error message appears. But
something is wrong. Your program did not do the things you have expected it to do!

What went wrong here?

```python
num1 = input('Enter a number: ')
num2 = input('Enter another number: ')
summed_up = num1 + num2

print(f'The sum of {num1} and {num2} is {summed_up}')
```

Identifying and debugging semantic errors is tricky! They often happen when you write code without actually knowing *exactly* what the code *should* output with a given input.  



## Debugging Exercise - Can you find all bugs?

You are given the following input data; a nested dictionary:

```python
node = {
   "text": "Is it a snake?", 
   "yes": {
      "text": "It is a Python!"
   }, 
   "no": {
      "text": "It is not a Python"
   }
}
```

The program is supposed to walk through the tree, asking the user where to go. First start with the syntax errors. Then fix the runtime errors. At the very end
check for any Semantic errors. 


```python
while not finished
    print(node['text']

   if len(node) == 1:
      finished = True
   else:
      answer == input()
      if answer.upper() in [yes', 'y']:
         node = node['no']
      else:
         node = node['yes']
```

## Project Challenge

{{% notice challenge "Paths" %}}

Until now you could teleport from one room to any other. That makes the game a bit boring.

- First, it is not clear which rooms you can go to.
- Second, you could enter "clearing", and the game ends right away.

The game would be a lot more interesting if only some rooms were connected. For that, we need a second dictionary that contains the connections. Each entry points from one starting room to one or more targets:

```python
paths = {
    "hometown": ["beekeeper", "forest"],
    "forest": ["hometown", "desert"],
    ...
}
```

You need two entries to create paths in both directions. If you leave one of them away, you also could create *one-way-streets*.

The paths for the current room could be displayed with the following line:

```python
print(paths[room])
```

or somewhat more nicely with:

```python
print(", ".join(paths[room]))
```

If you would like to extend the plausibility check, so that only the current paths are accessible, you need the following line:

```python
if target in paths[room]:
    ...
```

Execute the program and make sure it works.


{{% /notice %}}



## Reading


{{% notice reading "Reading" %}}

- [Python Syntax Errors](https://docs.python.org/3/library/exceptions.html#SyntaxError)
- [Python Exception Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

{{% /notice %}}

<br>

{{% notice copyright "Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}