---
title: "Filtering Dataframes"
weight: 60
---

![An intro image](/images/filter.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@nate_dumlao?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Nathan Dumlao</a> on <a href="https://unsplash.com/s/photos/filter?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

{{% notice warmup "Logical Comparison" %}}

You have the following two pandas Series:

```python
import pandas as pd

x = pd.Series([1, 4, 6, 2])
y = pd.Series([9, 2, 3, 2])
```

Try out the following statements line by line. Can you guess the outcome?

```python
x < y
x == y
x >= y
(x > 2) | (y == 9)
(x == 2) & (y == 2)
x.between(4, 6)
y.isin([2, 9])
x.isin(y)
```
{{% /notice %}}

## Logical Comparison

Take this dataset for example:

![An intro image](/images/filter_example.png)

Comparison operators can be used to filter dependent on one or more variables:

```python
df_example['age'] > 30
```
What does this code return us?

![An intro image](/images/bool_series.png)

Since the age column was selected it returns a series. Since a comparison operator was applied on the column it transforms the series into boolean values that reflect the results of the operation, `True` or `False`. 


## Boolean Masks

The boolean series can be used as a so-called **boolean mask**. It call also be thought of as a **filter**:

```python
age_filter = df['age'] > 30
df.loc[age_filter]
```

By passing the `age_filter` to `.loc[]` it will filter rows out that do not include an age over 30. 

![An intro image](/images/filtered_df.png)


### Comparison operators

Filtering dataframes can be done using all of the comparison operators

- `x == 100`
- `x > 2`, `y < x`
- `x != y` 
- `x.isin([...])`
- `x.between(a, b)`
- `x.isna()`

This operators are applied to columns of the data frame.

### Boolean operators

To chain several comparisons together, the boolean operators 

- `&` (AND)
- `~` (NOT)
- `|` (OR)

can be used:


```python
age_filter = (df['age'] > 30) & (df['age'] < 60)
df.loc[age_filter]
```

This filter sets an age range to filter. Keep in mind that multiple columns can also be selected if more complicated filtering is called for.

![An intro image](/images/complicated_filter.png)

## Exercises

Download the example dataset, read into empty notebook and experiment with different ways to filter the data.

{{% attachments title="Related files" pattern="filter_example" /%}}

Using the dataset above run the commands from the examples pertaining to this dataset to ensure you understand the syntax properly.

### Task 1

What will the following filter return? Why?
```python
age_filter = (df['age'] > 30) | (df['age'] < 60)
```
If the `&` represents **and** then what does ` | ` stand for?

### Task 2

What does `~` do? Try out the code below to help understand it. 
```python
age_filter = df['age'] > 30
df.loc[~age_filter]
```

### Task 3

Using the **between** syntax `df.loc[df[col].between(x, y)]` try and get the same result as this code returns:
```python
age_filter = (df['age'] > 30) & (df['age'] < 60)
df.loc[age_filter]
```

### Task 4

Experiment and get aquainted with the **condition** syntax coming up with your own ideas.  


## Project Challenges

{{% notice challenge "Analyzing Names" %}}

Using the **baby_names_all_years.csv** dataset created in [Methods, Functions, and Attributes]({{< ref "methods#project-challenges" >}}) solve the following tasks with `pandas`:

```python
# 1. Read in data:
df = pd.read_csv('../data/baby_names_all_years.csv')

# 2. Create a boolean mask for the name 'Martin'. It should just be a Series of True and False values.

# 3. Use this boolean mask to filter your original DataFrame and display a DataFrame which only has babies names 'Martin'. 

# 4. How many entries are the in the 'Martin' DataFrame? How many years are in the DataFrame? Why are there more entries of the name 'Martin' than years? In how many years does the name 'Martin' appear for both genders?

# 5. Filter the combined DataFrame for a DataFrame which only has names that have a frequency over 2000

# 6. Filter the combined DataFrame for a DataFrame which only has names that have a frequency over 2000 and for years starting with 2000. What is the most common name since 2000?

# 7. Filter the combined DataFrame for a DataFrame which only has names that have a frequency over 2000, for years starting with 2000 and for only females. What is the most common name given to females since 2000?

# 8. What is the percentage of names that have a frequency larger than 100?

```

{{% /notice %}}


{{% notice challenge "Filter the Data and Save" %}}

The combined dataset is very interesting because trends over time can be inspected. In order to analyze the trend of one name over time it would be beneficial to have a dataframe of particular names per gender overtime.

- Filter the combined dataset for the name **Emily**
- Filter that for only females
- Save the DataFrame for later analysis
- Filter and save other names of interest to analyze and investigate the popularity of celebrity names over time, e.g. try out Luke, Leia, Arielle, Tyrion, Barack

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}