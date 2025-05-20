---
title: "Foreign Keys"
weight: 70
---

 
![An intro image](/images/keys.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@alinnnaaaa?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alina Grubnyak</a> on <a href="https://unsplash.com/s/photos/connection?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}



{{% notice warmup "Add another table to database" %}}

1. Create new table called `songs` in the `music` database with the following columns: `band, song_name`
2. Insert the data from `songs.csv` into that table
3. Check the `music` database to ensure that both tables are there and have data in them

**Tip**: This can be done in the psql shell but a more clever way is to add the necessary code to the `music_tables.sql` file and execute using `-f`.

{{% attachments title="Related files" pattern="songs.csv" /%}}

{{% /notice %}}


## ALTER TABLE - review

The ALTER TABLE statement can be used to add, delete, or modify columns in an existing table.

```postgresql
ALTER TABLE songs      
ADD composer varchar(255);
```

```postgresql
ALTER TABLE songs
DROP COLUMN composer;
```

The ALTER TABLE statement is also used to add and drop various constraints on an existing table. 

## FOREIGN KEYS 

Thus far the tables created have been constrained using datatypes, a specific length in `VARCHAR`, `primary key` and more. `primary key` serves as a reference for each row and therefore must be unique and not contain null values.

The `foreign key` constraint is used to prevent actions that would destroy links between tables. A `foreign key` is a field (or collection of fields) in one table, that refers to the `primary key` in another table.

The table with the `foreign key` is called the child table, and the table with the `primary key` is called the referenced or parent table.

Here is the syntax and an example of how to add a foreign key using the `ALTER TABLE` command:

```postgresql
ALTER TABLE child_table_name
ADD FOREIGN KEY (child_foreign_key_column_name) REFERENCES parent_table(parent_primary_key_column);
```

Example using the `music` database:
```postgresql
ALTER TABLE songs
ADD FOREIGN KEY (band_name) REFERENCES bands(band_name);
```

`psql` with display `ALTER TABLE` if everything executed correctly. Otherwise there will be an error message. The command below displays the table's metadata. The output should also list all of the foreign key references made in the table:
```
\d table_name
```
Once this relationship has been established the parent table cannot be dropped unless the child is dropped beforehand. Any table that has dependents cannot be dropped.

The `foreign key` constraint also prevents invalid data from being inserted into the foreign key column, because it has to be one of the values contained in the parent table.

## CASCADE

One of the main reasons that tables are connected using primary and foreign keys is to ensure the integerity of the data. These relationships prevent the deletion or alteration of data one table that has a parent-child relationship with another.

The parent-child relationship prevents the parent table from being dropped using a normal `DROP TABLE` command. The work around is adding the `CASCADE` argument. This will in turn not only drop the parent table but will cascade to all the children tables and drop the `foreign key` contraints. 

Syntax:

```postgresql
DROP TABLE IF EXISTS table_name CASCADE;
```


## Cardinalities

You can use Foreign Keys to create three basic types of relationships. These are also called cardinalities of tables. 

**One to One**

In this type of entity the occurrence of one entity will be directly in relationship with only one occurrence of another entity. There should not be more than one occurrences for each entity.

*Example:  A car company only has one headquarters country. So there is always one to one relationship between Car Company –> Headquarters Country.*

**One to Many**

In one to many the occurrence of a single entity is always related to more than one occurrences (many) of another entity.

*Example: One doctor has many patients. That relationship is always one to many relationship. In our music data we have a one to many relationship with artist --> songs.*

**Many to Many**

In this type many occurrences of one entity are related to more than one occurrences of another entity.

*Example: Many students study many different subjects. If some of our artist covered each others songs then there would also be a many to many relationship*

![An intro image](/images/relations.svg)

## ER Diagrams 

Entity Relationship Diagrams visually depict the relationships of entity sets stored in a database. ER diagrams help to explain the logical structure of databases. They are often used by database designers as a blueprint during the data modeling stage. An ER diagram can be drawn using a paper and pencil or a program like **pg_admin** or **DBeaver**.

ER diagrams can range from very simple to complex. Here is an ER diagram of our `music` database at the moment:

![An intro image](/images/music_tables.png)

Here is an example of a more complex ERD base on a practice SQL dataset called *Northwind*:

![An intro image](/images/northwind.png)


## Exercises

### Step 1

Establish a primary-foreign key relationship between the songs and bands tables.
Make sure that this operation was successful (you can run `\d songs` in your psqlq client).

### Step 2

Attempt to drop the bands table. What result is returned?


## Project Challenges

{{% notice challenge "Add foreign keys to Movie-Lens dataset" %}}

Altering an existing table to have foreign keys can happen in practice. More commonly the foreign keys would be installed during the data modeling stage. In the movielens dataset there is one major attribute that should be a primary key in one table and a foreign key in all others --> `movieid`

1. Open the `movie_lens.sql` that was used to fill the database with tables and data. 
2. In each code block of the table creation except for the the `movies` table add `REFERENCES table(column)` to the `movieid`. This will create the table with a reference to the `movieid` in the `movies` table.
```postgresql
CREATE TABLE links (
    movieid INT REFERENCES movies(movieid),
    imdbid INT,
    tmdbid INT
);
```

**NOTE:** Keep in mind that the movies table must then be created before any table that `REFERENCES` it.

3. Run `-f movie_lens.sql` command in the power shell. Afterwards if the foreign keys have been correctly referenced the following command should result in an error:
```postgresql
DROP TABLE movies;
```
```
ERROR:  cannot drop table movies because other objects depend on it
```

4. Since the tables now have defined relationships between them a simple `DROP TABLE` will not suffice. `CASCADE` must be added. `CASCADE` will drop any of the contraints from one table on others in a cascading fashion. Add `CASCADE` to the relevant table(s).
```postgresql
DROP TABLE IF EXISTS table_name CASCADE;
```
If everything is modeled correctly then the `-f` command should create the tables, fill them with data and apply the constraints.


5. To check if the foreign constraints have been applied review the output of the following command:
```
\d table_name
```

6. Make sure that you have all the needed tables by running again the `movie_lens.sql` script.  

{{% /notice %}}



{{% notice challenge "Make ER diagram" %}}

Draw an ER diagram by hand including the foreign-primary key relationships for the movielens database and take a picture of it. This would usually be done before and during the modeling stage. 

**BONUS - Optional**

One of the advantages of **pgAdmin** over **psql** is the ability to create ER diagrams. **pgAdmin** has this functionality. Create an ER diagram by right clicking on the database of interest and selecting `Generate ERD`.

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of [academis.eu/posts/spiele_DE/textadventure.md](https://www.academis.eu/posts/games_EN/textadventure.md) by Dr. Kristian Rother, used under CC-BY-SA 4.0. 

{{% /notice %}}