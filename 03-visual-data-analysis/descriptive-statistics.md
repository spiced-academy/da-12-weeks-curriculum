---
title: "Descriptive Statistics"
weight: 30
---
 
![Population, sample and inference](/images/descriptive_stats.png)

{{% notice warmup "What do you think of the following statement?" %}}

At the University of North Carolina, geography students have the highest 
average starting salary (above *100000 USD*).

{{% /notice %}}

## Key Concepts

*Descriptive statistics* aims to describe a given data set visually and 
through metrics. There is no uncertainty in descriptive statistics! It is a 
crucial step in every exploratory analysis as we get a better feeling for the 
data, its characteristics and relationships.

In statistics, a *random variable* represents the input or output data of a 
statistical model. A variable can be described by a probability distribution 
function that assigns a probability to each possible outcome. [Probability distributions]({{< ref "probability-distributions" >}}) will be discussed in more detail in week 4.

In practice, each column of a data frame can be regarded as the observed values of an underlying random variable.

command  |  description
---|---|
`df['column'].mean()`      |     calculates arithmetic mean of a column
`df['column'].median()`      |      	calculates median of a column
`df['column'].var()`      |     calculates variance of a column
`df['column'].min()`       |     calculates the minimum of a column
`df['column'].max()`       |     calculates the maximum of a column
`df['column'].quantile()`       |     calculates quantiles of a column
`df['column'].value_counts()`       |     create a (relative) frequency tables for a column
`df['column'].corr()`       |      	calculates correlation between two columns
`df['column'].describe()`       |     calculates various descriptive statistics for each column



## Level of Measurement 

The most important metrics of descriptive statistics deal with measures of central tendency/location and measures of dispersion/variablity. Before having a look at those measures, please review how variables of interest can be classified - Why? Because the measures of central tendency and dispersion partly depend on the nature of the variable.

In [Introduction to Pandas - Level of Measurement]({{< ref "pandas#level-of-measurement" >}}) variables were broken down into three types **categorical**, **ordinal** and **metric**.  Knowledge of these will be invaluable in the following lesson. 


## Measures of Central Tendency

These statistics try to describe the “average” or typical observation. In the following examples, $n$ is the number of observations (e.g. 200 participants of a study) and $x_i$ is the value of a single observation.

### Mean (for numeric variables)

- Arithmetic Mean:  the sum of a collection of numbers divided by the count of numbers in the collection.

$$\bar{x} = \frac{\sum_{i=1}^n x_i}{n}$$

- Weighted Arithmetic Mean: similar to an ordinary arithmetic mean, except that instead of each of the data points contributing equally to the final average, some data points contribute more than others.

$$\frac{w_1 * x_1 + ... + w_n * x_n}{n}$$


### Median and Quantiles (for ordinal or metric variables)

- Median $x_{0.5}$ - 
The value that divides the sample into two groups of the same size. That means the probability of observing a value larger than the median and the probability of observing a value smaller than the median in the sample are 50% each.

- Quantile $x_p$ - 
The value that divides the sample into two groups of size $pn$ and $(1−p)n$, where $p$ is a value between 0 and 1. The median can be described as the 0.5-quantile: $x_{0.5}$.

### Mode (for ordinal or categorical variables)

The mode of a distribution is the value that occurs most often in the sample.

### Minimum and Maximum (for ordinal or metric variables)

- $min(x)$

The minimum is the smallest value in the sample.

- $max(x)$

The maximum is the largest value in the sample.

## Measures of Dispersion

These group of statistics try to measure the degree of variability in the data, i.e. how much the data fluctuates. It’s important to think about variability, because it’s much more difficult to accurately predict the value of a new observation when the dispersion is large.

### Variance (for metric variables)

Variance is a measure of dispersion, meaning it is a measure of how far a set of numbers is spread out from their average value. In mathematical terms it measures the average squared deviation from the average:

$$var = sd_x^2 = \frac{\sum_{n=1}^n (x_i - \bar{x})^2}{n-1}$$

However we usually report using the Standard Deviation since the units are the same as the given data:

$$sd_x = \sqrt{sd_x^2}$$

When we want to compare the standard deviation across different variables with different scales, we have to normalize it. This measure is called the coefficient of variation:

$$c_x = \frac{sd_x}{\bar{x}}$$

### Other measures of dispersion

- MAD (Median Absolute Deviation)

$$MAD_x = Median(|x_i - \bar{x}|)$$

- Range

$$R_x = max(x) - min(x)$$

- IQR (Inter Quartile Range)

$$IQR_x = x_{0.75}-x_{0.25}$$


## Frequency Tables (for categorical and nominal variables)

Because categorical or nominal variables have a finite number of categories, we 
can describe their empirical distribution with frequency tables. For each 
possible value of the variable we count the number of observations with this value.

```python
x = pd.Series(['blue', 'red', 'red', 'green', 'blue', 'blue'])
x.value_counts(normalize=True)
```

returns 

```txt
blue     0.500000
red      0.333333
green    0.166667
dtype: float64
```

By dividing everything by the total number of observations (`normalize=True`) 
we get relative frequencies. A relative frequency for a value is an estimator 
for the probability that a randomly chosen observation from our sample has this value.

For *numeric* variables you often use histograms to describe their empirical 
distribution. By this the numeric data is first bucketed into categories (hence, 
making it a categorical variable) and then visualized with a barplot.

## Descriptive statistics for two variables

Often we are not only interested in describing the distribution of a single variable but describing the joint distribution of two (or more) variables: Are two variables independent from each other? For a single observation, how does the value of one variable change if one changes the value of another variable?

![correlation plots](/images/correlation.png)

Pearson’s correlation coefficient describes the strength of the linear relationship between two variables. The coefficient is close to `1` if large positive values of one variable correspond to large positive values of the other. The coefficient is close to `-1` if large positive values of one variable correspond to large negative values of the other.

We can compute the pairwise correlation between all columns in a data frame with pandas.DataFrame.corr() or only between two columns with pandas.Series.corr().


## Exercise: Penguins Data

### Task 1

Read in the Penguins Dataset with pandas.

{{% attachments title="Related files" pattern="penguins_simple" /%}}


### Task 2

Go through each column and determine its level of measurement and `dtype`

### Task 3

Find out how to calculate some of the above statistics in pandas

### Task 4

Post one statistical observation about the penguins to the slack channel.


## Project Challenges


{{% notice challenge "PandasDescriptive Statistics Challenges" %}}

Solve the following pandas challenges:

```python
# 1. read the life expectancy cleaned dataset into your notebook (the dataset you created in Data Cleansing before). If you want to use country as the index you may use the `index_col` parameter while reading it from the file:

life_df = pd.read_csv('life_expectancy_cleaned.csv', index_col=0)

# 2. calculate the mean life expectancy
...

# 3. calculate the mean life expectancy for the year 2000
...

# 4. calculate the median for 1995
...

# 5. calculate the standard deviation
...

# 6. find the highest life expectancy
...

# 7. find the country and year for the highest life expectancy
...

# 8. find the lowest life expectancy
...

# 9. find the country and year was the lowest life expectancy
...

# 10. find the 90% quantile of the life expectancy
...

# 11. calculate min, max, mean and possibly other descriptors with a single line

```
{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}