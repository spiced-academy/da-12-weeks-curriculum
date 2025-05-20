---
title: "Recap Databases"
weight: 90
---

This is the learning path of PostgreSQL. Use this checklist to measure your knowledge of SQL!

![](/images/path_elephant.png)

## Level 1: Beginner

### Business Case for relational databases

-   Describe a few situations in which organizations use a relational database
-   Enumerate a few relational database technologies
-   Name a few features that a relational database needs to have
-   Distinguish SQL and NoSQL databases
-   Enumerate advantages of SQL over NoSQL and vice versa

### Getting Started with PostgreSQL


-   Draw a diagram explaining how a PostgreSQL server is structured
-   Install PostgreSQL
-   Create a database superuser
-   Create a database
-   Log into psql

### CRUD


-   Run a SQL query in psql
-   Create a table
-   Insert a new row into a table
-   Retrieve all rows from a table
-   Update the values in a specific row
-   Delete a row
-   Use the built-in help function to display the syntax of commands

### Creating Tables


-   Enumerate 7 data types you can use in PostgreSQL
-   Use the following constraints when creating a table:

    -   IF NOT EXISTS
    -   PRIMARY KEY
    -   UNIQUE
    -   NOT NULL
    -   DEFAULT
    -   CHECK

-   List all tables in a database

### Writing Select Statements


-   Write a SELECT statement using the following keywords:

    -   FROM
    -   WHERE
    -   GROUP BY
    -   ORDER BY
    -   HAVING
    -   LIMIT

-   Describe the aggregation functions *count(), sum(), avg(), stddev()*

### JOINs


-   Write a query that connects information from two tables
-   Distinguish INNER JOIN, LEFT JOIN, RIGHT JOIN and CROSS JOIN
-   Explain whether JOIN needs a primary key or not
-   JOIN a table with itself

## Level 2: Intermediate


### Database Clients

-   Enumerate programs that connect to PostgreSQL
-   Name the 5 parts of a database connection
-   Connect to a remote database
-   Access your database from your favourite programming language
-   Host a PostgreSQL database on a public server

### Data Modeling

-   Add FOREIGN KEY constraint to a table
-   Create a PRIMARY KEY over two columns
-   Explain three different cardinalities two tables can have
-   Draw an ER-diagram for your database
-   Explain why database normalization is important

### Data Import/Export

-   Use COPY to load a table from a CSV file
-   Use COPY to write a table to a CSV file
-   Dump an entire database to a text file
-   Restore a database to a text file
-   Use SQLAlchemy to read/write tables to pandas DataFrames

### Basic Administration

-   List all your databases
-   Add a column to an existing table
-   Create an index on a column
-   Delete a database
-   Delete a user
-   Change your password
-   Display/save the psql history

### Advanced SQL Queries

-   Use aliases for tables in a SELECT statement
-   Use the DISTINCT keyword
-   Request query results with a specific offset (paging)
-   Perform arithmetical operations in a SELECT statement (e.g. to
    normalize your data)
-   Enumerate functions you can use in a SELECT statement
-   Use a generator function to create data from scratch
-   Concatenate tables with UNION
-   Write query with a CASE statement
-   Write a query containing one or more Sub-SELECTs
-   Write a query prefixed by a WITH clause
-   Create a view from a SELECT statement


## Level 3: Advanced

### Data Cleaning

-   replace Null values in a column
-   factorize a column
-   calculate substrings of a column
-   create a pivot table

### More advanced queries

-   Define transactions with COMMIT/ROLLBACK
-   Use a cursor object
-   Use set operations
-   Use a temporary table
-   Use hash functions
-   Use window functions

### Full Text Search

-   Run a Regex query on a text column
-   Run a full text search with tokenization on a text column
-   Create an inverted index (gin)
-   Run an FTS query with a Levenshtein distance of 2
-   Run a trigram search and Metaphones

### Special Data Types

-   Run a proximity query based on geographical coordinates
-   Store JSON documents and run queries on multiple nested fields
-   Store parameters of a ML model in an array/cube object
-   Write a ORM class in SQLAlchemy

### Query Performance

-   Measure the performance of queries
-   Distinguish btree, gin, gist and hash indexes
-   Interpret the statistics PostgreSQL calculates on columns
-   Calculate and explain a query plan
-   know what VACUUM FULL ANALYZE does

### Administration

-   Manage multiple users
-   Alter read/write privileges of users
-   Know what a tablespace is
-   Set up an automated backup mechanism
-   Set up a distributed database

### Architecture

-   Group tables into multiple schemas
-   Define a Trigger function
-   Store schema migrations using a migration tool
-   Use an ETL tool (e.g. Airflow) to continuously update one DB from
    another
-   Understand how Streaming (with Kafka or Apache Flink) relates to a
    relational Database
-   Enumerate a few scenarios where using a different database than
    PostgreSQL is a good idea
-   Explain the First to Fourth Normal form and BCNF

<br>

{{% notice copyright "Kristian Rother, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of 

- https://github.com/krother/learning_paths

by Dr. Kristian Rother, used under CC-BY-SA 4.0. 
{{% /notice %}}