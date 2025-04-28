---
title: "Python Dictionaries"
weight: 32
---

![A book shelf](/images/library.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@alfonsmc10?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alfons Morales</a> on <a href="https://unsplash.com/s/photos/library-index?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
  
{{< /credits >}}

{{% notice warmup "Warmer: Storing Tabular Data" %}}

We want to store information about the frequency of names for newborn babies:

|name|frequency|
|--- | ---     |
|Alice| 234|
|Emily | 387|
|Madison | 103 |

In Python, we can represent this information in a list:

```python
namecounts = [
   'Alice', 234, 'Emily', 387, 'Madison', 103
]
```

What issues do you see with this code? Can you come up with better data structure to represent this information?

{{% /notice %}}


## Concepts

Dictionaries consist of *unordered* key-value pairs. They are very versatile data structures and good for looking up things, or searching in general.

command  |  description
---|---|
`ratios = {'Alice': 0.75, 'Bob': 0.55}`      |   dict creation
`ratios['Alice']`      |   accessing elements
`ratios.get('Alice')`      | accessing without error
`ratios['Tim'] = 0.43`       |     adding entries
`ratios.keys()`       |   get they keys of a dict
`ratios.values()`       |     get the values of a dict
`ratios.items()`   | get both keys and values 

## Dict Creation

You can store any value with a corresponding key. They key can be used to retrieve 
the value later:

```python
animals = {
   'cat':'Katze',
   'dog':'Hund',
   'fish':'Fisch'
}
```

They keys of this dict are `cat`, `dog` and `fish`. The values are `Katze`, `Hund`, `Fisch`. 


## Accessing elements of a dict

By using square brackets and a key, you can retrieve the values from a dictionary.
You can only retrieve a single key-value pair, at least if the key is present:

```python
animals['cat']         # Katze 
animals['elephant']    # KeyError!
```

With the `get()` method you can assign an alternative value if the key was not found:

```python
ratios.get('Alice')
ratios.get('Ewing')
ratios.get('Ewing', 'sorry not found')
```


## Updating a dict

The contents of a dictionary can be modified. For instance if you start with an empty dictionary:

```python
persons = {}
```

Now you can add or update values one key/value pair at a time:

```python
persons['Emily'] = 1977
```

## Checking whether a key exists

The `in` operators checks whether a key exists in the dictionary.

```python
if 'Bob' in ratios:
    print('found it')
```
{{% notice info "What data can I use as keys?" %}}

Valid types for keys are:

- numbers like `int` or `float`
- strings `str`
- tuples `tuple` 
- boolean `bool` values like `True` and `False`

You may mix keys of different type in one dictionary. However, mutable data types such as lists and other dictionaries are not allowed as keys.

The concept behind this phenomenon is that dictionaries use a hash function to sort the keys internally. The hash function is what allows to look up values very quickly.

{{% /notice %}}

## Exercises


### Dict Methods

Find out what each of the expressions does to the dict in the center.

![](/images/dicts.png)


### What do these commands produce?

```python
animals = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}

### 1.
print(animals['fish'])

### 2.
print('Hund' in animals)


### 3.
print(list(animals.keys()))

### 4.
print(animals.get('Katze', 'unknown'))
```

### Travelling

The following program allows you to travel from one city to the next. Unfortunately, it contains 4 bugs. Keep in mind semantic errors will not return an error message, but the program will not do as expected. Also remember that holding the ctrl or strg key and the letter c will break any infinite loop you get stuck in!  Find 5 errors and fix them.

```python
cities = {
    "New York": ["Tokyo", "Paris", "London"],
    "Poznan": ["London", "Berlin"],
    "London": ["New York", "Poznan"]
    "Berlin": ["Tokyo", "Poznan"],
    "Tokyo": ["New York", "Berlin"],
    "Paris": ["Katmandu"]
    }

location = "Paris"

print "\nYour task: fly to Katmandu\n"

while location in cities and location == 'Katmandu':
    print(f"You are in {location}")

    print("There are flights to ", cities[location])
location = input("Where would you like to travel?")

print("You have reached your destination")
```
Even after all of the error have been found there are numerous ways to make the program more robust. What ideas do you have?

## Project Challenges

{{% notice challenge "Data Structure" %}}

Checking every room with a separate if statement is feasible if you have 4 rooms. But imagine your game has 100 or more rooms – the program would become quite messy.

A better alternative is to structure the room data. We will use a dictionary that contains descriptions of all rooms:

```python
descriptions = {
    "hometown": """You are in your home town...""",
    "desert": """...""",
}

```

Define this dictionary at the beginning of the program. Now you can replace all if statements by a single request to the dictionary. The key is the room variable.

Add this command where applicable to the `while` loop:

```python
print(descriptions[room])
```

and remove the `if` statements from before. Execute the program and make sure it works.

{{% /notice %}}


{{% notice challenge "Checks II" %}}

You now have all rooms defined in the dict `descriptions`. Remove the list of rooms `rooms` 
and update your code that checks for a valid input.

The following code matches the users input with the keys of the dictionary descriptions:

```python
target = input("Where do you want to go? ")
if target in descriptions:
    ...
```

{{% /notice %}}

## Reading


{{% notice reading "Reading" %}}

[Dictionaries - In Depth Guide](https://realpython.com/python-dicts/)

{{% /notice %}}

<br>

{{% notice copyright "Kristian Rother, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of 

- http://www.academis.eu/python_basics/data_structures/dictionaries.html


by Dr. Kristian Rother, used under CC-BY-SA 4.0. 
{{% /notice %}}