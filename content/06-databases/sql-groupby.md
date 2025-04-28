---
title: "Aggregating Data with SQL"
weight: 60
---

![An intro image](/images/group.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@scottsweb?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Scott Evans</a> on <a href="https://unsplash.com/s/photos/organised?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}


{{% notice warmup "SQL commands" %}}

- Research the COUNT, DISTINCT, BETWEEN, CHAR_LENGTH and LIMIT SQL commands
- Experiment with them on the **bands** table
- Explain one of them to the class and give a practical example 

{{% /notice %}}

## Key Concepts

Data aggregation is a process in which data is gathered and represented in a summary form, for purposes including statistical analysis. Data is searched, gathered, and presented in a summarized format to achieve specific business objectives.


command  |  description
---|---|
`ORDER BY`      |     sort the result set in ascending or descending order
`COUNT`      |     returns the number of records returned by a select query
`SUM`      |     calculates the sum of a set of values
`MAX`       |     returns the maximum value in a set of values
`MIN`       |     returns the minimum value in a set of values
`AVG`       |     returns the average value of an expression  
`GROUP BY`  | performs aggregation after grouping data


## Examples


Using the `COUNT` command along with `*` will return a total count of all observatios in the data set:

```sql
SELECT COUNT(*) FROM bands;
``` 

Use `SUM` and the name of a column to return the sum of the specified column:
```sql
SELECT SUM(members) FROM bands;
``` 

Find the mean of a column using `AVG`:
```sql
SELECT AVG(members) FROM bands;
``` 

`ORDER BY` can be used with aggregate functions when they do not aggreate down to a single result or with basic SQL statements:

The following will show the data set and order it by the number of members in ascending order. The default it ascending order or `ASC` in SQL.
```sql
SELECT * FROM bands ORDER BY members;
```
In order to show the table with descending order add `DESC` to the command:
```sql
SELECT * FROM bands ORDER BY members DESC;
```

If the data type is not numeric it will follow that datatypes logical order e.g. string will be alphabetical and dates will be chronological. 

## GROUP BY

In SQL the GROUP BY clause is used with the SELECT statement to arrange data in groups based on similarities. These results are often then aggregated to reveal various aspects of the data. 

### Syntax

```sql
SELECT column1, AGGREGATION_FUNCTION(column2)
FROM table_name
GROUP BY column1
```


### Example

To find out how many bands are listed under each style of music:
```sql
SELECT style, COUNT(style) 
FROM bands
GROUP BY style;
``` 
Note: Here we used the same column name in the aggregation function but most of the times you will be using other columns there.

The `GROUP BY` statement groups the bands dependent on their style then counts how many are categorized as that style. The `SELECT` statement then shows the type of style and count of each style. What happens if the `GROUP BY` statement is left out?

Normally, conditions in SQL are set using the `WHERE` clause. The exception is when using `GROUP BY`. In order to execute `GROUP BY` with dependent conditions the clause `HAVING` is used.  

```sql
SELECT style, COUNT(style) 
FROM bands
GROUP BY style
HAVING COUNT(style) > 1;
``` 

{{% notice tip "Structure of a SELECT statement" %}}

When writing a single SELECT statement we always follow the same general order of the keywords:

```sql
SELECT <columns>
FROM <table_name>
WHERE <condition_on_the_row_level>
GROUP BY <column_to_group_by>
HAVING <condition_on_the_group_level>
ORDER BY <column_for_ordering>
LIMIT <count_of_displayed_rows>;
```

Most of these keywords are optional.

{{% /notice %}}


## Alias creation with `AS`

With `AS` we can also rename temporary tables and columns:

```sql
SELECT style, COUNT(style) AS style_total 
FROM bands
GROUP BY style
```
**Note:** `AS` is also used to create views, derived tables and has other functionality. More on this later in the lessons. 


## CREATE VIEW

A `VIEW` is a virtual table based on the result set of an SQL query. This table will change as the data changes.

The CREATE VIEW command creates a view:

```postgresql
CREATE VIEW new_wave AS
SELECT *
FROM bands
WHERE style != 'new wave'; 
```

A `VIEW` can be queried just as a `TABLE` would be using a `SELECT` statement:
```postgresql
SELECT * FROM new_wave; 
```
The result from this query shows that the view named 'new_wave' does not have the new wave bands in it. This calls for the view to be edited using the command `CREATE OR REPLACE VIEW`.

The CREATE OR REPLACE VIEW command updates a view or creates it if one does not already exist:
```postgresql
CREATE OR REPLACE VIEW new_wave AS
SELECT *
FROM bands
WHERE style = 'new wave'; 
```

A new query of the view will show that the correct bands are now in this view. If the following command is run to add another band to the `bands` table then the update will also be reflected in the view:
```postgresql
INSERT INTO bands (band_name, style, members) VALUES ('Weather Report', 'jazz', 4);
```

The `psql` command to display all view is `\dv`.

Much like tables and databases, views can be erased using the `DROP VIEW` command:

```postgresql
DROP VIEW new_wave; 
```

## Challenges

{{% notice challenge "Solve with SQL" %}}

Let's continue the analysis of the **movielens** database. Answer the following questions with SQL and store your queries in a `movielens_groupby.sql` file. Think about other questions that you would like to ask and add them to the same file as well (together with a description of what a query does).

1. How many ratings are available in the dataset?

    **Display the total row count of the ratings table.**

2. What is the distribution of genres combinations?

    **Display the total count of different genres combinations in the movies table.**

3. Have you already explored the tags table? What unique tags can you see for a selected movie?

    **Display unique tags for movie with id equal `60756`. Use tags table.**

4. How many movies from different years do we have in the dataset? Focus only on given time period.

    **Display the count of movies in the years 1990-2000 using the movies table. Display year and movie_count.**

5. Which year had the highest number of movies in the dataset?

    **Display the year where most of the movies in the database are from.**

6. One of the metrics that could be used to measure the popularity of the movies is the total count of ratings (the number of people who rated a movie). What are the most popular movies if we use this metric?

    **Display 10 movies with the most ratings. Use ratings table. Display movieid, count_movie_ratings.**

7. Another metric that we could use to measure the popularity of the movies is the average rating. However, to ensure the quality of this information we need to have at least a given number of ratings. What are the most popular movies using this metric?

    **Display the top 10 highest rated movies by average that have at least 50 ratings. Display the movieid, average rating and rating count. Use the ratings table.**

8. Imagine that you would like to continue focusing on the drama movies only. As you have multiple questions about drama movies you decided to create a view representing drama movies that you could reuse later on.

    **Create a view that is a table of only movies that contain drama as one of it's genres. Display the first 10 movies in the view.**


{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of [academis.eu/posts/spiele_DE/textadventure.md](https://www.academis.eu/posts/games_EN/textadventure.md) by Dr. Kristian Rother, used under CC-BY-SA 4.0. 

{{% /notice %}}