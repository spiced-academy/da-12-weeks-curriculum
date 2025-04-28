---
title: "Storytelling"
weight: 10
---

![dices](/images/dices.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@hugowiz">Ugo Mendes Donelli</a> on <a href="https://unsplash.com/s/photos/explore?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

In a regular job of a data analyst you will be asked to build dashboards to support your colleagues with data so they can make better informed decisions. 

The topic of this week is Tableau. But Tableau is just one of the tools to assist you in such a task. Tableau is one of the data visualization tools that is focusing on Business Intelligence (BI). Tableau is one of the leaders in this category (also very often mentioned in job postings), but there are more tools on the market that are serving a similar purpose and the concepts that you will learn with Tableau will also appear in similar forms in these tools. Just to name a few other solutions: Looker, Periscope, PowerBI, Metabase and many many more.

Remember that [Tableau](https://www.youtube.com/watch?v=7Jl-RwkzqQ4&t=2s&ab_channel=TableauTim) is just a tool and the real skill is the ability to make stories out of data.

## Storytelling

Storytelling refers to turning data into insights using proper communication, narrative, and visualizations. 

### Dashboards
Dashboard is a visualization tool that tracks / monitors the data that is designed for a specific group of people. It could be a general KPI dashboard but it could be a very specific dashboard relating to a particular part of the business.

When you are preparing for building a dashboard, it's important to follow the why-what-how framework where you start from understanding the need for a dashboard. That might require:
- understanding the (daily) job of your colleagues
- understanding what problem we are trying to solve
- understanding how your colleagues are making decisions
- understanding what information they are already using and how
- understanding the current situation of you colleagues in terms of their projects

Common problems when trying to come up with a dashboard:
- trying to show all the data
- going into too many details without a reason
- not listening to your colleagues at all in terms of the needs 
- just implementing a given specification without questioning it

## Brainstorming
### Superstore data
During our encounters we will be working with Superstore data to show you some of the concepts of working with Tableau. This dataset is embedded in Tableau and you don't need to download it from anywhere. For your project you will use one of the datasets from the index page.

### Dashboard requirements
For our Superstore data, let's imagine that we already talked to management and gathered all the requirements. After many conversations, what we have prepared, is a set of drawings that we would like to implement later on. This is what they look like:

**Sales vs Profit Discovery Dashboard**
![dashboard1_drawing](/images/discovery_dashboard1_drawing.png)

**Sales vs Profit for Categories Discovery Dashboard**
![dashboard2_drawing](/images/discovery_dashboard2_drawing.png)

**Sales vs Profit in Time Discovery Dashboard**
![dashboard3_drawing](/images/discovery_dashboard3_drawing.png)

**KPIs map Dashboard**
![kpi_dashboard1_drawing](/images/kpi_dashboard1_drawing.png)

**KPIs by Categories and States Dashboard**
![kpi_dashboard2_drawing](/images/kpi_dashboard2_drawing.png)

{{% notice question "Dashboards discussion" %}}

Look at all the presented dashboards and discuss what you like about them and what you would like to change. 

Do you have a better idea how to present sales and profit related information for Superstore? Present your thoughts to the group.

{{% /notice %}}


### Project Management Tools
To help organize the work you could use any of the project management tools such as [Trello](https://trello.com). Look at what you want to achieve and try to identify what tasks you need to do to get there. The tasks could be added then to your project board.



## Tableau Overview
Tableau is a visual analytics platform that includes multiple products:

### Tableau Prep
Data preparation tool, enabling to cleanse, aggregate and merge data for further analysis

### Tableau Server
Online hosting platform to share the workbooks and collaborate

### Tableau Desktop
Data visualization tool to create interactive reports. It will be the only Tableau product we will discuss more this week.

### Tableau Public
Free (and online) version of Tableau that allow you to connect to a spreadsheet or file and create interactive data visualizations for the web. This is also where you can create your Tableau portfolio.


## Tableau Installation
To install Tableau Desktop you need to register first. Go to [registration page](https://www.tableau.com/products/trial) and register with your email. After that you will recieve an email and click on the linkto activate your account in tableau server.
Now, you are ready to download tableau desktop. (We recommend you to use the 2023 version) Go to [the download page](https://www.tableau.com/support/releases/desktop/2023.1.12#esdalt) download and install it. It will give you a free access to Tableau Desktop for the next 14 days.

If you want to continue using Tableau after this period, you can switch to Tableau Public which is a web limited version of Tableau Desktop.


{{% notice info "Tableau course materials" %}}

You will find less materials in the Tableau week course materials comparing to the previous weeks. However, there are more links included there - most of them will guide you to the official Tableau documentation which uses examples, screenshots and videos which are very easy to follow.

{{% /notice %}}


{{% notice challenge "Project preparation" %}}

#### Exercise 1
Install Tableau Desktop and create a Tableau Public profile.

#### Exercise 2

Explore the chosen dataset. Open the files, play with the data first to see what is available (you can use jupyter notebooks and pandas data inspection methods). As you don't have a real user in front of you think on your own about what story you would like to tell with this data. Think about possible questions and how they could be arranged in a dashboard / multiple dashboards.

Note: The datasets are quite clean so we don't require any additional data processing in pandas. However, if you still want to do it you are welcome to update the datasets (do some feature engineering or deal with the remaining missing values) but don't spend more than the remaining time of the morning encounter on that.

#### Exercise 3
Draw your dashboard(s) on paper and try to identify the tasks that you need to do in order to achieve having it.

{{% /notice %}}

<br>

{{% notice copyright "Agnieszka Kaczmarczyk, Katerina Arsh" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}