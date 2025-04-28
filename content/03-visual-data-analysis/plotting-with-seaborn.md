---
title: "Plotting with Seaborn"
weight: 70
---

> Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. *(https://seaborn.pydata.org/)*


![](/images/seaborn_logo.svg)


{{% notice warmup "Explanatory Plots" %}}

##### Discuss the following questions:

  1.  Does the average person process numbers or pictures better?
  2.  What makes a graphic memoriable?
  3.  How does this relate to data storytelling?

{{% /notice %}}


## Key Concepts

Although `matplotlib` is the backbone to plotting in python, there are other libraries
that make our lifes easier by simplifying the creation of charts with matplotlib.

In `seaborn` you map *columns of a Data Frame* to features of the plot (e.g. the x values, 
the color or size of the points). `matplotlib` does not use any Data Frames. Here, 
we explicitly assign lists of values to plotting parameters. 

Each type of plot has its own function:

command  |  description | use case |
---|---|---|
`sns.scatterplot()`       |     creates a single scatter plot  | relationship of two variables and their class
`sns.lineplot()`      |     line plot of each column  | relationship of two variables
`sns.barplot()`      |     one bar for each column  | variable by category 
`sns.histplot()`       |     draws a histogram for each column  | groups defined by continuous variables   
`sns.boxplot()`       |     draws a boxplot for each column method  |  gives different insight into the distribution of the dataset
`sns.heatmap()`       |     plot rectangular data as a color-encoded matrix  |  can be used to get a visualization of missing values or comparison of values in the dataset

## Example

```python
import seaborn as sns

tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="time")
```

produces

![](/images/tips_hue.png)

Some additional parameters you can use for the `scatterplot` function:

parameter    |  description
---          |---|
`size`       |     grouping variable that will produce points with different sizes
`palette`    |     pass different color palettes for use
`style`      |     grouping variable that will produce points with different markers
`markers`    |     how to draw the markers for different levels of the style variable
`alpha`      |     Proportional opacity of the points
`hue`        |     Color the points according to the category they belong to in that column




## Seaborn Plotting Functions

![](/images/seaborn_plots.png)
{{% credits %}}
 taken from [https://seaborn.pydata.org/tutorial/function_overview.html](https://seaborn.pydata.org/tutorial/function_overview.html) 
{{% /credits %}}


## Advanced matplotlib commands

Under the hood, a plot produced with seaborn is still based on `matplotlib`. After 
calling one of the high level plotting funtions you usually want to change parts 
of the plots in more detail.

![anatomy of a matplotlib figure](/images/anatomy_mpl_figure.webp)
{{% credits %}}
 taken from [https://matplotlib.org/_images/anatomy1.png](https://matplotlib.org/_images/anatomy1.png)function_overview.html) 
{{% /credits %}}


command  |  description
---|---|
`plt.axis()`      |     Method used to set axis range
`plt.annotate()`      |    Annotate the point xy with text text. 
`plt.xticks()`      |     Used to manipilate the xticks
`plt.yticks()`       |     Used to manipilate the yticks
`plt.grid()`      |     Configure the grid lines
`plt.figure(figsize=(w, h))` | Set the width and height of a plot (in inches)


## Project Challenges

{{% notice challenge "Make a high quality plot" %}}

![](/images/quality_plot.png)


### Step 1

Open empty jupyter notebook and read in the dataframe that contains your 
gapminder data

### Step 2

Create subset of data for one year

```python
df_subset = df.___[df[___] == ____]
```

### Step 4

Plot the life expectancy vs fertility rate

```python
sns.scatterplot(___, ___, ___)
```

Which will return a rudimentary plot:
![](/images/raw_plot.png)

### Step 5

Using matplotlib add a title and labels. Increase the plot size to make it more readable. 

```python
plt.figure(figsize=(___, ___))
plt.____('Life Expectancy vs Fertility Rate')
plt.ylabel(____)
plt.____('Life Expectancy')
```

### Step 6

Weight the size of the scatter points to the population of each country. This can be done using the `size` parameter in the `sns.scatterplot()` function. 

*Tip:* the code above is correct but the magnitude of the population is astronomically larger than that of the life expectancy and fertility rate. Use some math to fix this.  

### Step 7

Setting the axes to display the origin also gives us a more complete picture of what is going on.

```python
plt.axis([0, 85, 0, 9.5])
```

### Step 8

Save the plot

### BONUS:

Try out different plotting themes and save the plots

{{% /notice %}}


## Reading

{{% notice reading "Links" %}}

- [Seaborn Documenation](https://seaborn.pydata.org/)
- [Data-to-Viz](https://www.data-to-viz.com/) gives great tips and inspiration about data visualizations
- [Seaborn Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf)

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}