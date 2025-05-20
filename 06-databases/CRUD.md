---
title: "CRUD"
weight: 50
---


![crud operations](/images/crud.png)

  
{{% notice warmup "DBeaver" %}}

**DBeaver** is a graphic interface for databases (not only postgres). Along with **psql** it is another client that can access the data stored on the server. 

- Download and install [DBeaver](https://dbeaver.io/download/)
- Connect to your DB and execute a simple SQL query

{{% /notice %}}

## CRUD

**CRUD** commands can be broken into two categories: 

1. DDL (Data Definition Language) - used to change the structure of the table
2. DML (Data Manipulating Language) - used to alter the records

Regarding commands learned so far the `CREATE` and `DROP` commands would be considered **DDL** and `INSERT` is considered **DML**.


## Read Data

The SQL operation that is most often performed is querying of data. The `SELECT` statement is used to select a specific query of data from a database. The data returned is stored in a result table, called the result-set. Read operations are done by DDL commands.

```postgresql
SELECT * FROM bands;
```
```
 band_name     |        style        | members 
---------------+---------------------+---------
 Madness       | two-tone            |       7
 The Cars      | new wave            |       5
 The Runaways  | punk                |       4
 Blondie       | punk                |       5
 Talking Heads | new wave            |       4
```
The asterisk `*` is used in conjunction with the `SELECT` to select all fields from a table or a query. 

Some of the main elements of a SQL query are:

```postgresql
SELECT columns
FROM table
WHERE condition
ORDER BY column ASC|DESC
LIMIT number;
```
`SELECT` can also be used to query specific columns. Instead of the `*`, you can specify the names of the columns separated by commas.  

The `WHERE` clause performs a query to find the row or rows that depend on the following condition. Various conditions can be passed such as `=`, `>`, `<` and more. 

The `ORDER BY` command is used to sort the result set in ascending or descending order.

`LIMIT` will return the specified number of rows. 

The column titles can also be specified with a different name using `AS` (creating an alias).

```postgresql
SELECT band_name as "name of bands" FROM bands;
``` 
```
 name of bands 
---------------
 Madness
 The Cars
 The Runaways
 Blondie
 Talking Heads
```

Giving the results of a `SELECT` statement an alias will come in handy depending on the task.

## Update Data

Altering the content of a table is done with the help of **Update Operations**. Two Commands are mostly used for Update Operation:

**UPDATE**: To update a row or rows, you use an `UPDATE` statement. This is the DML command used to alter the records.

```postgresql
UPDATE bands SET style = 'new wave, pop' WHERE band_name = 'Blondie';
```
The `SET` command is used with `UPDATE` to specify which columns and values that should be updated in a table.

**ALTER**: To *alter* the structure of a table the `ALTER` command is used. This is the DDL command since it defines the structure.

One example of the use of `ALTER` is adding a column
```sql
ALTER TABLE bands
ADD total_albums VARCHAR;
```

Another would be to `DROP` a column:
```sql
ALTER TABLE bands
DROP COLUMN total_albums;
```

`Alter` is used to add, delete, or modify columns. In addition it is used to add and drop various constraints on an existing table.


## Delete Data 

To delete a row or rows, you use `DELETE`. For example This SQL statement would only delete bands with 5 members.

```postgresql
DELETE FROM bands WHERE members = 5;
```
In the following example all bands without 5 members would be deleted. 
```postgresql
DELETE FROM bands WHERE members <> 5;
```
**Note:** The `<>` in the example above means ‘not equal’.


**DELETE (or SELECT) data that is LIKE**

The `LIKE` clause is used to compare a value to similar values using wildcard operators. The most commonly used wildcard operator is `%`. The percent sign `%` represents zero, one, or multiple characters.

**NOTE:** `LIKE` can also be used with `SELECT`. In that case, instead of removing the rows matching the pattern it will display them as an output.

The following statement deletes all bands where the style starts with "wave":
```postgresql
DELETE FROM bands WHERE style LIKE 'wave%';
```
The following statement deletes all bands where the style ends with "wave":
```postgresql
DELETE FROM bands WHERE style LIKE '%wave';
```
The following statement deletes all bands where the style with "wave" at any position in the column:
```postgresql
DELETE FROM bands WHERE style LIKE '%wave%';
```
**TIP:** The `ILIKE` clause works the same way as a `LIKE` clause but makes the language case-insensitive. Both the operators are used for pattern matching in PostgreSQL.

**NOTE:** `DELETE` is a DML command since it works on the records of the table whereas `DROP` is considered a DDL command since it works on the structure of the table.

{{% notice info ".sql file" %}}

Keep in mind that after executing any of the `DELETE`, `DROP` or other database altering commands that the database has been changed. This can lead to errors if the user expects that data to still be in the original state. An easy fix is to run the `music_tables.sql` file using `-f`. The database will then be brought to the state in which the `.sql` file has been programmed for.
 
{{% /notice %}}

## Project Challenges

{{% notice challenge "Solve with SQL" %}}

This is where we start the actual movielens dataset analysis. 8 SQL tasks below are helping you to perform some initial explanatory analysis. Save your queries in a file called `movielens_eda.sql`. Is there anything more you would like to explore at this stage, add more queries with a description of what they are doing.

SQL explanatory data analysis questions:

1. What is the data structure? What information do we have available for movies? 

    **Display the (whole) movies table.**

2. In the movies table there is a field called `movieId`. Sometimes we will not need this field for the analysis.

    **Display only title and genres of the first 10 entries from the movies table that is sorted alphabetically (starting from `A`) by the movie titles.**

3. How many movies do we have the data for?

    **Display the total row count**

4. Every movie has a genre assign to it. Maybe you have noticed that some of the movies has a few different genres assigned to them. Let's pick one of the genres - e.g. drama - and check how many movies we have that were classified as this genre only. 
    - **Display first 10 pure Drama movies. Only Drama is in the genre column.**
    - **Display the count of pure Drama movies.**

5. Some of the movies are classified as a combination of a few genres. Check how many movies have drama as one of the assigned genres.  

    **Display the count of drama movies that can also contain other genres.**

Is this number different from the one in the previous question? Why do you think so?

6. What is the count of movies that are not classified as drama movies?

    **Display the count of movies don't have drama (in any combination) as assigned genre**

7. What is the year distribution of the movies? Do you have a favorite film? Which year is it from? How many movies from this year are visible in the movies dataset?

    **Display the count of movies that were released in 2003.**

8. What is the year distribution of the movies? Do we have more movies from recent years? Do we have any movies from earlier years?

    **Find all movies with a year lower 1910.**

9. Have you ever watched Star Wars? Or is there a different series of movies that you loved. Let's see which of these movies are in the dataset.

    **Retrieve all Star Wars movies from the movie table.**

{{% /notice %}}

## Reading

{{% notice reading "SQL Cheat Sheet" %}}

{{% attachments title="Related files" pattern="sql-cheat-sheet" /%}}

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of [academis.eu/posts/spiele_DE/textadventure.md](https://www.academis.eu/posts/games_EN/textadventure.md) by Dr. Kristian Rother, used under CC-BY-SA 4.0. 

{{% /notice %}}