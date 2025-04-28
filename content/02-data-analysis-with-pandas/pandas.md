---
title: "Introduction to Pandas"
weight: 20
---

![a panda](/images/pandas.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@billow926?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">billow926</a> on <a href="https://unsplash.com/s/photos/pandas?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

{{% notice warmup "Working with Tables" %}}

- Collect core features of a typical spreadsheet editor.
- Anything you can't do with it?

{{% /notice %}}

## Installation

Install Pandas through a Terminal:

```bash
pip install pandas
```

## Key Concepts

Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language. Pandas developers have done the heavy lifting and programmed many useful functions that help in data analysis. 

To use functions from the `pandas` package you need to `import` it first:

```python
import pandas as pd
```

As a shortcut while programming developers typically use `pd` as an alias while programming to save time. 

command                       | description
---                           | ---
`df = pd.DataFrame(...)`      | DataFrame creation
`x = pd.Series(...)`          | Series creation
`df.shape`                    | tuple with the number of rows and columns
`df.head(n)`                  | shows `n` first rows
`df.columns`                  | list with column index names
`df.index`                    | list with row index
`df.dtypes`                   | returns data type of each column in the dataframe
`df.to_csv(file)`             | write a table to disk
`pd.read_csv(file)`           | read a table from disk


## DataFrames

``DataFrames`` are the central data structure in ``pandas``.

![](/images/dataframe.svg)

Each DataFrame consists of 

- multiple columns, each column is an object of type ``pd.Series``
- a row index (row names)
- a column index (column names)

Columns of a DataFrame are objects of type **pd.Series**. Each series only contains values 
of one specific data type:

- `int64` for integer values
- `object` for string values
- `bool` for boolean values
- `float64` for float values

## Level of Measurement

A `pandas` Series or DataFrame column can only contain variables of one data type. This is different than a `python` list where different data types can be mixed together. These variables fall under three categories: **catergorical**, **ordinal** and **metric**.  

### Inspecting the data type of a column

The data types of each column in a DataFrame can be listed as such:

```python
df.dtypes
```

It is also possible to use info()

```python
df.info()
```


### Categorical Variables

Categorical variables (also called *nominal* variables) have values or labels that do not follow a natural ordering. The labels of categorical variables can be encoded as numbers with the data type `int` or `float`. However, in this case mathematical operations (addition, multiplication, …) shouldn’t be applied.

Examples:

- Location (Berlin, Johannesburg, …)
- Nationality (German, Spanish, ...)
- Postal Codes (54296, 50679, …)

### Ordinal Variables

Ordinal variables are categorical variables that follow a natural order.
As with categorical variables this kind of data can be encoded with numeric values.

Examples:

- Movie Ratings (5 Stars, …, 1 Star)
- Evaluation (‘Very Good’, ‘Good’, …, ‘Aweful’)
- Month of the year (1, 2, 3, …, 12)

### Metric Variables

Metric or numeric variables have values with a natural ordering and the distance between two values is interpretable. Hence, we can say “this value is twice as large as the other value”.

- Height in cm (186, 150)
- Age in years
- Price in $

## Creating DataFrames from Scratch

### From a two-dimensional list

```python
import pandas as pd
import numpy as np

data = [[82_000_000, 1.9, "Europe"],
      [ 5_500_000, 1.8, "Europe"]]

df = pd.DataFrame(data,
                  columns=['population', 'fertility', 'continent'],
                  index=['Germany', 'Denmark'])
```

### From a dictionary

```python
data = {'spices': ['parsley', 'sage', 'rosemary', 'thyme'],
      'value': [1.2, 3.4, np.nan, 5.6],
      'good_for_spaghetti': [False, False, True, True]}

labels = ['a', 'b', 'c', 'd']
df=pd.DataFrame(data,index=labels)
```

### Series creation

In some cases we might also want to create a `pd.Series` object:

```python
data = [1.3, 2, 6, 3, 5]
x = pd.Series(data)
```

## Reading and Writing DataFrames

Using pandas dataframes can be `read` from all kinds of formats:

-  `pd.read_csv()`
-  `pd.read_excel()`
-  `pd.read_json()`

In turn the data can be made persistant using various `write` methods:

-  `df.to_csv()`
-  `df.to_excel()`
-  `df.to_json()`


### CSV files

A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. A CSV file typically stores tabular data (numbers and text) in plain text.

concept  |  description
---|---|
`name,year,frequency` | header line with column names
`Anna,1987,123` | a single record or observation

Comma-separated values (*csv*) files are text files that are commonly used for 
storing *tabular data*:

```bash
first;last;age
Emily;Smith;23
Charlie;Parker;45
```

- Each row is called a record or observation
- Each row can have multiple columns
- Values are separated by a comma `,`, semicolon `;` or tab `\t`
- Typically, the first row contains the name of each column

### Reading from a CSV file

The most commonly used read command is `pandas.read_csv`. In this example the data is read in and the first column is assigned as the row index:

```python
df = pd.read_csv("./relative/path/to/baby_names.csv")
```

The first and only required parameter in the `read_csv` function is the `file path`. 

Other useful parameters from `pd.read_csv`:

parameter                     | description
---                           | ---
``sep=","``                   | column separator when reading CSV
``header=True``               | whether there is a row with the header (boolean)
``names=['a', 'b', 'c']``     | column names when there is no header
``index_col=0``               | which column to use as row index
``na_values=['-9999', 'xxx']``| additional values that will be converted to missing `NA`/`NaN`

**Note**: The `read_csv` command can also be used to read in files with other formats such as `.txt`. 

```python
df = pd.read_csv("baby_names.txt")
```

### File paths and file endings

```bash
./data/baby-names/2012/names.txt
```

All files on your computer have a unique path that locates the file on your hard drive.
Files and folders are logically arranged in a hierarchical tree like structure:

{{% expand "Open the 'da-projects' file tree" %}}

```bash
da-projects
|
├── babynames
│   ├── df_total.csv
│   ├── names
|   |    ├── 1987.txt
│   |    └── ...  
│   ├── README.md
│   └── test.py
|
├── dogs_vs_cats
│   ├── dataset
│   │   └── test_set
|   |       |    ├── 1.png
│   |       |    └── ...
│   │       └── dogs
|   |            ├── 1.png
│   |            └── ...
│   ├── dataset.zip
│   ├── dogs_vs_cats.ipynb
│   └── README.md
|
├── flags
│   ├── europe.png
│   ├── flags.ipynb
│   ├── germany.png
│   ├── japan.png
│   ├── README.md
│   └── test.png
|
├── numbers
│   ├── hints
│   │   ├── hint_1.py
│   │   ├── hint_2.py
│   │   ├── hint_3.py
│   │   ├── hint_4.py
│   │   └── solution.py
│   ├── README.md
│   └── report.txt
|
└── README.md

```
{{% /expand %}}

{{% notice question "Paths" %}}

Look at the file tree above.

- What is the name of the root folder?
- How many python scripts do you count?
- Is there a Jupyter Notebook?
- How many folders are there? What is the deepest folder level?
- Specify the file path for `japan.png`!

{{% /notice %}}

A relative file path starts with a dot and a slash `./`. When you work in a notebook
the `./` is replaced by the location of the notebook. 

Each sub-folder in a path is separated by a slash `/`. 

The last part of a path is the *filename*. A filename usually consists of a name and a file ending separated with a dot `.` : `my-file.txt`.

### The `FileNotFoundError`

When using a file path that doesn't exist on your computer, you will receive an error:

```ipython
In [1]: file = open('my_file.txtxt')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-1-5fc146c60982> in <module>
----> 1 file = open('my_file.txtxt')

FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txtxt'

In [2]: 
```

## Task: Fix 5 Bugs

Copy code into a jupyter notebook and execute. Fix the bugs until the results are correct:

```python
import pandas

spices = ['One-Hot Chili Peppers',
          'Bayesian Basil',
          'Tensor Thyme'
          'Linear Lavender',
          'Artificial Neural Nutmeg',
          'Polynomial Peppermint',
          'Sigmoid Saffron'
          ]
participants = [2, 6, 9, 9, 9, 8]

df = pd.DataFrame({'name': spices,
                   'participants': participants
                   })

print(sort_values(by='participants', ascending=False))

print("\ntotal participants:", df.sum(['participants']))

```

## Project Challenges

{{% notice challenge "Reading data with pandas" %}}

   1.  Download the Jupyter notebook and save in `notebook` folder
   2.  Download the `yob` files and save in lessons' `data`folder 
   3.  Open the notebook in Jupyter
   4.  Execute the commands

   {{% attachments title="Related files" pattern="pandas_inspecting_data|yob" /%}}

{{% /notice %}}

## Reading

{{% notice reading "Pandas Cheat Sheet" %}}

{{% attachments title="Related files" pattern="pandas_cheat_sheet" /%}}


{{% /notice %}}


{{% notice reading "Pandas Practice" %}}

- [100 short Pandas exercises](https://github.com/ajcr/100-pandas-puzzles/blob/master/100-pandas-puzzles.ipynb)
- [101 pandas exercises](https://www.machinelearningplus.com/python/101-pandas-exercises-python/)
- [More pandas exercises](https://github.com/guipsamora/pandas_exercises)
- [Pandas Tutorial](https://github.com/jorisvandenbossche/pandas-tutorial)

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}