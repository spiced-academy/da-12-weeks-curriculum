---
title: "What is Machine Learning ?"
weight: 10
---

![some intro image](/images/machine_learning.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@markuswinkler">Markus Winkler</a> on <a href="https://unsplash.com/photos/f57lx37DCM4">Unsplash</a>
{{< /credits >}}



## Definition
“A program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T as measured by P, improves with experience E.”
(Tom Mitchell, 1998.)

## Core concepts


![Core concepts](/images/core_concepts.png)
concept   |  description
---          |---
**Supervised Learning**      |   we know the input data X and correct answers y  
**Classification**     |  y are categories   
**Regression**    |  y is a scalar   
**Unsupervised Learning**    |  we know X but not y   
**Model**      |     a program that generates from X
**Model Parameters**        |  this is what the program “learns” from the data  
**Loss**   |   a number that tells us how good the model is
**Hyperparameter**  |  a number that we have to set before training

## What are the most important Machine Learning methods?

In *Supervised Learning* we know the correct answers. The model is predicting an output value y based on an input X.
Supervised learning has two subtypes: `Classification` and `Regression`. In Classification, we want to predict a category, in regression, we want to predict a scalar.
In *Unsupervised Learning* we have input data X, and examine the structure of the data without knowing what the outcome should be.




Data Science deals with many different types of problems:
![Scikit Learn Models](/images/scikit_learn_models.png)
{{< credits >}}
Map of estimation problems and suitable models <a href="https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html"> Scikit Learn documentation</a>
{{< /credits >}}



----------------------------------------------------------
Building such models is primarly a responsibility of Data Scientists. However, there is no clear division between Data Science and Data Analytics (and also other data related roles) with respect to metrics. Data Analysts will work on such problems as well. One of the most common examples is probably the Linear Regression model, which is the topic of this week. 


## Python Implementation with scikit-learn

 Scikit-learn is a powerful library in Python that provides simple and efficient tools for predictive data analysis. It is built on top of popular scientific computing packages such as NumPy, SciPy, and matplotlib. If you're looking to perform tasks like classification, regression, clustering, or dimensionality reduction, scikit-learn offers a wide range of algorithms and functionalities to support your needs.

By leveraging scikit-learn, you can benefit from its user-friendly and intuitive API, making it accessible even to those new to machine learning. The library offers a comprehensive suite of functions and classes for preprocessing data, feature selection, model evaluation, and much more. Whether you're a beginner or an experienced data scientist, scikit-learn provides a reliable foundation for developing machine learning solutions. The online documentations are hosted at 

 [scikit-learn.org](https://scikit-learn.org/)

 The package can be easily installed using `pip`:

```python
pip install scikit-learn
```

## Project Challenges

{{% notice challenge "Data Cleaning" %}}

Exploring data and data cleaning are crucial steps in the machine learning workflow. Exploring data allows us to gain insight and understand the data characteristics. Additionally, cleansing data ensures that the data is accurate and consistent, which improves the quality of machine learning models. To explore and clean the car data, please follow the steps outlined below.

1. Open an empty notebook and read in the car dataset.

2. Check information about the data. How many numerical and categorical variables exist in the dataset?

3. Check the statistical description of the data. What are the maximum and minimum prices of the cars? What is the standard deviation of the city fuel consumption of the cars?

4. Check how many cars from each brand are in the dataset.

5. Check the column name of the dataset. Is there any inconsistency in the column names?  Is there a way to resolve the inconsistency in this case?

**Hint**: A naming convention can be used to resolve inconsistencies. Consider using lowercase letters, shortening names, and clear names, such as **hp** instead of **Engine_HP**, **drive** instead of **Driven_Wheels** , **price** instead of **MSRP** and etc.

6. Check the duplicate rows. What should we do about the duplicate data?

7. Check data for null values. Remove the rows with missing values from the dataframe.

***Note***: Removing missing values is one of the methods that can be used to resolve the issue. In the following days, we will learn how to deal with those in a systematic manner.


8. Save the dataframe under a suitable name for further analysis.



{{% /notice %}}






  




{{% notice copyright "Sara Maras, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}