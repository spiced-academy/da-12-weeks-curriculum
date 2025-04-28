---
title: "Intro to Analytical Engineering/pipelines"
weight: 10
---

![cartoon](/images/pipeline.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@quinten149?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Quinten de Graaf</a> on <a href="https://unsplash.com/photos/L4gN0aeaPY4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

{{% notice warmup "Is your private data safe?" %}}

#### How do you store your passwords?
Reflect on these questions:
- what is a bad password? (present some concrete ideas)
- how to not store a password?
- what might go wrong when experiencing a data breach?

{{% /notice %}}

### Pyramid of needs in data aka data roles

In 2017 Monica Rogati wrote an [article about pyramid of needs in Data Science](https://hackernoon.com/the-ai-hierarchy-of-needs-18f111fcc007). 

![pyramid](/images/monica_rogati.jpeg)

The pyramid of needs stresses the fact that the most essential thing in data projects is data maintenance that includes data collection, data cleaning, data storage, data modelling, etc. which is typically considered data engineering. The next step refers to data analytics and data science / AI should be only a cherry on the top but only if all the other parts of the pyramid were covered before.

Even though the article is focused on AI and Data Science it opened a discussion about different parts of data projects, different roles in data and how they are all connected with each other. 

### Data roles

Typically in data we distinguish following roles that will be connected with mentioned tasks and areas:
- Data Engineers
  - building and maintaining data infrastructure (data pipelines)
  - collecting raw data sources 
  - cleaning and modelling data for the later data analysis usage 
- Data Analysts
  - (exploratory) data analysis
  - A/B testing 
  - communication with stakeholders (domain knowledge)
- Data Scientists
  - feature engineering
  - machine learning
  - predictions and estimations

However, even though we usually put boundaries between these roles, in reality it's much more complex. Many times data analysts will be covering some of the topics from the data engineering or data science area, and the other way around. 


### Tech stack

There are plenty of tools and types of tools used in data projects. Some of them, as BI tools (e.g. Tableau) are usually exclusive for data analytics, on the other hand many others will be shared between different data roles. 

![stack](/images/data_stack.png)

### ETL vs ELT

Data engineering is many times connected with creating data pipelines - a technical solution that will be responsible for data collection, storing, cleaning and modeling the data for further usage. There are two different strategies or types of data pipelines: ETL and ELT:

ETL                   |  ELT
:--------------------:|:-------------------------:
![etl](/images/etl.png)  |  ![elt](/images/elt.png)

The letters in both names refer to:
- (E)xtract - identifying data from one or more sources (such as databases, files, ERP, CRM, etc.)
- (T)ransform - process of transforming the raw data source into the target format required for analysis projects
- (L)oad - storing the extracted raw data (usually in a data warehouse or a data lake)

Historically data pipelines used to be ETL ones since it was expensive to store huge amount of data. In ETL structure the transformation and modelling of the data for the further analysis was done before loading (storing it).
As we do have more and more easy and cheap ways of storing data, the ELT model became way more popular recently. In this structure data is firstly loaded and could be transformed later on. That means that you don't neccessarily need to know in advance how you want to use your data which makes it more flexible. This model also made it more accessible for data analysts to work on data transformations together with data engineers.

In our case our ELT process will be covered by:
- (E)xtract - fetching our data (in a json form) using weather API
- (L)oad - using a db client (`sqlalchemy`) to connect with a db and sending the raw data to it
- (T)tansform - `dbt` as a data transformation tool

### `dbt`

`dbt` is a transformation workflow (it handles the `T` part from ELT) that we're gonna learn about this week. More on that in the following encounters but some of the properties of it are:
- `dbt` compiles and runs your analytics code against your data platform
- reusable, or modular, data models that can be referenced in subsequent work 
- you can design tests to check the quality of your data as well as generating documentation for your tables


### .env Files


 It's common for teams to maintain distinct "environments" for their codebase. These separate environments allow thorough testing before deploying changes to the production environment, where they interact with end-users. In scenarios involving multiple environments, developers often opt to use multiple .env files to store credentials. For instance, they might have one 
 .env file containing database keys for development and another for production.

 This separation of code and credentials lower the risk of unauthorized individuals gaining access to sensitive data in the cloud.

**.env** files are specifically designed to store credentials in a key-value format for the various services that the program utilizes. These files are intended to be stored locally and not shared in online code repositories, ensuring that sensitive information remains confidential. Each developer within a team typically manages one or more `.env` files, tailored for the specific environments they are working on.

### Usage

In this section, we’ll walk through how to use a `.env` file in a basic python project.

1. To begin, head to the root of your project folder and create an empty `.env` file containing credentials you’d like injected into your codebase. It may look something like this:

```python
WEATHER_API_KEY="924a137562fc4833be60250e8d7c1568"

```

2. Next, you’ll want to ignore the `.env` file from being committed to git. If you haven’t already, create a .gitignore file. 


3. Now to inject the secrets into your project, you can use a popular module like dotenv; it will parse the `.env` file and make your secrets accessible within your codebase under the process object. Go ahead and install the module:

```python
pip install python-dotenv

```

4. Import the module at the top of the start script for your codebase:

```python
from dotenv import dotenv_values

config = dotenv_values()
api_key = config['WEATHERAPI'] # align the key label with your .env file !

```
Cool. We’ve successfully added a `.env` file into your project with some secrets and accessed those secrets in your codebase. Additionally, when you push your code via git, your secrets will stay on your machine.


{{% notice challenge "Design your work" %}}

Get ready for the week! Do you have any idea how we can use the data from website and put it on a dashboard with some cleaning and processing in the middle?  

Before we start making API calls, let's get our credentials (API-Key) ready, let's consider the steps from data source to a dashboard, then we should explore what data we can get and brainstorm what facts and insights we **might** want to present next week.

**Note:** Keep in mind we are preparing the data for future reports (visuals and dashboard next week). Our tables will be optimized for relevant data, but they also should be usefull for different types of aggregation and filtering. The analytical part and visualizations are not goals of this week. 

- Sign up for trial of weatherapi at: https://www.weatherapi.com/pricing.aspx 
  
- Create a `.env` file for your project with the API Keys. Tipp: Save it on the highest level inside your student-code repo (where the README.txt is) - as long as the file is in a higher hirarchy folder dotenv will find it.

- Study the **History API** from [weatherapi.com](https://www.weatherapi.com/docs/#apis-history) that we're gonna get the data from  
  
- Grab a piece of paper and try to design the data workflow  
  (What would be the steps if you want to photocopy a page from a certain book from a city library? Start with going to the library's adress...)
  
- Check out the metrics available in the History API. **Brainstorming:** What KPIs you would like to get out of this data? (Weekly temperature average, total number of rainy or snowy days, ...) Imagine what do you expect to see in a Weather report or on a Climate Dashboard.
  
- Discuss your ideas with the rest of the group

In the next encounters we will guide you through an exemplary process to solve this task and you will have a chance to confront your ideas!

{{% /notice %}}


<br>

{{% notice copyright "Agnieszka Kaczmarczyk, Samuel McGuire" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}