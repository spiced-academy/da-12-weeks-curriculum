---
title: "Data Cleansing and Missing Data"
weight: 20
---

![An intro image](/images/clean.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@thecreative_exchange?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">The Creative Exchange</a> on <a href="https://unsplash.com/s/photos/cleaning?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

{{% notice warmup "Data Prep Still Dominates Data Scientists’ Time" %}}

Read through the article 
[Data Prep Still Dominates Data Scientists’ Time, Survey Finds](https://www.datanami.com/2020/07/06/data-prep-still-dominates-data-scientists-time-survey-finds/)!

Collect your main takeaways!

{{% /notice %}}


## Key Concepts

Data is often very disorganized. Messy data can hinder data exploration and other steps in your analysis. Data cleansing is about identifying incorrect, incomplete, inaccurate, or irrelevant data, fixing the problems, and making sure that all such issues will be fixed automatically in the future.

### Pandas topic related commands

command                          | description
---                              | ---
`df.info()`                      | prints concise summary of dataframe
`df.rename()`                    | alter row or column axes labels
`df.dropna()`                    | removes rows or columns that contain missing values
`df.set_index()`                 | assign a column to be the row index of the table
`df.reset_index()`               | replace the current row index with a default
`df["col_name"].isna()`          | identify missing values in a column
`df["col_name"].replace()`       | replace values in a Series
`df["col_name"].fillna()`        | fill NaN values using the specified method

## Data Cleansing

### Renaming the column index

Looking at the gapminder data, what could be **cleaned** in this case?

![An intro image](/images/pop.png)

The first column has the name `Total population`. This is the name of our dataset and not the value of column. The column should be called `country`, which would make much more sense. How can this be changed? 

```python
import pandas as pd

pop = pd.read_csv('population.csv')
rename_dict = {'Total population':'country'}
pop.rename(columns=rename_dict, inplace=True)
```

After reading in the data we define a python dictionary that maps the old name to the new name. This mapping dictionary is passed to the parameter `columns` since a column is being renamed. The `.rename()` method also has parameters for a general `mapper` or the `index`. Notice that this is also a case where `inplace=True` is required for the result to be made persistant. More information on this function can be found here [pandas.DataFrame.rename()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html) 


## Missing Data

Missing data can invalidate the data analysis, reports, dashboards, etc that are being created. Thus it is esstential to deal with in some fashion before the actual analysis begins. 

In `pandas` missing data is represented by the values `NA` or `NaN`. As data comes in many shapes and forms, pandas aims to be flexible with regard to handling missing data. 

While NaN is the default missing value marker for reasons of computational speed and convenience, we need to be able to easily detect this value with data of different types: floating point, integer, boolean, and general object. In many cases, however, the Python None will arise and we wish to also consider that “missing” or “not available” or “NA”.

Common missing values representations:

- NaN (the primary one and the one used by pandas)
- Empty string “”
- Other strings (e.g. “unknown”, “uncategorized”, “?”, etc.)
- Negative values (i.e. -1, huge negatives like -999)

### Where does missing data come from?

-  Failure of measurement
    - No information (e.g. lack of observation)
    - Technical issue (e.g. battery in a smart watch died)

- Programming error

**Note:** Some missing data can still be representaional of an event or data point:
- Purchase data with NaNs in coupon discount column - it will mean that a customer didn't use a coupon code
- Recipe data with NaN for amount of the ingredient - it will mean we don't this ingredient at all


### Detecting missing data 

We can filter for rows that contain missing data with the functon `isna()`:

```python
row_filter = df["age"].isna()
df.loc[row_filter]
```

## Dealing with missing data

If upon inspecting data, missing values are evident how to handle them becomes of the utmost importance. This will always depend upon the situation. Above all the introduction of any bias into the dataset must be avoided. Therefore one option would be to leave it as is, yet that may also hinder the use of some valuable data analysis tools. Here are some options as to how to deal with missing data:

-  drop the observations with missing values
-  insert mode/mean/median depending on data type
-  insert the next or last known value using `pandas.DataFrame.fillna()`
-  insert the mean/median dependent on another column 
-  for time series data: interpolate using `pandas.Series.interpolate`

### Examples

![An intro image](/images/missing_data.png)

#### Dropping rows

If the following command is used on the above dataset only one observation will be left. This is because the `how` parameter is set to **any**. :

```python
import pandas as pd

df = pd.read_csv('../data/example_missing.csv')
df.dropna(how='any', inplace=True)
```

If only observations with a particular variable missing should be drop that can be done with the collowing command:

```python
df.dropna(subset=['age'], inplace=True)
```

This will drop any observations that have a `NaN` in the `age`column. The `subset` parameter can be passed multiple columns in the form of a list. 

#### Dropping Columns

If a column has such a high percentage of missing values it should be dropped completely the following command from the lesson **Selecting Rows and Columns** can by used:

```python
df.drop(columns=['age'], inplace=True)
```

#### Imputing Data

The act of imputing or imputation is the process of replacing missing data with substituted values.

The code below will impute the number `0` anywhere in the data set above that is missing data.

```python

df['age'].fillna(0, inplace=True)
```

Another option is to impute the average of a column:
```python
df['age'].fillna(df['age'].mean(), inplace=True)
```

Other statistics commonly used in imputation are **mode** and **median**. These statistical methods will be discussed in more detail in the [Descriptive Statistics]({{< ref "descriptive-statistics" >}}) lesson. Just keep in mind that **mean** and **median** are used for numeric data and **mode** most often for **categorical** data. 

Although these methods can make the dataset whole they also have drawbacks which include:

- reduction of variance in the data
- doesn’t reflect any uncertainty
- introduction of  imbalance / bias 


## Exercises

{{% attachments title="Related files" pattern="missing_example" /%}}

Practice the pandas methods in an empty notebook with the **missing_example** data:

### Task 1

What information does `df.info()` reveal about the data?

### Task 2

Try the examples above and look deeper into the pandas methods used. 

### Task 3

Impute the missing data with something other than the mean. Try the mode or median or something else. 


## Project Challenges

{{% notice challenge "Clean Gapminder" %}}


1. Rename columns: use the method from the example above to properly name any columns that seem 
mislabeled in the `population` dataset. The `population` dataset was given in the [EDA]({{< ref "eda" >}}) lesson warmer

2. Missing data: first check and see which and how much data is missing in the `population` dataset

3. Remove missing data: drop all observations with missing data

4. Filter for relevant data: filter the dataset that it begins with the year 1950

5. Make data persistant: save the dataset as a `.csv` file in your `data` folder as they will be used for the week's project

6. Repeat for the the **life_expectancy**, and **fertility_rate** datasets which are available below

**Hint**: one of the files is not a `.csv` and must be read in using a pandas function other than `read_csv()`

{{% attachments title="Related files" pattern="fertility_rate|life_expectancy" /%}}

{{% /notice %}}

{{% notice reading "BBI Bonus But Important: Tidy Data" %}}

This section is an excerpt of *Wickham, H. (2014). Tidy data. The Journal of Statistical Software, 59, http://www.jstatsoft.org/v59/i10/*

It is often said that 80% of data analysis is spent on the cleaning and 
preparing data. [...] The principles of tidy data provide a standard way to 
organise data values within a dataset. A standard makes initial data cleaning 
easier because you don’t need to start from scratch and reinvent the wheel every time. [...]

> Happy families are all alike; every unhappy family is unhappy in its own way — Leo Tolstoy

Like families, tidy datasets are all alike but every messy dataset is messy in 
its own way. Tidy datasets provide a standardized way to link the structure of a dataset (its physical layout) with its semantics 
(its meaning). [...] A dataset is messy or tidy depending on how rows, columns and tables are matched up with observations, variables and types. In tidy data:

- Every column is a variable.
- Every row is an observation.
- Every cell is a single value.


{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}

