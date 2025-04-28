---
title: "Python Lists"
weight: 31
---

![A container ship](/images/list.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@ventiviews?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Cameron Venti</a> on <a href="https://unsplash.com/s/photos/container?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

{{% notice warmup "Warmer: Lists" %}}

Try a few commands for creating lists:

```python
numbers = [1, 2, 4, 8, 16, 32]
numbers.extend([64, 128, 256])

movies = ["Star Wars", "Star Trek", "Ratatouille"]
movies.append(["Arrival", "Interstellar"])
```

Print the lists.

{{% /notice %}}


## Concepts

Lists can be used to combine multiple *arbitrary* values into a new *container-like* data structure. 

To process larger amounts of data, we cannot invent a new variable name for every entry (and write the code for it). Somehow it has to be possible to store multiple data records in one variable. 

This is where lists come in.


command  |  description
---|---|
`numbers = [1, 2, 3, 4, 4]`      |   list creation
`numbers.append([2, 3])`      |   append the item to the end of the list
`numbers.extend([2, 3])`      | append each element to the end of the list
`numbers[3]`       |     indexing
`numbers[2:4]`       |    slicing
`len(numbers)`       |     returns the length of a list
`numbers.count(4)`   | searches for and counts the number of an element in a list

## List Creation

Lists represent a sequence of values. You can store and mix different values in a single list:

```python
namecounts = ['Hannah', 123, 'Emiliy', 234, 'Madison', 23]
```


## Accessing elements of lists

You have already seen how to do indexing and slicing with strings. Now you can do the same with lists!

Lists are a simple sequence of elements. However, Python is counting differently than humans:

![](/images/list_index.PNG)

Using square brackets, any element of a list can be accessed. The first element has the index 0:

```python
numbers[0]
numbers[3]
```

Negative indices start counting from the last character:

```python
namecounts[-1]
```

What do the following commands result in?

```python
numbers[4]
movies[0]
movies[-1]
numbers[-3]
```

Remember that the right number is not included when extracting several elements from a list:

```python
namecounts[1:3]
namecounts[:3]
namecounts[-2:]
```

What do the following commands result in?

```python
movies[2:]
movies[:2]
numbers[2:-2]
numbers[::2]
```

## Adding and removing elements

Add a new element to the end of the list:

```python
numbers.append(45)
```

Remove a defined element:

```python
numbers.remove(4)
```

Remove an element at a given index position:

```python
numbers.pop(3)
```

Or remove the last element:

```python
numbers.pop()
```

{{% notice info "In-place Operations" %}}

The string methods in the previous chapter returned a copy of the string and left the original string unmodified. The `pop()`, `append()`, `remove()` and other list methods modify the list *in-place*. They directly change the content of the original list!

{{% /notice %}}

## Checking whether an element exists

With the `in` operator we can check whether an element exists in the list:

```python
if 34 in numbers:
   print("let's go on")
```

## Exercises


### List Methods

Find out what each of the expressions does to the list in the center.

![](/images/list_methods.png)


### List Transformation I

Use the expressions to modify the list as indicated. Use each expression once.

![](/images/list_funcs1.png)

### List Transformation II

Use the expressions to modify the list as indicated. Use each expression once.

![](/images/list_funcs2.png)

### Combine your knowledge: conditional loops and lists

The following if loop searches for 33 in the data. Modify the code, so that it uses a while loop instead.

```python
data = [5, 7, 33, 12, 4, 3, 18]

found = False

if data[0] == 33:
   found = True
   print(f"The value 33 has been found: {found}")
elif data[1] == 33:
   found = True
   print(f"The value 33 has been found: {found}")
elif data[2] == 33:
   found = True
   print(f"The value 33 has been found: {found}")
elif data[3] == 33:
   found = True
   print(f"The value 33 has been found: {found}")
elif data[4] == 33:
   found = True
   print(f"The value 33 has been found: {found}")
elif data[5] == 33:
   found = True
   print(f"The value 33 has been found: {found}")
elif data[6] == 33:
   found = True
   print(f"The value 33 has been found: {found}")
else:
   print(f"The value 33 has been found: {found}")
```

## Project Challenges

{{% notice challenge "Checks I" %}}

At the moment the program is not checking whether a room you entered really exists. If you enter a wrong room (or make a typo), the program stops with an error message.


Let’s check the input to prevent that. Outside of the main loop, create a list 
of rooms `rooms` the player can go to: 

```python
room = 'hometown'
honey = False
rooms = ['hometown', 'another room', 'even another room'] # list rooms that are in your game
```

Then check if the room entered by the player is in your list before moving onto the puzzles. The following code matches the users input with the list of rooms:

```python
...
if target in rooms:
   ...
   room = target
   ...
else:
   print("Stop! There is no such place.")
```

- Find out where in the program these lines need to be inserted. Execute the program and make sure it works.
- How can you make sure that the selection mechanism also works in case the user types in e.g. `"Hometown"`, `"HOMETOWN"` or `"hometown"`?

{{% /notice %}}

## Reading

{{% notice reading "Reading" %}}

[List and Tuples - In Depth Guide](https://realpython.com/python-lists-tuples/)

{{% /notice %}}

<br>

{{% notice copyright "Kristian Rother, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).  It is a derivative of 

- http://www.academis.eu/python_basics/reference/lists.html

by Dr. Kristian Rother, used under CC-BY-SA 4.0. 
{{% /notice %}}
