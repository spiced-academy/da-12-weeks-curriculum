---
title: "KPIs"
weight: 20
---


![KPIs photo](/images/kpis.jpg)
{{< credits >}}
Photo  by <a href="https://unsplash.com/@walls_io">Walls Io</a> on <a href="https://unsplash.com/photos/CmOTdH1dfg4">Unsplash</a>
{{< /credits >}}






## Key Concepts

`Metrics` is a very wide term used in many different occassions to provide a measure for something. We usually use them for comparing and tracking purposes. Today, we will make a distinction between business metrics and error metrics, both are widely used in the data field.

concept   |  description
---          |---
`metric`       |     the variable that we are trying to understand and predict
`KPI`      |     Key Performance Indicator



## KPIs
`Key Performance Indicators (KPIs)` are metrics, but not all the metrics are KPIs. Because of the fact that we can't put the `=` sign between these two, it's important to understand what both of them represent.

KPIs are metrics that are used to measure business critical initiatives, goals and objectives. They are agreed on by the team (a metric that is a KPI in your company doesn't need to be a KPI in a different company). A KPI does not only clearly explain how to calculate it but also includes information about the planned target (so the team / company can check if they are where they want to be).

Examples of metrics that could be KPIs:
- Growth in Revenue
- Net Promoter Score (NPS)
- Number of Qualified Leads (per period)
- Number of New Customers (per period)
- Customer Life Time Value (LTV)
- Average Support Resolution Time 

and many more.


## Business metrics
KPIs are very particular metrics in the business world. All the measures that are used to track, monitor and assess the success or failure of different angles of the business could be called business metrics.


## Exercises

In groups discuss the following questions then present one KPI to the class.

Referring to the bikes dataset: 
- Are there some business metrics you could build from the data we already have?
- What KPIs could you add with the additional data that Capital offers here [capital data](https://ride.capitalbikeshare.com/system-data)
- If you had access to all of the data you could imagine Capital collects, what other KPIs would you track? 
- Present one KPI to the class as a group.


## Final Projects Tips

Typically questions are made by stakeholders. Data Analysts attempt to answer them using data. This approach can also be used in your final project. You will play the role of the stakeholder and the data analyst. 

- Think about any questions you would like to answer from the stakeholder perspective. Then search for a dataset(s) that will help answer the questions. Then from a data anlyst's perspective, using the tools you learn thoughout the bootcamp, answer the questions. 

Another approach would be to search for ways to analyze or optimize whatever is associated with a dataset that interests you:

- Pick a dataset then think about the questions, KPIs and metrics that could be used to the analyze or optimize the goal associated with the dataset.


{{% notice challenge "Muesli Dataset KPIs" %}}

Analyze the content of the Muesli Dataset again. Think about KPIs that would be useful for tracking the delivery processes.   
Think about their definitions, the reasoning behind your choice and how to calculate them. 
​

**1. Merge all datasets together:**
- pay attention which columns need to be parsed as datetime
- compare column names of all datasets, consider cleaning them
- when merging - you need to make sure you are merging **ON** the right column or multiple columns
- check if there are duplicated rows (all values same as in another row!), drop these duplicates
​

**2. Create 3 KPI for delivery processes as columns:**
- **Order To Truck Time** (order date - on truck scan date)
- **Processing time** (order date - ready to ship date)
- **Waiting time** (ready to ship date - on truck scan date)
- (optional) add KPIs of your choice
​

**3. perform EDA:**

- plot distribution of "order to truck time" split by ship mode
- plot distribution of "processing days" split by  ship mode
- plot distribution of "waiting time" split by  ship mode
- ...


{{% /notice %}}








<br>

{{% notice copyright "Dina Deifallah, Agnieszka Kaczmarczyk, Samuel McGuire, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}