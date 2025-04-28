---
title: "Advanced SQL Queries"
weight: 90
---

![cartoon](/images/sql_injection.png)
{{< credits >}}
<a href="https://xkcd.com/327/">xkcd</a> cartoon on SQL injection
{{< /credits >}}

{{% notice warmup "Northwind data" %}}

Use SQL to accomplish the following task and answer the questions:

1. Log in to a remote database with `psql` using the creditials made available by the instructor. 
2. How many tables are in the database? 
3. What kind of dataset is this? Which data types are there?
4. Which tables have foreign keys?

{{% /notice %}}

This chapter discusses more advanced SQL queries that will help answer more complicated questions. The class material will be done using the **Northwind** dataset from the remote database in the **warmer**.


## The `IN` operator

Useful in case we want to select a subset of rows based on a match against a list of values. This ugly query:

```sql
SELECT COUNT(*) 
FROM suppliers
WHERE country='UK' OR country='USA' OR country='Italy';
```

Can be written as: 

```sql
SELECT COUNT(*) 
FROM suppliers
WHERE country IN ('UK', 'USA', 'Italy');
```

The `IN` operator can be used in both the `SELECT` and `WHERE` clause.


## The `CASE` operator

With the `CASE` operator we can run a *conditional* query. It's like if/else in other programming languages.

It can be used to bucketize a column:

```sql
SELECT 
    CASE 
        WHEN unit_price > 150 THEN 'expensive'
        WHEN unit_price BETWEEN 20 AND 150 THEN 'normal'
        ELSE 'cheap' 
    END 
FROM order_details;
```

Or to quickly calculate a relative frequency count:

```sql
SELECT AVG(CASE WHEN country IN ('UK', 'USA', 'Italy') THEN 1 ELSE 0 END)
FROM suppliers;
```
The `CASE` operator can be used in both the `SELECT` and `WHERE` clause.

## Type Casting with `CAST`

Sometimes the type of a column must be explicitly changed. For example changing the price from dollars to cents: 

```sql
SELECT unit_price*100 AS price_in_cents FROM order_details LIMIT 5;
```

```price_in_cents 
------------------
              1400
 980.0000000000001
3479.9999999999995
1860.0000000000002
              4240
```

Postgres does not know that there are no fractional cent in the normal economy. This can be remedied using `CAST` to  change the data type to `INTEGER`.


```sql
SELECT CAST(unit_price*100 AS INTEGER) AS price_in_Cents FROM order_details LIMIT 5;
```

**Note:** Type casting can also be done using `::`

```sql
SELECT (unit_price*100)::INTEGER AS price_in_Cents FROM order_details LIMIT 5;
```

## Working with timestamps using `DATE_PART`

As was seen in `pandas` a timestamps allows access to different time related features. The `DATE_PART()` function extracts a subfield from a date or time value. The syntax can be seen below: 

```sql
SELECT date_part('day', order_date) AS day, 
    date_part('month', order_date) AS month,  
    date_part('year', order_date) AS year 
FROM orders LIMIT 5;
```
**Note:** Timestamps can also be used to filter easily using different comparison operators. 

## Derived Tables - Review

The results of a `SELECT` statement is considered a derived table. It is a table derived from another table(s). The results can be made persistant using the `CREATE TABLE` statement in conjection with `SELECT`.

Create a dervied table that has the monthly freight costs for each month in the dataset:

```sql
CREATE TABLE monthly_freight AS SELECT SUM(freight) AS monthly_freight, 
                                        DATE_PART('month', shipped_date) AS month, 
                                        DATE_PART('year', shipped_date) AS year
FROM orders 
GROUP BY year, month;
```

## Sub queries

The `FROM` clause can be used to specify a sub-query expression in SQL. The relation produced by the sub-query is then used as a new relation on which the outer query is applied. This can look a bit overwehlming but comes in handy. 


```sql
SELECT year, avg(max_quantity) AS avg_of_max 
FROM (
    SELECT product_id, 
        max(order_details.quantity) AS max_quantity, 
        date_part('year', shipped_date) AS year 
    FROM order_details 
    JOIN orders USING (order_id)
    GROUP BY product_id, year
    ORDER by max_quantity DESC) mx
GROUP BY year 
ORDER BY avg_of_max DESC LIMIT 5;
```

## Working with strings

There are many ways to manipulate and clean strings in SQL below are a few of the most used functions:

command  |  description
---|---|
`CONCAT(str1,str2,...)`                       |   takes an argument list as an input and returns a concatenated string
`LENGTH()`                      |     used to find the length of a string
`LOWER()`               |     used to convert a string from upper case to lower case
`UPPER()`                   |      used to convert a string from lower case to upper case
`REPLACE()`           |     replace all occurrences of matching_string in the string
`SUBSTRING(str FROM pos)`           |     returns a part of string
`SPLIT_PART()`             |      splits a string on a specified delimiter and returns the nth substring

### **Working with Strings Examples**

`CONCAT(str1,str2,...)`

```sql
SELECT CONCAT(first_name, ' ', last_name) 
    FROM employees;
```

`LENGTH()` 

```sql
SELECT first_name,LENGTH(first_name) 
AS "Length of a First Name" 
FROM employees 
WHERE length(first_name)>7;
```

`LOWER()`  

```sql
SELECT LOWER(first_name) 
FROM employees;
```

`REPLACE()` 

```sql
SELECT employee_id,title, 
replace(title,'Representative','Rep')
FROM employees 
WHERE country='USA';
```

## **Exercises:** Convert the lat, lon coordinates into numerical format

The following exercise uses the `climate` data.

1. Take a look at the `stations`table:

```sql
TABLE stations limit 5;
```

```
 staid |                 staname                  | cn |    lat    |    lon     | hght 
-------+------------------------------------------+----+-----------+------------+------
     1 | VAEXJOE                                  | SE | +56:52:00 | +014:48:00 |  166
     2 | FALUN                                    | SE | +60:37:00 | +015:37:00 |  160
     3 | STENSELE                                 | SE | +65:04:00 | +017:09:59 |  325
     4 | LINKOEPING                               | SE | +58:24:00 | +015:31:59 |   93
     5 | LINKOEPING-MALMSLAETT                    | SE | +58:24:00 | +015:31:59 |   93

```

The best option when creating the table was to define the `lat`and `lon` columns as `VARCHAR`. Yet to use the for geographical plotting the values must be numeric. The format of the values makes that a bit tricky. Using the `POINT` datatype, the `split_part()` function and some math new columns with relevant values can be made. 

2. Add two new columns called `latitude` and `longitude` which will be updated versions of `lat` and `long` that we already have in our table:

```sql
ALTER TABLE stations ADD latitude NUMERIC;
ALTER TABLE stations ADD longitude NUMERIC;
```


3. Although the current datatypes of the `lat` and `lon` columns are both `VARCHAR` the values are meant to hold the following information:

- `lat` : Latitude in degrees:minutes:seconds (+: North, -: South)
- `lon` : Longitude in degrees:minutes:seconds (+: East, -: West)

In order to extract the latitude or longitude in a decimal form the math would be as follows:

$$ degrees + minutes/60 + seconds/(60*60) $$

Using the PostgreSQL `split_part` function and casting the results to the numeric datatype the correct value can be calculated. `split_part` is used to split a given string based on a delimiter and pick out the desired field from the string, start from the left of the string where the first value would be **1** and so on.

After running the follow command take a look at the table and decipher the results in the new columns:

```sql
UPDATE stations SET latitude = (
    split_part(lat, ':', 1)::numeric + -- the degrees
    split_part(lat, ':', 2)::numeric/60+ -- the minutes divided by 60
    split_part(lat, ':', 3)::numeric/(60*60) -- the seconds divided by 3600 all summed up 
);
```

```sql
UPDATE stations SET longitude = (
    split_part(lon, ':', 1)::numeric +
    split_part(lon, ':', 2)::numeric/60+
    split_part(lon, ':', 3)::numeric/(60*60)
);
```
Now the data is ready for geographical plotting. 


## Advanced SQL Challenges

{{% notice challenge "Solve with SQL" %}}

1. Create a derived table called `yearly_mean_temperature` that contains the yearly temperature averages for all weather stations from the `mean_temperature` table. It should contain `staid`, `yearly_temp` and `year` as columns.

2. **Bucketize** `tg` values in the `mean_temperature` table. Use `CASE` to to return a column that will hold the value **hot** when the temperature is above 25 degrees, **normal** when between 10 and 25 and **cold** when under 10.

3. Using `GROUP BY` and a subquery show the yearly average of the maximum temperatures of all stations in the `mean_temperature` table.

Bonus:

- Create other derived tables that might be of interest. 

{{% /notice %}}

## Reading

{{% notice reading "CTE or Common Table Expressions" %}}

Another practical tool in SQL is the usage of CTEs. Take a look at this introduction for more information:

[Common Table Expressions](https://learnsql.com/blog/what-is-common-table-expression/)

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}