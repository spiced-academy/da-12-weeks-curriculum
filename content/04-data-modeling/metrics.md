---
title: "Metrics"
weight: 50
---

![International Bureau of Weights and Measures](/images/international_bureau_of_weights_and_measures.png)
{{< credits >}}
International Bureau of Weights and Measures <a href="https://en.wikipedia.org/wiki/Metre#/media/File:Metric_seal.svg">Wikipedia</a>

{{< /credits >}}

{{% notice warmup "Bias in data" %}}

{{% attachments title="Here you find a PDF with cognitive biases:" pattern="cognitive_biases" /%}}

Pick one - read the description and think about the examples of it.

You can think about the questions below:
- Do you recall situations where you saw this cognitive bias at work or your daily life?
- What cognitive biases are you aware of **right now**?
- What decisions of a Data Analysts and Scientists could be affected by cognitive bias?
- what can we do against it?

{{% /notice %}}


## Key Concepts

`Metrics` is a very wide term used in many different occassions to provide a measure for something. We usually use them for comparing and tracking purposes. Today, we will make a distinction between business metrics and error metrics, both are widely used in the data field.

concept   |  description
---          |---
**metric**      |     measures a relationship between numbers
**error metric**    |    metric used to measure the error of a  model 
**MSE**    |     Mean Square Error
**RMSE**        |     Root Mean Square Error
**MSA**     |     Mean Absolute Error
**R2**        |    R squared metric
**residuals**    |   differenece between real and estimated value
**regression analysis**  |  estimating the relationships between a dependent variable and one or more independent variables




## Metrics used in research 
Metrics is not a term that is only reserved for the business world. Metrics are widely used in forecasting/estimation models to provide the error of their performance (so we know which models are better). 



Depending on the problem we are working on there will be a different set of possible metrics we could use to evaluate the performance of our model (for example classification metrics will have different purpose from regression metrics). Also, while each metric is focusing on providing slightly different information, it's important to understand what we want to optimize for so we could choose the most suitable error metric.

As our next step will be learning about Linear Regression (which is one of the most popular regression models), let's explore some of the regression error metrics a bit more.

## Regression error metrics

Regression analysis is a process used to study sets of data in order to determine whether any relationship(s) exist. It can be thought of as a best guess at the trend that the data follows, and can be useful for making predictions about the data.

Regression error metrics will try to compare the estimations and real data points. The most popular are: MSE, RMSE, MAE, etc.


### MSE

One of the most common **loss functions** that can capture the **error** of the model is **MSE (Mean Squared Error)**:


$$ MSE = \frac{1}{N}\sum_{i=1}^{n}(\widehat{y}_i - y_i)^2 $$ 

Notice that in the MSE equation we square the difference (i.e. error) between the predicted and the actual value, since we only care about the magnitude of the error and not its sign. Some properties of MSE:
- we will penalize bigger differences between real and estimated values
- the bigger MSE is, the worse your model is performing
- MSE can't be represented by a negative number
- there is no upper range for MSE  
- you can only compare MSE for different models working on the same dataset
- the units of MSE are squared units


### RMSE
**RMSE (Root Mean Square Error)** is an extension of MSE:

$$ RMSE = \sqrt{\frac{1}{N}\sum_{i=1}^{n}(\widehat{y}_i - y_i)^2} $$ 

Properties of RMSE are very similar to MSE besides the units part - the units of RMSE are the same as the units of the value we are trying to estimate.

### MAE

Another variant is to minimize the **Mean Absolute Error**:
$\newline$
$$ 
MAE = \frac{1}{N}\sum_{i=1}^{N}|y_i-\hat{y}_i|
$$ 
$\newline$





### R2

**Coefficient of Determination**, denoted by $ R^2 $ (R squared) can be defined as follows:

$$ R^2 = 1 - \frac{SSE}{SS_{total}} $$

where

$$ SSE = \sum_{i=1}^{n}(\widehat{y}_i - y_i)^2 $$ 

$$ SS_{total} = \sum_{i=1}^{n}(\bar{y}_i - y_i)^2  $$

One can interpret this equation as a comparison of the model to the average value of the response variable: The value of $ R^2 $ has a maximum value of one. If we get an $ R^2 $ of zero, that means that the model is no better than a simple average over all points. On the other hand, if the value of $ R^2 $ is equal to one, that means that model has a loss of zero, i.e. estimates the data points perfectly or a **perfect fit**!





## Python Implementation with scikit-learn

The code snippet imports the necessary functions **mean_absolute_error** and **mean_squared_error** from the **sklearn.metrics module**. These metrics are typically used to assess the performance of a regression model by comparing the predicted values (predicted) with the actual values (ytest). In this example below, the metrics are calculated and then stored in the variables MAE, MSE, and RMSE.


```python
from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import mean_squared_error 

MAE = mean_absolute_error(
    y_true=ytest, 
    y_pred=predicted 
)
MAE.round(2)

MSE = mean_squared_error(
    y_true=ytest, 
    y_pred=predicted 
)
MSE.round(2)

# Square root of MSE gives RMSE
RMSE = MSE**(1/2)
RMSE.round(2)

```




**Note:** evaluating $r^2$ with code will be done in the linear regression lesson



## Project Challenges

{{% notice challenge "Car dataset metrics" %}}

Generally, there are various metrics that can be utilized to interpret the car dataset, offering valuable insights into different aspects of the data. The following are some of them that you can find. Explain how these can be useful after calculating them.

- All car price range
- Size based price range
- Popularity by door configuration
- Fuel efficiency by fuel type
- Engine horsepower by car size

**Bonus:** Provide additional metrics for the car dataset



{{% /notice %}}

{{% notice challenge "Regression error metrics" %}}

Take the last model that you trained as part of the linear regression challenge. Calculate the regression error metrics as follows:

- Define the `X_test` and the `y_test`
- Make predictions based on the test data
- Calculate the regression error such as `MAE`, `MSE`, and `RMSE`

**Bonus:** The predictions indicate some negative prices, which are unreasonable. What is your explanation for this? What can be done to resolve this issue? 



{{% /notice %}}


## Links

{{% notice reading "Additional Resources" %}}

- [Jason Brownlee on Regression Metrics](https://machinelearningmastery.com/regression-metrics-for-machine-learning/)
- [Understanding Data Bias](https://towardsdatascience.com/survey-d4f168791e57)

{{% /notice %}}

<br>

{{% notice copyright "Dina Deifallah, Agnieszka Kaczmarczyk, Samuel McGuire, Sara Maras, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}