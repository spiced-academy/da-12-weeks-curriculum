---
title: "Feature Engineering II"
weight: 70
---

![some intro image](/images/meter.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@siora18">Siora Photography</a> on <a href="https://unsplash.com/photos/cixohzDpNIo">Unsplash</a>
  
{{< /credits >}}


## Handling Numerical Variables: Normalization,Standardization, Kbins

Numerical variables play a crucial role in data analysis and machine learning, providing quantitative measurements that inform predictions and insights. However, these variables often differ in scales and distributions, which can introduce biases and inaccuracies in analytical techniques. To address this challenge, it is essential to preprocess numerical variables using normalization, standardization, and K-bins techniques.

## Normalization

Normalization is a data transformation approach that rescales numerical variables to a common range, typically between 0 and 1. This process eliminates the influence of varying scales, ensuring that no single feature dominates the analysis based solely on its magnitude. Common normalization methods include min-max scaling, which linearly maps the values using the minimum and maximum of the variable.

$$\dfrac{x - min(x)}{max(x) - min(x)}$$



### Implementation with scikit-learn

Here in this code snippet are using MinMaxScaler class from the sklearn.preprocessing module in Python's scikit-learn library. It performs min-max scaling on the bill_length_trans and bill_depth_trans columns of a DataFrame called df.


```python
from sklearn.preprocessing import MinMaxScaler
cols = df[['bill_length_trans','bill_depth_trans']]
min_max = MinMaxScaler()
min_max.fit(cols)
t = min_max.transform(cols)

```
The fit() method computes and stores the minimum and maximum values of each column in cols, which will be used for scaling the data.





## Standardization

Standardization, on the other hand, focuses on transforming numerical variables to have a mean of 0 and a standard deviation of 1. It centers the data around the mean and scales it by the standard deviation.


 $$\dfrac{x - mean}{sd}$$

 Standardization is useful for algorithms that assume a Gaussian distribution or when comparing variables with different scales.


### Implementation with scikit-learn

 ```python

 from sklearn.preprocessing import StandardScaler
cols = df[['flipper_length_trans']]
scal = StandardScaler()
scal.fit(cols)
s=scal.transform(cols)
 
```
In the provided code, the fit() method is used to compute and store the mean and standard deviation of the column. These statistics are essential for standardizing the data.



 ## K-bins

 K-bins, also known as binning or discretization, involve dividing continuous variables into discrete bins or categories. This technique converts numerical values into categorical representations, enabling the analysis of relationships and patterns that may not be apparent when treating the variable as continuous. K-bins are valuable when dealing with non-linear relationships, handling outliers, or incorporating domain knowledge. Various binning methods exist, including equal-width bins, equal-frequency bins, and customized binning based on specific criteria.

 ### Implementation with scikit-learn

 ```python
 from sklearn.preprocessing import KBinsDiscretizer
kbins = KBinsDiscretizer(n_bins=3, encode='onehot-dense', strategy='quantile')
cols = df_new[['body_mass_trans']]
kbins.fit(cols)
t = kbins.transform(cols)

```
The ***kbins = KBinsDiscretizer(n_bins=3, encode='onehot-dense', strategy='quantile')*** creates an instance of the KBinsDiscretizer class and assigns it to the variable kbins. The 
`n_bins`  parameter is set to 3, indicating that the data will be divided into three bins. The `encode`  parameter is set to 'onehot-dense' to encode the discretized values using a one-hot encoding scheme. And in the end we set the `strategy`  parameter to 'quantile', which means that the bin edges will be determined based on the quantiles of the data.











## Project Challenges


{{% notice challenge "Linear regression with scaled numerical features" %}}

This challenge aims to investigate the impact of scaling numerical features on our linear regression model. Here are the steps you need to follow:

1. Apply `StandardScaler()` to the numerical subset of the train dataset

2. Create a dataframe with encoded categorical (from the previous challenge) and scaled numerical features for train dataset

3. Repeat the above steps on the train dataset

4. Build a linear regression model using the encoded categorical and scaled numerical features. Observe how R2 has changed from the last model you constructed in the previous challenge. How do you explain it?

{{% /notice %}}

## Reading

{{% notice reading "Reading" %}}



{{% /notice %}}

{{% notice copyright "Sara Maras, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}