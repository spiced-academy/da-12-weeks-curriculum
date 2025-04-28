---
title: "Visualizing Geospatial Data with Plotly"
weight: 30
---

{{< plotly html="/map_world.html" height="550" >}}


{{% notice warmup "Gapminder data in plotly" %}}
Run the following code in a notebook or `.py` file:

```python
import plotly.express as px

df = px.data.gapminder()
df = df[df['year'] == 2007]

fig = px.choropleth(
    data_frame=df, locations="iso_alpha", projection='orthographic',
    color="lifeExp", # lifeExp is a column of gapminder
    hover_name="country", # column to add to hover information
    color_continuous_scale=px.colors.sequential.Blues
)
fig.write_html('life_expectancy.html', include_plotlyjs='cdn')
```

- Open the generated file `life_expectancy.html` in your browser!
- What does the column `iso_alpha` contain?
- What means `projection='orthographic`?
- Plot the data for the year 1952!

{{% /notice %}}


## Our first Choropleth map

A Choropleth is a map with areas colored by some property. Execute the following  code in a Python script/notebook. This will create a file named `map.html` that can be opened in a browser.

```python
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    'iso3_country': ['DEU', 'USA', 'FRA', 'CHN'],
    'value': [100, 120, 78, 23]
})

fig = px.choropleth(df, locations='iso3_country', 
                    projection='orthographic',
                    scope='world',
                    color='value', locationmode='ISO-3')
fig.write_html('map.html')
```

{{% notice question "Choropleth Maps" %}}

Check out the documentation for [`px.choropleth](https://plotly.com/python-api-reference/generated/plotly.express.choropleth.html#plotly.express.choropleth).

- Change some of the highlighted countries and values by editing the DataFrame.
- Change the projection of the map with ``projection``.
- Change the colorscale with ``color_continuous_scale``.
- What can you use the arguments ``animation_frame`` and ``animation_group`` for?

{{% /notice %}}



## Tile based maps


This code prints a scatterplot on a tile based map background:

```python
import pandas as pd
import plotly.express as px


data = pd.DataFrame({
    'lat': [50.9375, 52.5200, 53.5511, 48.7758],
    'lon': [6.9603, 13.4050, 9.9937, 9.1829],
    'city': ['Cologne', 'Berlin', 'Hamburg', 'Stuttgart'],
    'population': [1086000, 3645000, 1841000, 634830]
})


fig = px.scatter_mapbox(data, 
                        lat="lat", lon="lon", 
                        hover_name="city", size="population",
                        # start location and zoom level
                        zoom=4, center={'lat': 51.1657, 'lon': 10.4515}, 
                        mapbox_style='carto-positron')

fig.write_html('map.html')

```

      
You can chose different styles by changing ``mapbox_style``. Try out:

- 'open-street-map'
- 'white-bg'
- 'carto-positron'
- 'carto-darkmatter'
- 'stamen- terrain'
- 'stamen-toner'


## Retrieving coordinates


If you have an address and need the coordinates, go to Google maps or use ``geopy``:

```python

# !pip install geopy
from geopy.geocoders import Nominatim

loc = Nominatim(user_agent="mymap").geocode(
    "1209 Campbell street, Oakland"
)
print(loc.address, loc.latitude, loc.longitude)
```


## Custom choropleth maps with GeoJSON data


`Plotly` has some built-in lists of locations of US-states and countries worldwide. 
If you want to map values from a DataFrame to other areas at a different scale 
(such as European regions, or Berlin districts) 
you need an additional file that contains geometry information about these regions.

The GeoJSON is a popular format for specifiying such geometric boundaries: 

```json
{
    "type": "FeatureCollection", 
    "features": [
    {
            "type": "Feature", 
            "id": "01001",
            "properties": {
                "NAME_3": "Autauga",
            }, 
            "geometry": {
                "type": "Polygon", 
                "coordinates": [
                [
                        [-86.496774, 32.344437], 
                        [-86.717897, 32.402814], 
                        "..."
                ]
                ]
            } 
    }, {
            "type": "Feature", 
            "properties": {
                "..."
            }
            "..."
    }
    ]
}


```

You can then make custom choropleth maps with mapbox and a geojson file!
Check out the function [plotly.express.choropleth_mapbox](https://plotly.com/python-api-reference/generated/plotly.express.html#plotly.express.choropleth_mapbox).

```python

import pandas as pd
import plotly.express as px
import requests

url = "https://raw.githubusercontent.com/isellsoap/deutschlandGeoJSON/main/4_kreise/3_mittel.geo.json"
resp = requests.get(url=url)
geojson_data = resp.json()

data = pd.DataFrame({
    'name': ['Oldenburg', 'Osnabrück', 'Bremen Städte'],
    'population': [168210, 164748, 569352]
})

fig = px.choropleth_mapbox(data, 
                            locations='name',
                            color="population",
                            geojson=geojson_data, 
                            featureidkey="properties.NAME_3",
                            opacity=0.8,
                            zoom=5, 
                            center={'lat': 51.1657, 'lon': 10.4515},
                            mapbox_style='carto-positron')

fig.write_html('map.html')
```

Plotly maps the id field `properties.NAME_3` of the provided geojson with the column `name` of the DataFrame.
Which id you want to map to which column of your DataFrame depends on the specific GeoJSON you are using. With the
argument `color` we can then give each geographic region a color according to the value provided by the column `population`. 


{{% notice challenge "Create an interactive temperature map with plotly" %}}

   
Choose one (or more) of these options and plot using `plotly`:



- Create animated choropleth map of the temperature of selected countries over time.

    **Tips**: To be able to make a choropleth map, you are going to need the iso alpha codes for the countries you selected. After preparing your dataframe you can use the iso_codes.csv file below and concatenate with the prepared dataframe you are going to use for your map. You can use average, min or max temperatures. Use the `choropleth` plot function from `plotly` with its `animation_frame` parameter in order to animate the plot for different time. 

    {{% attachments title="Iso codes" pattern="iso_codes" /%}}

- Create scattermap of all the locations in the data.

    **Tips**: You can use the filtered datamarts for some specific countries. For this map, you are going to need the `lat` and `lon` data for the stations, which already exist in the original data. Use the `scatter_geo` function from `plotly`to visualize the locations of the each weather station/city. [scatter_geo Documentation](https://plotly.com/python-api-reference/generated/plotly.express.scatter_geo.html) 

- Bonus

    Create warming stripes for one station over time to inspect warming over time.

    **Tips**: Use a data mart you prepared or filter data for one location over the largest timeframe possible. Use the date, average temp to create warming stripes showing the change in average temperature over time. This can be done using the bar()plot with some tweaks. The goal is a plot similar to this with some anntonation if possible.



  

{{% /notice %}}

{{% notice reading "Where to find GeoJSON files?" %}}

-  [Germany, github.com/isellsoap/deutschlandGeoJSON](https://github.com/isellsoap/deutschlandGeoJSON)
- [German postal codes, github.com/yetzt/postleitzahlen](https://github.com/yetzt/postleitzahlen)
-  [World / Europe, geojson-maps.ash.ms](https://geojson-maps.ash.ms/)

{{% /notice %}}

{{% notice reading "Reading" %}}

- [More plotly map examples](https://plotly.com/python/choropleth-maps/#choropleth-map-with-plotlyexpress)
-  [GeoJSON Tutorial](https://leafletjs.com/examples/geojson/)

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart, Hilal Işık" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}
