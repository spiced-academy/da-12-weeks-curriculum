---
title: "Visualization types in Tableau"
weight: 20
---

![An intro image](/images/charts.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@jcoudriet?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jason Coudriet</a> on <a href="https://unsplash.com/s/photos/charts?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>  
{{< /credits >}}


## Inspiration / goal
We will prepare visuals for two of the dashboards:

- **Sales vs Profit Discovery Dashboard preparations**
![dashboard1_drawing](/images/discovery_dashboard1_drawing.png)

- **Sales vs Profit for Categories Discovery Dashboard preparations**
![dashboard2_drawing](/images/discovery_dashboard2_drawing.png)


## Data sources
Tableau has a wide range of possible data connections - it works with files with different extensions, databases, cloud databases, etc. This week we will work with Sample Superstore dataset that is already embedded in your Tableau.

Data Source tab in Tableau is the place where you can manage your data sources, do some simple data manipulations, joins, view your data, etc. More sophisticated data wrangling can be achieved with Tableau Prep or with any other tool (like python, sql, etc.). 

If you want to dive in into more of data manipulation options in Data Source tab you can check out [this tutorial](https://help.tableau.com/current/pro/desktop/en-us/howto_connect.htm).

## Tableau Workbook
Tableau Workbook is your whole working environment in Tableau that consists of the data / the information about the data you're working with and all the visuals (worksheets), dashboards and stories you create with your data.

## Tableau Extensions
Tableau use its own extensions to save the **workbooks** which are:
- *.twb* stores all of your work (worksheets, dashboards, stories) and a reference to the data but without the data itself
- *.twbx* stores everything that *.twb* does and additionally it adds the data to it


## Tableau principles
Tableau works according to 3 principals:
- Drag & Drop: The SQL queries for visual analysis are largely run via Drag & Drop (VizQL)
- Aggregate and drill down: The measures are aggregated and then drilled-down to the level of detail of the dimensions in the view
- Combine


## Measures and dimensions
[Measures and dimensions](https://help.tableau.com/current/pro/desktop/en-us/datafields_typesandroles.htm) refer to the columns in your dataset (the original ones and the ones that you create later on as well):
- dimensions represent qualitative information that could be used to categorize your data. Dimensions could be used for segmenting your data 
- measures represent numeric information. Measures can be aggregated

When you load the data, each column will be automatically understood as either measure or dimension but if it makes sense it could be edited.


## Drag and drop concept
Tableau can make it very easy to create a visual just by [dragging and dropping](https://help.tableau.com/current/pro/desktop/en-us/buildmanual_dragging.htm) things around. The way how it is understood by Tableau is automatic but you can change its behavior if it's not what you want.


## Visualization types
Tableau can create [different visualization types](https://help.tableau.com/current/pro/desktop/en-us/what_chart_example.htm). All possible visualization types for the selected data could be found under the Show Me button or the Marks section.


## Groups
[Groups](https://help.tableau.com/current/pro/desktop/en-us/sortgroup_groups_creating.htm) help you to create new dimensions (a new category) based on the selected data points.

### Groups in geo data
When you're in a map visualization you can create a group by selecting the needed locations, hovering over it and clicking on a clip icon. You can create groups in a similar way for other type of data as well.

### Reading

{{% notice reading "Reading" %}}
- [how to create a dual axis](https://help.tableau.com/current/pro/desktop/en-us/multiple_measures.htm)
- [geographical data](https://help.tableau.com/current/pro/desktop/en-us/maps_howto_simple.htm)
- [more about aggregate functions in Tableau](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_aggregate_create.htm)
- [marks explained](https://help.tableau.com/current/pro/desktop/en-us/viewparts_marks_markproperties.htm)
- [measures vs dimensions](https://onenumber.biz/blog-1/2022/5/2/discrete-vs-continous-in-tableau)
{{% /notice %}}


## Get to know Tableau basic functionalities
Tableau has a lot of teaching materials available online. [This tutorial](https://help.tableau.com/current/guides/get-started-tutorial/en-us/get-started-tutorial-home.htm) is an introduction to your Tableau journey and it is highly recommended if you want to go through the basics once again.


{{% notice challenge "Project preparation" %}}

Load your dataset into Tableau and start doing a data exploration of your datasets.

Note: Remember that this week there are no guided exercises for you to finish your weekly project. The concepts that we will be learning about during the encounters are there to help you with implementing your ideas but should also not limit you.

{{% /notice %}}

<br>

{{% notice copyright "Agnieszka Kaczmarczyk, Katerina Arsh" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}