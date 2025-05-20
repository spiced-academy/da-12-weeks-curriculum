---
title: "Cloud Databases"
weight: 10
---

![data center](/images/data_center.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@dianamia?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">C Dustin</a> on <a href="https://unsplash.com/s/photos/cloud-computing?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}


{{% notice warmup "Data Centers" %}}

Read the following story:  [Interxion Data Center in Bunker](https://arstechnica.com/information-technology/2019/06/why-a-former-nazi-sub-base-in-marseille-is-becoming-a-data-center/)

- What is a data center?
- Why would companies use one?
- What infrastructure would you expect a data center to provide?
- What makes an old submarine bunker in Marseille a good place for a data center? 

{{% /notice %}}


## The Cloud

The cloud is a phrase often tossed around without much thought as to what it actually is. In it's most basic sense the cloud is a computer running 24 hours a day 365 days a year that users can access whenever needed for various tasks. Companies such as AWS, Google, Microsoft and many others offer cloud services for the smallest to the largest of customers. 

Google cloud offers many different cloud computing services. They are run on the same infrastructure that Google uses internally for its end-user products, such as Google Search, Gmail, Google Drive, and YouTube. Alongside a set of management tools, it provides a series of modular cloud services including computing, data storage, data analytics and machine learning.

{{% notice info "The Essentials of GCP" %}}

{{< youtube 4D3X6Xl5c_Y >}}

{{% /notice %}}

## Cloud Databases

A cloud database is a database that typically runs on a cloud computing platform (i.e. google cloud) and access to the database is provided as-a-service. Storing data in a cloud database enables authenticated users to access data remotely, from anywhere in the world, via a working internet connection.

## Database Structure

Although there are different types of ways to structure databases, *relational databases* will be focused on this week. A relational database is a digital database based on the relational model of data, as proposed by E. F. Codd in 1970. In Relational Databases data is organized in tables and sometimes we also refer to such databases as SQL databases. Rows of data could be related to other rows of data between the tables. 

Relational Databases are probably the most popular ones, but it's not the only way how the data could be organized. We can work with hierarchical, network, graph and other ones. Non-relational databases are also refered as NoSQL databases.

## Database vs Data Warehouse vs Data Lake

Database is a structure that is storing data from a single data source. However, many times we would like to combine multiple data sources together to have a greater picture of a topic. 

### Data Warehouse

Data Warehouse is used to store large amount of structured data coming from multiple sources. Because of very well defined structure, it's easy to perform reliable analytical requests. An example of a Data Warehouse could be a BI Analytics system where the data is already preprocessed (e.g. having a table that is grouped by months and products, with calculated metrics) and very easy to query.

### Data Lake 

Data Lake is used to store structured, semi-structured and unstructured data, which is not necessarily processed (keeping the data in the raw format). Such a setup creates a flexible infrastructure which enables more open questions. Only when the data is needed it will be properly tranformed.


In real world, you could also find infrastructures that are a hybrid solution between a Data Warehouse and a Data Lake.

## Exercises

1. Visit the google cloud product page: [https://cloud.google.com/products/](https://cloud.google.com/products/)
2. Pick one of the services that seems interesting and research it. 
3. Report back to the class about the product and the features, costs, documentation or anything else compelling.


## Project Challenges

{{% notice challenge "Setup Google Cloud" %}}

There are many cloud providers available. This week's project will use google-cloud. Please make an account:

- [https://cloud.google.com/](https://cloud.google.com/)

**Note:** A credit card is required to register. Each user recieves 300$ credit to start with and no charges will be made to the credit card unless approved by the user. If any problems are encountered in the account registration please contact the instructor for help and/or other options.

{{% /notice %}}


## Reading

{{% notice reading "Links" %}}

- [How to get started with Google Cloud](https://cloud.google.com/gcp/getting-started)
- [Database vs Data Warehouse vs Data Lake](https://youtu.be/-bSkREem8dM)
{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of [academis.eu/posts/spiele_DE/textadventure.md](https://www.academis.eu/posts/games_EN/textadventure.md) by Dr. Kristian Rother, used under CC-BY-SA 4.0. 

{{% /notice %}}