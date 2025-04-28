---
title: "Plotly: Introduction"
weight: 20
---

{{< plotly html="/3dscatter.html" height="550" >}}

{{% notice warmup "Quick Start with Ploty" %}}

Open a command prompt and install plotly:

```bash
pip install plotly
```

Open a Jupyter Notebook and run the following commands:
```python
import plotly.express as px
 
fig = px.line(x=[1, 2, 3], y=[1, 2, 3])
fig.show()
```
If the jupyter notebook does not display the plot, please use `fig.show(renderer='notebook_connected')`

When using only 2 lines of code to produce a plot what is the difference from the results of `matplotlib` and `plotly`?

{{% /notice %}}


## Concepts

`plotly` is a package for interactive ``html`` based visualizations. It is based on a javascript library ``plotly.js``. When displaying charts in the browser, the Python code is converted into the corresponding Javascript which is placed inside a `html` file.


## Package Structure of Plotly

concept  |  description
---|---|
`plotly.express`      |   high level plotting library similar to `seaborn`
`plotly.plotly`      |   interface between the local machine and Plotly
`plotly.graph.objects`      |   contains the objects that are responsible for creating the plots
`plotly.tools`      |  contains many helpful functions facilitating and enhancing the Plotly experience

**Note:** `plotly.express` module can create the entire Figure at once. It uses the graph_objects internally and returns the graph_objects.Figure instance.

## Plotly Express

The `plotly.express` is an interactive, open-source plotting toolkit that supports over 40 different chart types for statistical, financial, geographic, scientific, and 3-dimensional applications. The following example will demostrate some of its power and ease of use. 

concept  |  description
---|---|
`scatter()`      |  each row of data_frame is represented by a symbol in a flat 2D format
`scatter_3d()`      |  each row of data_frame is represented by a symbol in a 3D format
`line()`      |   each row of data_frame is represented as part of continuous line
`bar()`      |   each row of data_frame is represented as a rectangular
`violin()`      |   rows of data_frame are grouped together into a curved mark to visualize their distribution
`box()`      |   rows of data_frame are grouped together into a box-and-whisker mark to visualize their distribution
`density_heatmap()`      |  rows of data_frame are grouped together into colored rectangular tiles to visualize the 2D distribution of an aggregate function histfunc (e.g. the count or sum) of the value z

Like `seaborn` `plotly` has a few datset that come along with the library to showcase its abilities. The following examples are done with the **gapminder** data. 

```python
import plotly.express as px

df = px.data.gapminder()
```

#### **Simple line plot**

Rendering an interactive and sleek plot is very simple and intuitive using plotly. Taking that into account user can add many layers of complexity if applicable.  

The following code first filters for Canada and then plots the life expectancy over time. Notice the menu in the top right corner. What are users able to do to and with the plot?

```python
df_canada = df[df['country']=='Canada']
fig = px.line(df_germany, x='year', y='lifeExp', title='Life Expectancy in Canada', markers=True)
fig.show()
```
{{< plotly html="/line_simple.html" height="550" >}}

Plotting several counties on one plot is as easy as filtering for them and running almost the same code. Below the only difference is the addition of the `color` parameter used to distiguish one line from the other. 

```python
df_europe = df[df['continent'] =='Europe']
fig = px.line(df_europe, x='year', y='lifeExp', color='country')
fig.show()
```
{{< plotly html="/line_multi.html" height="550" >}}


#### **Scatter plots**


Two dimensional scatter plot visualize the relationship between two variables. However in the example below the size of the marker denotes the population. Therefore in this case a third variable is being taken into account.

```python
fig = px.scatter(df_canada, x='year', y='lifeExp', size='pop', title='Life Expectancy in Canada')
fig.show()
```
{{< plotly html="/scatter_1.html" height="550" >}}


In this following case plotting the information in three dimensional scatter plot allows for the addition of a fourth and fifth variable. These are represented by the color and size of the markers.  

```python
df_oceania = df[df['continent']=='Oceania']
fig = px.scatter_3d(df_oceania, x='year', y='gdpPercap', z='pop', color='country', size='lifeExp')
fig.show()
```
{{< plotly html="/3d_example.html" height="550" >}}

However, is it easy to interpret this visualization? Remember to not overuse 3 dimensional graphs!

{{% notice info "How to save plots as html" %}}

The plots rendered on this page are backended by `Plotly` and coded with `html`. In order to save the plot as an `html` file for use in a website use the following command:

```python
fig.write_html("/path/to/file.html")
```

{{% /notice %}}

#### **Bar Plots**

A bar chart or bar graph is a chart or graph that presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent. The bars can be plotted vertically or horizontally.

A bar graph shows comparisons among discrete categories. One axis of the chart shows the specific categories being compared, and the other axis represents a measured value.

Using `pandas` a subset of the data can be directed used as a plot parameter and plotted for the comparision of life expectancy in Germany of time. 

```python
fig = px.bar(df[df['country']=='Germany'], x='year', y='lifeExp')
fig.show()
```

The subset can be easily expanded and visualized to 3 countries using `pandas`and the `color` parameter. Here the data is stacked for comparison. 

{{< plotly html="/bar_simple.html" height="550" >}}

```python
fig = px.bar(df[df['country'].isin(['Germany', 'Belgium', 'Denmark'])], x='year', y='lifeExp', 
                color='country')
fig.show()
```

{{< plotly html="/bar_stacked.html" height="550" >}}

In order to compare the results side by side the parameter `barmode`need to be set to **group**.

```python
fig = px.bar(df[df['country'].isin(['Germany', 'Belgium', 'Denmark'])], x='year', 
                y='lifeExp', color='country', barmode='group')
fig.show()
```

{{< plotly html="/bar_side.html" height="550" >}}

There are many different plot methods available in `plotly`. Feel free to explore them all the options they offer. 

{{% notice reading "Low level plotting API" %}}

Type in `print(fig)` and you will see that a plotly graph is a large 
nested dictionary that contains all the visual declarations and the data for plotting.

`plotly.express` is a high level API that works similar to `seaborn` as columns 
of your DataFrame are mapped to visual parameters of the plot. But you can also directly change all values in the dictionary to fine-tune the plotly figure.

To do that use the functions `fig.update_*(key=dict(...))`. 

```python
fig.update_layout(title_text="Using update_layout() With Graph Object Figures",
                  title_font_size=30)
 
# print to see that the new information was added to the fig object
print(fig)
```

You find the complete reference [in the online documentation](https://plotly.com/python/reference/).

{{% /notice %}}

{{% notice challenge "Solve with SQLalchemy, pandas and plotly" %}}
- Import your table with average temperatures into a Python DataFrame
- Create interactive temperature bar plots for Berlin and other locations (if you have them) using `plotly`
- Experiment with other visualization types (e.g. line charts) and choose a preferable one for showing this data
- If you created more tables last week, create more visualizations for them
{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}