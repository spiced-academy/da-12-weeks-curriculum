---
title: "A/B Testing 2"
weight: 80
---

![ab_testing](/images/ab_testing_2.jpg)
{{< credits >}}
Illustration by <a href="https://unsplash.com/@jdent?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jason Dent</a> on <a href="https://unsplash.com/photos/JVD3XPqjLaQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}
  

## Key Concepts


concept   |  description
---          |---
`test statistics` | statistical test that we will use to assess our A/B test
`z-test`  |   test statistics that is using standard normal distribution
`t-test`    |    test statistics that is using Student's distribution
`scipy`       |   python module for scientific computing
  

## Test statistics
In hypothesis testing we always work with the same concept but depending on the metric we're testing and the population characteristics we might be using different test statistics.
Test statistics refer to different distribution functions and will have different assumptions about the data. Some of them are described below:

### t-test
T-test, also named Student's test, and it's used when:
- the observations are normally distributed (or the sample size is large)
- the sampling distributions have similar variances
- appropriate for comparing means

### z-test
- the sample is normally distributed
- we know the true characteristics of the populations (mean & standard deviation)
- widely used in the marketing sector for comparing conversion rates
- appropriate for comparing means

Note: if the samples are large enough, even if not all the conditions are met, we usually go for z-test instead of t-test statistics

### chi$^2$-test
- categorical values to compare

### Welch's t-test
- similar to regular t-test but doesn't hold the requirement on the similar variances

### Fisher's exact test
- used when comparing two binomial distributions such as a click-through rate

And many more...

![test_statistics](/images/test_statistics.png)
{{< credits >}}
Choosing a test statistics by Francesco Casalegno <a href="https://towardsdatascience.com/a-b-testing-a-complete-guide-to-statistical-testing-e3f1db140499">medium</a>
{{< /credits >}}

## Python packages in hypothesis testing
Besides the online calculators and other dedicated software we can also find supporting libraries in python. The two main libraries that share different hypothesis testing tools are: **statsmodels** and **scipy**. 

The examples of usage could be also found in the teaching notes notebook.

### **statsmodels**

Statsmodels is heavily statistic oriented python module including an implementation of different statistical models, statistical testing tools and others.

#### Example - A/B test comparing conversion rates

Using the `proportions_ztest` function from the `statsmodels.stats.proportions` we can compare two conversion rates. The code below presents how to perform such a test for a dataset where you have two variants and a conversion column. Note that in order to perform this kind of a test we have to make sure that we meet the conditions.

```python
from statsmodels.stats.proportion import proportions_ztest

variant_a_data = data[data['variant'] == 'A']
variant_b_data = data[data['variant'] == 'B']

successes = [variant_a_data['conversion'].sum(), variant_b_data['conversion'].sum()]
nobs = [len(variant_a_data), len(variant_b_data)]

z_stat, pval = proportions_ztest(successes, nobs=nobs)

```

### **scipy** 
Scipy package in python is about scientific and technical computing which includes implementation of different techinques used in hypothesis testing.

#### Example - A/B test comparing means of two samples

Using the `ttest_ind` function from the `stats` module in the [scipy python package](https://scipy.org/) we can for instance compare two means with an option for the samples with different variances. Note that this is an example of the t-test statistic so we have to make sure we meet the condition for this test.

The example below shows an independent two sided T-test from the stats module in the scipy package. Assume a 95% significance value, i.e. if p-value > 0.05 we can not reject the null hypothesis that e.g. different penguin species have the same bill length, but if p-value is less, we can reject the null hypothesis and conclude that the two species of data have different true means. Note that in our case we have three species of penguins in the dataset which means that if we want to perform hypothesis testing we can only do it with two species at a time.

If you imagine that you have two lists of numbers representing the observations that you have gathered for two variants - `data_a` and `data_b` - you could use the following code:

```python
test_statistic, pvalue = stats.ttest_ind(data_a, data_b)
print (test_statistic, pvalue)

```


### Online Calculators for other tests


There is a number of online tools that are there to help you with your A/B testing analysis. As we do use different test statistics, make sure you use the one that is serving your needs. This is an example of an online calculator that uses t statistics: [t-test online calculator](https://www.medcalc.org/calc/comparison_of_means.php)


{{% notice question "Parameters changes in a t-statistics test" %}}

- How is the **p-value** in a t-test affected by (*hint*: use this [online calculator](https://www.medcalc.org/calc/comparison_of_means.php) to help you)
  1. the difference between the means of the two groups
  2. the variance (or the standard deviation) of the two samples
  3. the size of the samples

{{% /notice %}}


### Collection of Samples

In this step, we set up the A/B test and collect the samples of the two groups. The amount of data that is needed to collect depends on all, the **significance level** and the **test power**, and the **MEI** we decide upon before running the A/B test. The smaller the difference between the two groups we aim to detect, the more data we need to collect. 


#### Online calculators for sample size

Similarly to the test statistics, there are also online calculators for computing sample size of datapoints that you should gether:
- [abtestguide sample size online calculator](https://abtestguide.com/abtestsize/)

{{% notice question "Parameters changes in a statistical test part 2" %}}

- How is the sample size needed for the test affected by (*hint* use this [online calculator](https://abtestguide.com/abtestsize/) to help you):
  1. relative MEI
  2. test power
  3. significance level
  How can you estimate number of weeks needed to run the experiment?  

{{% /notice %}}





## Challenge

{{% notice challenge "Optional: A/B Testing in python" %}}

**Penguins:**

Do you still remember the penguins?
Study the notebook with penguins data to get more examples about how AB testing could be used to compare two species.

{{% attachments title="Penguins notebook:" pattern="penguins" /%}}

**Visitors:**

Study a marketing example to discover which search result is performing better.

{{% attachments title="Visitors example files:" pattern="visitors" /%}}

{{% /notice %}}



<br>

{{% notice copyright "Agnieszka Kaczmarczyk" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}