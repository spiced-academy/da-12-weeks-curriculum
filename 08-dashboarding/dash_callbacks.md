---
title: "Interactive Components and Callbacks"
weight: 60
---

![callback](/images/callback.png)

{{< credits >}}
Photo by <a href="https://unsplash.com/de/@alex_andrews?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alexander Andrews</a> on <a href="https://unsplash.com/de/fotos/JYGnB9gTCls?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

## Callbacks and Core Components
In the previous encounters we already prepared the structure of our dash app and added the plotly graphs inside with the help of dash core components `dash.dcc`. In this encounter we will learn how to add some dash core components to generate higher-level components like controls.

`dash.dcc` gives us access to many interactive components such as dropdowns, sliders, radioitems, buttons, textarea. We will cover dropdowns, radioitems and buttons.

To be able to add these interactive components we need to use callback functions, which are "automatically called by Dash whenever an input component's property changes, in order to update some property in another component (the output)."

{{% notice info "What is a callback?" %}}

In the callbacks, the user interacts with an element and as a result of this interaction a python function is triggered to change something.

1. To build the callback, we start with a decorator: `@callback()` (you may also see in the previous version examples `@app.callback()` )

2. Inside of the decorator, we have Input and Output. Whenever the input changes, the function that the callback decorator wraps will get called automatically. The Output is where to send the function return.

```python
Output(component itself/component_id, component_property)
```
{{% /notice %}}



{{% notice %}}
## Adding Interactive components into our dash

#### 1. Open a jupyter notebook 
We will use the bar chart we created with Germany, Denmark and Belgium to check 3 different interactive components. Therefore, we are creating the same last structure from the previous session.

#### 2. Import the necessary libraries
Since we are going to use `callback`, in addition to the libraries we used in the previous encounter, we are also going to import `from dash.dependencies` `Input`, `Output`, `State`.

#### 3. Dropdowns
To be able to create a dropdown, we are going to define it first and add the values we would like to be able to select from the dropdown menu.

```python
dcc.Dropdown([{'label': ['Germany', 'Belgium', 'Denmark'], 'value': 'Germany'},])
```

After creating it, we need to add it into the skeleton after the division and before the graph.

```python
app.layout = html.Div(children=[
    html.H1(children='Gap Minder Analysis of Germany'),
    html.Div(table, graph1, dropdown,graph2)
    ])
``` 

However, we are not done yet. Our graph should react to user's selection from the dropdown menu. Therefore we need to add callback and a function, which masks the dataframe according to the user's selections:

```python
@callback(
    Output(graph, "figure"), 
    Input(dropdown, "value"))

def update_bar_chart(country): 
    mask = df_countries["country"] == country
    fig =px.bar(df_countries[mask], 
             x='year', 
             y='lifeExp',  
             color='country',
             barmode='group',
             height=300, title = "Germany vs Denmark & Belgium")
    return fig
```

After that run the cell and see how it works.

#### 4. RadioItems

`dcc.RadioItems` are used for rendering a set of radio (or option) buttons.
Like in dropdowns, first we need to create our radio item, and add callback and a function, which filters the data for the bar chart.

```python
radio= dcc.RadioItems(id="companies",options=['Germany', 'Belgium', 'Denmark'], value="Germany", inline=True)
```

After that using the `@callbacks` and the function we can activate it.

#### 5. Download Button
Finally, we will add a download button to our web application so that the user can download the data we use.
First, let's save the df_germany as a txt files in the same folder. Since `Downloadbutton` is not supported anymore, we are going to use the `html.Button`

```python
html.Button("Download Data", id="btn-download-txt"),dcc.Download(id="download-text")
```
This time, our `@callback` will look a bit different, since we are not masking the dataframe accoring to the user's selections.

```python
@callback(
    Output("download-text", "data"),
    Input("btn-download-txt", "n_clicks"),
    prevent_initial_call=True
)


def download_table(n_clicks):
    return dict(content="Gap Minder Germany", filename="germany_table.txt")
```


{{% /notice %}}


{{% notice challenge "Add interactive components to your dash app" %}}

- Add a dropdown component to your bar graph. 
- Check the documentation to add at least one more interactive component into your app.
[here](https://dash.plotly.com/dash-core-components).
- Adjust the color and the styling of the interactive components.


**BONUS:**
- Select another location to focus on and follow all the steps you did for the first location.
- Following the steps in the link [here](https://dash.plotly.com/dash-core-components/tab) create a new tab about the new location for your dash app.

{{% /notice %}}



<br>

{{% notice copyright "copyright Samuel McGuire, Hilal Işık" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}