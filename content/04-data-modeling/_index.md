---
chapter: true
pre: '<i class="fas fa-chart-line fa-fw"></i> <b>4. </b>'
title: Data Modeling
weight: 40
---

### <i class="fas fa-chart-line"></i> Chapter 4 - Data Modeling

# Project: Cars


![cars_picture](/images/cars.png)

Photo by <a href="https://unsplash.com/@mutecevvil">Ahmed</a> on <a href="https://unsplash.com/photos/PMsrwEVDaag">Unsplash</a>



{{% notice challenge "Project Description" %}}

There are plenty of cars with varying features, styles, and performance capabilities in the automobile industry. It is crucial for manufacturers, dealerships, and consumers to determine the appropriate price for a vehicle. Understanding the factors that influence car pricing is essential for both sellers and buyers. Several factors determine vehicle value, including fuel efficiency, engine attributes, and physical characteristics. By analyzing these features and their impact on MSRP (Manufacturer's Suggested Retail Price), we can build a model that provides reliable price estimations.

This week, you will develop a predictive model using linear regression to estimate the MSRP of cars based on their features. The data we use comes from Kaggle. It describes almost 12000 car models sold in the United States between 1990 and 2018, including some features and market prices.


{{% attachments title="Related files" pattern="cars_data" /%}}

##### 🎯 Goal: Explore Cars data and fit a regression line to the data. 

- **Define Questions**
  - Example questions will be given
  - Students can develop own questions
- **Identify Data Sources**
  - csv files given in course material
- **Retrieve Data**
  - Read the car data into a DataFrame
- **Data Wrangling, Exploration and Cleaning**
  - Clean data and account for data inconsistencies, missing and duplicate data
  - Split data into train and test dataset
- **Analyze Data**
  - Summarize the main characteristics of the data, using exploratory data analysis (EDA)
  - Calculate correlation between dependent and independent variables
  - Build a base model that can predict the MSRP of the cars
  - Enhance the performance of the model by utilizing feature engineering techniques
  - Cluster cars based on their price and fuel consumption attributes
- **Present Data to Stakeholders**
  - Gather plots and metrics to make a story



#### Dataset description:

- `Make`: brand of the car
- `Model`: specific model of the car
- `Year`: manufacturing year of the car
- `Engine HP`: power output of the car's engine in horsepower
- `highway MPG`: how far the car is able to travel for every gallon of fuel it uses in the highway (MPG stands for miles per gallon)
- `city mpg`: how far the car is able to travel for every gallon of fuel it uses around the city (MPG stands for miles per gallon) 
- `Engine Fuel Type`: type of fuel used by the car (e.g. premium unleaded, diesel, electric, and etc)
- `Engine Cylinders`: number of cylinders in the car's engine
- `Transmission Type`: type of transmission system in the car (e.g. automatic, manual, and etc)
- `Driven_Wheels`: type of wheels that provide power and traction to the car (e.g. front-wheel drive, rear-wheel drive, or all-wheel drive and etc)
- `Number of Doors`: total count of doors in the car,
- `Market Category`: specific category or segment in which the car belongs based on its characteristics
- `Vehicle Size`: overall size classification of the car (e.g. Compact, Midsize, Large)        
- `Vehicle Style`: body style or design of the car (e.g. Coupe, Sedan, Wagon and etc)          
- `Popularity`:  represents a measure of popularity derived from Twitter data
- `MSRP (Manufacturer's Suggested Retail Price)`: recommended selling price provided by the manufacturer for the car      

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart, Sara Maras, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}
