---
title: "Calculated Fields and Parameters"
weight: 30
---

![calculator](/images/calculator2.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@stm_2790">Sumundu Mohottige</a> on <a href="https://unsplash.com/photos/nST4hDE7BRI">Unsplash</a>  
{{< /credits >}}

{{% notice warmup "Interactivity" %}}

Look at the visuals that we have created yesterday. Can you come up with any ideas about how to make them more interactive or customized? 

{{% /notice %}}

## Inspiration / goal
We will improve the visuals from the previous encounter to make them more interactive:

- **Sales vs Profit Discovery Dashboard preparations**
![dashboard1_drawing](/images/discovery_dashboard1_drawing.png)

- **Sales vs Profit for Categories Discovery Dashboard preparations**
![dashboard2_drawing](/images/discovery_dashboard2_drawing.png)

## Filters
[Filters](https://help.tableau.com/current/pro/desktop/en-us/filtering.htm) give you a possibility to make your visuals customized - a user can decide which part of the data they want to look at.

### Top 10
You can also limit the amount of the data visiable by showing only the most / the least ranked data using a condition.

## Calculated Fields
[Calculated fields](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_create.htm) help you to create new measures or dimensions using the data that you already have. It's like feature engineering in pandas. Calculated fields when created they will be available within the whole workbook.

{{% notice ethics "Personal Data and GDPR" %}}

Superstore dataset that we are exploring this week presents orders where for every order we know the customer name. In real world, such data should definitely not be publicly available. What is more, this data should not be available for all of the employees of the company and it's our responsibility to make sure that all the personal and sensitive data is properly protected.

Information such as name, birth date, address, gender but also the history of credit cards payments and social media behaviour are examples of sensitive data that should be well protected.

In the EU and the European Economic Area (EEA) we need to follow General Data Protection Regulation (GDPR). GDPR restricts how personal data should be used which includes:
- limitations on data processing and customer profiling
- the right to know how your data is processed (and e.g. how decision models work)
- the right to forget customer's data
- clear communication about how customers' data is being used

{{% /notice %}}


{{% notice question "Customer Name" %}}

The data in Superstore is distinguished by customer names. Do you have an idea how we could replace (anonymize) customer data so we can't identify the customer directly?

{{% /notice %}}


## Parameters
[Parameters](https://help.tableau.com/current/pro/desktop/en-us/parameters_create.htm) are another way how to customize your visuals in Tableau. They enable you to create some abstract that you could use to manipulate other measures or dimensions.


{{% notice reading "More about data protection" %}}

- [GDPR explained](https://www.youtube.com/watch?v=acijNEErf-c&list=LL&index=1&t=3s&ab_channel=Channel4News)
- [How GDPR affects Data Science](https://www.kdnuggets.com/2017/07/gdpr-affects-data-science.html)
- [Identifying people based on available data](https://archive.nytimes.com/bits.blogs.nytimes.com/2015/01/29/with-a-few-bits-of-data-researchers-identify-anonymous-people/)

{{% /notice %}}

<br>

{{% notice copyright "Agnieszka Kaczmarczyk, Katerina Arsh" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}