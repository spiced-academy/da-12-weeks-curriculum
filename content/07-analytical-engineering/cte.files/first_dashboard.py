# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash('spices')

# homemade dataframe
df = pd.DataFrame({
    "spice": ["basil", "mint", "saffron", "basil", "mint", "saffron"],
    "amount": [4, 1, 2, 2, 4, 5],
    "country": ["Italy", "Italy", "Italy", "Canada", "Canada", "Canada"]
})

# uses plotly express to create bar plot
fig = px.bar(df, x="spice", y="amount", color="country", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Spiceling'), # creates header for website

    html.Div(children='''
        Dash: A web application framework for your data. 
    '''), # header for the first Div or division

    dcc.Graph(
        id='example-graph',
        figure=fig
    ) # adds graph to the Div
])


if __name__ == '__main__':
    app.run_server(debug=True) # runs a local server for the website to run on