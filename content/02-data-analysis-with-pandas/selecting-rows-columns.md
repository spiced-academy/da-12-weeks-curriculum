---
title: "Selecting Columns and Rows"
weight: 40
---

![](/images/select.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@poleznova?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Vitamina Poleznova</a> on <a href="https://unsplash.com/s/photos/select?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
  
{{< /credits >}}


## Key Concepts

It is an essential part of working with data to able to select specific parts of a dataset.  For example in order to fill in missing data in a particular column(s) this skill comes in very handy. This means that you should be very comfortable with the syntax of selecting rows and columns.

command  |  description
---|---|
`df[col]`                       |     select one column as a **Series**
`df[[col]]`                      |     select one column as a **DataFrame**
`df[[col1, col2, ... ]]`               |     select 2+ columns as a **DataFrame**
`df['column_name'] = new_values`      |     assign new values to the column
`df.drop()`      |     drop specified rows or columns
`df['column'].astype()`       |    cast a pandas column to a specified `dtype`
`df.loc[row]`                   |      select one row as a Series **by index**
`df.loc[[row1, row2]]`           |     select 1+ rows as a DataFrame **by index**
`df.loc[[row], [col]]`           |     select rows and columns as a DataFrame **by index**
`df.iloc[a:b, c:d]`             |      select rows/columns by **integer-location**
`df.set_index()`             |      set selected column as **index**


## Examples

### Selecting Columns


To work with one column in particular it can be explicitly selected:

```python
df['column_name']
```

This will extract the column as a `pd.Series`.

{{% notice info "pd.Series" %}}

Remember that dataframes are made up of columns, all of which are in fact `pandas.Series` objects. Most operations in pandas work for both dataframes and series of a dataframe.

{{% /notice %}}


### Changing the data type

When reading in a table with postal codes, pandas assigns the `int64` datatype to the column.
Technically postal codes are numbers but they don't have a numerical meaning. It
does not make sense to add two postal codes together or to calculate the average postal code.

Therefore changing the datatype to `string` values would be clever:

```python
df = pd.DataFrame({
   'PLZ': [54296, 50679, 38273, 16938]
})
df['PLZ'].astype(str)
```

This returns a *copy*  of the column and the original column does not change. To update the column and overwrite the current data use the following command:

```python
df['PLZ'] = df['PLZ'].astype(str)
```

{{% notice info "Common data types" %}}

Common data types in pandas are:

- `str` or `"object"` for strings
- `int` or `"int64"` for integer numbers
- `bool` for `True` and `False` values
- `float` or `"float64"` for floating point numbers
- `"datetime64"` for date and times


{{% /notice %}}

### Adding Columns

To assign the same values to all rows of a column write:

```python
df['new_column_name'] = 0
```

The new column can also be the result of an arithmetic operation:

```python
df['old_column_squared'] = df['old_column']**2
```

It can even be based on the calculations across several columns

```python
df['new_column'] = df['old_column_1']/df['old_column_2']
```


### Dropping Columns

An irrelevant column can be deleted with:

```python
df.drop('column_name', axis='columns')
``` 

A list of column names to be dropped can also be passed to the `.drop()` method and then  several columns will be dropped at once:

```python
df.drop(['col1', 'col2', 'col3'], axis='columns')
```

This operation returns a *copy* of the original DataFrame. To make the update persistent 
we need to add the function parameter `inplace=True`. 

```python
df.drop(['col1', 'col2', 'col3'], axis='columns', inplace=True)
```

{{% notice info "Inplace operations" %}}

Many operations in pandas return a *copy* of a series or table. The original data is left unchanged.
Typing

```python
df.drop('column_name', axis='columns')
```

returns a *copy* of the dataframe without that particular column. With the parameter 
`inplace=True` the operation is directly applied on the original column or table.

```python
df.drop('column_name', axis='columns', inplace=True)
```

Keep in mind that the `inplace=True`parameter will also work for other operations that return a pandas Series (columns in a DataFrame). In the following example the values of a column are sorted persistently. 

```python
df.sort_values('column_name', ascending = False, inplace = True)
```

This could also be done by overwriting the column with the sorted values: 

```python
df['column_name'] = df.sort_values('column_name', ascending = False)
```

or create a new column and keep both versions:

```python
df['new_column'] = df.sort_values('column_name', ascending = False)
```
{{% /notice %}}



{{% notice info "Vectorization" %}}

When performing arithmetic operations or logical comparisons in pandas, we apply 
the operations to whole columns of our dataset at once. Usually, when working
with pandas there is no need to write any `for` loops to iterate over rows or
columns of the data. This makes data handling in pandas clean and fast!

{{% /notice %}}

### Selecting rows with `.loc[row_index]`

Example dataset with a **numeric** index:

![](/images/number_index.png)

To select a row use the `.loc` command. `.loc` is short for *location*. The location is based on the index value. If the index is numeric then the first row can be selected as follows:

```python
df.loc[0]
```

![](/images/loc_0.png)


This returns a `pd.Series`.

If the index is set with **strings** such as a person's name then we would use the string to locate the row:

Example dataset with a **string** index:
![](/images/name_index.png)

```python
df.loc['Peter']
```
![](/images/loc_peter.png)


### Selecting rows with `.iloc[integer_position]`

Another selecting command is `.iloc`. Instead of location this stands for *integer location*. This means that selection is done according to the count from the first (zero) row or column. To achieve the same result as in either of the example dataframes above the syntax using `.loc` would be:

```python
df.iloc[0]
```


**Note:** Since the **i** stands for integer **only** an integer can be passed to `.iloc`.

### Selecting multiple rows

To select multiple rows use slicing or a list of values. The syntax is the same as the Python `list` slicing method. The example below selects only the first two rows:

```python
df.iloc[0:2]
```

Or without slicing:

```python
df.iloc[[0, 1]]
```

Both `.loc` and `.iloc` allow slicing to be used. Below are two examples that may not result in what one expects:

```python
df.loc['Peter':'Wendy']
df.iloc[0:1]
```

Leaving out the first or the last positon of the index in a slice will take all values from the beginning or to the end of the index into account:

```python
df.iloc[:3]
df.iloc[1:]
```

When slicing using `.loc` or `.iloc` the step can also be defined. In the example below we select every second row:

```python
df.iloc[::2]
```



### Selecting both rows and columns with `.iloc` and `.loc` 

To select the first two rows and the first row columns use the following syntax:

```python
df.iloc[0:2, 0:2]
```

The steps can be defined for the rows as well as for the columns. In this example every second row and every second column is selected:

```python
df.iloc[::2, ::2]
```

To select the *City* of *Peter* and *Wendy* the following syntax is used:

```python
df.loc[["Peter", "Wendy"], "City"]
```


{{% notice question "Returning a series or data frame" %}}


What is the difference? Execute each line separately and carefully inspect the
returned object!

```python
df.loc[["Peter"]]
df.loc["Peter"]
df["City"]
df[["City"]]
```

{{% /notice %}}

## Exercises

Download the small dataset below and try the examples and other commands from above in an empty notebook:

{{% attachments title="Related files" pattern="selecting_rows_example.csv" /%}}


## Project Challenges

{{% notice challenge "Selecting rows and columns" %}}

Download the attachments and save in `data` and `notebooks` folders. Run the commands in the notebook and make sure you're comfortable with the syntax. Take your time to understand what each command does.

{{% attachments title="Related files" pattern="selecting_rows_and_columns|yob_1880.csv" /%}}
{{% /notice %}}

{{% notice challenge "Solve One-Liners" %}}

Using the same dataset from the challenge above solve the following tasks with pandas one-liners:

```python
# 1. Read in data:
df = pd.read_csv('../data/yob_1880.csv', index_col=0)

# 2. display the 'frequency' column

# 3. display the 'gender' and 'frequency' columns

# 4. display the data for row(s) containing William

# 5. display the data for all rows with William, Paul, and Anne

# 6. display the 'frequency' column for William, Paul, and Anne

# 7. display the first three names and both columns

# 8. display the both columns for every second name

```

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}
