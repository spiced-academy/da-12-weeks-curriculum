---
title: "Data Wrangling"
weight: 90
---

![some intro image](/images/mud.jpg)
{{< credits >}}
Photo by Quino Al on Unsplash
{{< /credits >}}

{{% notice warmup "Data Wrangling" %}}
 
Data wrangling is part of the early stages of the data analytics process. It involves transforming and mapping data from one format into another. The aim is to make data more accessible for things like business analytics. The data wrangling process can involve a variety of tasks. 

- Research what these tasks are.
- Discuss which of these task have been covered in the course far.  

{{% /notice %}}

## Key Concepts

The goal of **Data Wrangling** is to have the data in a format which will lend ease to transformation, analysis, and visualization. 

Data in pandas and tabular data in general can exist in two forms: long and wide format.

![some intro image](/images/long_vs_wide.png)

In the long format, there is a single value column and another column that contains the variable name for each of the values. This format is great for plotting with seaborn.

In the wide format, each variable has its own column. This format is great for calculating descriptive statistics.

The conversion between long and wide format helps you to bring data into the right format for merging, concatenation or plotting.

Before applying the transformations, make sure that your data is Tidy Data. Once your data is tidy, transformations from one format to the other will become simple.


concept   |  description
---          |---
`df.melt()`       |     converts a df from wide to long format
`df.pivot()`    |      converts a df from long to wide format, without aggregation
`df.pivot_table()`    |      converts a df from long to wide format, with aggregation
`df.transpose()`      |  swaps rows and columns


#### `df.melt`
`Melt` is used to transform the data from wide to long format.

- **id_vars**: Column(s) to use as identifier variables
- **value_vars**: Column(s) to unpivot. If not specified, uses all columns that are not set as id_vars.
- **var_name**: Name to use for the ‘variable’ column.
- **value_name**: Name to use for the ‘value’ column.

#### `df.pivot`
`Pivot` is the transformation from long to wide format. There are no aggregations here - the data is just reorganized.

- **index**: Column to use to make new frame’s index.
- **columns**: Column to use to make new frame’s columns.
- **values**: Column(s) to use for populating new frame’s values.

#### `df.pivot_table`
`Pivot table` is a version of pivot but in this version the data will be aggregated.

- **values**: Column to aggregate, optional.
- **index**: Column, Grouper, array, or list of the previous.  
If an array is passed, it must be the same length as the data.
- **columns**: Column, Grouper, array, or list of the previous.  
If an array is passed, it must be the same length as the data.
- **aggfunc**: function, list of functions, dict, default `numpy.mean`  
If list of functions passed, the resulting pivot table will have hierarchical columns whose top level are the function names (inferred from the function objects themselves) If dict is passed, the key is column to aggregate and value is function or list of functions.


### Exercise - `df.melt`, `df.pivot`, and `df.pivot_table`

Practice melting and pivoting techniques using penguins dataset.

Remember that you can read this dataset directly from seaborn as well as a few other exemplary datasets:
```python
penguins = sns.load_dataset("penguins")
```

#### Task 1
Prepare a boxplot showing average bill measurements (both bill length and bill depth on the same graph) dependent on the island where they live. 
Tip: Melt the dataset first.

#### Task 2
Come back to the previous form of the dataset using the pivot function.

#### Task 3 
Calculate descriptive statistics (e.g. mean values of the measurements) for penguins defined by island and sex.
Note: instead of using `.describe` try using `pivot_table` on a melted dataset.

### Bonus Exercise
Note: This exercise is not needed for a weekly project but provides with additional practise if wanted. 

The original data directly from gapminder comes in wide format:

{{% attachments title="Related files" pattern="gapminder_total_fertility" /%}}

Follow the following steps to wrangle the data into the format that was needed to accomplish the week 3 project. 

#### Task 1
In the original gapminder dataset the columns are the country names and years.
```python
fert = pd.read_csv('data/gapminder_total_fertility.csv')
fert.head()
```

#### Task 2
`melt` the table into a form that resembles the data received in week 3.
```python
fert_melted = fert.melt(id_vars= 'country', 
                var_name = 'year', 
                value_name= 'fertility_rate')
fert_melted.head()
```
#### Task 3
`pivot` the table back to its original form.
```python
fert_melted.pivot(values='fertility_rate', 
                columns='year', 
                index='country')
```
#### Task 4
Create an aggreate table with the average `fertility_rate` of each country.
```python
fert_melted.pivot_table(values='fertility_rate', 
                      columns='country', 
                      aggfunc='mean')
```

## Project Challenges

{{% notice challenge "Optional - Data Wrangling" %}}

At this point you should have one dataframe with gapminder data storing all the features (where every metric is a single column). 
Imagine that you want to create a line chart with seaborn showing the development of fertility rate and life expectancy in time. Both of the lines should be visible on one graph and the legend should say which line is talking about which metric.

Tip: before you start visualizing, consider melting your gapminder data to have a column representing the name of the metric and a column for the value for this metric (keep the structure of the countries, and years)

Do you have some other ideas where you could apply melting or pivoting on the gapminder dataset?

{{% /notice %}}


## Reading

{{% notice reading "Reading" %}}

- [Long vs Wide Pandas docs](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html)
- [What is tidy data?](https://towardsdatascience.com/what-is-tidy-data-d58bb9ad2458)

{{% /notice %}}

<br>

{{% notice copyright "Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}