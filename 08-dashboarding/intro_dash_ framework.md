---
title: "Introduction to Dash Framework"
weight: 40
---

![A dash board](/images/dashintro_12.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/de/@chrisliverani?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Chris Liverani</a> on <a href="https://unsplash.com/de/fotos/dBI_My696Rk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> 
{{< /credits >}}


{{% notice warmup "Warmer: Dash app structure" %}}

1. Create a python file and name it as `my_first_dashapp.py` 

2. Copy and paste the code below into your python file.

```python
import dash
from dash import Dash, html

app =dash.Dash()

app.layout = html.Div(html.H1(children = 'My First Spicy Dash'))

if __name__ == '__main__':
     app.run_server() 
```

3- Run the code and try to understand the steps

{{% /notice %}}


## Introduction

Dash is the original low-code framework for rapidly building data apps in different languages such as Python, R, Julia, and F#. To be able to use dash, you do not need to know any html or CSS.

The basis for a Dash dashboard is a Dash object. Much like when a pandas DataFrame object is instantiated all of the methods and attributes of the DataFrame class are available, the same can be said for a Dash object. Once it has been instantiated it will act as the interface to all of the methods and attributes available in the Dash class. The developers at Dash did this in order to simplify things for programmers using the library.

## Pillars of Dash
1. Dash Components: They can be anything from checkbox, slider, checkbox, date picker, dropdown, input, textarea,radioitems, buttons etc.

2. Plotly Graphs: graphs, charts from plotly that we can use to visualise the data and tell the story

3. Callback: They have the being the glue between the first two components and connect them with each other.

## A Basic Dash App

```python
import dash
from dash import Dash, html
```
Depending on the complexity of your app you need to import the necessary packages from dash

```python
app = dash.Dash()
```
This part is to initialize the app.


```python
app.layout = html.Div(html.H1('My First Dash'))
```

Here we are setting our app layout. The app.layout is composed of a tree of `components` such as  `html.Div` and `dcc.Graph`.


The basis for a Dash dashboard is a `Dash` object. Much like when a pandas `DataFrame` object is instantiated all of the methods and attributes of the `DataFrame` class are available, the same can be said for a `Dash` object. Once it has been instantiated it will act as the interface to all of the methods and attributes available in the `Dash` class. The developers at Dash did this in order to simplify things for programmers using the library.

{{% notice info "`pd.DataFrame` vs `Dash('name_of_app')`" %}}

When instantiating a dataframe `df = pd.DatFrame()` is used. Running this code will make an empty dataframe. Usually data is read into the dataframe at the time of defining it. Now methods and attributes can be accessed through `df`. For example:

```python
df.head()
df['columnd_num'].sum() # and any other methods and attributes
``` 

When running the code `app = Dash('name_of_app')` a very similar thing happens. There is now an empty dash app. Accessing the applicaiton via `app.layout` allows the user to add components to the application and `app.run_server()` turns on the server to then render the dashboard in a web based browser.

```python
if __name__ == '__main__':
     app.run_server() 
```

This part runs a local server for the dashboard app to run on.It turns on the server to then render the dashboard in a web based browser.The browser itself is where the rendering is happening.
{{% /notice %}}

{{% notice reading "What is `if __name__ == '__main__':`" %}}

A deeper explanation of `if __name__ == '__main__':` can be found [here](https://realpython.com/if-name-main-python/).

{{% /notice %}}


In order for the dashboard to render in a web browser (much like a jupyter notebook) a server must be started. The final bit of code starts a developmental server and then allows the user to view the dashboard on [http://127.0.0.1:8050/](http://127.0.0.1:8050/)

{{% notice warning ".env credentials" %}}

If you are getting the data from cloud, you are going to need the .env file for your credentials. DO NOT name your credentials as "HOST" or "PORT" since your app is going to get your ip and port as a host and port to run the app and you are going to get an error. Name them differently such as "HOST_POSTGRES" or "PORT_APP"

{{% /notice %}}


{{% notice challenge "Create a dash app" %}}

- With the temperature plots, graphs and maps you have made with plotly, you will create a dash web app in the next two sessions. Start preparing the skeleton and the style of your dash using the code from course materials 
- Try some different themes. You can find the available themes list [here](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)
- You can also check different html components for styling [here](https://dash.plotly.com/dash-html-components)



{{% /notice %}}


{{% notice reading "dash in juypter notebooks" %}}

- To develop with dash in jupyter notebooks: [dash in jupyter](https://github.com/plotly/jupyter-dash)


{{% /notice %}}

<br>

{{% notice copyright "copyright Samuel McGuire, Hilal Işık" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}