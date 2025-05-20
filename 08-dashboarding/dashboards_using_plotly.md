---
title: "Dashboards using Plotly"
weight: 50
---

![dash](/images/dash.jpg)

{{< credits >}}
Photo by <a href="https://unsplash.com/@lukechesser?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Luke Chesser</a> on <a href="https://unsplash.com/s/photos/dashboard?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}
  

## Plotly - Dash
In the previous encounter, we created the skeleton of our web app and we talked about the usage of the basics. In this encounter we are going to add the graphs and tables into our structure.

Thus far in the course we have made different examples from static to dynamic visuals. Yet they have all been separate unless they were built into a story or some sort. Often analyst would like to have a nice overview of different statistics, models, and trends all in one place as a visual report to share with the stakeholders. Those visual reports are the dashboards what we already covered at the beginning of this week.

Plotly a plotting tool for scientists, analysts and engineers should be familiar from previous lessons. Flask is a library that makes the creatation of user interfaces simple. Building up these two libraries Dash enables the creation of dashboad using python code. 


{{% notice %}}

## Creating gapminder dashboard for Germany

#### 1. Create a jupyter notebook

To make it easy to debug and check step by step, we will use jupyter notebook.But after making sure that you are confident with your dashboard, create a python file and copy the code there. This will also help for us to render. 

#### 2. Importing the libraries
In the previous encounter, we imported `dash`,`html` and `Dash` to create the main structure. We also imported ` dash_bootstrap_components` to change our app layout theme. In this session, since we are starting to add the graps and the tables into our dash, we are going to need `dash_table` and dash core components `dcc`. 

#### 3. Add the code that starts the server for the dashboard
Use the structure you made in the last encounter. 

```python
app.layout = html.Div(children=[
    html.H1(children='Gap Minder Analysis-Germany'),
    ])
``` 

#### 4. Add data to the program

In order to create a a proper dashboard first some plots are needed. Before plots are created data is needed! Load the gapminder data from the plotly express, filter the data for Germany and then  just keep the columns that you would like to show in your dash.

#### 5. Create a table to be added to the dashboard
We are going to use the code below to create a table:

```python
dash_table.DataTable(data.to_dict('records'),[{"name": i, "id": i} for i in data.columns])
```

To be able to align our table with our app styling, we need to pass the parameters like `style_data` and `style_header`.


#### 6. Create a plotly line graph to be added to the dashbaord 

The code below is directly from [Plotly: Introduction]({{< ref "plotly-intro" >}}) expect the `fig.show()` has been removed, because instead of showing it or writing it, it will be added to the dashboard. 

```python
fig_1 = px.line(df_germany, x='year', y='lifeExp', title='Life Expectancy in Germany', markers=True)
``` 

#### 7. Create a plotly  bar graph to be added to the dashbaord 
We are going to filter our dataset for 3 countries  Germany, Denmark and Belgium, and create a bar graph.

```python
fig_2 = px.bar(df_countries, x='year', y='lifeExp', title="Germany vs Denmark & Belgium", markers=True)
``` 
Do not forget to change the background colors of the graphs so they align with the style of our app.

#### 8. Use dcc.Graph to create components
After creating the graphs we need to create the components before passing them inside of our dash app.`dcc` allows the user to add various [dash core components](https://dash.plotly.com/dash-core-components) to the dashboard. We are going to use the code below for both of the graphs.

```python
graph = dcc.Graph(figure=fig)
``` 

#### 9. Add the graph and the plots to the dashboard

 Now add the`dcc` component to the `app.layout` so the layout code looks as the example below. 


```python
app.layout = html.Div(children=[
    html.H1(children='Gap Minder Analysis of Germany'),
    html.Div(table, graph1, graph2)
    ])
``` 
 
Run the complete app cell and check the browswer. 

The following image should be rendered in the web browswer. 

![dash_!](/images/dash_2.png)


#### 9. Exercise Challenge - Add more graphs

Add more graphs from the [Plotly: Introduction]({{< ref "plotly-intro" >}}) and [Visualizing Geospatial Data with Plotly]({{< ref "plotly-maps" >}}) to the `app.layout`
{{% /notice %}}

### Dash's capabilities

There is loads more that can be done with dash and we have only scratched the surface. A rangeslider can be added, dropdown menus, user input, radio buttons, makedown can be used and so much more! We are going to practice some of them during the next sesion. You can take a look over the documentation [here](https://dash.plotly.com).


{{% notice challenge "Add tables and graphs into your dash app" %}}

- Create a table which focuses on only one location with using `dash_table.DataTable`.
- Add the temperature plots, graphs and maps you have made with plotly into the `dash` dashboard skeleton you prepared. 
- Check this documentation to add some explanation info into your app.
[here](https://dash.plotly.com/dash-html-components).
- Adjust the color and the styling.

{{% /notice %}}

{{% notice reading "Make a dashboard app with Plotly and Dash" %}}

Another dash tutorial could be found [here](https://realpython.com/python-dash/)

{{% /notice %}}

<br>

{{% notice copyright "copyright Samuel McGuire, Hilal Işık" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}
