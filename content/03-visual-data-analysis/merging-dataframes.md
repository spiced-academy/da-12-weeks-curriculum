---
title: "Merging Dataframes"
weight: 40
---
  
![An intro image](/images/merge.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@pinewatt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">pine  watt</a> on <a href="https://unsplash.com/s/photos/merge?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

{{% notice warmup "Glueing tables together" %}}

Take a look at this two DataFrames:

```python
df1 = pd.DataFrame(
   {'day':['Mo', 'Tu', 'We'], 'sunny':[True, False, False]}
)

df2 = pd.DataFrame(
   {'day':['Tu', 'We', 'Th'], 'temp': [12, 14, 9]}
)
```

1. Draw the two tables on a piece of paper
2. Think of different ways you could combine the two tables into a single table
3. Draw the resulting table and present it!

{{% /notice %}}

## Key Concepts

A *join* or *merge* is used to combine two or more tables *horizontally*. Rows 
are glued together based on one or several common column(s) between them.

We can join tables in different ways:

![](/images/joins.png)


command                          | description
---                              | ---
`df1.merge(df2)`                 | joins two dataframes horizontally, based on specific indexes/columns
`pd.concat([df1, df2])`      | joins two or more datarames vertically together


## Using `df.merge()`

- You always merge two dataframes. 
- With the `on` parameter, you specify the columns (or index) that is to be used for matching rows
- With the `how` parameter, you specify the type of join

- An *inner* join will discard rows that don't have a common key in both tables
- A *left* join will keep all the rows from the first table 
- An *outer* join will keep all rows from both tables

![](/images/merge_in_o.png)

With left and right joins you can decide which of the two DataFrames may result in missing values.

![](/images/merge_leftright.png)

{{% notice info "indicator parameter" %}}

When first getting used to joining dataframes the `indicator` parameter from `merge()` can be a big help. Adding `indicator=True` to `merge()` will add a column that denotes from which dataframe the data stems from. Below are some examples using the same **Spice** datasets from the previous examples. 

As can be seen below when using an `outer` join all of the data is combined into one dataframe reagardless of whether there is any overlap between the dataframes or not. Using `indicator=True` craeated a *new*  column named `_merge` that denotes the dataframe of origin. 

![](/images/outer_true.png)

Using the `indicator` parameter on an `inner` join we can see that only the data that has an overlap in both dataframes is combined. If the `how` parameter is completely left out this would also be the result. This is due to the fact that `how = 'inner'` is the default setting. 

![](/images/inner_true.png)

Below are examples of the a **left** and **right** join with the `indicator` parameter set to `True`. 

![](/images/left_true.png)

![](/images/right_true.png)


One last tip is that instead of passing `True` a string can be passed such as `'df_source'`. This will then be set as the column heading instead of the default `_merge`. 

![](/images/string_true.png)


{{% /notice %}}

## Using `pd.concat()`

On a high level `pd.concat` can be compared to what `.append()` is for lists. It adds data to the end of the rows or columns. 

Main points behind `pd.concat`:  

- can combine multiple dataframes
- default is outer join
- dataframes to be combined are passed in a list
- dataframes can be added along either rows or columns
- when concatenating along rows the original index will be kept unless `ignore_index=True`

Example of simple concat where data is added along the rows and the original index is kept intact:

```python
pd.concat([df1, df2])
```

![](/images/concat1.png)

To perform the same concatenation but have a consistent and serial index:

```python
pd.concat([df1, df2], ignore_index=True) 
```

![](/images/concat_ignore_index2.png)

To combine the data along the column index:

```python
df3 = pd.concat([df1, df2], axis=1) 
```

![](/images/concat_axis1.png)

As can be seen here two columns have the same name. This could cause confusion and would call for joining the data in another matter or renaming a column. 


What happens when the following command is run on this dataframe:

```python
df3['spice']
```


## Project Challenges

{{% notice challenge "Challenge: Combining DataFrames" %}}

1. Open empty notebook and read in life_expectancy and continents datasets. Both of these datasets are available from earlier lessons. Life expectancy dataset should be a cleaned version of the original dataset (the outcome of Data Cleansing project milestones).
 
2. Merge the two dataframes into one using `pandas.DataFrame.merge()`
   
   **Link to documentation:** [pandas.DataFrame.merge()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge)

   **Note:** Keep in mind this will render the merged dataframe in your notebook. However in order to execute commands on the merged dataframe you must put it in a variable i.e. `df_merged = df1.merge(df2)`

3. Repeat steps 1 and 2 with population and total_fertility (the cleaned versions as well) until you have a single dataframe that contains the information from all four original dataframes

**Tip:** the column on which the dataframes are merged *on* must have the same data type in both dataframes. If you have numbers in both but in one dataframe they are strings and the other integers the dataframes will not merge properly. Use `.astype()` to remedy this.  

4. Write new dataframe to hard drive as `gapminder_total.csv` in this week's `data` folder for use in the upcoming lessons. 

{{% /notice %}}

## Reading

{{% notice reading "Links" %}}

[Here](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) is a tutorial from pandas about the different join options

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}

