---
title: "SQL Joins"
weight: 80
---


![An intro image](/images/joins.png)



{{% notice warmup "Merge" %}}

- What was merged when the command `pd.merge()` was used in week 3?
- Why do we merge data? Give examples if possible. 
- What are other names for merging?

{{% /notice %}}

## Joins

To query data that exists in different tables you join the tables together and conduct the query on the combined table. As was seen in the *Merging Dataframes* lesson in chapter 3, there are several different kinds of joins that deliver different results depending on the user's goal. 

When doing joins in `SQL` the syntax in used is table_name.column as not to have any confusion in which column is from which table:

```postgresql
SELECT bands.band_name as band, songs.song as song, bands.style as style
FROM bands 
JOIN songs 
ON bands.band_name = songs.band_name;
```

```
     band      |         song          |  style   
---------------+-----------------------+----------
 Joe Jackson   | got the time          | jazz
 Talking Heads | once in a lifetime    | new wave
 Madness       | our house             | two-tone
 The Cars      | just what i needed    | new wave
 Joe Jackson   | one more time         | jazz
 Blondie       | heart of glass        | punk
 The Runaways  | cherry pie            | punk
 Talking Heads | buring down the house | new wave
```

The example above is an **INNER JOIN**. The **INNER JOIN** is the default in SQL and therefore can be executed with a plain **JOIN** command. It excludes rows from both tables that do not match. The band *Weather Report* has no entries in the song table and therefore will not be included in the resulting joined table. 

An **OUTER JOIN** includes all rows from both of the tables even if there is no linkage between these tables. The SQL command for an **OUTER JOIN** is **FULL JOIN**:

```postgresql
SELECT bands.band_name as band, songs.song as song, bands.style as style
FROM bands 
FULL JOIN songs 
ON bands.band_name = songs.band_name;
```

```
      band      |         song          |    style     
----------------+-----------------------+--------------
 Joe Jackson    | got the time          | jazz
 Talking Heads  | once in a lifetime    | new wave
 Madness        | our house             | two-tone
 The Cars       | just what i needed    | new wave
 Joe Jackson    | one more time         | jazz
 Blondie        | heart of glass        | punk
 The Runaways   | cherry pie            | punk
 Talking Heads  | buring down the house | new wave
 Weather Report |                       | fusion-jazz
```
The band *Weather Report* has now been included in the table although they do not have a song listed in the *songs* table. Using the **FULL JOIN** resulted in every row from both tables having representation in our resulting table. 

The **LEFT** and **RIGHT** joins are dependent on the **ON** statement. When doing a **LEFT JOIN** all of the rows that have representation from the table declared on the *left side* of **ON** will be present in the resulting table. In turn when doing a **RIGHT JOIN** all of the rows that have representation from the table declared on the *right side* of **ON** will be present in the resulting table.

**NOTE:** If the column that is being joined on has the same name in both tables then the **USING** clause can replace **ON** and the name of the column (in parenthesis) only must be stated once. This is case in the example above. Therefore the following code will result in the same table:

```postgresql
SELECT bands.band_name as band, songs.song as song, bands.style as style
FROM bands 
FULL JOIN songs 
USING (band_name);
```

## Derived Table

The above **JOIN** can be made persistant change the code as follows:

```postgresql
CREATE TABLE bands_total AS (
SELECT bands.band_name AS band, songs.song AS song, bands.style AS style
FROM bands 
FULL JOIN songs 
USING (band_name)
);

```

This is referred to as a **derived table**. What is the difference between a TABLE, VIEW, and derived TABLE? 

{{% notice info "Materialized View" %}}

What is a **materialized view**? 

A materialized view is a view that is saved as a table in the Database. It is similar to a view or derived table in that it is based on a SQL query on other tables. However unlike a view it is actually made persistant and unlike a derived table is it updated on a regular basis.  

What are the advantages and disadvantages of a TABLE, a VIEW, a derived TABLE and a MATERIALIZED VIEW?

[Tutorial on materialized views](https://www.postgresqltutorial.com/postgresql-views/postgresql-materialized-views/)

{{% /notice  %}}


## Exercises

In order to be able to do more interesting **JOIN** exercises a table with the **genres** would be of help. The exercise below goes through a complex SQL query that will make a **genres** table from the data in the **movies** table. 

### Step 1: Inspect the genres

Connect to the movielens database. Select the **genres** column to inspect the data:

```postgresql
SELECT genres FROM movies LIMIT 5;
```
```
                   genres                    
---------------------------------------------
 Adventure|Animation|Children|Comedy|Fantasy
 Adventure|Children|Fantasy
 Comedy|Romance
 Comedy|Drama|Romance
 Comedy
```
The result shows that when the movie is labeled with multiple genres they are separated by the `|`.

### Step 2: Split the genres

To map each indivdual movie to a genres the `regexp_split_to_table(column, 'pattern')` can be used. The first argument is the column on which to execute the function and the second the pattern to split the string with:

```postgresql
SELECT movieid, regexp_split_to_table(genres, '\|') FROM movies LIMIT 10;
```

```
 movieid | regexp_split_to_table 
---------+-----------------------
       1 | Adventure
       1 | Animation
       1 | Children
       1 | Comedy
       1 | Fantasy
       2 | Adventure
       2 | Children
       2 | Fantasy
       3 | Comedy
       3 | Romance
```

The resulting table is each genre being mapped to the corresponding `movieid`. Having a table like this to refer to will help filter results by specific genres. 


### Step 3: Create a genres tables

The table above is only a result of the query. In order to make the results persistant as a table the following code can either be executed in the `psql`shell or added to the `movie_lens.sql` and run with the `-f` argument:

```postgresql
DROP TABLE IF EXISTS genres;
CREATE TABLE genres AS (
    SELECT 
    	movieid,
    	regexp_split_to_table(genres, '\|') AS genre
    FROM movies
);
```
Note: Maybe you have noticed already that SQL doesn't require indentations as python does. However, when you start writing more complex SQL queries, indented code will be way easier to read.

Here the results of the `SELECT` statment are saved as a table. This is a so-called **derived table** since it is derived from one or more other tables. Therefore if this code is to be added to the `move_lens.sql` file it must be after the `movies` table has been created. Otherwise the execution of the file will result in an error. 

#### BONUS

Use `ALTER TABLE` command to add foreign key constraint to `movieid`. This would create a primary-foreign key relationship between the **genres** and **movies** tables. 


### Step 4: Inspect the result

After executing the code the following command should result in a table similar to the results above.
```postgresql
SELECT * FROM genres LIMIT 10;
```

## Project Challenges

{{% notice challenge "Solve with SQL" %}}

Let's take our analysis even further. With the knowledge of joins make the connection between the tables and analyze the data as a whole. Store the queries answering the below questions in a `movielens_joins.sql` file. Add your own queries with the descriptions of what they are doing to the same file.

1. Imdb is one of the movie platforms which has its own movies database where movies also have their own ids. Find 5 movie titles from our database with the lowest imdb ids (the movies that were added at first to the platform).

    **Using a JOIN display 5 movie titles with the lowest imdb ids**

2. As we have created the genres table before, we want to modify the query asking about the count of drama movies.

    **Display the count of drama movies**

3. One of the ways to describe the movies is to assign the genres to them. Besides genres, there is also tags information available for us. Find out all the movies that are matching a defined tag (e.g. 'fun'). 

    **Using a JOIN display all of the movie titles that have the tag `fun`**

4. Not all the movies where marked with a tag by the users. Find the first movie without any tags in the database.

    **Using a JOIN find out which movie title is the first without a tag**

5. Which genres are the most liked ones? Calculate average rating for all the genres and show the 3 highest rated ones. (Tip: Join the genres and the rating table.)

    **Using a JOIN display the top 3 genres and their average rating**

6. Let's assume that number of ratings is proportional to the number of people who watched a film. Which movies where watched by the biggest group of people? 

    **Using a JOIN display the top 10 movie titles by the number of ratings**

7. If you have seen Star Wars, do you have your favorite Star Wars movie? Compare your verdict with the ratings from the dataset.

    **Using a JOIN display all of the Star Wars movies in order of average rating where the film was rated by at least 40 users**

8. Imagine that you will need to reuse the results of one of the queries above. Save the results in the derived table.

    **Create a derived table from one or more of the above queries**

    What is the difference between this and a VIEW?

BONUS:

9. Come up with your own questions and solve them using the SQL tools you have learned thus far. Use these insights as an argument to the board of governors in order to give a certain movie or movies recognition. 

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of [academis.eu/posts/spiele_DE/textadventure.md](https://www.academis.eu/posts/games_EN/textadventure.md) by Dr. Kristian Rother, used under CC-BY-SA 4.0. 

{{% /notice %}}