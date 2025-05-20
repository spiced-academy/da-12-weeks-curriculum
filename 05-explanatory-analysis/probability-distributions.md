---
title: "Probability Distributions"
weight: 40
---

--------------------------


![Statistical_dist](/images/stats_dist.jpg)


--------------------------




### What is a Random Variable ?

A variable whose value is determined by a random process. It's a set of possible values from a random experiment.

![random-variable](/images/random_variable.png)
{{< credits >}}
Random variable <a href="https://www.mathsisfun.com/data/random-variables.html">Source</a>
{{< /credits >}}

It could represent an outcome of a single experiment (e.g. one coin toss) or an overall outcome of a set of experiments (e.g. multiple coin tosses).

## Probability Distributions

A probability distribution is a mathematical function or model that describes the likelihood of different outcomes or events in a random or uncertain process. In other words, it provides a way to assign probabilities to various possible outcomes of a random variable. Probability distributions are fundamental concepts in statistics and probability theory and are used to characterize and analyze random phenomena in various fields, including science, engineering, economics, and social sciences.

[![The Main Ideas Behind Probability Distributions](https://img.youtube.com/vi/oI3hZJqXJuc/0.jpg)](https://www.youtube.com/watch?v=oI3hZJqXJuc)


<div style="text-align: center;">
   Probability Distributions Video by StatQuest
</div>

<br>




## Types of Probability Functions 

Probability distributions are often represented using probability mass functions (PMFs) for discrete distributions or probability density functions (PDFs) for continuous distributions.


#### Probability Mass Function

Probability mass function (pmf) deals with **discrete variables**:

$$ f(x) = P(X = x) $$

Given a random variable X, the probability mass function is defined as a function that for each value x returns the probability that the realization of the random variable X is equal to the value x.

#### Probability Density Function

Probability density function (pdf) deals with **continous variables**:

$$ f([a, b]) = P(a \leqslant X \leqslant b) $$

Given a random variable X, the probability densitiy function (pdf) is defined as a function for which the area under the curve for each interval [a, b] returns the probability that the realization of the random variable X is within the intervall [a, b].

#### Cumulative Distribution Function

It gives the cumulative probability up to a specific point on the distribution.
The CDF is defined for both discrete and continuous random variables.
In the case of discrete random variables, the CDF is constructed by summing the probabilities up to a particular value.

$$ f(x) = P(X \leqslant x) $$

It gives the cumulative probability up to a specific point on the distribution.
The CDF is defined for both discrete and continuous random variables.
In the case of discrete random variables, the CDF is constructed by summing the probabilities up to a particular value.



## Types of Probability Distributions


#### Bernoulli Distribution

A Bernoulli distribution describes the outcome of a Bernoulli trial, which is simply an experiment that has two options, "success" (True) and "failure" (False). The Bernoulli distribution has only a single parameter $ p $, which is defined as the probability of "success". 

The **probability mass function** or pmf of the Bernoulli distribution can be expressed as:

$$ f(k) = p^{k}(1-p)^{1-k} $$

where $ k = 0, 1 $, with $ k = 1 $ corresponding to a "success".

An example of a Bernoulli trial is the flipping of a coin, with the event of getting a head interpreted as a success. 

![bernoulli pmf](/images/bernoulli.png)

We can simulate a coin flip in python using the numpy random module:

```python

import numpy as np

np.random.seed(42)
random_numbers = np.random.random(size=10)
heads = random_numbers > 0.5
print(f"Outcomes of 10 fair coin flips: {heads}")
print(f"Number of heads= {np.sum(heads)}")
```

#### Binomial Distribution

The Binomial distribution is the probability distribution for the number of successes in a sequence of Bernoulli trials. It has two parameters: $ p $, which is the probability of success and $ n $ which is the number of of the trials.

The pmf of the Binomial distribution is:

$$ f(k) = {n\choose k}p^{k}(1-p)^{n-k} $$

where $ k $ can take the values $ 0,1,2,...n $

An example of the Binomial distribution can be the number of tails we get when we repeatedly toss a fair coin for $ n $ times.

![binomial](/images/binomial.png)


#### Uniform Distribution

Uniform Distribution is a discrete distribution where every possible value has the same probability of appearance. The Discrete Uniform Distribution is characterized by its lower bound, a, and its upper bound, b. All values in the range are equally likely to occur. The pmf of the Discrete Uniform Distribution is:

$$ f(x) = \frac{1}{n} $$

Uniform Distribution is a great help if you want to come up with a list of random points within a range. In python you could use: ```np.random.uniform()``` function to generate such a set of points.

![uniform_distribution](/images/uniform_distribution.png)

#### Poisson Distribution

$$ f(x) = (λ^k * e^(-λ)) / k!$$ 


The Poisson Distribution is characterized by the rate lambda λ.

It is used to model the number of occurences of an event in one timestep.

![poisson_dist](/images/poisson.png)




#### Normal Distribution

The **probability density function** or **pdf** of a normal distribution can be written as follows:

$$ f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{(-\frac{1}{2}(\frac{x-\mu}{\sigma})^2)} $$

The Normal Distribution is characterized by its mean $ \mu $ and its standard deviation $ \sigma $.

It is the most widely used distribution in Data Science. That is largely due to the Central Limit Theorem.

![normal_distribution](/images/normal_distribution.png)

{{< credits >}}
Normal distribution of a mean 0 and standard deviation of 1. <a href="https://medium.com/swlh/a-simple-refresher-on-confidence-intervals-1e29a8580697">Source</a>
{{< /credits >}}





{{% notice challenge "Coin Flips" %}}

1. Simulate a fair coin flip for 10 times and calculate the estimated probability of getting a head (number of times you got a head divided by 10). Repeat for 100, 1000 and 10000 times. How does the estimated probability changes ? How can we interpret that ?
2. Plot the pmf of the Binomial distribution of $ n = 10 $ and $ p = 0.5 $. (*hint*: start by sampling from the distribution for 100_000 times)
3. Research other commonly used probability distributions and the random real life processes and events they are used to model.

{{% /notice %}}


{{% notice challenge "Analyzing Exam Scores with the Normal Distribution" %}}

You are given a list of exam scores representing students' performance in a class. Solve the following tasks to analyze the distribution of these scores using normal distribution concepts. The list of exam scores is:
```python
exam_score =  [85, 90, 78, 92, 88, 95, 70, 60, 82, 75, 80, 98, 88, 91, 83, 77, 89, 94, 86, 72]
```
1. Calculate the mean and standard deviation of the scores.


**Hint:** Use the numpy `mean` and `std` functions.


2. Plot the distribution of the score as a histogram.


3. Plot the normal distribution curve of the scores.


**Hint:** To visualize the normal distribution curve, you can use the `norm.pdf` function from `scipy.stats` (more details [here](https://www.mathsisfun.com/data/random-variables.html)) You will need to specify the mean and standard deviation calculated in Task 1 and create spaced numbers over the range of the scores which can be done using:

```python
x_range = np.linspace(min(exam_scores), max(exam_scores), 100)

```


4. Calculate the percentage of students who scored above a certain threshold score (for example above 80)


**Hint**: In this case, you can use `norm.cdf` from `scipy.stats`

(more details [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)) as the following:

``` python
percentage_above_threshold = (1 - norm.cdf(threshold_score, mean_score, std_deviation)) * 100

```

{{% /notice %}}





<br>

{{% notice copyright "Dina Deifallah, Kristian Rother, Agnieszka Kaczmarczyk, Sara Maras, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}