---
title: "Conditional Loops"
weight: 30
---

![a staircase](/images/loop.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@procaffeinator?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Arfan Abdulazeez</a> on <a href="https://unsplash.com/s/photos/infinite?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

{{% notice warmup "Warmer: Repeating Instructions" %}}

What issues do you see with this piece of code?

```python
name = input('What is your name?' )
if name != 'Spiced':
   print('unauthorized name, please try again')
   name = input('What is your name?' )
   if name != 'Spiced':
      print('unauthorized name, please try again')
      name = input('What is your name?' )
      if name != 'Spiced':
         print('unauthorized name, please try again')
         name = input('What is your name?' )
```
{{% /notice %}}


## Introduction

In our early programs, each Python instruction was executed only once. That makes programming a bit pointless, because our programs are limited by our typing speed.

With the `while` statement you can repeat one or more instructions several (or infinite) times.

```python
i = 0
while i < 5:
   print(i)
   i = i+1
```

The `while` loop is executed as long as the conditional expression at the beginning holds (=`True`). The conditional expressions work in exactly the same way as in `if` statements. It's up to you to make sure that at some point the conditional expression returns `False`. Otherwise your program will run forever!

{{% notice info "Loops" %}}

A `while` loop is useful if the number of repetitions is unknown at the beginning. In cases
where you already know the number of iterations you should use a [`for` loop]({{< ref "for-loops" >}}).

{{% /notice %}}


## Examples

### Counting until a certain value

A simple usage of while is to count until an exit condition is met. The following loop calculates the sum of all numbers from 1 through 10:

```python
i = 0
total = 0
while i < 10:
    print(i)
    i = i + 1
    total = total + i
```

### Waiting for user input

With a `while` loop the code from the warmup gets much easier to read: 

```python
name = ''
while name != 'Spiced':
   name = input('What is your name?' )
   if name != 'Spiced':
      print('unauthorized name, please try again')
...
```

### Endless loops

With while it is possible to build loops that never stop. Most of the time this happens by accident. In the following loop, the instruction to decrease `a` is missing. It runs endlessly:

```python
a = 10
b = 1
while a > 0:
    b = 1 - b
    print(b)
```

How can you fix the loop?  

{{% notice info "Keyboard Interruption" %}}

To stop a running program press the keys `Ctrl`+`c`.

{{% /notice %}}

## Exercises

### Task 1

![while loop examples](/images/while.png)

Match the expressions so that the while loops run the designated number of times.

### Task 2

Which of these while commands are correct?

```python
while a = 1:

while b == 1

while a + 7:

while len(c) > 10:

while a and (b-2 == c):

while s.find('c') >= 0:
```

### Task 3

Which statements are correct?

- while is also called a conditional loop
- The expression after while may contain function calls
- It is possible to have while loops that run forever
- The colon after while may be omitted
- The code block after while is executed at least once



### Task 4

Which of the following while loops will finish?

##### A

```python
count = 0
while count > 0:
    print(count)
    count += 1

```

##### B

```python
text = "a"
while "z" not in text:
    text += "a"
```


##### C

```python
a = 7
b = 135
while a != b:
    a += (a - b) / 10.0
    b -= (a - b) / 10.0
```

##### D

```python
n = 0
while n * 5 != n ** 2:
    n += 2

```


## Project Challenges

{{% notice challenge "The Main Loop" %}}

The most important structural element of most games is the *main loop*. In each round ("iteration") of the loop you can enter a command. The game should end once you reach the final destination.

At the beginning it is unknown how many instructions the player will enter. Therefore the number of loops is unknown. In such situations a conditional loop with `while` is a good choice.

### Step 1

Define a variable that contains the current location. In Python you can use the name of the room as a string:

```python
room = "hometown"
```

### Step 2

In the version we are creating here as soon as you reach the room "clearing", the game ends. You can check that in the condition of the while loop. This ensures that once the user enters the "clearing" the loop will break, ending the game. 

Wrap the if-statements from the last version into the while loop. The `target` variable is used to differentiate between where the player is and where the player is going.  

```python
while room != "clearing":
    print(f"You are in {room}")
    target = input("Where would you like to go? ")
    ...

```

### Step 3

Add other rooms and puzzles, execute the program and make sure you can finish the game.
Remember to move the player to the next room by writing 

```python
room = target
```

within but at the end of the `while` loop. Also make sure your congratulations to the player winning is outside of the while to ensure it is only printed once the player has reached the clearing. 

{{% /notice %}}

## Reading

{{% notice reading "Reading" %}}

[W3 Tutorial on Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)

{{% /notice %}}

<br>

{{% notice copyright "Kristian Rother, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of 


- http://www.academis.eu/python_basics/reference/while.html

by Dr. Kristian Rother, used under CC-BY-SA 4.0. 
{{% /notice %}}

