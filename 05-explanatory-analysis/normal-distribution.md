---
title: "Normal Distribution"
weight: 30
---

![gaussian distribution on mark](/images/gauss_deutschemark.jpeg)

{{< credits >}}
A ten Deutsche mark note featuring Gauss and the Gaussian distribution. <a href="https://en.wikipedia.org/wiki/File:10_DM_Serie4_Vorderseite.jpg">Source</a>
{{< /credits >}}

{{% notice warmup "Descriptive Statistics vs. Inferential Statistics" %}}

1. In a new notebook, import the penguins dataset and explore it

```python
import seaborn as sns
penguins = sns.load_dataset("penguins")
```
2. Subset the dataset to extract only the `Gentoo` species
3. Calculate three descriptive statistics of the data
4. Plot a histogram of one of the columns in the data

{{% /notice %}}



## Key Concepts


concept   |  description
---          |---
`descriptive statistics`       |     summarising the basic features of a collected dataset, such as its central tendency (e.g. mean, median, mode) and its variability (e.g. range, variance and standard deviation), to better understand it
`inferential statistics`       |     using sample data to draw conclusions about the features of the larger population and using probability to quantify how confident we are about those conclusions
`random variable`    |     a quantity or object which depends on random events. It can take discrete or continuous values
`discrete variable`		| a variable that can take one of very well defined set of values
`continuous variable`	| a variable that can take any of the values within a specified range
`probability mass function`      |     for discrete random variables (e.g. dice throw), it is a function that gives the probability that the random variable is exactly equal to some value
`probability density function`    |     for a continuous random variable, it is a function that gives the probability that the value of the random variable falls in a given range
`cumulative distribution function`		|	a function that for each value x returns the probability that the realization of the random variable X is smaller than or equal to the value x


## Inferential Statistics

![Population, sample and inference](/images/descriptive_stats.png)

The goal of inferential statistics is to draw probabilistic conclusions about what we might expect if we collected the same data again, i.e. we want to draw more general conclusions from a limited number of observations or a small **sample** of a larger pool of data, i.e. the **population**.

For example, if we consider the iris dataset, which contains the sepal and petal dimensions in cm of three Iris flower species, where for each species, 50 flowers were examined and their data recorded. For each species in this example:

- the **sample** consists of the 50 flowers in the data
- The **population** can be all the flowers of that species growing in the world or the specific region were the flowers were collected for this dataset

Note that taking different samples from the same population will result in different sample statistics. This is called **sampling error** or variation due to sampling. 

There are two main areas of inferential statistics:

1. **Estimating parameters**: This means taking a statistic from your sample data (for example the **sample mean**) and using it to say something about a population parameter (i.e. the **population mean**). Practically speaking, we can never truly know the value of the population parameter, since we do not have access to all the data of the entire population. However, we can use a sample of the population to calculate a **confidence interval**, which is a range of values that is likely to include a population parameter with a certain **confidence level** (usually 95%).  In other words, confidence interval is simply a way to measure how well your sample represents the population you are studying.

2. **Hypothesis tests**: This is where you can use sample data to answer research questions. For example, you might be interested in knowing if a new cancer drug is effective. Or we might want to know, given the samples we have in the iris data set, whether the mean sepal length of one species is actually different (greater than or smaller than) from the mean sepal length of another species. We will cover it more in the A/B testing lesson.


## Central Limit Theorem


The Central Limit Theorem (CLT) is a fundamental concept in statistics that helps us understand how the averages of many random samples from a population tend to behave.

In simple terms, the Central Limit Theorem says that no matter what the original population looks like, if we take a bunch of random samples from that population and calculate the average of each sample, those sample averages will tend to form a bell-shaped curve, known as a normal distribution.

[![Central Limit Theorem](https://img.youtube.com/vi/YAlJCEDH2uY/0.jpg)](https://www.youtube.com/watch?v=YAlJCEDH2uY)


<div style="text-align: center;">
   Central Limit Theorem  Video by StatQuest
</div>




## Normal Distribution

![normal_distribution](/images/normal_distribution.png)

{{< credits >}}
Normal distribution of a mean 0 and standard deviation of 1. <a href="https://medium.com/swlh/a-simple-refresher-on-confidence-intervals-1e29a8580697">Source</a>
{{< /credits >}}




The **probability density function** or **pdf** of a normal distribution can be written as follows:

$$ f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{(-\frac{1}{2}(\frac{x-\mu}{\sigma})^2)} $$

The Normal Distribution is characterized by its mean $ \mu $ and its standard deviation $ \sigma $.

It is the most widely used distribution in Data Science. That is largely due to the Central Limit Theorem.


[![Normal Distribution](https://img.youtube.com/vi/rzFX5NWojp0/0.jpg)](https://www.youtube.com/watch?v=rzFX5NWojp0)


<div style="text-align: center;">
   Normal Distribution Video by StatQuest
</div>

<br>


## Law of Large Numbers

The Law of Large Numbers (LLN) is a fundamental principle in probability and statistics that describes the behavior of sample averages as the sample size increases. In simple terms, it states that as you take more and more observations or samples from a population, the average of those observations or sample means will tend to get closer and closer to the population's true mean.

It is also a key factor in understanding the Central Limit Theorem, which explains the behavior of sample means from any population, regardless of its original distribution, when the sample size is sufficiently large.

{{% notice challenge "Muesli Distribution" %}}

Create a notebook that is solving following questions:

1. Filter muesli order data for one month
2. Using sns.displot() plot the distribution of the quantity during that month (Try setting the parameter kde=True). More info on this plotting function here: [displot](https://seaborn.pydata.org/generated/seaborn.displot.html)
3. Filter muesli order data for the year 2017 and Los Angeles city
4. Again using sns.displot() plot the distribution of the discount for the Los Angeles and year 2017.
{{% /notice %}}



## Additional Resources

{{% notice reading "Reading" %}}

- [Why do we use probability distributions and why do they matter?](https://towardsdatascience.com/before-probability-distributions-d8a2f36b1cb#:~:text=Probability%20distributions%20help%20to%20model,the%20probability%20of%20an%20event.)
- [Random Variables explained](https://www.mathsisfun.com/data/random-variables.html)


{{% /notice %}}


<br>

{{% notice copyright "Dina Deifallah, Kristian Rother, Agnieszka Kaczmarczyk, Sara Maras, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}




