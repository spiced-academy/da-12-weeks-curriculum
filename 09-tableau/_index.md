---
chapter: true
pre: '<i class="fas fa-columns fa-fw"></i> <b>9. </b>'
title: Tableau
weight: 90
---

### <i class="fas fa-columns fa-fw"></i> Chapter 7 - Tableau

# Project: Dashboard

![tableau](/images/tableau-01.png)

{{% notice challenge "Project Milestone" %}}

##### 🎯 Build a Dashboard with Tableau!

- Use one of the datasets attached here ([City Bike rentals](https://ride.citibikenyc.com/system-data) or [SF crime data](https://datasf.gitbook.io/datasf-dataset-explainers/sfpd-incident-report-2018-to-present))
    - Note: The data available to download here was lastly updated in August 2022. If you would like to experiment with these datasets more in the future, the datasets are updated on a regular basis including present data (available from the linked websites)
- Create at least two dashboards (combined in a story)
- Include at least three different chart types
- Include filters (and preferably parameters) to make the dashboard interactive
- Publish your dashboards/story on Tableau Public

Note: When pushing the files from this week to your github repository be careful about the data files. Both of the data files exceed 100MB which is a size limitation of a single file for git. However, when compressed, they should meet the pushing criteria.  

{{% attachments title="Datasets files" pattern="sf_crime|JC_citibike" /%}}

**Data Analytics Workflow steps:**

- Define questions:
    - Students are asked to develop their own questions
    - Exemplary questions are also provided
- Identify data sources:
    - csvs files given in course material
- Retrieve data:
    - Read in a csv file to Tableau
- Data wrangling, exploration and cleaning:
    - If wanted, perform feature engineering
- Analyze data:
    - Use Tableau visualizations to analyze the data and prepare visual answers to the questions
- Present data to stakeholders:
    - Present Tableau story (dashboards)

{{% /notice %}}


{{% expand "Data Analytics Workflow" %}}

![](images/da_workflow.png)

{{% /expand %}}


{{% notice info "Tips regarding SF crime dataset" %}}

- the full description of the fields can be found at [the dataset source page](https://datasf.gitbook.io/datasf-dataset-explainers/sfpd-incident-report-2018-to-present)
- not all the fields are included in the zip file. Also, in your project you might decide to use even less fields than available there
- when uploading the dataset into your Tableau workbook you might want to double check if the data types are detected correctly. In this dataset pay attention especially to two of the fields:
    - `Point` - should be understood as a spatial data type (as it's storing latitude and longitude). You can check the data type at the Data Source tab, in a table representing the dataset metadata at bottom left. Spatial data type is denoted as a [globe icon](https://help.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.htm). If it's not, right click on the icon and select `Change data type -> spatial`
    - `Report Datetime` - should be understood as a datetime data type (calendar page with a clock icon). If it's not, change it in a similar way as we changed the data type for `Point`
- it's fully up to you, what kind of story you want to create with this dataset, but you can get inspired by these questions:
    - When are most of the crimes happening (weekdays, times of the day, months, etc.) and when are they reported?
    - Are there more or less crimes happening in time?
    - What kind of crimes are most common?
    - Where are the crimes happening? Which neighborhoods are mostly affected by crimes?
- if you want to add a google maps background view in your map visualization, you can follow instructions from this [tutorial](https://help.tableau.com/current/pro/desktop/en-us/bkimages_maps.htm)

{{% /notice %}}

{{% notice info "Tips regarding JC bikes dataset" %}}

- a more detailed description of the dataset can be found at [City Bike website](https://ride.citibikenyc.com/system-data)
- the file that is visible here is using only the JC data. As this data is spread into multiple files at the website, a few data processing methods were used to come up with a single file:
    - the column names were unified
    - some columns were removed
    - some rows were removed (missing end station name)
    - some empty data was filled with new values:
        - missing gender was changed to unknown
        - missing rideable type was changed to unknown
        - missing user type was changed to unknown
        - missing ride id was changed to a randomly generated id (16 characters with both letters and numbers)
    - user types were unified to Subscriber/Customer only
- if you have problems loading the file you might want to limit the number of rows (you can modify it using pandas and for example selecting only one year of data)
- again, it's fully up to you, what kind of story you want to create with this dataset, but you can get inspired by these questions:
    - What are the most frequent stations?
    - What is a typical duration time of the trip?
    - Are there more subscribers or non-subscribers using the bikes? Are there any changes in the behavior of different user types?
    - What kind of bikes are used by the users?
- as above, if you want to add a google maps background view in your map visualization, you can follow instructions from this [tutorial](https://help.tableau.com/current/pro/desktop/en-us/bkimages_maps.htm)
- the bikes dataset is distributed using a [specified license agreement](https://ride.citibikenyc.com/data-sharing-policy)
- if you encounter problems reading the geospatial data and you are working on a computer that is using german formatting you might need a different syntax inside your csv data (in german formatting decimal point will be marked as `,` instead of a more common `.`).
{{% /notice %}}

<br>

{{% notice copyright "Agnieszka Kaczmarczyk, Katerina Arsh" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}