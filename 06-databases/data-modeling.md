---
title: "Data Modeling"
weight: 30
---


![header](/images/table_header.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@alevisionco?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">alevision.co</a> on <a href="https://unsplash.com/s/photos/organized?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}


{{% notice warmup "Movie-Lens Data" %}}

**Discuss and investigate the data for the weekly project**:

- Download the attached files from the **movie-lens** dataset

- Open up the files in a text editor or jupyter notebook and discuss the data and any insights you have. The README.txt can also be a valuable source of information

- Discuss with the class

{{% attachments title="Related files"  /%}}

{{% /notice %}}

## PSQL Shell

Once logged into the **psql shell** the user is automatically in the default database named **postgres.** The user should see something like this on the screen:

```
psql (13.5 (Ubuntu 13.5-2.pgdg20.04+1), server 13.4)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

postgres=> 
```
Many **psql shell** commands start with `\`. In the table below are a few that are often used and can be tried out in the terminal.

{{% notice info "Important psql shell commands" %}}

Command | Description
---|---|
\h [SQL command] | for help with SQL commands
\\? | for help with psql commands
\c [database_name] | to connect to database
\l |  to list databases
\dt | to display tables in current database
\q | to quit the shell or exit a secondary screen


{{% /notice %}}

#### Exercise

Answer the following questions using the appropriate **psql shell** command:

1. Are there any other default databases? If so, what are they called?
2. Are there any tables in the `postgres` database?
3. Find another useful **psql shell** command using the print out from the command `\?`. 
**Tip**: Exit explanation screen using \q. This will return the user to the **psql shell** prompt. 

## SQL

{{% notice info "SQL vs Pandas" %}}

Some refer to SQL as the grandparent of pandas. Here are some of the naming equivalents:

 Pandas | SQL 
---|---
 dataframe | relation  
 column | attribute 
 row | tuple 
 cell | field 

{{% /notice %}}

Keep in mind the commands that use `\` are **psql shell** specific. On the other hand SQL or Structured Query Language is used in programming and designed for managing data held in relational database management systems. It has been used for almost 50 years and although it has many dialects depending on the RDBMS, the basics are the same across most database systems.

**Note:** Although SQL is case insensitive SQL keywords are typically written in UPPERCASE letters.  

{{% notice challenge "CREATE DATABASE" %}}

Create a database for the weekly project called **movielens** using SQL:

1. Type the following command to create the database:
```sql
CREATE DATABASE movielens;
```
2. Check to see if the database is listed when using the `\l` command.
3. Using the following command to delete the database:
```sql
DROP DATABASE movielens;
```
4. Check again to see if the database is listed when using the `\l` command.
5. Create the database again, this time do not delete. It will be the primary source of data for the weekly project. 
6. Navigate to your newly created database using the `\c` command. If this operation was successful you will see that the psql prompt will change.

{{% /notice %}}

## CREATE TABLE, constraints and Data Types

To create a table you use a CREATE TABLE statement, specifying the column names you would like to use as well as the data types they may contain. 

Note: Make sure you are located in the right database at first. When creating a new table it will be put into the same location as you are in.

```sql
CREATE TABLE table_name (
    id SERIAL primary key,
    column_name_1 VARCHAR(255) not null,
    column_name_2 VARCHAR(255),
    column_name_3 INTEGER
);
```
Here `id`, `column_name_1`, `column_name_2`, and `column_name_3` are all column names. The rest of the code are constraints on the each column and field values in those respective columns. 

The `SERIAL` type is really an integer but one that will increment with each row that is added, guaranteeing that each row has a unique primary key. 

The `primary key` constraint uniquely identifies each record in a table and cannot contain NULL values. A table can only have **ONE** primary key.

The `VARCHAR` is for text of a length that is not predetermined. The parenthetical number 255 in the example above specifies the maximum length to allow.

`not null` indicates that the column_name_1 field is required.

{{% notice info "PostgreSQL Datatypes" %}}

The most important data types in PostgreSQL are:

data type | description
---|---
INT | integer number
NUMERIC | floating point number
TEXT | long text
VARCHAR(N) | text with a maximum length of N characters
DATE | year/month/day
TIMESTAMP | year/month/day hour:min:sec
SERIAL | integer that counts up automatically
BOOL | boolean

{{% /notice %}}

#### Exercise

1. Log into default **postgres** database. Create practice database and table using the code blocks below in the **psql shell**. Feel free to edit the name of the table, columns and data types. The blocks can be copied and pasted in the **shell** or each line separately. Notice that the prompt will not execute the command until it ends with `;`. 

Create `music` database:
```postgresql
CREATE DATABASE music;
```

Connect to `music` database:
```
\c music
```

In the `music` database create a table that will hold information about various bands. 
```postgresql
CREATE TABLE bands (
    band_name VARCHAR(255) primary key,
    style VARCHAR(255),
    members INT
);
```
2. Display all tables in your `music` default database. using the `\dt` psql command. 
3. Display table using the the `TABLE` command:
```postgresql
TABLE bands;
```
4. Just like with a database, a table can also be dropped. Use the following command:
```postgresql
DROP TABLE bands;
```
**Note:** The `DROP` command removes tables, indices etc. Note that there is no way of undoing this! In this case the entire bands table will be deleted.


## -f Argument

As was shown in the **PostgreSQL** chapter there are many arguments that can be used with the **psql** connection command. The most important being `-U` for user name, `-p` for port number, and `-h` for host name. 

However `-f` can also be very advantageous. The `-f` argument allows for a `.sql` file to be executed. In other words the user can develop an entire **SQL** script to be executed instead of entering the commands one by one into the **psql shell**. 

#### Exercise: create table using `-f`

1. Open a text editor
2. Copy the following text and paste into the text editor:
```postgresql
DROP TABLE IF EXISTS bands;
CREATE TABLE bands (
    band_name VARCHAR(255) primary key,
    style VARCHAR(255),
    members INT
);
```
3. Save file as `music_tables.sql`
4. Open the command shell in that folder containing `music_tables.sql`
5. Execute the following command in the shell with the correct arguments:
```
psql -U [user_name] -p 5432 -h [ip_address] -d [destination_database_name] -f [file_name_to_execute]
```
6. Connect to `music` database and assure that the bands table exists

{{% notice info "createdb" %}}

In order to run the `-f` argument in relation to a specific database that database must exist. Instead of logging into the database, creating it and then exiting the `createdb` command can be used. This command is run from the terminal and will create the database without having to login. 

```
createdb -U [user_name] -p 5432 -h [ip_address] -p 5432 [name_of_db]
```

Then the database is ready for tables and the `-f` argument can be used to create and populate the tables. 

{{% /notice %}}

{{% notice challenge "CREATE TABLE using `-f` argument" %}}

1. Write a CREATE TABLE statement in a text editor
2. Inspect one of the movie-lens csv files in a text editor
3. Include columns for all fields from the movie-lens data
4. Choose a name for the table
5. Choose aproppriate data types
6. Make sure to include a primary key column
7. Decide whether you need NOT NULL on a column
8. Save the file as `movie_lens.sql`
9. Execute the file to create the tables in your database using the following command:
```
psql -U [user_name] -p 5432 -h [ip_address] -d [destination_database_name] -f [file_name_to_execute]

```
10. Log into the **psql shell**, use the commands you have learned so far to connect to the **movielens** database and list the table(s)
11. Develop and save this script to create tables for all of the **movielens** csv files

**Tip:** When the `.sql` file is run multiple times an error will occur if a table already exists. To avoid this add the command `DROP TABLE IF EXISTS table_name;` directly before the `CREATE TABLE` statement for every table. 

{{% /notice %}}

## Reading

{{% notice reading "The Relational Data Model" %}}

For a more in depth read into relational data modeling: [Stanford InfoLab article](http://infolab.stanford.edu/~ullman/focs/ch08.pdf)

{{% /notice %}}


<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of [academis.eu/posts/spiele_DE/textadventure.md](https://www.academis.eu/posts/games_EN/textadventure.md) by Dr. Kristian Rother, used under CC-BY-SA 4.0. 

{{% /notice %}}