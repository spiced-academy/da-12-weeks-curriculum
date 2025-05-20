---
title: "Common Table Expressions"
weight: 60
---

![cte](/images/olive_buffet.jpg)

{{< credits >}}
Photo by <a href="https://unsplash.com/de/@bashton?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">
Benjamin Ashton</a> on <a href="https://unsplash.com/s/photos/dashboard?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}


{{% notice warmup "Warmup: Sub-Queries" %}}

{{% attachments title="Related files" pattern="cte_queries_backup.zip" /%}}

1. Download the linked backup file `cte_queries_backup.sql`
2.  Connect to your Postgres RDBMS via psql client in your Terminal and create a database named "cte_queries"
```sql
CREATE DATABASE cte_queries;
```
1. Quit psql
2. Connect to the new database in your Terminal and run `cte_queries_backup.sql`  
```bash
psql -U postgres -p 5432 -h <IP address of your RDBMS> -d cte_queries -f cte_queries_backup.sql
```
1. Find the new database in DBeaver
2. Create a query with subqueries for the following steps. Each next step shall be an outer query for the previous step(s).  
   **&rarr;** show weekly average rate per currency   
   **&rarr;** what was the maximum weekly average rates per currency?  
   **&rarr;** add the max weekly average and week number to each record in the original table   
  
The result set should look similar to this:
![cte](/images/cte_warmup_result.PNG)
{{% /notice %}}

### What are CTEs ?

Common Table Expression, or CTE, is a powerful SQL concept / technique / construct that helps to keep complex queries understandable and more versatile. It first appeared in the SQL standard in 1999, and the first implementations began appearing in 2005.

{{% notice info "Definition: CTEs" %}}

Common Table Expressions allow you to create **temporary *named* result sets** from a simple query. You can then use these result sets in subsequent statements of the query. CTEs act as virtual tables, created during the execution of a query, used by the query, and eliminated after query execution.
> **Flashback:** every SQL query returns a result set - a table with records and columns.

##### There are two types of CTEs:

**Non-Recursive** CTEs are mainly used for filtering and transforming data, joining tables, also for performing calculations without the need for complex subqueries.

**Recursive** CTEs are helpful when you have to work with hierarchical data, compute recursive aggregates, implement graph algorithms, do recursive calculations like factorials or the Fibonacci series, or generate a sequence of numbers or dates.

{{% /notice %}}

## Non-Recursive CTEs

In this lecture we are going to focus on the none-recursive type of Common Table Expressions.

### Syntax

Common Table Expressions start with the **WITH** statement, followed by the **Expression Name**, the name for a **SELECT Statement** inside parantesis, which is the content of a single CTE. You can define one or more common table expression in this fashion. The CTEs construct ends with a **final query** that will give us our result output.

```sql
WITH my_cte AS (
                SELECT column1,
                       column2,
                       column3,
                FROM table_name
)
               
SELECT * FROM my_cte;
```

### Example: 
*Let's re-write the query with subqueries from the Warmup as a CTE Query.*

1. We start with the most-inner query, which returns average values for each calender week per currency

```sql
WITH rates_avg AS (
                   SELECT quote,
                          DATE_PART('week', date) AS week,
                          AVG(rates) as weekly_avg
                   FROM rates_raw                  
                   GROUP BY (quote, week)
)

SELECT * 
FROM rates_avg 
ORDER BY quote, week;
```

2. Now we have used just one temporary result set in a WITH clause. Let's add the next step and show the maximum weekly average value per currency.

```sql
WITH rates_avg AS (
                   SELECT quote,
                          DATE_PART('week', date) AS week,
                          AVG(rates) as weekly_avg
                   FROM rates_raw                  
                   GROUP BY (quote, week)
),

rates_max AS (
              SELECT quote,
                     MAX(weekly_avg) as max_weekly_avg
              FROM rates_avg 
              GROUP BY quote
)

SELECT * 
FROM rates_max
ORDER BY quote;
```
{{% notice tip "Note" %}}
- the `rates_max` CTE is quering from the `rate_avg` CTE
- the final SELECT statement is quering from a different CTE
{{% /notice %}}

3. At last we need to perform a JOIN in order to add the weekly average maximum values to each record in the original table. We can do it in the final SELECT statement.
   
```sql
WITH rates_avg AS (
                   SELECT quote,
                          DATE_PART('week', date) AS week,
                          AVG(rates) as weekly_avg
                   FROM rates_raw                  
                   GROUP BY (quote, week)
),

rates_max AS (
              SELECT quote,
                     MAX(weekly_avg) as max_weekly_avg
              FROM rates_avg
              GROUP BY quote
)

SELECT r.*, 
       rm.max_weekly_avg
       FROM rates_raw r
LEFT JOIN rates_max rm
USING (quote)

ORDER BY r.quote, r.date;
```

##### Bonus Tasks:
In the final result add for each record in the original table
- a column showing the calender week
- a column with the weekly average to each record in the original table
- can we move the joins to a separate CTE step?  

**HINT:** you will need to make an additional join and pay attention to the columns you are joining on.

### In a Nutshell

As you can see with CTEs we can perform Multistage Data Transformation in a linear step-by-step way.

### Benefits of CTEs

- **Readability:** the query logic is easier to follow and to understand
- **Resusage of intermediate results:** a CTE can be referenced multiple times in a query
- **Maintanance:** single steps can be easily tested, which helps a lot when debugging or optimising a query
- **Substitute for a VIEW:** often DB permissions do not allow saving VIEWs, also usage of VIEWs can be significantly more expensive
- **Recursive ability:** Self-referencing queries (see below)

### Limitations of CTEs

- **Duration and scope:** CTEs results are used only within a query and are not stored in the database
- **Indexing**: Because CTEs are not stored in a database as just temporary result sets they can't be indexed
- **Conditions:** CTE's can't be used in the WHERE clause
- **Nesting:** Depending the meaning of Nesting. For once it is not possible to start another CTE chain within a CTE. If you mean by "nested CTEs" multiple CTEs keep in mind that some databases limit the number of CTEs used in a query.
- **Compatibility:** Even though CTEs are quite popular, some database management systems do not support them, or have limited support.

{{% notice info "What about Recursive CTEs?" %}}

Recursive CTEs are used in management of hierarchical or graph-based data structures, or for generating sequences of numbers or dates, calculating the Fibonacci sequence or factorials, etc.

It is used to solve problems requiring repeated processing (kind of loops) of the same data aka recursion. The recursive query references itself until a condition met. This condition has to be specified in a WHERE clause to stop the recursion.

**Example:** Generate a sequence of numbers from 1 to 50.  
NOTE: This is a Microsoft SQL Server dialect example. PostgreSQL recursive CTE statement starts like this: `WITH RECURSIVE...`
![cte](/images/recursive_cte.png)
{{< credits >}}
Source: <a href="https://www.essentialsql.com/introduction-common-table-expressions-ctes/">
Common Table Expressions – The Ultimate Guide</a> By: Kris Wenzel <a href="https://www.essentialsql.com/">essentialsql.com</a>  
<br><br>  

**More information:**  
<a href='https://www.stratascratch.com/blog/learn-to-use-a-recursive-cte-in-sql-query/'>How to Use a Recursive CTE in SQL Query</a>  
{{< /credits >}}

{{% /notice %}}

{{% notice challenge "Practice CTE" %}}

From the `cte_queries` database you imported in the Warmup please use the table `weather` for the following challenge: 

**Write a CTE query with following steps:**

1. Add columns for the year, month and week  
   **Tip:** <a href="http://spiced-12-weeks-da.s3-website.eu-central-1.amazonaws.com/06-databases/sql-advanced.html#working-with-timestamps-using-date_part">Working with timestamps</a>

2. Show average, highest and lowest temperature per week for each location  
   **Tip:** group by used date parts and location  

3. Show max weekly average, highest and lowest temperatures per month for each location  
   **Tip:** group by used date parts and location  

4. Join results from Step 1. and Step 2. to the original daily data.  
   **Tip:** In original table, add missing features on which th **temporary named result sets** will be join on  
###### BONUS:
1. think of your own CTE queries

{{% /notice %}}


{{% notice reading "Extra materials" %}}

- <a href='https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-cte/'>PostgreSQL Tutorial - CTE</a>  
- <a href='https://docs.getdbt.com/terms/cte'>dbt - CTE in SQL</a>  
- <a href='https://betterprogramming.pub/unleashing-the-hidden-potential-of-common-table-expressions-44278fdaa62c'>Unleashing the Hidden Potential of "Common Table Expressions"</a>  
- <a href='https://www.essentialsql.com/introduction-common-table-expressions-ctes/'>essentialsql - Common Table Expressions</a>  

- <a href='https://www.stratascratch.com/blog/sql-interview-questions-you-must-prepare-the-ultimate-guide/'>SQL Interview Questions: The Ultimate Guide</a>  
{{% /notice %}}



<br>

{{% notice copyright "copyright Alex Schirokow" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}
