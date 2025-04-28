---
title: "Machine Learning Workflow"
weight: 20
---

![some intro image](/images/workflow.png)
{{< credits >}}
Photo by <a href="">Alvaro Reyes</a> on <a href="https://unsplash.com/photos/qWwpHwip31M">Unsplash</a>
{{< /credits >}}

## Goal of Machine Learning

The primary goal of machine learning is to develop models that leverage data to assist in decision-making, problem-solving, and answering inquiries, empowering us to gain valuable insights and actionable outcomes. By analyzing patterns and relationships within the data, machine learning enables intelligent systems to learn, adapt, and make accurate predictions or recommendations.


## Machine Learning Workflow

![Machine Learning Workflow](/images/machine_learning_workflow.png)
{{< credits >}}
Machine Learning Cycle <a href="https://towardsdatascience.com/the-machine-learning-workflow-explained-557abf882079">
The Machine Learning Workflow Explained</a>
{{< /credits >}}


### Step 1. - Define Business Goal

In the machine learning workflow, the first crucial step is to clearly define the business goal that the machine learning project aims to achieve. This step sets the foundation for the entire process and ensures that the efforts are aligned with the overarching objectives of the organization.


### Step 2. - Get the Data

Once the business goal is defined, the next step in the machine learning workflow is to gather the necessary data. High-quality, relevant data is crucial for training and building accurate machine learning models. This step involves identifying potential data sources, collecting the data, and ensuring its availability for analysis.


### Step 3. - Train-Validation-Test-Split

After you collect your data, you should split the dataset into training data, validation data and test data. You will not touch the test data until the end of the workflow. Why do we do that?
In the end we are mostly interested in how good our model is if applied to unseen data (data it has not been trained on). To estimate how good it is on unseen data we will use part of our dataset, the test data, to simulate this scenario. We train our model on the training data and select few best models based on evaluating them on the validation data. Only at the very end, after we made all possible decisions about the model, we evaluate how good it works for unseen test data.


Scikit-learn provides a function to randomly split our data into training and validation (or test) data:
```python
from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25)
```

### Step 4. - Explore the Data

In this step, the acquired dataset is analyzed to gain insights and understand its characteristics. Visualizations, summary statistics, and feature analysis are used to identify patterns, distributions, and potential data challenges. These insights guide data preprocessing and model development decisions.

### Step 5. - Feature Engineering

Feature engineering involves creating, transforming, selecting, and encoding features to enhance the model's predictive power and performance. It includes generating new features, transforming existing ones, selecting relevant features, and encoding categorical variables.

To delve deeper into feature engineering techniques, we will explore this topic in more detail on Wednesday.

### Step 6. - Train model(s)

In the machine learning workflow, step 6 involves training the model(s) using the prepared dataset. This process entails feeding the data into the selected model and allowing it to learn patterns and relationships within the data.





### Step 7. -  Calculate Test Score

In step 7 of the machine learning workflow, the trained model's performance is evaluated on a separate test dataset. This step involves calculating the test score to assess how well the model generalizes to unseen data.

### Step 8. - Deploy + Monitor Model

In this last step of the machine learning workflow, the trained model is deployed into a production environment to make predictions on new, unseen data. Additionally, the model is monitored to ensure its continued performance and reliability over time.



## Project Challenges

{{% notice challenge "Exploratory data analysis (EDA)" %}}

Having cleaned the data, it is now time to analyze it to gain insight and understand its characteristics. But before we do that, we have to split the data into training and test. Afterward, we analyze the training data in order to better understand the dataset by examining its various features, distributions, and patterns. In order to accomplish this, please follow the steps below and answer the questions.

1. Open the previous challenge notebook.

2. Separate the features (**X**) and label (**y**).

3. Split the dataframe into training and test data

4. Recombine the train features (**X_train**) and label (**y_train**) in one dataframe. As we analyze training data, we need to combine them into one dataframe
5. Answer the following questions:

 - How does the car price distribution look?
- What is the effect of engine horsepower on car price?
- What are the top 5 most expensive car brands?
- What are the top 5 most popular car brands?
 - How does the price distribution look for the top 5 most popular car brands?
- What is the count of cars with different numbers of doors according to less than and more than 4 cylinders?
- How does the average price change per year?


   


{{% notice reading "Reading" %}}

- [Machine Learning Workflow Explained](https://towardsdatascience.com/the-machine-learning-workflow-explained-557abf882079)


{{% /notice %}}





{{% /notice %}}




{{% notice copyright "Sara Maras, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}