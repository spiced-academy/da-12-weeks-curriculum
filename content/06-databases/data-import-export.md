---
title: "Data Import/Export"
weight: 40
---
 
![An intro image](/images/import.png)
{{< credits >}}
Photo by <a href="https://unsplash.com/@ouch_media?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">John Simmons</a> on <a href="https://unsplash.com/s/photos/import-export?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

{{% notice warmup "Warmer" %}}

##### Discuss:

   1.  What are the advantages of having a defined datatype for a column?
   2.  In what cases in python are datatypes static and in which dynamic?
   3.  What SQL constraints can ensure data reliability? 

{{% /notice %}}


## Insert Data

To add rows to a table you use an INSERT statement, specifying the name of the table and the names of the columns you are inserting data into as well as the values for each column.

##### Example:

```postgresql
INSERT INTO table_name (col_1, col_2, col_3) VALUES (val_1, val_2, val_3);
```

## Exercise:

Connect to `music` database and add data to the **bands** table created in the previous lesson using command such as those below. Feel free to use the example or add other bands and data:

```postgresql
INSERT INTO bands (band_name, style, members) VALUES ('Madness', 'two-tone', 7);
INSERT INTO bands (band_name, style, members) VALUES ('The Cars', 'new wave', 5);
INSERT INTO bands (band_name, style, members) VALUES ('The Runaways', 'punk', 4);
INSERT INTO bands (band_name, style, members) VALUES ('Blondie', 'punk', 5);
INSERT INTO bands (band_name, style, members) VALUES ('Talking Heads', 'new wave', 4);
```

## Importing Data

Inserting data row by row in single command is very inefficent. There are various ways to import chucks of data depending on the data structure. `.csv` files are a very common source. Here is an example of how to import that from a `.csv` file using the `\COPY` command:

```
\COPY table_name FROM 'relative/path/to/data/file.csv' DELIMITER ',' CSV HEADER;
```

Following the `\COPY` command, the table in which the data should be imported is specified. The order of the columns must be the same as the ones in the CSV file. 

If the CSV file does not contain all of the columns in the table, they will need to be specified explicitly.

```
\COPY table_name(col_1, col_2) FROM 'relative/path/to/data/file.csv' DELIMITER ',' CSV HEADER;
```

The path to the file containing the data comes after the `FROM` keyword. Due to the fact that the `.csv` file format is used, the `DELIMITER` clause as well as the delimiter type must be specified.

The `HEADER` keyword indicates that the CSV file contains a header. Unless the `HEADER` keyword is used the `\COPY` ignores the header of a file.

On successful completion, a COPY command returns a command tag of the form:
```
COPY count
```
The count is the number of rows copied. More information on the `COPY` command can be found here: https://www.postgresql.org/docs/10/sql-copy.html .

#### Exercise: use `\COPY` to import data

1. Open `music_tables.sql`
2. Download `bands.csv` and save in the same folder as `music_tables.sql`


{{% attachments title="Related files" pattern="bands.csv" /%}}

3. After the `CREATE TABLE` statement add the following to the line of code:
```
\COPY bands FROM './bands.csv' DELIMITER ',' CSV HEADER;
```
4. Connect to `music` database and look at the table's contents. What is different?



{{% notice challenge "Copy Movie-lens Data to Database" %}}

1. Open the `movie_lens.sql` file
2. Add the `\COPY` command and all necessary arguments to one of the tables in the script
3. Run the script using the `-f` argument
4. Connect to the movielens database and check that the table now has data using the following command:
```postgresql
TABLE table_name;
```
**Tip:** Exchange 'table_name' for the name of the table the data was copied into. 

5. Once this works add the `\COPY` command to all tables and check them all to ensure the data was imported

{{% /notice %}}

## Bonus: Exporting Data

Migrating and backing up data is a crucial part of data management. The **movielens** database that has been created using the `movielens.sql` script is static. No new data is added at any interval. Therefore in essence the `movielens.sql` script along with the `.csv` files are a backup and could be used to import the data into any database with minimal changes to the script.

However in the real world data is altered, added, or deleted on a regular basis. For numerous reasons this data might have to be migrated and of course should be backed up on a regular basis. Since the data changes so often the original import scripts and files will not be up to date and of little use. 

One option for exporting the data from a database is script dump or **db dump**. Script dumps are plain-text files containing the SQL commands required to reconstruct the database to the state it was in at the time it was saved. To restore from such a script, feed it to psql. Script files can be used to reconstruct the database even on other machines.

### Bonus Exercise: pg_dump

`pg_dump` is a postgresql command for backing up a PostgreSQL database. You can create a dump from the command line with:

```shell
pg_dump -U [user_name] -p 5432 -h [ip_address] -d [source_database_name] -f [backup_file_name.sql]

```
Many of the arguments should look familiar from the previous exercises. However when using `pg_dump` the `-d` argument is now used for the database which we want to dump. 

The `-f` argument defines the name of the file in which to save the database dump in. The name of the file is arbritray and a path could be added if desired. 

Attempt a db dump of the **movielens** database using the command above. Upon success open the file and inspect the code.  This file can be used much like the `movielens.sql` to import the database wherever necessary.

What is the biggest difference between **movielens.sql** and **backup.sql**?

{{% notice reading "pg_dump" %}}

For more information about pg_dump and its functionality see the documentation:

www.postgresql.org/docs/current/app-pgdump.html

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of [academis.eu/posts/spiele_DE/textadventure.md](https://www.academis.eu/posts/games_EN/textadventure.md) by Dr. Kristian Rother, used under CC-BY-SA 4.0. 

{{% /notice %}}