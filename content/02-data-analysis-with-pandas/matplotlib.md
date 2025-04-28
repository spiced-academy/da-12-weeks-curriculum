---
title: "Matplotlib"
weight: 70
---

> Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible (*https://matplotlib.org/stable/index.html*). 

![paint](/images/paint.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@mikepetrucci?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Mike Petrucci</a> on <a href="https://unsplash.com/s/photos/painter?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

{{% notice warmup "The Data Viz Project" %}}

Go to the [Data Viz Project](https://datavizproject.com/) and pick your favorite diagram. 

- Present the characteristics of your chart to the others
- Show your favorite example

{{% /notice %}}

## Installation

Open a terminal and install Matplotlib:

```bash
pip install matplotlib
```

### Key Concepts

`matplotlib` is capable of producing static images of all common types of diagrams in print quality. It is the most widely used plotting library in the Python Data community. It also serves as the backbone for other plotting libraries, like `pandas` (yes, plotting is possible with `pandas` as will be shown later) and `seaborn`.

command  |  description
---|---|
`plt.plot(x, y)`         | create a line plot
`plt.scatter(x, y)`      |    create a scatter plot
`plt.bar(x, height, width)` | create a bar plot
`plt.hist(x, bins)` | create a histogram
`plt.axis((xmin, xmax, ymin, ymax))`      |   set the x/y boundaries
`plt.title()`      |    set the title
`plt.xlabel()`       |     set the label for the x-axis
`plt.ylabel()`       |     set the label for the y-axis
`plt.savefig(filename)`       |     save the plot
`plt.style.use('ggplot')` | set a global style sheet
`plt.legend()`     | place a legend
`plt.figure(figsize=(width, height))`  | change the size of the figure


## Getting started

### Import matplotlib

The `matplotlib.pyplot` module contains all important functions. It is common to alias the `pyplot` submodule as `plt`:

```python
from matplotlib import pyplot as plt
```

All functions can be accessed by typing `plt.<function-name>`.

### Set a style and figure size

A theme for all plots can be set in a notebook. Usually this is executed only once at the beginning after importing the library:

```python
plt.style.use('ggplot')
```

To get a list of all available themes run:

```python
print(plt.style.available)
```

To set the figure size (in inches) use: 

```python
plt.figure(figsize=(width, height))
```

at the beginning of the plot. By default, the dimensions are `(6.4, 4.8)`.


### Plot the data

```python
x_vals = range(1, 8)
y_vals = [12, 34, 23, 98, 38, 45, 12]
plt.plot(x_vals, y_vals, label='some random data')
plt.show() #You don't need to include this line in Jupyter Notebook
```

The `x` and `y` parameters passed to `matplotlib` should be an array-like object or a scalar. This can include python lists, a `pandas` Series, a `pandas` DataFrame column (which in fact is a `pandas` Series) and more. 

### Add elements to the figure

After creating the plot you can customize it using additional functions. Put all functions for a plot into the same cell of a Jupyter Notebook before `plt.show()`:

```python
...
plt.title('My Title')
plt.ylabel('y values')
plt.xlabel('x values')
plt.legend()
...
plt.show()
```

### Save the plot

To save the plot as an image on the hard drive you need to call `plt.savefig` at the very end:

```python
...
plt.savefig('./path/to/some-random-plot.png')
```

## Customizing the plotted data

The functions `plt.scatter`, `plt.hist`, `plt.bar` and `plt.plot` accept many input parameter that can be used to fine-tune the plotted data.

### Markers

Determine the shape of the plotted points. Try: `v`, `.`, `o` or `s`.

```python
plt.scatter(x_vals, y_vals, marker="v")
```

A complete list of possible markers can be found [**here**](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers).

### Colors

A single color can be provided: 

```python
plt.bar(x_vals, y_vals, color='tomato')
```

or a list of colors

```python
plt.bar(x_vals, y_vals, color=['tomato', 'steelblue'])
```

to change the color of the bars, points or lines. A list of possible named colors can be found [**here**](https://matplotlib.org/stable/gallery/color/named_colors.html).

### Size

Along with the size of the markers, the thickness of lines or the width of bars can also be changed:

- For barplots use the parameter `width`:

   ```python
   plt.bar(x_vals, y_vals, width=0.1)
   ```   

- For scatterplots use `s`:

   ```python
   plt.scatter(x_vals, y_vals, s=100)
   ```

- For lineplots use `linewidth`:

   ```python
   plt.plot(x_vals, y_vals, linewidth=5)
   ```

### Legend

To draw a legend use the function `plt.legend()` after creating the plot. For the legend labels use the `label` parameter of the plotting functions:

```python
plt.bar(x_vals, y_vals, label='some random data')
plt.legend()
```

{{% notice info "Plotting with Pandas" %}}

Although `matplotlib` is the foundation for plotting in python there are other libraries such as `seaborn` and `plotly` that shall be covered later in the course. These libraries are built on top of the `matplotlib` foundation. 

Along with these and other plotting specific libraries `pandas` also has integrated `matplotlib` plotting abilities into it's methods. 

Take for example a `pandas` DataFrame filtered from the baby names combined dataset for the name **Mary** and the **F** gender called `df_mary`. The `.plot()` method can be called on the `df_mary` DataFrame object with the columns of interest to plot.  

```python
df_mary.plot(x='year', y='frequency')
```

The default plot is a line plot but that can be altered using the `kind` parameter. Many of the controls you have with `matplotlib` can be used to manipulate and alter the plot using the plot method's parameters. 


{{% /notice %}}

## Exercises

### Task 1: Debugging

Find all bugs:

```python
plt.style.use('colorful')
months = [
   'Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
mean_temp_ber =  [0.5, 1, 5, 8.5, 14, 17, 19, 19, 15, 9.5, 4.5, 2]
mean_temp_col = [2, 3, 6.5, 9.5, 13.5, 16.5, 18.5, 18.5, 15, 11, 6.5, 3]

plt.plot(months, mean_temp_ber, linewidth=4, alpha=0.8, label='Berlin')
plt.plot(months, mean_temp_col, lineswidth=4, alpha=0.8)
plt.legend()
plt.ylabel('Temperature')
plt.title('Monthly average temperatures', loc='left')
plt.savefig('temperature.jpgs')
```

![](/images/temperature.png)

### Task 2: Plot a quadratic function

- create a list of x values ranging from `-10` to `10`
- create an empty list for the `y` values
- loop over the values of `x` and calculate $y=x^2$ 
- append each value of `y` to the list
- make a lineplot of the data
- add a legend, title and axis labels to the plot


### Task 3: Plot your typical week

- create a list of weekdays:
   ```python
   x = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
   ```
- For each day of the week write down the number of times you called someone and use those figures to make a list called `y` 
- Visualize the data with a bar plot
- Change the color of the bars, add a tile
- Save the plot as a `.png` file

## Project Challenges

{{% notice challenge "Visualize the Names Dataset" %}}

Create a plot of the summed up frequency (total births) per year from 1880 to 2020.

#### Step 1 - Create the data

1. Make a empty dictionary that maps the column names `year` and `total_births` to empty lists:
```python
births_dict = {'year':[], 'total_births':[]}
```

2. Loop over the years from 1880 to 2020
3. Use your `parse_dataset(year)` function to parse each year
4. Use the `pandas.sum()` method to calculate the sum of the frequencies (births)
5. Append the result to the dictionary using `births_dict['total_births'].append()`
6. Also append the year to `births_dict['year']`
7. Create a `yearly_births` DataFrame by passing `births_dict`to `pd.DataFrame()`

This should result in a DataFrame that has the `year` as one column and the `total_births`in that year in another column.

![yearly_births](/images/yearly_births.png)

#### Step 2 - Plotting

- use `pandas` to make a quick plot of your results
- use `matplotlib` to make a more detailed plot but adding a legend, title and and axis labels  
- try other plot types 

{{% /notice %}}


{{% notice challenge "Visualize the Distribution of Names" %}}

- Read in a single dataset for one year using the `parse_dataset()` function and create a histogram of the frequency column.
- The distribution is highly skewed! Include the following `log=True` in `plt.hist` to improve the visualization!
- Play around with the number of bins `bins` to make the visualization even clearer.
- Do the same for another year and compare the two distributions with each other.
- Add labels and a title

{{% /notice %}}

{{% notice challenge "Number of unique names over time" %}}

- How has the number of unique names given to newborn children varied over time?
- For each year from 1880 til 2020
   - read in the data using the `parse_dataset()` function
   - use `nunique()` to count the unique names for each year
   - keep track of the year and the count in a dictionary
   - convert dictionary to `pandas`DataFrame as was done in the first milestone for this lesson
- Visualize the data, use the years on the x-axis and the counts on the y-axis.


{{% /notice %}}


{{% notice challenge "Track a name over time" %}}

- Using any of the single name over time dataframes created in [Filtering DataFrames]({{< ref "filtering-dataframes#project-challenges" >}})
- Create a line plot with the years and the (relative) frequencies of a specific name

{{% /notice %}}


{{% notice challenge "Analyze the length of names" %}}

- Plot the distribution of the length of each name for a given year
- Does the distribution change over time?
- Plot the average length of names over time!

{{% /notice %}}

## Reading


{{% notice reading "Reading" %}}

[Website and documentation for Matplotlib](https://matplotlib.org/)

{{% /notice %}}

<br>

{{% notice "Malte Bonart, Spiced Academy" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}