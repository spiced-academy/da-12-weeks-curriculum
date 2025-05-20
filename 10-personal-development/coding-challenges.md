---
title: "Coding Challenges"
weight: 90
---

![challenge](/images/coding_challenge.jpg)

{{< credits >}}
Photo by <a href="https://unsplash.com/@olav_ahrens?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Olav Ahrens Røtne</a> on <a href="https://unsplash.com/s/photos/challenge?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

This part has been prepared to simulate the coding challenge you may encounter as part of a real job interview/recruitment process.
Below you will find 3 different challenges. The job title, provided data and the tasks to be performed differ in each of them. 
Please choose one of these challenges and make the requested analysis and share your findings with us on Thursday. 
It is expected that your presentation will have a more business/professionally oriented structure, 
unlike the presentations you have made within the scope of the bootcamp so far.



## Challenge 1:  Business Analyst Projects & Operations



### Background information

You are a Business Analyst in the Projects & Operations Team at smartbuy (an e-commerce company). You just visited a Training session by the Content Department at smartbuy. The Content
Department is responsible for managing the categories at smartbuy. During the training they explain the process of how they manually identify the seasonality of a category. The word ‘manually’ makes
you curious and you quickly realize that there must be a more effective way to identify different seasonality patterns. So, you reach out to the content team and they are grateful that you are willing
to help. They give you a list of csv-files which contain the pageviews of a given category in a specific month.

### Data

{{% attachments title="Related files" pattern="eCommerce_business_case" /%}}

Attached above is a list of 100 csv-files, each containing the same columns:

- category name - name of the category
- month – number of the month
- year – year
- clicks - page views of the category

### Tasks

Create an analysis to help the content team and answer following questions:

1. Is there a seasonal pattern for all categories?
2. What are common patterns that we observe within the categories?
3. Are there categories with a similar fingerprint?
4. Now that you know the seasonal pattern, what next actions would you recommend for the company?
5. Create a presentation to show what you did. Make your results accessible for a broad audience so that they can use it.


***


## Challenge 2:  Sales Analyst Restaurant

### Background information

You are newly hired as a data analyst to deliverando (food delivery service). The company is
successfully growing. But because of the newly opened delivery companies in the city Graz, the
competition in the field is becoming huge. The strategy team has requested a competitor
analysis which would help to create an accurate roadmap for growth optimization.

### Data

{{% attachments title="Related files" pattern="sales_analyst" /%}}

You received a list of 2 files, which are:
1. Internal data set with the columns: name, zip, kpi, Month 1, Month2 and delivery service
2. Competition dataset with the columns: name, zip, orders, month, and delivery service

NOTE: the excel file of the competition data has 2 sheets (Month 1 and Month 2)

#### Glossary:
**KPIs**

- % Kill rate - the percentage of customers who did not order again on the platform after placing an order with the restaurant.
- Positive comment - number of reviews with positive comments
- Negative comment - number of reviews with negative comments
- Avg time to accept (s) - the average time (in seconds) to accept an order
- Graz Relevant zip codes 8010, 8020, 8036, 8041, 8042, 8043, 8045, 8051, 8052, 8053,
8054, 8055, 8063, 8077
- Commissionable Orders - the orders that deliverando earns commissions
- Avg Basket Size €- the number of products a customer buys per single transaction. This
is calculated as the total number of units sold divided by total transactions

### Tasks

Create an analysis for the city Graz and answer following questions:

1. How many restaurants are active on deliverando or our competitors in the given months (>0 orders per month)?
    - How much have the respective platforms grown?
2. How many restaurants are exclusively online with our competitors and not available on deliverando?
3. Which restaurants have placed the most orders with our competitors (top 10)?
    - Are these restaurants also active on deliverando and if so, how did the orders on the deliverando platform compare to the performance on the competitor platform?
4. What conclusions regarding other KPIs can you draw from the performance of the top restaurants on deliverando?
5. Based on your analysis:
    - Which recommendations would you make to the sales or account management team?
6. Create a presentation to show what you did. Make your results accessible for a broad
audience so that they can use it.


***


## Challenge 3:  NGO Happiness Analysis

### Background information
You are working as a researcher at the NGO ‘Equal Opportunity for Everyone (EOE)’. As EOE,
within the scope of your advocacy-based project, which aims to take fundamental steps in the
field of equal opportunity around the world, you are planning to prepare a report for the United
Nations 20 March International Day of Happiness. In this report you want to highlight how
different political/social and economic circumstances affect the happiness score of the
population of countries. You have been commissioned to do this analysis. They give you a list of
csv-files which contain different information about the countries.


### Data

{{% attachments title="Related files" pattern="happiness_analysis" /%}}

You received a list of 8 csv-files, which are:

1. Happiness score (from the Happiness world report)[`0` to `100`] 
2. Average daily income [`$` american dollars]
3. Country-Continent info
4. Democracy Index [`0` to `100`]
5. Index of functioning goverment (EIU) [`0` to `100`]
6. Income Inequlity= [Gini coefficient from `0` to `100:= complete inequality`]
7. Population [`#` of people]
8. Women participation in parliament [`%`]


### Tasks

Create an analysis for the International Day of Happiness and answer following questions:

- How is the distribution of the Happiness score across:
    - countries?
    - continents?
- How has happiness changed through the years?
- Which other variables correlate with the happiness score?
- Are there other interesting patterns in the other variables?
- Create a presentation to show what you did. Make your results accessible for a broad
audience (other NGO’s, political organizations, media etc) so that they can use it
