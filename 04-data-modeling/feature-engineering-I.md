---
title: "Feature Engineering I"
weight: 60
---

![some intro image](/images/sewing.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@kellysikkema">Kelly Sikkema</a> on <a href="https://unsplash.com/photos/2k_3X5bU2SU">Unsplash</a>
  
{{< /credits >}}


## What is feature engineering?

**Feature engineering** involves the preprocessing of data before constructing a model. The objective of feature engineering is to obtain an improved representation of the input data.

In this first chapter, you will learn how to utilize scikit-learn functionality to apply a set of feature engineering techniques on individual columns. 


## Handling Categorical Variables: Imputation, One Hot Encoding


### What can we do with the missing values?

When dealing with missing values in a dataset, there are several approaches that can be taken to handle them effectively. Some common strategies for dealing with missing values include:

**Dropping missing values:** If the number of missing values is relatively small compared to the size of the dataset, one option is to simply remove the rows or columns containing missing values. However, this approach should be used with caution, as it can result in the loss of valuable information.

**Imputation:** Missing values can be filled in using various imputation techniques. 

Some common imputation methods include:

    - Replacing missing values with the mean, median, or mode of the available values in the same column.
    - Forward fill or backward fill: Propagating the last known value forward or the next known value backward to fill in missing values.
    - Interpolation: Estimating missing values based on the values of other data points using techniques like linear interpolation or spline interpolation.


The choice of which method to use for handling missing values depends on factors such as the amount and pattern of missingness, the nature of the data, the significance of the missing values, and the specific requirements of the analysis or modeling task.


#### Example with scikit-learn

By using **SimpleImputer** with the 'most_frequent' strategy, missing values in the 'sex' column are filled with the most common value present in that column. This technique ensures that the data is complete and ready for further analysis or modeling tasks.

```python
from sklearn.impute import SimpleImputer

cols = df[['sex']]
imputer = SimpleImputer(strategy = 'most_frequent')
imputer.fit(cols)
t = imputer.transform(cols) # <- output is a numpy array
```


### Converting categorical variables into numerical representations

Converting categorical variables into numerical representations is an important step in many machine learning algorithms, as these algorithms typically operate on numerical data. This process is known as categorical encoding or feature encoding. The goal is to transform categorical variables into numerical form while preserving the underlying information or relationships between categories.

- **One-Hot Encoding:** In one-hot encoding, each category is represented as a binary vector where only one element is 1 (indicating the presence of the category) and the rest are 0. This approach creates a new binary feature for each category, effectively expanding the feature space. For example, if there are three categories (A, B, and C), one-hot encoding would result in three binary features: [1, 0, 0], [0, 1, 0], and [0, 0, 1]. One-hot encoding is suitable when there is no inherent order or hierarchy among the categories.


#### Example with scikit-learn

When you use the OneHotEncoder with the specified parameters, the 'species' column is one-hot encoded, which means it is converted into multiple binary columns representing each unique category. The fit method analyzes the unique categories, and the transform method applies the encoding transformation. The resulting t variable contains the transformed data, where each unique category is represented by a set of binary columns. This one-hot encoded representation is commonly used for categorical variables in machine learning models.



```python
from sklearn.preprocessing import OneHotEncoder
ohc = OneHotEncoder(sparse=False,handle_unknown= 'ignore')
cols = df[['species']]
ohc.fit(cols)
t = ohc.transform(cols)

```


## Project Challenges


{{% notice challenge "Impute missing values" %}}

In order to deal with missing values in the car dataset, follow these steps:

1. Read the cars_data.csv as a part of feature engineering challenge.

2. Check data for null values.

3. Split the dataframe into training and test data

4. Use the appropriate strategy that you have learned during the encounter to impute missing values for both the train and test datasets separately

**Hint:**  Drop the `Market Category` column as it contains too much of null values and also this feature doesn't have high importance regarding the target feature which is the price

5. Combine the train and test data into one dataframe, then save the cleaned and imputed data for further analysis.
{{% /notice %}}



{{% notice challenge "Linear regression with categorical features" %}}

Use the following steps to encode categorical features and build a linear regression model with categorical and numerical features.

1. Subset the dataframe from the previous challenge to extract the categorical columns.

2. apply one-hot encoder to the categorical subset of the train dataset 

3. Convert back the result object into pandas dataframe

4. Add numerical features to the encoded dataframe from the previous step

5. Repeat the above steps on the test dataset

6. Build a linear regression model using the encoded categorical and numerical features. Observe how R2 has changed from the last model you constructed using only numerical features.

7. Make predictions and plot predicted and actual values in one scatter plot.  

{{% /notice %}}



## Reading

{{% notice reading "Reading" %}}

- [Introduction to Feature Engineering – Everything You Need to Know!](https://www.analyticsvidhya.com/blog/2021/10/a-beginners-guide-to-feature-engineering-everything-you-need-to-know/)

{{% /notice %}}


{{% notice copyright "Sara Maras, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}