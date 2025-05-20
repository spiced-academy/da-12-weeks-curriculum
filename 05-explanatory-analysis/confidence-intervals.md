---
title: "Confidence Intervals"
weight: 50
---

![planche_de_galton](/images/Planche_de_Galton.jpg)

{{< credits >}}
The bean machine, a device invented by Francis Galton <a href="https://en.wikipedia.org/wiki/Normal_distribution#/media/File:Planche_de_Galton.jpg">Source</a>
{{< /credits >}}


## Key Concepts


concept   |  description
---          |---
`confidence intervals (CI)`       |     a range of values you expect your estimate to fall between
`confidence level`	| 	explains how sure we are about our estimation, usually 90%, 95% or 99%
`bootstrapping`		| 		a statistical procedure using random sampling with replacement
`Central Limit Theorem (CLT)`	| 	states that when independent random variables are summed up, their properly normalized sum tends toward a normal distribution
`z value`	| 	also called `z score` or `standard score`; the number of standard deviations by which the value of a raw score is above or below the mean value of what is being observed or measured  

## Confidence Intervals

Confidence Intervals are used to describe a population characteristic with a given percentage of certainty. It's a range of estimates for an uknown parameter.

## Calculating Confidence Intervals

Calculating confidence intervals of a population parameter can be done using several methods. We will focus here on two methods that are most commonly used:

1. Bootstrapping (simulation)
2. Statistical formulas

### Bootstrapping

![bootstrapping](/images/bootstrapping.png)

{{< credits >}}
An example of bootstrap sampling. <a href="https://www.researchgate.net/figure/An-example-of-bootstrap-sampling-Since-objects-are-subsampled-with-replacement-some_fig2_322179244">Source</a>
{{< /credits >}}

Bootstrapping is a statistical procedure that resamples a single dataset to create many simulated samples.  The dataset is sampled with replacement. This means that each time an item is selected from the original dataset, it is not removed, allowing that item to possibly be selected again for the sample. 

To calculate the confidence interval of a population parameter with a confidence level $ {\alpha} $ such as the population mean, we carry out the steps written in the following pesudocode:

```python
import pandas as pd

sample_means = []

for i in range(n_bootstaps):
	sample = select_sample_with_replacement(data)
	sample_mean = calculate_mean(sample)
	sample_means.append(sample_mean)
    
alpha = 0.95 # chosen confidence level
lower_quantile = (1-alpha)/2
upper_quantile = alpha +((1-alpha)/2)

sample_means = pd.Series(sample_means) # convert to pandas series for use of pandas methods

lower_limit = sample_means.quantile(lower_quantile)
upper_limit = sample_means.quantile(upper_quantile)

```

### Statistical Formula

Another method to calculate the confidence interval of the population mean from a sample is to use the following formula:

$$  CI = \bar{x} \pm z_{c}\frac{\sigma}{\sqrt{n}} $$

where $ \bar{x} $ is the sample mean, $ z_{c} $ is the Z value for the confidence level we require, $ \sigma $ is the sample standard deviation and $ n $ is the size of our sample. The second term of the equation is also called the **standard error**.

This equation is build on the **Central Limit Theorem**, which states that the distribution of sample means approximates a **Normal Distribution** as the sample size $ n $ gets larger, regardless of distribution of the original population. Sample sizes equal to or greater than 30 are often considered sufficient for the CLT to hold.

The value of $ z_{c} $ can be determined from the table below:

![confidence_intervals](/images/confidence_interval.png)

{{< credits >}}
Confidence levels and corresponding critical values (z-values). <a href="https://www.researchgate.net/figure/Showing-confidence-level-and-Critical-Values-z-value_tbl1_317567323">Source</a>
{{< /credits >}}

Notice that the width of the confidence intervals depends on two variables:

1. The sample standard deviation $\sigma $, which is our estimate of the degree of variation in the population. The higher the value of $\sigma $, the wider the confidence interval.

2. The size of the sample $ n $. The larger our sample is, the smaller the confidence interval is. Theoretically, if we have an infinite number of samples, our confidence interval shrink to be exactly equal the population mean! 


## Challenges



{{% notice challenge "Confidence Intervals" %}}

For the muesli order data set, calculate the 95% confidence intervals for the mean of the profit feature using bootstrapping. Create a notebook in which following questions shall be solved:

1. Initialize empty list called `sample_means`
2. Create a `for loop` that will loop 10,000 times
3. In each iteration using the pandas method `.sample()` sample 100 profits with replacement
4. Also in that same iteration take the mean of these 100 samples and then append it to the `sample_means` list
5. Using `sns.displot` plot the distribution of the `sample_means` list
6. Convert `sample_means` list to **pandas** `Series` 
7. Using pandas `.quantile()` calculate the upper (0.975) and lower (0.025) limits of the confidence interval of the `sample_means` Series 

**Bonus** 

8. Calculate using the `z-value` formula
9. Compare to the results of the bootstrapping method

{{% /notice %}}

## Additional Resources

{{% notice reading "Reading" %}}

- [Understanding confidence intervals ](https://www.scribbr.com/statistics/confidence-interval/#:~:text=A%20confidence%20interval%20is%20the,another%20way%20to%20describe%20probability.)

- [Bootstrapping Statistics. What it is and why it’s used](https://towardsdatascience.com/bootstrapping-statistics-what-it-is-and-why-its-used-e2fa29577307)

{{% /notice %}}

<br>

{{% notice copyright "Dina Deifallah, Kristian Rother, Agnieszka Kaczmarczyk" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}