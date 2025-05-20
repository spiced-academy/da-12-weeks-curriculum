---
title: "SQL Window Functions"
weight: 150
---


![window](/images/window.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@rotekirsche20?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">rotekirsche20</a> on <a href="https://unsplash.com/s/photos/window?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}


{{% notice warmup "Pandas `groupby` vs `groupby().transform`" %}}

- Download the notebook
- Run the code
- Discuss the questions in small groups
- Discuss as a class

{{%attachments title="Related files" pattern="groupby_vs_groupbytransform_warmer"/%}}

{{% /notice %}}

## Quick review of aggregation functions and `GROUP BY`


As was seen in [Aggregating Data with SQL]({{< ref "sql-groupby" >}}) when using an aggregate statistic the data is aggregated down to the result. For example to find the mean of the product unit price in the Northwind table **products**:

```sql
SELECT AVG(unit_price) AS avg_unit_price
FROM products;
```

returns

```
   avg_unit_price   
--------------------
 28.866363636363637
(1 row)
``` 

Information like this and `MAX()`, `MIN()`, `SUM()` among others are routinely used when making reports in data analysis. 

Then when looking to a bit more granularity out of the results `GROUP BY` and an aggregate statistic can be calculated per category rather than over the entire dataset. Here is an example also using the Northwind dataset that calculates the avgerage unit price per category:

```sql
SELECT category_id, AVG(unit_price) AS avg_unit_price
FROM products
GROUP BY category_id
ORDER BY category_id;
``` 

returns

``` 
 category_id |   avg_unit_price         
-------------+--------------------
           1 | 37.979166666666664
           2 |            23.0625
           3 |              25.16
           4 |              28.73
           5 |              20.25
           6 |  54.00666666666667
           7 |              32.37
           8 |            20.6825
(8 rows)
``` 

The result is a table with each `category_id` and the average price for the products in that category. Keep in mind the original records have been collapsed into groups in this aggregated table. What if the goal was to create a table with the `product_name`, `unit_price`, `category_id`, and  `avg_unit_price` or `avg_category_price`? `GROUP BY` cannot acheive this since it collapses the data. 



## Window Functions in action

Unlike `GROUP BY` window functions will not collapse the dataset and leave the original data intact if that is the users goal. The example below shows the penguins dataset. A window function can be used to add the average body mass of each penguins species while keeping observations intact.

![](/images/partition_by.png)

In the cases like that referred to at the end of the last section a **window function** would be called for. A window function can be used like *pandas* `.groupby().transform()`. Here is the code that would return a table with `product_name`, `unit_price`, `category_id`, and  `avg_unit_price`:

```sql
SELECT product_name, 
       unit_price, 
       category_id, 
       AVG(unit_price) OVER() AS avg_price
FROM products;
``` 

returns

```
           product_name           | unit_price | category_id |     avg_price 
----------------------------------+------------+-------------+--------------------
 Chai                             |         18 |           1 | 28.866363636363637
 Chang                            |         19 |           1 | 28.866363636363637
 Aniseed Syrup                    |         10 |           2 | 28.866363636363637
 Chef Anton's Cajun Seasoning     |         22 |           2 | 28.866363636363637
 Chef Anton's Gumbo Mix           |      21.35 |           2 | 28.866363636363637
...
``` 

The actual result is 77 rows, but just from this small sampling of the table it can be seen that all of the desired columns are there and the data has not be collapsed.  

A short analysis of the syntax used:

Removing the window function leaves a vanilla `SELECT` statement:

```sql
SELECT product_name, 
       unit_price, 
       category_id
FROM products;
``` 

This would return the same table as above without the `avg_price` column. The one line that is new and does all the 'magic' is:

```sql
AVG(unit_price) OVER() AS avg_price_category
``` 

Looking at it in smaller pieces will help to deconstruct it:

`AVG(unit_price)` alone in this code will calculate the mean of the `unit_price` column. 

However it is now followed by `OVER()`. The `OVER()` clause lets you define the windows for window functions. It also lets you define the order in which a given window function is executed.

`AS avg_price_category` just gives the column an intended name. 

In the example above the `OVER()` clause is empty. In other words smaller windows are defined therefore by default the mean is calculated for the entire length of the table which can be considered one all emcompassing window.

Returning a table with `product_name`, `unit_price`, `category_id`, and `avg_category_price` is a little more tricky:

```sql
SELECT product_name, 
       unit_price, 
       category_id, 
       AVG(unit_price) OVER(PARTITION BY category_id) AS avg_category_price
FROM products;
``` 

returns

```
           product_name           | unit_price | category_id | avg_category_price 
----------------------------------+------------+-------------+--------------------
 Guaraná Fantástica               |        4.5 |           1 | 37.979166666666664
 Ipoh Coffee                      |         46 |           1 | 37.979166666666664
 Chartreuse verte                 |         18 |           1 | 37.979166666666664
 Côte de Blaye                    |      263.5 |           1 | 37.979166666666664
 Steeleye Stout                   |         18 |           1 | 37.979166666666664
 Sasquatch Ale                    |         14 |           1 | 37.979166666666664
 Lakkalikööri                     |         18 |           1 | 37.979166666666664
 Rhönbräu Klosterbier             |       7.75 |           1 | 37.979166666666664
 Outback Lager                    |         15 |           1 | 37.979166666666664
 Chai                             |         18 |           1 | 37.979166666666664
 Laughing Lumberjack Lager        |         14 |           1 | 37.979166666666664
 Chang                            |         19 |           1 | 37.979166666666664
 Gula Malacca                     |      19.45 |           2 |            23.0625
 Original Frankfurter grüne Soße  |         13 |           2 |            23.0625
 Northwoods Cranberry Sauce       |         40 |           2 |            23.0625
...
``` 

The table is longer but it can be seen that the average per category is different from category 1 and 2. This behavior continues until the end of the table. 

The difference now is in the `AVG(unit_price) OVER(PARTITION BY category_id) AS avg_category_price`. Now `PARTIION BY` has been introduced. This is one of the three arguments that can be passed to `OVER()` The other will be discussed later. 

The developers for SQL cleverly picked a synonym for **group** when coming up with this argument for `OVER()`. So in essence whichever categorical column is passed to `PARTITIONED BY` will create 'windows' for each category, then perform the window function (in this case `AVG()`) on each window and return the resulting set upcollapsed with the new column added.

## Window Functions in General

Window functions are divided into three types value window functions, aggregation window functions,  and ranking window functions:

### Aggregate window functions

See [Aggregating Data with SQL]({{< ref "sql-groupby" >}}) for examples of SQL aggregate functions. They are the same as would be used in a window function.  

### Value window functions

window function | description
-| -|
FIRST_VALUE() | returns the first value in an ordered set of values
LAG() | accesses data of a previous row from the current row
LAST_VALUE() | returns the last value in an ordered set of values
LEAD() | accesses data of a row at a specific physical offset that follows the current row

### Ranking window functions

window function | description
-| -|
CUME_DIST() | calculates cumulative distribution values of rows 
DENSE_RANK() | ranks rows in partitions with no gaps in ranking values
NTILE() | break a result set into a specified number of buckets
PERCENT_RANK() | calculate the percentile rankings of rows in a result set
RANK() | find the rank of each row in the result set
ROW_NUMBER() | assign a sequential number to each row in a query result set

### General Syntax

SQL window functions perform calculations based on a set of records AKA observations. The initial examples showed the parallels of window functions with pandas `groupby().transform()`. However there is a lot more that can be accomplished with window functions. First things first get an understanding of the syntax. Here is the general syntax and argument options for a window function: 

```sql 
window_function_name ( expression ) OVER (
                                            partition_clause
                                            order_clause
                                            frame_clause
                                        )
```

### order_clause

As was seen in the previous section the partition clause groups the data according to categorical date. The order_clause or `ORDER BY` should be familiar from [CRUD]({{< ref "crud" >}}) lesson. However in conjunction with a window function like `RANK()` some very interesting information can be extracted from the data.

```sql
SELECT product_name, 
       unit_price, 
       category_id, 
       RANK() over(ORDER BY unit_price DESC) AS overall_rank
FROM products;
``` 

returns (and 72 more observations)

``` 
           product_name           | unit_price | category_id | overall_rank 
----------------------------------+------------+-------------+--------------
 Côte de Blaye                    |      263.5 |           1 |            1
 Thüringer Rostbratwurst          |     123.79 |           6 |            2
 Mishi Kobe Niku                  |         97 |           6 |            3
 Sir Rodney's Marmalade           |         81 |           3 |            4
 Carnarvon Tigers                 |       62.5 |           8 |            5
...
``` 

The reply to this could be that the same result could be accomplished with `ORDER BY unit_price DESC` at the end of the simple `SELECT` statment. The first rebutle to this would be that there is now this great `overall_rank` column that we can use. The second would be that adding a partition clause will open up new worlds of analysis:

```sql
SELECT product_name, 
       unit_price, 
       category_id, 
       RANK() over(PARTITION BY category_id ORDER BY unit_price DESC) AS overall_rank
FROM products;
``` 

returns

```
           product_name           | unit_price | category_id | overall_rank 
----------------------------------+------------+-------------+--------------
 Côte de Blaye                    |      263.5 |           1 |            1
 Ipoh Coffee                      |         46 |           1 |            2
 Chang                            |         19 |           1 |            3
 Chai                             |         18 |           1 |            4
 Lakkalikööri                     |         18 |           1 |            4
 Steeleye Stout                   |         18 |           1 |            4
 Chartreuse verte                 |         18 |           1 |            4
 Outback Lager                    |         15 |           1 |            8
 Sasquatch Ale                    |         14 |           1 |            9
 Laughing Lumberjack Lager        |         14 |           1 |            9
 Rhönbräu Klosterbier             |       7.75 |           1 |           11
 Guaraná Fantástica               |        4.5 |           1 |           12
 Vegie-spread                     |       43.9 |           2 |            1
 Northwoods Cranberry Sauce       |         40 |           2 |            2
 Sirop d'érable                   |       28.5 |           2 |            3
...
```

Once again there are 77 observations in total however from this sample it can be seen that the ranking has now been done per category instead of the entire dataset. Each *window* has it's own ranking.  

### frame_clause

A very interesting feature of the OVER clause is the ability to specify the upper and lower bounds of a window frame. 

The window frame is a set of rows that are somehow related to the current row. Their bounds can be defined for each row in the query result with a `ROWS` subclause, which has the following syntax:

```sql
ROWS BETWEEN lower_bound AND upper_bound
``` 

There are different options for the lower and upper bound in the frame_clause. 

frame_clause options | complete syntax
---|---| 
UNBOUNDED PRECEDING | BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
n PRECEDING | BETWEEN n PRECEDING AND CURRENT ROW
n FOLLOWING | BETWEEN AND CURRENT ROW AND n FOLLOWING
UNBOUNDED FOLLOWING | BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING

Using `UNBOUNDED PRECEDING` for example will select all rows until the upper bound of the partition. The other extreme is `UNBOUNDED FOLLOWING` which will select row until the lower bound of the partition.  

The following example selects the `product_name`, `unit_price`, and `category_id` as would be done in a simple query. 

The fourth line adds a column that will present the `MAX` price in each `category_id` partition. The frame clause `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` explicitly defines the window as the entire `category_id` going from the upper to lower bound. 

```sql
SELECT product_name, 
       unit_price, 
       category_id, 
       MAX(unit_price) OVER (PARTITION BY category_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS max_in_category             
FROM products;
```

``` 
           product_name           | unit_price | category_id | max_in_category 
----------------------------------+------------+-------------+-----------------
 Guaraná Fantástica               |        4.5 |           1 |           263.5
 Ipoh Coffee                      |         46 |           1 |           263.5
 Chartreuse verte                 |         18 |           1 |           263.5
 Côte de Blaye                    |      263.5 |           1 |           263.5
 Steeleye Stout                   |         18 |           1 |           263.5
 Sasquatch Ale                    |         14 |           1 |           263.5
 Lakkalikööri                     |         18 |           1 |           263.5
 Rhönbräu Klosterbier             |       7.75 |           1 |           263.5
 Outback Lager                    |         15 |           1 |           263.5
 Chai                             |         18 |           1 |           263.5
 Laughing Lumberjack Lager        |         14 |           1 |           263.5
 Chang                            |         19 |           1 |           263.5
 Gula Malacca                     |      19.45 |           2 |            43.9
 Original Frankfurter grüne Soße  |         13 |           2 |            43.9
 Northwoods Cranberry Sauce       |         40 |           2 |            43.9

``` 

Instead of using `UNBOUNDED` an exact number of rows can be passed:

```sql
SELECT product_name, 
       unit_price, 
       category_id, 
       MAX(unit_price) OVER (PARTITION BY category_id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS max_in_three_window_in_category             
FROM products;
```

Now the window is not only limited to the `category_id` partition but also only the current row and one before and after. The windows are a maximum of 3 rows in size and the result is the following:

```
           product_name           | unit_price | category_id | max_in_three_window_in_category 
----------------------------------+------------+-------------+---------------------------------
 Guaraná Fantástica               |        4.5 |           1 |                              46
 Ipoh Coffee                      |         46 |           1 |                              46
 Chartreuse verte                 |         18 |           1 |                           263.5
 Côte de Blaye                    |      263.5 |           1 |                           263.5
 Steeleye Stout                   |         18 |           1 |                           263.5
 Sasquatch Ale                    |         14 |           1 |                              18
 Lakkalikööri                     |         18 |           1 |                              18
 Rhönbräu Klosterbier             |       7.75 |           1 |                              18
 Outback Lager                    |         15 |           1 |                              18
 Chai                             |         18 |           1 |                              18
 Laughing Lumberjack Lager        |         14 |           1 |                              19
 Chang                            |         19 |           1 |                              19
 Gula Malacca                     |      19.45 |           2 |                           19.45
 Original Frankfurter grüne Soße  |         13 |           2 |                              40
 Northwoods Cranberry Sauce       |         40 |           2 |                              40
``` 

{{% notice info "ROWS vs RANGE" %}}

In the frame clause there is another alternative to `ROWS`. Whereas `ROWS` defines the window using upper and lower values for the amount of rows above and below the current row, `RANGE` defines a numerical range in which a fields values can have. Due to it's releation to another value `ORDER BY`must be included to indicate which value is being refered to. 

For example if there is a column called `month`.

`ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING` will only perform the window function over 3 rows. 

However using `ORDER BY month RANGE BETWEEN 1 PRECEDING AND 1 FOLLOWING` will check the value of `month` in the current row and then take all rows with the `month` value of `current_row + 1` and `current_row - 1`. See image below:

![](/images/range.png)

{{% /notice %}}

### Using the frame_clause for cumulative calculations

Using a window function can be a elegant way to calculate the cumulative sum of a value. The following query uses `ROWS UNBOUNDED PRECEDING` to calculate the cumulative sum of the quantities ordered in the Northwind data set:

cum sum per row
```sql
SELECT order_id, product_id, quantity,
       SUM(quantity) OVER(ORDER BY order_id ROWS UNBOUNDED PRECEDING) AS cumulative_quantity
FROM order_details;
``` 

returns:

```
 order_id | product_id | quantity | cumulative_quantity 
----------+------------+----------+---------------------
    10248 |         11 |       12 |                  12
    10248 |         42 |       10 |                  22
    10248 |         72 |        5 |                  27
    10249 |         14 |        9 |                  36
    10249 |         51 |       40 |                  76
    10250 |         41 |       10 |                  86
....
``` 
In the `cumulative_quantity` column the quantity is continuous added from the quantity column. If our analysis called for the sum of each order and then cumulative quantity of each order in total the following code would suffice. In it `RANGE` is used instead of `ROWS`. The range is then based on the `order_id`. Therefore the sum is calculated per `order_id` and then added cumulatively per `order_id`:  

```sql
SELECT order_id, product_id, quantity,
       SUM(quantity) OVER(ORDER BY order_id RANGE UNBOUNDED PRECEDING) AS cumulative_quantity_per_order
FROM order_details;
``` 

returns:

```
 order_id | product_id | quantity | cumulative_quantity_per_order 
----------+------------+----------+-------------------------------
    10248 |         11 |       12 |                            27
    10248 |         42 |       10 |                            27
    10248 |         72 |        5 |                            27
    10249 |         14 |        9 |                            76
    10249 |         51 |       40 |                            76
    10250 |         41 |       10 |                           136
    10250 |         51 |       35 |                           136
    10250 |         65 |       15 |                           136
...
``` 

In order to see the cumultive quantity within each order the data should be then partitioned by the `order_id`. 

```sql
SELECT order_id, product_id, quantity,
       SUM(quantity) OVER(PARTITION BY order_id ORDER BY order_id ROWS UNBOUNDED PRECEDING) AS cumulative_quantity
FROM order_details;
```

returns

``` 
 order_id | product_id | quantity | cumulative_quantity 
----------+------------+----------+---------------------
    10248 |         11 |       12 |                  12
    10248 |         42 |       10 |                  22
    10248 |         72 |        5 |                  27
    10249 |         14 |        9 |                   9
    10249 |         51 |       40 |                  49
    10250 |         41 |       10 |                  10

...    
``` 

### `LAG()` 

Comparison of values and calculations of the difference is a vital part of data analysis. Using a **value window function** we can extract the information from other rows of data. Comparing values is easier done when the data exists in another column. `LAG()` or `LEAD()` make this possible. 

The following query not only selects the `product_name` and `unit_price` but also adds a third column based on the `unit_price`. It will just offset the column with a 'lag' of one row. 

```sql
SELECT product_name, unit_price, 
       LAG(unit_price) OVER() AS previous_unit_price
FROM products;
``` 

returns:

``` 
           product_name           | unit_price | previous_unit_price 
----------------------------------+------------+---------------------
 Chai                             |         18 |                    
 Chang                            |         19 |                  18
 Aniseed Syrup                    |         10 |                  19
 Chef Anton's Cajun Seasoning     |         22 |                  10
 Chef Anton's Gumbo Mix           |      21.35 |                  22
 Grandma's Boysenberry Spread     |         25 |               21.35
``` 

Now comparison calculations can easily be done between the `unit_price` column and the `previous_unit_price` column. For example the percent difference between them can be calculated.

```sql
SELECT product_name, 
       unit_price, 
       LAG(unit_price) OVER() AS previous_value,
       (unit_price - LAG(unit_price) OVER()) * 100 / unit_price as percent_difference
FROM products;
``` 

returns

```
           product_name           | unit_price | previous_value | percent_difference  
----------------------------------+------------+----------------+---------------------
 Chai                             |         18 |                |                    
 Chang                            |         19 |             18 |  5.2631578947368425
 Aniseed Syrup                    |         10 |             19 |                 -90
 Chef Anton's Cajun Seasoning     |         22 |             10 |   54.54545454545455
 Chef Anton's Gumbo Mix           |      21.35 |             22 |  -3.044496487119431
 Grandma's Boysenberry Spread     |         25 |          21.35 |  14.599999999999996
``` 



{{% notice reading "Window Functions" %}}

- [window functions](https://towardsdatascience.com/a-guide-to-advanced-sql-window-functions-f63f2642cbf9)
- [postgresql window functions](https://www.postgresqltutorial.com/postgresql-window-function/)

{{% /notice %}}



<br>

{{% notice copyright "Samuel McGuire" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}