---
title: "Working with Timestamps"
weight: 10
---

![some intro image](/images/timestamp.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@heatherz?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Heather Zabriskie</a> on <a href="https://unsplash.com/s/photos/time?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

{{% notice warmup "Data Types Review" %}}

1. Read shopper data into a jupyter notebook
2. Look at the data and try to understand what it is.
3. What datatype does each column have?
4. Could we change datatypes any for better data analysis? If so how?

{{% attachments title="Related files" pattern="shopper_week" /%}}

{{% /notice %}}

#### **Key Timestamp Commands**

command   |  description
---          |---
`pd.to_datetime()`       |     converts a column to timestamps
`pd.date_range()`        |      creates a list of timestamps
`pd.period_range()`       |     creates a list of periods
`pd.DateTimeIndex.resample()`        |      rebuilds a DateTimeIndex with a specific interval
`pd.Series.rolling()`       |     groups with sliding window along the time axis

#### **Converting columns to Timestamps**

When you read timestamp data in a string format, the first thing you may want to do is to convert it to the datetime data type.

This can be done manually using the following code:
```python
import pandas as pd

df = pd.read_csv('../data/shopper_week.csv')

df['datetime'] = pd.to_datetime(df['datetime'])
```

A more elegant way is to read in the data already in the datetime format:
```python
df = pd.read_csv('../data/shopper_week.csv', parse_dates=True)
```

#### **Accessing DateTime column**

Sometimes we don't need a full datetime but instead we're interested only in a particular component of it. Datetime column has the functionality of time related features extraction and for this purpose the `dt` accessor would have to be used:

command   |  description
---          |---
`df.dt.year`       |     extract year from timestamp
`df.dt.month`        |      extract month from timestamp
`df.dt.month_name()`       |     extract month name from timestamp
`df.dt.day`        |      extract day of the month from timestamp
`df.dt.weekday`       |     extract day of week from timestamp (where Monday=0, Sunday=6, etc.)
`df.dt.day_name()`       |     extract day of week name from timestamp
`df.dt.hour`        |      extract hour of day from timestamp
`df.dt.minute`        |      extract minute from timestamp
`pd.cut()`  | bins values into discrete intervals


#### **DateTime as an index**

It can also be advantageous to set the datetime information as the index:
```python
df = pd.read_csv('../data/shopper_week.csv', parse_dates=True, index_col=0)
```

Having datetime as an index makes it easier to slice the data by it. Pandas `.loc` knows how to interpet datetime values:
```python
df.loc['2011-01-01']
df.loc['2011-01-01':'2011-01-07']
``` 

If you want to access the more specific datetime information from the index, instead of using `.dt` accessor we use `.index` accessor. It works the same way as with the regular columns.

### Exercises

Expand on the dataframe above. Make columns for the day of the week, month, and year. 

#### Task 1 - create day column

Add column that contains the day of the week:
```python
df['day'] = df['timestamp'].dt.weekday
```

#### Task 2 - create hour column

Add column that contains the month:
```python
df['hour'] = df['timestamp'].dt.hour
```

#### Task 3 - create time of day column

Our task is to create a column which divides day into morning, afternoon and evening. For this purpose we can use pandas `cut` function which bins values into discrete intervals. 

In order to accomplish this, first the time of day labels must be defined as a list:
```python
bin_labels = ['morning', 'afternoon', 'evening']
```
Then the time boundaries must be defined in a list. The max and min values are not included so we set them a bit higher and lower than those in the dataset. First check the max and min values for the hour:
```python
df['hour'].min(), df['hour'].max()
```
Then set the values accordingly:
```python
bin_boundaries = [6.9, 12, 17, 21.1] 
```
Using the above parameters the data can be cut into 3 segments: `morning`, `afternoon`, `evening`:
```python
df['part_of_day'] = pd.cut(df['hour'], bins=bin_boundaries, labels=bin_labels)
``` 

**Question:** What benefits do these *new* columns bring to the analysis? 

### Rolling Mean

The rolling mean or a moving average is a calculation to analyze data points by creating a series of averages of different subsets of the full data set. It could be used if we want to smooth our observations in time.

In other words it helps calculate trends when they might otherwise be difficult to detect. For instance, if the data set includes many points where the numbers shift up and down drastically, it might be hard to see whether it trends up or down over time. This smooth version of the data might give insight into a trend that might otherwise not be clearly visible. 

Using `pd.Series.rolling()` a user defined window can be specified and the desired function can then be applied, in this case `mean()`.

### Exercises

Add rolling mean to dataset and plot the shopper density and rolling mean on one graph:

{{% attachments title="Related files" pattern="shoppers_hourly" /%}}

#### Task 1 - create rolling mean column

Add rolling mean column with a window that gives some insight into the data. Test with different values for `window` (for example, an integer will indicate that an exact number of observations will be taken into account).  
```python
df_hourly = pd.read_csv('../data/shoppers_hourly.csv', index_col=0, parse_dates=True)
df_hourly['rolling'] = df_hourly['customer_count'].rolling(window=___).mean()
```


#### Task 2 - visualize rolling mean results 
Plot `customer_count` and `rolling` versus time to see selected window size gives insight. Return to **Task 1** and try various `window` values and plot. Clean up plot as seen fit. 


## Project Challenges

{{% notice challenge "Applying Datetime functions" %}}

 Create a notebook in which you will solve the following questions:

1. Read in the muesli_orders.csv file and examine it


2. Change the column name to facilitate further analysis (make everything lowercase and use undescore to seperate words)



3. Make sure that there are no duplicate orders or missing values in the data

4. Extract features like month, day, etc. from the Order Date datetime column into their own columns.

5. Plot small sections of the order date over time (1 week, 1 month, etc.)

6. Plot the number of orders per weekday

{{% /notice %}}



## Reading


{{% notice reading "Reading" %}}

- [Rolling Mean in Pandas](https://datagy.io/rolling-average-pandas/)
- [Pandas Datetime documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)

{{% /notice %}}

<br>

{{% notice copyright "Milad Behrooz, Samuel McGuire, Kristian Rother" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}