---
title: "Aggregation and Groupby"
weight: 50
---

![some intro image](/images/colgroups.jpg)
{{< credits >}}
Photo by Ricardo Gomez Angel on Unsplash
{{< /credits >}}

{{% notice warmup "Aggregate Functions" %}}
1. In an empty notebook,open a dataset about pengiuns which is 'built-in' to the `seaborn`library using the following commands:
    ```python
    import seaborn as sns

    df = sns.load_dataset('penguins')
    df.head()
    ```

2. Calculate the average bill length in the dataset
3. Find out which gender of pengiuns occurs the most in the dataset

{{% /notice %}}

## Aggregation

Data aggregation is a process in which data is gathered and represented in a summary form, for purposes including statistical analysis.

Some aggregation methods were encountered in the [descriptive statistics]({{< ref "descriptive-statistics" >}}) lesson. However in this lesson they will be applied to a `groupby` object in order to aggregate by groups.  

command  |  description
---|---|
`.sum()`       |     calculate the sum of each column(s)
`.mean()`      |     calculates arithmetic mean of a column(s)
`.median()`      |      	calculates median of a column(s)
`.var()`      |     calculates variance of a column(s)
`.std()`  |  calculates standard deviation of a column(s)
`.value_counts()` |  returns a Series containing counts of unique values in each column
`.corr()`       |      	calculates correlation between two columns

Applying any of these methods to a dataframe will return a summarization that gives insight into the data. A common example would be the mean of a column:

```python
df['column_name'].mean()
```

In cases where more than one aggregate result is of interest `.agg()` can be of use. This pandas method allows multiple aggregation methods to be executed on data:

```python
df['column_name'].agg(['mean', 'median', 'std'])
```

There are other ways to apply the `.agg()` method which can be found [_here_](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html) in the documentation


## Group by: split-apply-combine

By “group by” we are referring to a process involving one or more of the following steps:

- **Split** the data into groups based on some criteria.

- **Apply** a function to each group independently.

- **Combining** the results into a data structure.

![some intro image](/images/aggregate_steps.png)
{{< credits >}}
Flowchart by Samuel McGuire
{{< /credits >}}

## Key Groupby Concepts

Using the commands below will group the data in different ways and access the groups. This would be considered the **split** step shown above. 

command  |  description
---|---|
`df.groupby('column_name')`       |     groups data according to categorgies in column
`df.groupby(['column_1', column_2])`    |     groups data according to categorgies in multiply columns
`.groups`      |     attribute showing the group names and observations in each group
`.get_group('column_name')`    |     retrieves all data from the specified group in a dataframe

After defining a dataframe the data can be grouped dependent on a categorical column. 

For example in the flowchart above the data is grouped by the `column_name` column. That can be achieved with the following code:
```python
df.groupby('column_name')
```
Using this code will only return a `groupby` object. There are various options at this point. One would be save the object in a variable as is done in the following code:
```python
df_group = df.groupby('column_name')
``` 
Now aggregate functions can be applied to the groups and then combined into an aggregated dataframe for analysis.

{{% notice info "Transform method" %}}

Grouping the data with `groupby()` will always result in a table that explains the results of the various statistical methods on each group. The original format and detail of the table is lost. All records have been aggregated to the number of gourps specified. 

What if the analyst wished to keep the data in the same format but add these insights to the original table? Then `transform()` would be used instead. 


![some intro image](/images/transform_before.png)

```python
penguins['species_avg_flipper_length'] = penguins.groupby('species')['flipper_length_mm'].transform('mean')
```

**Note:** The above command is all one line of code. 

Where useing `groupby()` on its own results in the number of rows being equal to the number of groups, this method keeps all the original rows and introduces the new information as an additional row. The result is this example is the orginal penguins dataset with one new row of information which has the average flipper length for the species that this oberseved penguin belongs to.  

![some intro image](/images/transform_after.png)

For more information on [tranform](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transform.html).

{{% /notice %}}

#### Additional methods that can be applied to the groupby object: 

command  |  description
---|---|
`.first()`       |     returns the first value for each group
`.min()`       |     calculates the minimum a column(s)
`.max()`       |     calculates the maximum a column(s)
`.nth()`       |      	returns the nth value for each group

##### Examples

```python
df.groupby('column_name').sum()
```
Or on the variable that has the saved object:
```python
df_group.sum()
``` 
**Note:**  include NA in group keys or not by using dropna parameter, the default setting is True.
```python
df.groupby(by="column_name", dropna=False).sum()
```

### Grouping by multiply columns

When looking for a higher granularity (more detailed groups), grouping by multiple columns can be done. In this case the columns of interest are passed as a list. Using more columns in turn will divide the data into more (detailed) groups. 

The aggregate function is then to be applied to these more detailed groups. In the example below the `mean` will be applied to groups where `column_name`and `another_column_name` variables names are uniquely matched. 

```python
df.groupby(['column_name', 'another_column_name']).mean()
```
If we would like to see it as a dataframe, we can pass the column names to display. 

```python
df[['col1', 'col2','col3', 'col4', 'col5','col6']].groupby(['col1', 'col2']).mean()
```

![some intro image](/images/groupby_multiple.jpg)

## Project Challenges

{{% notice challenge "Solve aggregation and groupby One-Liners" %}}

Using the **gapminder_total** dataset solve the following tasks with pandas one-liners:

```python
# 1. Read in data:
df = pd.read_csv('../data/gapminder_total.csv')

# 2. What is the median population in the data set?

# 3. How often does each continent appear in the data set?

# 4. Which continent has the lowest average fertility rate overall?

# 5. What was the average life expectancy in Europe in 2015? 
# Hint: first filter for 2015 then apply groupby.

# 6. How many countries does each continent have in the dataset?
# Hint: filter for one year and count

# 7. What is the average population of a European country in 1976 compare to 2015?
# Hint: once again filter for the year in question and do each year separately to compare

# BONUS

# 8. What is the highest population a continent ever had?
# Hint: group by multiple columns

# 9. Which continent had that population and in which year?
# Hint: group by multiple columns and filter for the result from #6

# 10. Plot a bar plot comparison of life_expectancy, fertility, population average per continent
# Hint: for a quick and dirty graph use Pandas ploting ability
# Hint: use log=True to make the visual more friendly to the eyes

```

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}