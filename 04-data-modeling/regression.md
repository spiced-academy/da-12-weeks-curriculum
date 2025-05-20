---
title: "Linear Regression"
weight: 30
---

![linear_regression_architecture](/images/linear_regression.jpg)
{{< credits >}}
Photo by StockSnap on <a href="https://pixabay.com/photos/architecture-bridges-suspension-2609343/">Pixabay</a>

{{< /credits >}}

{{% notice warmup "Datasaurus datasets" %}}

1. Read the Datasaurus dataset:

{{% attachments title="Download the data:" pattern="datasaurus" /%}}

2. Calculate a few descriptive statistics for each of the datasets (mean, standard deviation, correlation)

3. Plot the data for every dataset

Read more about the Datasaurus from [Alberto Cairo](http://www.thefunctionalart.com/2016/08/download-datasaurus-never-trust-summary.html).


{{% /notice %}}

## Key Concepts

Linear Regression is a statistical method for modelling the relationship between a scalar response (a.k.a *dependent variable*) and one or more explanatory variables (a.k.a *independent variables* or *features*)

![linear_regression_plot](/images/linear_regression_plot.png)


concept   |  description
---          |---
`dependent variable`       |     the variable that we are trying to understand and predict
`independent variable`    |     the variables influencing the dependent variable
`OLS`      |     Ordinary Least Squares, a method used to estimate the parameters for Linear Regression
`MSE`        |     Mean Square Error
`R2`     | R squared metric
`coefficient of determination`        |    a *Goodness of Fit* measure that tells us how much of the variance in the response can be explained by the features


## Linear Regression Models

### Simple Linear Regression Model

A simple Linear Regression is a straightforward model. It describes the relationship between a single feature and the response of interest. It basically fits a straight line to the data points using the following linear equation:

$$ \widehat{y} = w_0 +  w_1 x $$

where $ w_0 $ is the **intercept** (also called the bias) and $ w_1 $ is the **slope** (a.k.a the **weight** or **coefficient**) of the line.

### Multiple Linear Regression

In the case where our response is influenced by more than one feature, the linear regression model equation becomes:

$$ \widehat{y} = w_0 +  w_1 x_1 + w_2 x_2 + ... + w_n x_n  $$

where in this case, each of the $ n $ features, i.e. $ x_1, x_2, ..., x_n $, has a corresponding weight, i.e. $ w_1, w_2, ..., w_n $, in addition to the bias intercept $ w_0 $.


## Evaluation of Linear Regression Models

In order to evaluate how well our linear regression model is doing, we need to use a **loss function** that can capture the **error** of the model. One of the most widely used loss metrics is the **Mean Squared Error**.

The reason why we choose MSE here is that we only care about the magnitude of the error and not its sign. 


## Fitting a Linear Regression Model

The objective of fitting a linear regression equation to a given dataset is to find the **optimal weights** for the features/independent variables such that the MSE is minimized. This most common estimator used for linear regression is called OLS (Ordinary Least Squares). OLS method minimizes the sum of squared residuals. Using linear algebra, the analytical (a.k.a *closed form*) solution to this optimization problem can be expressed using the following equation:

$$ \boldsymbol{\widehat{w}} = (\boldsymbol{X^{T}}.\boldsymbol{X})^{-1}(\boldsymbol{X^{T}}.\boldsymbol{y})  $$

This equation is called the **Normal Equation** and it guarantees to produce the optimal weights. 

However, the computational time required to solve the normal equation grows to the power of 3 with the number of data points. Therefore for many data points and/or features, the normal equation becomes very slow. 

An alternative numerical approach, **Gradient Descent**, also finds optimal (or in some cases near optimal) weights. It starts with a random guess for the values of the weights and iteratively performs a set of steps to minimize the MSE until it reaches optimal values for the weights.


## Goodness of Fit

Once a linear regression model is fit to the data, it is important to check how well our model is explaining the data. This can be achieved by tellling how much of the variation in the response variable is actually explained by the features/independent variables. The most commonly used Goodness-of-fit statistical metric for Linear Regression is **Coefficient of Determination**, denoted by $ R^2 $.

## Linear Regression in Python

There are multiple ways how Linear Regression can be implemented in Python. Two most popular solutions include `statsmodels` and `scikit-learn` libraries. The first is usually used for regression, econometric and time series related topics and the other for gathering different Machine Learning models (very popular tool in the Data Science field).

### scikit-learn

We will be using a version of `scikit-learn` library. Start with importing it:

```from sklearn.linear_model import LinearRegression```

Then prepare your dataset in a dataframe format. Both independent variables as well as dependent variable needs to be present. The next step is preparing and and splitting the data.

After splitting the data first create the Linear Regression model .

```lin_model = mlin = LinearRegression()```

After that train the model on Xtrain and ytrain.

```lin_model.fit(Xtrain,ytrain)```


#### Getting the parameters

The Linear Regression model will give us a set of parameters: intercept and coefficients.

```print("Coefficients:", lin_model.coef_)```
```print("Intercept   :", lin_model.intercept_)```


How to interpret the parameters?

Intercept will stand for the value of the dependent variable when all the independent variables are 0.
Every other coefficient will tell you how your output will change when you change only this particular variable (while the other ones remain constant). A unit of change with this variable will result in a change equal to the value of the coefficient. 


#### Calculate the R-squared value

Lastly, in scikit-learn's Linear Regression, the score() method returns the coefficient of determination (R-squared). The R-squared value indicates how well the linear regression model fits the given data. It represents the proportion of the variance in the dependent variable that can be explained by the independent variables.


```print("train score :", lin_model.score(Xtrain, ytrain))```
```print("test score  :", lin_model.score(Xtest, ytest))```



## Project Challenges

{{% notice challenge "Linear Regression" %}}

Open the previous challenge notebook and perform the following tasks:

1. Subset the train dataframe to extract the numerical columns. (In this case, do not consider the popularity column.)

2. Generate a heatmap of the subset dataframe. Which feature has the highest correlation with the price column?

3. Using that feature from step. 2, build a simple linear regression model with price as the target variable. Calculate R2.

4. Add four more additional features with high correlation to the price and repeat the previous step. Observe how R2 changes. How can this change be explained?

5. Add the remaining feature and repeat the previous step. Does the model improve when the remaining column is added as a feature?


{{% /notice %}}



## Links


{{% notice reading "Additional Resources" %}}

- [Gradient Descent, Step by Step](https://www.youtube.com/watch?v=sDv4f4s2SB8)
- [Performing Linear Regression using the Normal Equation](https://towardsdatascience.com/performing-linear-regression-using-the-normal-equation-6372ed3c57)
- [Fitting a line to data by StatQuest with Josh Starmer](https://www.youtube.com/watch?v=PaFPbb66DxQ&ab_channel=StatQuestwithJoshStarmer)
- [Ordinary Least Squares presented visually](https://setosa.io/ev/ordinary-least-squares-regression/)
- [Linear Regression and its metrics explained by StatQuest with Josh Starmer](https://www.youtube.com/watch?v=nk2CQITm_eo&ab_channel=StatQuestwithJoshStarmer)
- [Interpreting Linear Regression through statsmodels.summary()](https://medium.com/swlh/interpreting-linear-regression-through-statsmodels-summary-4796d359035a)

{{% /notice %}}




{{% notice copyright "Dina Deifallah, Agnieszka Kaczmarczyk, Sara Maras, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}