---
title: "Query optimization and indexing"
weight: 96
---

![Manchester Central Library Catalogue](/images/library_index.jpg)
{{< credits >}}
Photo by <a href="https://www.flickr.com/photos/16712259@N04">Ricardo</a> on <a href="https://commons.wikimedia.org/wiki/File:2010_Manchester_UK_4467481691.jpg">Wikimedia Commons</a> licensed under cc-by-2.0.
  
{{< /credits >}}

{{% notice warmup "A library catalog" %}}

- What was the purpose of the objects in the picture above?
- What was written on the index cards?
- What advantages and disadvantages has a library catalog over randomly storing books in a libary?

> Read more about analog library catalogs [here](https://en.wikipedia.org/wiki/Library_catalog).

{{% /notice %}}


## Concepts

*Query optimization* deals with the minimization of execution time it needs to fetch, update or insert data in a relational database. *Indexes* are lookup data structures that accelerate your database queries and can help to optimize queries.

concept  |  description
---|---|
`EXPLAIN`      |   show the DB's query execution plan for a given SQL query
`EXPLAIN ANALYZE` | show *and carry out the plan*
`\timing` | toggle timing of queries in `psql`
sequential scan     |  DB scans through every data field sequentially for filtering
index scan     | DB uses an existing index structure to quickly filter the data
B-tree index | index structure commonly used in PostgreSQL


## Query execution plan

When the database server receives a query, it first gets optimized by the query planner. The query planner estimates the time it needs to execute each part of the query and possibly rearranges the query in such a way that the costs are minimized. 

The `EXPLAIN ANALYZE` keywords can be used to inspect the query plan and execute a query. 

### Sequential scan

To analyze a query that fetches all ratings for the first Star Wars movie run:

```postgresql
EXPLAIN ANALYZE SELECT * FROM ratings WHERE movieid=260;
```

returns

```txt
                                               QUERY PLAN                                                
---------------------------------------------------------------------------------------------------------
 Seq Scan on ratings  (cost=0.00..1903.45 rows=269 width=20) (actual time=0.019..9.761 rows=251 loops=1)
   Filter: (movieid = 260)
   Rows Removed by Filter: 100585
 Planning Time: 0.084 ms
 Execution Time: 9.803 ms
```

The database server performed a sequential scan of the data and estimated that it will return 269 rows. 
Executing the query actually took around 10ms and returned 251 rows. 

![](/images/sequential_scan.svg)

Just like with a `for` loop, in a sequential scan, the database server 
sequentially scans each row and checks it. Doubling the amount of data also roughly 
doubles the time needed to scan all data. The processing time increases
linearly with the amount of data, in short: $O(n)$.


### Index scan

An index is an additional data structure that helps finding values quicker. The following graph contains the same values as before but sorted in a binary tree like data structure:

![](/images/index_scan.svg)

Once the initial sorting is done (the index creation) finding values requires much less time than before. Doubling the amount of data now only adds a single additional depth to the tree. The processing time therefore increases only binary logarithmically, in short: $O(\log_2 n)$.

## Index creation

To create an index run

```postgresql
CREATE INDEX ON ratings(movieId);
```

This instructs the Management System to create a B-tree index on the column `movieId` of the `ratings` table.

The query plan for finding all ratings of the first Star Wars movie now looks like this: 

```txt
                                                           QUERY PLAN                                                           
--------------------------------------------------------------------------------------------------------------------------------
 Bitmap Heap Scan on ratings  (cost=6.38..507.76 rows=269 width=20) (actual time=0.065..0.532 rows=251 loops=1)
   Recheck Cond: (movieid = 260)
   Heap Blocks: exact=213
   ->  Bitmap Index Scan on ratings_movieid_idx  (cost=0.00..6.31 rows=269 width=0) (actual time=0.033..0.034 rows=251 loops=1)
         Index Cond: (movieid = 260)
 Planning Time: 0.098 ms
 Execution Time: 0.572 ms

```

Note that the execution time dropped from 10ms to roughly half a millisecond! 


To check for and prevent duplicate values in a column, the `UNIQUE` option can be added:

```postgresql
CREATE UNIQUE index on movies(title);
```

{{% notice info "Unique constraint and primary keys" %}}

When specifying a unique constraint, PostgreSQL implicitly create a unique index for that column. This is also true for `PRIMARY KEY` constraints!

{{% /notice %}}

After index creation you can also `ALTER` or `DROP` an index after creation.





## Pros and Cons

### Advantages

#### Faster reads

Indexes speed up searches. They allow the database to find and retrieve specific rows much faster. This is especially relevant for queries that contain a `WHERE` clause (`SELECT`, `UPDATE` or `DELETE` statements). 

#### Free Sorting

The B-tree index also sorts the output. Therefore, adding a `ORDER BY` does not increase the cost of the query.

Typically, you only want to use indexes for tables that are read or updated often and you want to place the index on the column(s), that is (are) typically used to filter the table. 

### Disadvantages

#### Locked tables

For larger tables, the creation of an index can take many hours to complete. During the index creation no `INSERT`, `UPDATE` or `DELETE` queries are allowed. The table is locked. 

{{% notice info "Locked tables" %}}

A locked table accepts `SELECT` statements but its data cannot be altered.

Use the `CONCURRENTLY` option to build the index in a much less efficient way but without locking writes. 

{{% /notice %}}

#### Slower writes

After the index creation, every subsequent `INSERT` statement also triggers an update operation for the index. For a table where new data is inserted at a high frequency this can create a massive overhead. 

#### More storage

The index is a data structure that requires additional hard drive storage (and memory). You can check the file size for all indexes of a table with the command:

```postgresql
SELECT pg_size_pretty(pg_indexes_size('tablename'));
```

## Summary

- Queries run faster only if the indexed column is used in a query
- `PRIMARY KEY` columns use an index by default
- Indices trade memory for computation time, so the total size of your database on the disk grows.
- Because indices have to be modified (or even rebuilt from scratch), updating the data will be slower
- Indexes should not be used on small tables.
- Indexes should not be used on tables that have frequent, large batch update or insert operations.
- Indexes should not be used on columns that contain a high number of NULL values.
- There are different types of indices in PostGreS, but the default (btree) usually does the job
- Columns that are frequently manipulated should not be indexed.


## Exercise - Accelerate a Query

Execute the following coe step by step:

1. Enable query timing with `\timing`

2. Create some random data and fill a table with it:

    ```postgresql
    CREATE TABLE sampledata(
            uid SERIAL primary key,
            c1 int,
            c2 numeric,
            c3 int
    );

    INSERT INTO sampledata (c1, c2, c3)
    SELECT
        random()*10000,
        10000*random(),
        random()*99999
    FROM generate_series(1,10000000);
    ```

3. Inspect the data:

    ```sql
    SELECT * FROM sampledata LIMIT 5;
    ```

4. Run a difficult query and time it:

    ```sql
    SELECT count(*) FROM sampledata
    WHERE c1 between 100 and 200
        and c2 between 100 and 200
        and c3 between 200 and 300;
    ```


5. Add an index

    ```SQL
    CREATE INDEX idx1 on sampledata(c1);
    ```

6. Time the query again. 

7. Add more indexes and run the query again.

> adopted from [here](https://medium.com/@Alibaba_Cloud/principles-and-optimization-of-5-postgresql-indexes-btree-hash-gin-gist-and-brin-4d133e7f1842)




{{% notice challenge "Index creation" %}}

- Create an index on the `date` column in the `climate` database on the `mean_temperature`table
- Measure the disk size of the index
- Think about other columns where adding an index might help to speed up `SELECT` statements

{{% /notice %}}



{{% notice reading "Reading" %}}

- [Documentation for CREATE INDEX](https://www.postgresql.org/docs/9.1/sql-createindex.html)
- [General documentation for Indexes](https://www.postgresql.org/docs/9.1/indexes.html)

{{% /notice %}}

<br>

{{% notice copyright "Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}