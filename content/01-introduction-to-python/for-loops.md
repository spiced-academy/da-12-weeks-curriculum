---
title: "For Loops"
weight: 80
---

![a staircase](/images/for_loop.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@crissyjarvis?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Crissy Jarvis</a> on <a href="https://unsplash.com/s/photos/counting?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

{{% notice warmup "Warmer: Repeating Instructions" %}}

What does the following program do?

```python
for number in range(1, 43):
    print(number)
```
What advantages does the for loop have over the following one?

```python
print(0)
print(1)
print(2)
print(3)
print(4)
...
```


{{% /notice %}}


## Introduction

With the `while` statement you could repeat one or more instructions several (or infinite) times until a boolean condition was fulfilled. A `for` is used to repeat the instructions for a *fixed* number of times that you know in advance!

```python
import time

for i in [1, 2, 3, 4, 5]:
    print("You are great at programming!")
    time.sleep(5)

```

To write a for loop you need two things: *First* a sequence-like object (e.g. a list, a string, a dictionary or the output of a function producing sequences). *Second*, a variable that takes different values as the loop iterates over the sequence.

{{% notice info "Loops" %}}

Things you can iterate over with for loops:

- strings (character by character)
- lists (element by element)
- dictionaries (over keys, values, or both keys and values)
- files (line by line)
- iterable functions (like `range`)

{{% /notice %}}


## Examples

### Indented block

All indented commands after the colon are executed within a for loop. The first unindented command is executed after the loop finishes.

```python
for i in range(5):
    print('inside')
    print('also inside')
print('outside')
```

### Loops executing a given number of times

With the `range()` function, you can set the number of iterations easily:

```python
for i in range(7):
    print(i)
```

or using an interval:

```python
for i in range(10, 17):
    print(i)
```

or backwards:

```python
for i in range(17, 10, -1):
    print(i)
```

### Loops over a string

With a string as the sequence, you obtain single characters in each iteration.

```python
for char in 'ABCD':
    print(char)
```

### Loops over a list

A list iterates simply once through each element:

```python
for elem in [1, 22, 333, 4444, 55555]:
    print(elem)
```

### Loops over a dictionary

With a dictionary, the for loop iterates over the keys. Note that the dictionary is inherently unordered. Theoretically, you could get the keys in a different order each time.

```python
pairs = {'Alice': 'Bob', 'Ada': 'Charlie', 'Visual': 'Basic'}
for key in pairs:
    print(key)
    print(pairs[key])
```

You can also loop over the values:

```python
for value in pairs.values():
   print(value)
```

### Looping over two lists simultaneously

Sometimes, you want to look up corresponding items from two lists. A straightforward solution is to loop over an index:

```python
names = ['Alice', 'Bob', 'Charlie', 'Delia']
jobs = ['admin', 'builder', 'cook', 'developer']

for i in range(4):
    print(names[i] + ' works as a ' + jobs[i])
```

However, the *pythonic* solution would be to use zip:

```python
for name, job in zip(names, jobs):
    print(name + ' works as a ' + job)
```

## `zip(l1, l2, ...)`

The `zip` function is the shorthand version of the previous example. It combines
two or more lists of the same length and returns a single list of lists where each
inner list contains the combined elements of each original list. 


```python
names =  ['Mary', 'Helen', 'Anna']
genders = ['F', 'F', 'F']
frequencies = [16705, 6342, 6114]

for name, gender, frequency in zip(names, genders, frequencies):
    print (name, gender , frequency)
```

returns 

```python
Mary F 16705
Helen F 6342
Anna F 6114
```

{{% notice info "Lists and Tuples" %}}

If you closely check the output of the previous two examples you will notice a slight difference:

```python
[['Mary', 'F', 16705], ['Helen', 'F', 6342], ['Anna', 'F', 6114]]
```

is not exactly the same as

```python
[('Mary', 'F', 16705), ('Helen', 'F', 6342), ('Anna', 'F', 6114)]
```

`('Mary', 'F', 16705)` is called a *tuple*. For most cases tuples work the same as lists
but there is one important difference:

Tuples can't be changed or extended after their creation, they are *immutable*. Lists are of
variable length and can be updated and changed, they are *mutable*. 

This operation will result in an error

```python
x = ('blue', 'green', 'yellow')
x[1] = ['purple']
```

```python
TypeError: 'tuple' object does not support item assignment
```

It seems that lists always beat tuples but in some cases tuples are more efficient and safer to use.  
We can always convert a tuple to a list with `list()` or vice versa with `tuple()`.

{{% /notice %}}

## `enumerate(list)`

Enumerate returns a list of tuples where each tuple contains the original list element and a counter:

```python
x = ['a', 'b', 'c', 'd']
list(enumerate(x))
```

returns 

```python
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
```

Using enumerate in a loop allows access to each item and it's index:

```python
for index, item in enumerate(x):
    print(f'index postiion: {index}, value: {item}')
```

returns

```python
index postion: 0, value: a
index postion: 1, value: b
index postion: 2, value: c
index postion: 3, value: d
```



## Exercises

### Task 1

Write a for loop that creates the following output

```txt
1
4
9
16
25
36
49
```

### Task 2

Explain the difference between the following two programs:

```python
total = 0
for number in range(10):
    total = total + number
    print(total)
```

and

```python
total = 0
for number in range(10):
    total = total + number
print(total)
```

### Task 3

What does the following program do?

```python
text = ""
characters = "Hannah"
for char in characters:
    text = char + text
print(text)
```

### Task 4

Write a program that calculates the number of characters in `"Stefani Joanne Angelina Germanotta"`. Spaces count as well!

### Task 5

The following for loop searches for 33 in the data. Modify the code, so that it uses a while loop instead.

```python
data = [5, 7, 33, 12, 4, 3, 18]

found = False
for n in data:
    if n == 33:
        found = True

print("The value 33 has been found: {}".format(found))
```

### Task 6

The following while loop counts numbers higher than 10. Change the code so that it uses a for loop instead.

```python
data = [4, 7, 11, 1, 3,  15]

i = 0
high = 0
while i < len(data):
    if data[i] > 10:
        high += 1
    i += 1

print(f"There are {high} values higher than 10")
```

{{% notice reading "Reading" %}}

[Guide on Python For Loops](https://realpython.com/python-for-loop/)

{{% /notice %}}

{{% notice info "Bonus: List Comprehension" %}}

There is a clever shortcut that was introduced in python 2.0 called *list comprehension*. Using a `for` loop, the results can be imediately added to a list:

```python
In [1]: new_list = [x for x in range(10)]

In [2]: new_list
Out[3]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
``` 
This removes the need to initalize an empty list and use append. How does it work? 

![list comprehension](/images/list_comprehension.png)

For more info follow the link: [list coprehension](https://www.geeksforgeeks.org/python-list-comprehension/)

{{% /notice %}}

<br>

{{% notice copyright "Kristian Rother, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of 


- http://www.academis.eu/python_basics/reference/for_loops.html

by Dr. Kristian Rother, used under CC-BY-SA 4.0. 
{{% /notice %}}