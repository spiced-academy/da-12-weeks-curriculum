---
title: "Writing Functions"
weight: 30
---

![assembly line](/images/function.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@carlosaranda?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">carlos aranda</a> on <a href="https://unsplash.com/s/photos/factory?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

{{% notice warmup "Built-in functions and keywords" %}}

Collect as many built-in python *functions* and *keywords* that you can think of that we have used so far.

{{% /notice %}}


## Built-in Python Functions

In Python, there is a basic set of about 70 functions called [built-in functions](https://docs.python.org/3/library/functions.html). Many of them are shortcuts that make your everyday programming a lot easier. Here, the 25 most important ones are given.


 type conversion | 	I/O |	math |	iterables 	| introspection
 --- | --- | --- | --- | --- 
`int`   |	`print` |	`abs`   |	`range`    |	`type`
`float` |	`input` |	`round` |	`len`      |	| 
`str`   |	`open` 	|  `sum`   |	`sorted`   |	|
`bool`  |		   |  `min`   |	`reversed` | 	|
`tuple` |	      |  `max`   |	`enumerate`| 	|
`list` 	|		   |  | `zip`  	         ||
`dict` 	|		   |	|`filter`||
`set` 	|	      | |`map`||

These 25 functions are your basic vocabulary, knowing these is a must to write Python efficiently!


## Defining Custom Functions

You can also create your own functions! A function definition is like a blue-print of an automated assembly line. With a function you *describe* an autonomous sub-program with its own **local variables**, input and output:

```python
def find_name(data, name, year):
    '''Returns records from a dictionary (data) of a baby name (name) in a given year (year).'''

    result = []

    for record in data[year]:
        if record[0] == name:
            result.append(record)
            
    return result
```

![python function](/images/function.PNG)


## Calling a function

Once defined, the function can be *called* everywhere in your program and multiple times. This helps you divide your program into smaller logical portions. It is much easier to write, reuse and debug a program consisting of many small functions than a single huge blob of code.

Our data:
```python
babynames = { 1985 : [('Rachel','F',16362) , ('Naomi','F',1078) , ('Estefania','F',22) ,
                      ('Juluis','M',12) , ('Tyrone','M',22) , ('Rachel','M',77)],

              2000 : [('Rachel','F',10680) , ('Naomi','F',1756) , ('Estefania','F',232) ,
                      ('Juluis','M',485) , ('Tyrone','M',607) , ('Rachel','M',12)],

              2015 : [('Rachel','F',1934) , ('Naomi','F',3772) , ('Estefania','F',195) , 
                      ('Juluis','M',1146) , ('Tyrone','M',233) , ('Naomi','M',5)] 
            }
```

The input arguments are matched with the parameters of the function:

```python
find_name(babynames, 'Rachel', 1985)
```

For complicated functions with a lot of input parameters, it is good practice to write out both the function parameter and its value:

```python
find_name(data=babynames, name='Rachel', year=1985)
```

You can call the function as many times as you like:

```python
print(find_name(babynames, 'Rachel', 1985))
print(find_name(babynames, 'Rachel', 1985))
```

You can also store the result of a function call in a new variable:

```python
rachel_stats = find_name(babynames, 'Rachel', 1985)
print(rachel_stats)
```

You can also store the input value in a variable before passing it into the function:

```python
forename = 'Naomi'
born = 2015

find_name(babynames, forename, born)
```


## Obligatory and optional parameters

Each function can have obligatory parameters that must be given when calling the function and optional parameters that have default values. The following function can be called in two ways:

```python
def find_name(data, name, year=2000):
    '''Returns records from a dictionary (data) of a babyname (name) in a given year (year).'''
    result = []
    for record in data[year]:
        if record[0] == name:
            result.append(record)
    return result

print(find_name(babynames, 'Rachel'))
print(find_name(babynames, 'Rachel', 2015))
```

## Return values

A function may return values to the program part that called it:

```python
return 10680
```

You can also return a list or dictionary of values:

```python
return {'name': 'Rachel', 'sex': 'F', 'frequency': 10680}
```

In any case, the `return` statement immediately ends the execution of a function!


## Exercises





### Task 1

Fill in the missings!

```python
___ make_path(year):
   """Given a year, constructs a valid file path for the names dataset"""
   ___ = f'./___/yob{year}.txt'
   ___ path

print(___(1987))
```

*Example*: Calling the function with

```python
make_path(1945)
```

should return 

```txt
'./data/yob1945.txt'
```

### Task 2

Fill in the missings! How could we connect it with the previous function?

```python
def read_year(___):
    df = pd.____csv(path, ____=['name', 'gender', 'frequency'])
   return df

```

### Task 3

Bring the following statements into correct order:

```python
   total_minutes = minutes + hours*60
   return total_seconds
def time_to_sec(hours, minutes, seconds):
print(time_to_sec(10,10,10))
   total_seconds = seconds + total_minutes*60
```

### Task 4

Find all bugs and make the functions work!

```python
def add_together(a):
   return a+b

bool_to_string(boolean) def:
   """converts True to 'true' and False to 'false'"""
   str(boolean).lower()

def first_and_last(element):
   """returns the first and last element in a list"""
   return [elements[0], elements[10]]

def average(numbers):
   """calculates the average of a list of numbers"""
   return summ(numbers)/numbers.len()

def words_to_upper(words):
   """converts all words in the list to uppercase"""
   words_upper = []
   for word in words:
      return word.upper()
```

## Project Challenges


{{% notice challenge "Names Dataset" %}}

Write a function `parse_dataset(year)` that helps you work with the data.

The function should:

- accept a single year as input value
- construct a valid file path 
- read in the corresponding names dataset
- define the correct column index for the data set
- output the dataset as a pandas dataframe

Example: Calling the function with `parse_dataset(year=1880)` should return:

![birth table](/images/parse_dataset.png)

Tips:

- First develop the code in a cell of a Jupyter notebook
- Start by defining a year variable `year=1880`
- Test the code on a few text lines only
- If everything works wrap the code into a function


{{% /notice %}}


{{% notice reading "Reading" %}}

[Tutorial on python functions](https://www.datacamp.com/community/tutorials/functions-python-tutorial)

{{% /notice %}}

<br>

{{% notice copyright "Kristian Rother, Malte Bonart, Samuel McGuire" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of 

- https://www.academis.eu/posts/python_reference/functions.md
- https://www.academis.eu/posts/python_reference/builtin_functions.md


by Dr. Kristian Rother, used under CC-BY-SA 4.0. 
{{% /notice %}}