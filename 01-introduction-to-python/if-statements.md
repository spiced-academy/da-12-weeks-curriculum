---
title: "If Statements"
weight: 29
---

![An intro image](/images/decision-if.jpg)
{{% credits %}}
Photo by <a href="https://unsplash.com/@madebyjens?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jens Lelie</a> on <a href="https://unsplash.com/s/photos/decision?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{% /credits %}}

{{% notice warmup " Warmer: Decision" %}}

Create a new python file `rps.py` and test the following program with different inputs:

```python
player = input("Please enter R, P or S (for [R]ock, [P]aper and [S]cissors) ")
computer = "P"

if player == computer:
    print("it's a draw")
```

{{% /notice %}}

## Concepts

An important structural element in programming is making decisions. In Python, the 
instruction `if` allows you to make decisions (conditional statements). 

concept  |  description
---|---|
`bool`          | Built-in type that represents the boolean values `True` and `False`.
`if`            | Python keyword for making a decision. 
`<=`    | Comparison operator that evaluate to a `bool` value, e.g. `2 < 5`.
`and`   | Boolean operator to chain several logical expression together, e.g. `2<5 and 2!=3`.
indention | Created with the `Tab` Key. Used to group statements together to a block of code.

## Comparison Operators

Operators compare two numbers, strings (and other values) with each other. The result of the 
operation is a `bool` value (`True` or `False`).

operator | description                 | example          
---      | ---                         | ---              
`==` 	   | Equal to                    | `name == "Bob"` 
`!=` 	   | Not equal to                | `2**4 != 1024`
`<` 	   | Less than                   | `napples < 1000`
`>`      | Greater Than                | `8**2 > 80`
`<=`     | Less than or Equal to       | `'A' <= 'B'`
`>=`     | Greater than or Equal to    | `'Z' >= 'X'`

## Boolean Operators

Operators compare two `bool` values with each other. Boolean Operators can be used to chain several
logical comparisons together.

operator | description                                           | example          
---      | ---                                                   | ---              
`and` 	| `True` only if both values are `True`                 | `name == "Bob" and name != 'Peter'` 
`or` 	   | `True` if at least one value is `True`                | `name == 'Bob' or name == 'Peter`
`not` 	| Converts `True` to `False` (and the other way around) | `not True`


{{% notice info "Boolean values and integers" %}}

`bool` values only have two possible states: `True` or `False`. That's why we 
often represent `bool` values as binary numbers: `0` or `1`! 
Do you know which value belongs to which number? Run the following statements to find out:

```python
True + True
False - True
False + False
True + 10
```

{{% /notice %}}

## If-Statements

To only execute some operations in case something happened use a single `if` statement:

```python
name = input('What is your name?')
if name == 'Bob':
   print('The name is Bob! Convert to uppercase...')
   name = name.upper()
print(name)
```

To also execute some operations in case the opposite happened add an `else` statement:

```python
...
else:
   print('The name is something else. Convert to lowercase...')
   name = name.lower()
print(name)
```

To chain several cases together you can add as many `elif` statements as you wish:

```python
name = input('What is your name? ')
if name == 'Bob':
   print('The name is Bob! Convert to uppercase...')
   name = name.upper()
elif name == 'Alex':
   print('The name is Alex! Reverse it...')
   name = name[::-1]
else:
   print('The name is something else. Convert to lowercase...')
   name = name.lower()
print(name)
```

{{% notice info "Boolean check short-cut" %}}

When only checking whether a variable is True or False:
```python
work = True

if work == True:
    print('I am working!')
else:
    print('Off work, leave me alone.')
```

The following code will preform the same check:
```python
work = True

if work:
    print('I am working!')
else:
    print('Off work, leave me alone.')
``` 

In other words `if work == True:` and `if work:` are the same thing as far as python is concerned. Using this information what would the shortcut for `if work == False:` be?

{{% /notice %}}

## Nested if-statements

When the condition for an if or elif statement is met then the indented code block beneath it is executed. 
```python
name = 'Bob'

if name == 'Bob':
    name = name.upper()
    print(name)
elif name == 'Malte':
    name = name.lower()
    print(name)
else:
    print('I do not know you!')
``` 

For example the code above will return BOB since the if condition was met. Once this condition is met we can add more nested conditions to check other details.

```python
teacher = True
name = 'Bob'

if name == 'Bob':
    name = name.upper()
    if teacher:
        print('Mr. ' + name)
elif name == 'Malte':
    name = name.lower()
    print(name)
else:
    print('I do not know you!')
``` 

Now the code first checks `name`. If `name` is Bob the if will first overwrite the name variable with the the result of `name.upper()`, afterwards it will then check the `teacher` variable and if that is `True` then it will print out `Mr. BOB`. 

Keep in mind in order for a nested if-statement to be executed the parent condition must first be met. The parent condition is the condition one level above. 

Try both code blocks and change the `name` variable to see how the program reacts. The `name` variable can also be set so the user enters it using `input()`. How could the program be adjusted in case the user enters a name other than Bob or Malte?

## Exercises: Rock Paper Scissors

### Step 1: Alternative Decisions

Insert the words `elif`, `else` and `if` into the gaps in the code so that it runs:

```python
import random

player = input("Please enter R, P or S (for [R]ock, [P]aper and [S]cissors) ")
computer = random.choice('RPS')

____ player == 'R' and computer == 'P':
    print("Computer wins")
____ player == 'R' and computer == 'S':
    print("Player wins")
____:
    print("it's a draw")
```

### Step 2: Paper

Extend the program, so that it also works if the player chooses paper or scissors.

### Step 3: Debugging

Copy the code into a text file. Reorder and debug the code until it runs with no errors:

```python

player = input('Please enter R, P or S (for [R]ock, [P]aper and [S]cissors): ')

elif player.upper() not in 'RPS':
    print('Invalid input. Please enter R,P or S.')

elif player == computer
    print('You chose the same as I did')

if player = 'S':
    print('You chose "scissors".')

computer = 'P'

else:
print('You chose something else than "scissors"')
```


### Step 4: Expressions

Which comparisons in the following `if` statements result in `True`:


```python
a = 3
b = 4
c = 7

if a + b < c:
    print(True)

if a + b == 5 + 2:
    print(True)

if a * b == 12 and b * c == 28:
    print(True)

if a + b * c >= 28:
    print(True)

if a + b == "7":
    print(True)

```

### Step 5: State variables

The following program saves a comparison expression in a variable of the data type `bool`. Complete the code:

```python
player_wins = (player == "R" and computer == "S") \
               or (player == "P" and ...) \
               or (...)

if player_wins:
    print('You won!')
```

### Step 6: Nested if statements

Complete the program, so that it covers all possible situations:

```python
winner = 'draw'

if player == "S":
    if computer == "P":
        winner = "player"
    elif computer == "R":
        winner = "computer"

elif player == "P":
    ...

print("The winner is:", winner)
```

### Step 7: Complete the game

Complete the Rock-Paper-Scissors game.

Optional goals:

- take draws into account as a possibility
- inputs should be valid in upper and lower case
- use a single if..elif..else block
- use state variables, so that only one or two if statements (without elif or else) remain

## Project Challenges

{{% notice challenge "Improve your Text-Adventure with descriptions" %}}

Write interesting descriptions of the rooms and print them by adding if instructions like the following:

```python
if room == "hometown":
    print("""
    You are in your home town.
    A small trading spot at the desert border.
    """)
```

{{% /notice %}}


{{% notice challenge "Puzzles!" %}}


An interesting adventure should also contain a few puzzles. Here is how a puzzle could look like:

```bash
Where would you like to go? forest

There is a BEAR in the forest!!! You run away.

...

Where would you like to go? beekeeper

You buy a pot of honey at the beekeeper.

...

Where would you like to go? forest

You leave the honeypot to the bear and carefully sneak through.

```

How to implement such a puzzle?

#### Step 1

Define a state variable before the main game. The state variable is used to keep track
of the players' global state,  e.g.:

```python
honey = False
```

#### Step 2

Check whether the state should change, and then change it. In case we do not have honey when we go to the beekeeper we shall buy some:

```python
if room == "beekeeper" and not honey:
    print("You buy a pot of honey from the beekeeper.")
    honey = True
```

#### Step 3

Check the state variable to allow actions or prevent them. Here nested if-statement is added, first to check which room is entered and then what happens in the room dependent upon a state variable. If we go to the forest and we have no honey then we will run away from the bear:

```python
if room == "forest":
    if honey:
        print("You leave the honeypot for the bear and carefully sneak by.")
        honey = False  # you can use the honey only once
    else:
        print("There is a BEAR in the forest!!! You run away.")
```

It is not easy to place all statements in the right order. A good idea is to run the program after each modification to see what happens. 

Keep in mind the program is not finished, so the current state of the game is not complete and that is ok! However no error messages should be returned when running it. Feel free to integrate the puzzles listed here or any others. 


{{% /notice %}}

<br>

{{% notice copyright "Kristian Rother, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). 

- http://www.academis.eu/python_basics/reference/if.html

by Dr. Kristian Rother, used under CC-BY-SA 4.0. 
{{% /notice %}}