---
title: "Methods, Functions, and Attributes"
weight: 50
---

![lens](/images/data_processing.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@srkraakmo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Stephen Kraakmo</a> on <a href="https://unsplash.com/s/photos/filter?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

{{% notice warmup "Methods, Functions, and Attributes" %}}

Discuss the syntax differences between the following commands:

```python
df = pd.DataFrame(data)
df.sum()
df.shape
```

{{% /notice %}}


## In Python everything is an object

### What is an object?

- this is a very philosophical question in python where it is said that (almost) everything is an object
- that means 7, 'Chair', `sum()` and everything else in python is an object 
- behind each of these objects is architecture (code) that defines what they are and what they can do
- what they are is called **attributes**
- what they can do is called **methods**

This lesson should shed some light on this philosophy.

In the warmer above there are 3 types of `pandas` commands listed **methods**, **functions** and **attributes**. Take a look at the differences:

### Functions

Typically functions are passed data, perform a transformation on the data and then return the result:

```python 
df = pd.DataFrame(data)
```

The `pandas.DataFrame()` function can take in various forms of data and transforms them into a `pandas` DataFrame.  In this case the dataframe would be stored in the varibale `df`.

Some of the most used `pandas` functions:

command                       | description
---                           | ---
`df = pd.DataFrame(...)`      | DataFrame creation
`x = pd.Series(...)`          | Series creation
`pd.read_csv(file)`           | read a table from disk
`pd.unique(values)`           | returns unique values in 1d array-like object
`pd.concat([df1, df2])`       | used to combine `Series` or `DataFrame` objects

**Note:** The syntax of a `pandas` function would always be as follows:

```python
pandas.function_name(data_passed)
```

Since we use the alias `pd` for `pandas` the commands listed above all start with `pd.`

### Methods

Methods perform a transformation or filter information from an object that it is called on. Using the dataframe stored in the `df` variable various pandas DataFrame methods can be called on `df`.

```python
df.head(n)
```

The pandas DataFrame method `.head()` shows us the top **n** rows on the dataframe it is called upon. 

The difference between a `method` and a `function` is that a function is given data to perform a transformation upon and a method performs the transformation on a defined object it is associated with. In this case that object would be a pandas DataFrame. 

Some common `pandas` methods:

command                       | description
---                           | ---
`df.to_csv(file)`             | write a table to disk
`df.sum()`                    | returns the sum of the values over the requested axis
`df.sort_values()`            | sorts by the values along either axis
`df.count()`                  | returns count non-NA cells for each column or row
`df.nunique()`               | returns the number of unique values in a Series or DataFrame
`df['col'].str.len()`         | returns the length of each string in `pandas` Series

**Notes:** 

- When applying `python` string methods to `pandas` Series the method must be preceded by `.str` accessor in order for the method to be called correctly
- Keep in mind that many but not all `pandas`methods can be applied to `pandas` DataFrames and Series


### Attributes

Attributes are values that describe a defined python object. In the case of a pandas DataFrame object one attibute would be the shape of the dataframe, how many rows and columns it has. An attribute is called in the same way as a **method** but has no `()` after the call.

```python
df.shape
```
Some common `pandas` attributes:

command                       | description
---                           | ---
`df.shape`             | returns tuple representing the dimentionality of the DataFrame
`df.index`                    | returns the index as an array-like object
`df.columns`            | returns the column index as an array-like object
`df.dtypes`                  | returns the data types in the DataFrame
`df.values`         | returns the values of the DataFrame as an array-like object
`df.ndim`         | returns an integer representing the number of axes

Functions, methods and attributes all depend on how the developers of a language or library program and design it. In the case of `pandas` the developers use Object Oriented Programming and instilled all three options for the users. 

## Project Challenges

{{% notice challenge "Total number of babys in specific years" %}}

- Using your `parse_dataset()` function write a program that calculates the total number of babys for the year 2020 and prints the number to the screen. Make sure to select the correct column to sum. 
- Do the same for 1950 and compare the results
- What other interesting insights can you find about about a year using some of `pandas` methods?

*Hint:*  Try combining some methods like `.sort_values()`, `.count()`, `.head()` and others. 

{{% /notice %}}

{{% notice challenge "Write code to combine datasets for analysis" %}}

Using the `parse_dataset(year)` custom function as a starting point, create code that loops over every year in the baby names data folder and combine the datasets into one dataset. 

1. Define empty `DataFrame` with the columns **names, gender, frequency** as `df`
2. Loop over each year and apply the `parse_dataset()` function to each year and save it in a variable such as `df_temp`. The loop would look something like this:

```python
for year in range(1880, 2021):
    ...
```

3. Within the loop add a `column`to `df_temp` in each iteration with the following code:

```python
df_temp['year']=year
```

4. Use the `pd.concat()` function to combine `df` and `df_temp` in every iteration until all datasets have been combined into one. The code should then return the `df`variable as a DataFrame with all names from 1880 to 2020 similar to the image below:

![baby df](/images/combine_baby_names.png)

5. Save the DataFrame in your `data` folder for later use:

```python
df.to_csv('../data/baby_names_all_years.csv', index=False)
```

6. Using the combined DataFrame and the method `.sort_values()` figure out which name had the all time highest frequency and in which year. 

**Bonus:**

- Wrap code into a function
- Input arguments could be the start and end year
- Output would be the complete dataframe with all years and names
- Function could also save the dataframe locally for later use

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}