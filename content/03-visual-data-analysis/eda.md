---
title: "EDA - Exploratory Data Analysis"
weight: 10
---

![a panda](/images/eda.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@sadswim?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">ian dooley</a> on <a href="https://unsplash.com/s/photos/explore?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

{{% notice warmup "Get to know this week's data" %}}

   1.  Download the Jupyter notebook
   2.  Download the files
   3.  Save the notebook in the `notebook`folder and the `.csv` files in the `data` folder
   4.  Open the notebook in Jupyter
   5.  Complete and Execute the commands

   {{% attachments title="Related files" pattern="pandas_eda_warmer|population|continents" /%}}

{{% /notice %}}

## Key Concepts

According to Wikipedia, EDA “is an approach to analyzing datasets to summarize their main characteristics, often with visual methods”. In other words, it is about knowing the data, gaining a certain amount of familiarity with the data, before one starts to extract insights from it.

### General Outline of EDA

- Preview data
- Check total number of entries and column types
- Check for null values
- Check duplicate entries
- Plot distribution of data (numeric or categorical)

A high level introduction of these concepts are here in this lesson. However many of these will be looked at in more depth throughout the course and some of the basics of EDA were performed in week 2. 

Here are some `pandas` commands that are used during EDA:

command                       | description
---                           | ---
`.dtypes`                     | returns the dtypes in the DataFrame
`.astype()`             |   cast a pandas object to a specified dtype
`.info()`         | returns a concise summary of a DataFrame
`.isnull()`      | detects missing values for an array-like object
`.duplicated()`          | returns boolean Series denoting duplicate rows
`.drop_duplicates()`                    | returns DataFrame with duplicate rows removed
`.value_counts()`       | returns a Series containing counts of unique rows in the DataFrame

#### **Preview data**

After reading in the data the first thing to do to get a feel for the data is to look at the size and shape of the dataframe. Then looking at the first few columns gives a sense of what is being dealt with. The common `pandas` commands used here would be `.shape`, `.size`, `head()` and more. 

### **Check entries and datatypes**

When exploring the data the datatypes can be of valuable help. If there is a column in which statistical analysis should be made but the column is `string` known in `pandas` as an `object` then the column datatype needs to be converted to `integer`. Only then is `pandas` able to perform mathematical methods on the desired data.

There is more than one way to check the datatypes. One that is straightforward is using the `.dtypes` attribute:

```python
df.dtypes
```

This returns a Series with the data type of each column. The result’s index is the original DataFrame’s columns. Columns with mixed types are stored with the object dtype. 

![dtypes](/images/dtypes.png)

Another option would be the `.info()` method. This will not only return the column datatypes but also more information such as the amount of **non-null** data in each column. 

If there is a column with the incorrect datatype then the `.astype()` method can be used to change the datatype. For example is there is a column year that is currently a `string` known in `pandas` as an `object`, `.astype()` can be used to transform the column and it's content into a column of `integers`.

```python
df['year'] = df['year'].astype(int)
```

The new datatype is passed as an argument in the `.astype()` method. In this case `int` is passed to cast the column and it's contents as `integers`.

**Note:** Keep in mind that `.astype()` is not an **inplace** method and therefore the column must be overwritten in order to complete the transformation.

###  Check for null values

What is a `null` or `NaN` value? It is a placeholder for missing data. It just means that there is no data in that cell. When getting an understanding of the data, knowing how many values are missing is of high importance. 

It will not only help getting deeper knowledge of the data but will also lead to conclusions on what to do with the missing data. What to do about missing data is a challenge that will be dealt with in future lessons. For now recognizing what is missing will be focused on.

The `.isnull()` method will return a DataFrame or Series as a boolean mask. In this case the `True` values are the missing values:

```python
df.isnull()
```

![isnull](/images/isnull.png)

What is nice about boolean mask is not only can they be used to filter DataFrames but they can also be summed up where `False` is 0 and `True` is 1. So if the `.sum()` method is added to the above command the total missing values will be returned. 

```python
df.isnull().sum()
```

![isnullsum](/images/isnullsum.png)

As can be seen above the `Total population` and `year` column have no missing values, however the `population` column has 2099 missing values. 

### Check for duplicate entries

Duplicate entries refers to rows that have the same data in every column and are then in many cases irrelevant. To check for such data the `.duplicated()` method can be used. It also returns a boolean mask on which `.sum()` can be used to find out the amount of *duplicated*  observations.

```python
df.duplicated().sum()
``` 

If the duplicated data is redundant it can be removed using the `.drop_duplicates()` method. Keep in mind this is not a **inplace** method. However it does have the argument `inplace=` which can be set to `True` in order to perform the method on the object inplace. 

```python
df.drop_duplicates(inplace=True)
```

### Plot distribution of data

Looking at the distribution of the data can reveal many statistical insights. Trend or seasonality may become apparent and other statistics such as max and min can be visualized. Some numeric data can be extracted from categorical columns such as the count of each category. 

In order to count the total occurences of a category or even the total occurences of a `integer` or `float` the method `.value_counts()` can be used. 

```python
df['population'].value_counts()
```

![value counts](/images/value_counts.png)

The results show that the population of 905 shows up in the `population` column 9 times. The population of 63 shows up 7 times! Is that 7 different countries with the same population or a country with zero population growth?

**Bonus Task** 

Use `pandas` to find out which country or countries have a population of 63. Where is it located? Have you ever heard of it?




## Project Challenges

{{% notice challenge "Solve with One-Liners" %}}

Using the **large_countries_2015.csv** dataset solve the following tasks with pandas one-liners:

{{% attachments title="Related files" pattern="large_countries_2015" /%}}

```python
# 1. read in data:
df = pd.read_csv('../data/large_countries_2015.csv', index_col=0)

# 2. check dataframe for null values

# 3. check datatypes

# 4. check how many countries from each continent are in the dataset

# 5. display a dataframe which only has countries located in Asia

# 6. display a dataframe which only has countries that have a population over 250,000,000

# 7. display a dataframe which only has countries that have a population of no less than 100,000 and no more than 250,000,000

# 8. display a dataframe which only has countries located in Asia that have a fertilitiy rate of less than 1.8

```
{{% /notice %}}

{{% notice challenge "Countries per Continent distribution" %}}

Using **pandas** `.value_counts()` and `.plot()` create a bar plot from the `continents.csv` that shows the distribution of countries per continent. 

*Hint*: remember **pandas** methods can be stacked against each other. For example:

```python
df.isnull().sum()
```

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}