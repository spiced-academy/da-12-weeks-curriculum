---
title: "A/B Testing 1"
weight: 70
---

![ab_testing](/images/ab_testing.png)
{{< credits >}}
Illustration by Isak Kabir on <a href="https://towardsdatascience.com/how-to-conduct-a-b-testing-3076074a8458">medium</a>
{{< /credits >}}

## Key Concepts


concept   |  description
---          |---
`A/B testing`       |   method of comparing two (or more) versions of a feature or product by showing them to different groups of users and assessing which version performed better based on a metric (e.g. CTR, conversions, etc.)
`hypothesis testing`       |   method of statistical inference used to decide whether the data at hand sufficiently support a particular hypothesis 
`null hypothesis`      |  the hypothesis that the true means of two groups are equal   
`alternative hypothesis`    |   the hypothesis that the true means of two groups are different  
`significance level`      |   probability of rejecting the null hypothesis when in fact it is correct
`p-value`   |   probability saying how likely it is that your data could have occured assuming that the null hypothesis is true
`test power`        |    probability of rejecting the null hypothesis when in fact it is false 


  

## Hypothesis Testing 

Hypothesis testing is a group of statistical inference tests used to decide whether the data at hand sufficiently support a particular hypothesis. When we conduct A/B tests our objective is to decide, based on samples taken from two different groups (i.e. populations), whether the two groups are different or not. Hypothesis testing usually consist of these elements:

### Hypotheses

In hypothesis testing, we have two opposing theories about our data, called **hypotheses**. These hypotheses are:

- Null Hypothesis $ H_{0} $: two metrics representing given two groups are equal. For example, the mean CTRs (click through rates) of the two ads A and B are equal, i.e. they do not perform differently
- Alternative Hypothesis $ H_{1} $: two metrics of the two groups are unequal. For example, the mean CTR of ad B is higher than the mean CTR of ad A, i.e. ad B is performing better

### Choosing the parameters

There are multiple parameters that should be chosen before we start running an experiment. Depeneding on the type of the test statistics we decide for, the set of parameters we need to think about may vary. Let's start with the ones that always appear:

#### Minimum Effect of Interest

The **Minimum Effect of Interest (MEI)** is the difference in results you want to detect (the minimum difference which makes two samples truly different from each other, and it may be understood as a target we want to reach). Smaller differences are harder to detect. If the difference between our variants doesn't reach MEI, we know, for example, that the new variant is not performing better than the base variant.

#### One-tailed vs two-tailed tests
On top of choosing the right statistics for your test we should also decide if the test will be one or two tailed.

One-tailed tests form the hypothesis in a way that the direction of the difference between the tested groups is important, while in a two-tailed tests this direction doesn't matter. To give an example, testing if a variant B performance is better (higher) than the variant A performance will be denoted as one-tailed test. On the contrary, if we just want to know if the variants are different (it doesn't matter if the metric of variant B is significantly higher **or** lower) it will be a two-tailed test. The decision either a test is one-tailed or two-tailed will influence analyzing the resulted p-value.

#### Parameters connected with errors

![testing_errors](/images/testing_errors.png)
{{< credits >}}
Research Gate error types illustration <a href="https://www.researchgate.net/figure/Graphical-representation-of-type-1-and-type-2-errors_fig1_268035363">medium</a>
{{< /credits >}}

**Power level** ($1-\beta$) refers to Type-II Error and it's about the probability of deciding against the variant whereas in reality the variant is better than the current version. Usually set to 80%.

**Significance level ($\alpha$)** refers to Type-I Error and it determines the probability that we are implementing a variant whereas in reality it is not better than the control version. The most common values for significance level are 90, 95 or 99%. Significance level is the threshold for the p-value. $1-\alpha$ will be called a confidence level.

#### P-value

**P-value** is the probability of an observed result assuming that the null hypothesis is true. P-value will be checked against a chosen threshold to ensure the significance of our A/B test. We usually choose p-value thresholds $\alpha$ of 10%, 5%, 1% for our hypothesis testing, whereas the most popular one is 5%. In short words, we want to have p-value as low as possible in order to reject the null hypothesis.


### Calculation of the p-value and concluding your test

The conclusion we make depends on the chosen parameters and the resulting p-value:

1. if p-value >= $\alpha$, then we **fail to reject** $ H_{0} $ and conclude that there is no difference between the metrics
2. if p-value < $\alpha$, then we **reject** $ H_{0} $ and conclude that the groups are indeed different. A very small p-value means that such an extreme observed outcome would be unlikely under the null hypothesis


### Helper tools for A/B testing

#### Online calculators
There is a number of online tools that are there to help you with your A/B testing analysis. As we do use different test statistics, make sure you use the one that is serving your needs (more on that in the next topic). 


**Comparing conversion rates**
In the marketing world, most of the times we compare metrics similar to conversion rates. Most suitable test statistics for this use case are z-test and chi$^2$-test. There are also multiple helper tools including online calculators like this one: [z-test online calculator](https://abtestguide.com/calc/)


{{% notice question "Parameters changes in an A/B test comparing conversion rates" %}}

  
-  How is the test **p-value** and the result of the test affected by (*hint*: use this [online calculator](https://abtestguide.com/calc/) to help you):
  1. the difference between the conversion rates for the two groups
  2. the fact if the test is one or two sided
  3. the size of the samples
  4. chosen confidence
  
{{% /notice %}}

## Challenge

{{% notice challenge "A/B Testing" %}}

Let's think about the Muesli Dataset. What do you think could be A/B tested here and why? Consider the features that you already have in the dataset but feel free to also suggest to track new data. Discuss it in the groups and present your ideas to the whole cohort. 

{{% /notice %}}


## Additional Resources

{{% notice reading "Reading" %}}

- [Hypothesis testing: step by step](https://www.youtube.com/watch?v=0zZYBALbZgg&t=82s)
- [Statistical Power explained](https://cxl.com/blog/statistical-power/)
- [Guide to statistical testing](https://towardsdatascience.com/a-b-testing-a-complete-guide-to-statistical-testing-e3f1db140499)
- [T-test explained for beginners](https://towardsdatascience.com/the-statistical-analysis-t-test-explained-for-beginners-and-experts-fd0e358bbb62)
- [more about p-values from StatQuest](https://www.youtube.com/watch?v=vemZtEM63GY&t=12s&ab_channel=StatQuestwithJoshStarmer)

{{% /notice %}}

<br>

{{% notice copyright "Dina Deifallah, Agnieszka Kaczmarczyk" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}