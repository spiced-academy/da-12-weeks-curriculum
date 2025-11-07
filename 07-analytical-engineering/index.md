---
# Analytical Engineering
---
Welcome to our module on Analytical Engineering! Explore the lessons below:

- [Lesson 1: Intro Analytical Engineering](intro_analytical_eng.md)
- [Lesson 2: SQL-Python](sql-python.md)
- [Lesson 3: APIs](apis.md)
- [Lesson 4: dbt Intro and Setup](dbt-set-up.md)
- [Lesson 5: dbt Stages](dbt-stages.md) 
- [Lesson 6: dbt Marts](data-mart.md)
- [Lesson 7: CTE](cte.md) 
- [Lesson 8: Logging](logging.md)
- [Lesson 9: Advanced SQL Administration](advanced-sql-administration.md)
- [Lesson 10: Advanced SQL Index](advanced-sql-index.md)
- [Lesson 11: Recap](recap.md)

## Project: Climate Data

![](/images/paper_boats.jpg)
{{< credits >}}
Photo by <a href="https://www.freepik.com/author/prostooleh">@prostooleh</a> on <a href="https://www.freepik.com/free-photo/funny-kids-rain-boots-playing-with-paper-ship-by-puddle_9245085.htm">Freepik</a>
{{< /credits >}}

{{% notice challenge "Project Description: Climate Data" %}}

##### 🎯 Project Goal: Construct ELT data pipeline using python, pandas, more advanced SQL, SQLalchemy, and dbt

In this week, you will learn how to connect to your database with Python and how to design and to automate a pipeline. Next week we will use the collected data for a Dashboard to visualize the results. 

The next days, you will work with a comprehensive real world API from https://www.weatherapi.com/. We will get access to historical weather records (daily and hourly) from basically everywhere around over the world. We will aim to obtain weather data for Berlin a few additional locations from the past 365 days (trail account limitations). 

#### Milestones

- **Define Questions**
  - Example questions will be given
  - Students can develop own questions
- **Identify Data Sources**
  - Access data from real world API using a python script (https://www.weatherapi.com/pricing.aspx)
- **Retrieve Data**
  - Querying the API and using SQLalchemy and import raw data into postgres database 
  - Optional: Setting logging in order to catch problems and log successes
  - Connect database to dbt cloud - which will be used to parse and prepare the data
- **Data Wrangling, Exploration and Cleaning**
  - Learn how to use Common Table Expressions in SQL
  - Clean prepare the data on dbt cloud using CTE and the power of dbt
  - Prepare data marts that will be used to answer stakeholders questions
- **Analyze Data**
  - Not part of this week
  - Will be continued next week
- **Present Data to Stakeholders**
  - Not part of this week
  - Will be continued next week

##### Note
Lectures Logging, Managing PostgreSQL users and roles, Query optimization and indexing would go beyond the scope of this week. Consider these topics as the next steps to look into.

### Data Analytics Workflow

![](images/da_workflow.png)

{{% notice copyright "Samuel McGuire, Malte Bonart, Agnieszka Kaczmarczyk" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of [academis.eu/posts/spiele_DE/textadventure.md](https://www.academis.eu/posts/games_EN/textadventure.md) by Dr. Kristian Rother, used under CC-BY-SA 4.0. 

{{% /notice %}}
