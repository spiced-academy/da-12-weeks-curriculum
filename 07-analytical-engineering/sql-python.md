---
title: "SQL with Python"
weight: 30
---

In this lesson, we will use the library `SQLAlchemy` and `pandas` to talk to a database from within Python.

![A book shelf](/images/alchemy.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@miracleday?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Elena Mozhvilo</a> on <a href="https://unsplash.com/s/photos/alchemy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>  
{{< /credits >}}



{{% notice warmup "A complex SQL query" %}}

Write a SQL query for the **movie-lens** dataset using as many of the following keywords as possible:

```txt
SELECT, WHERE, FROM, BETWEEN, COUNT, GROUP BY, ORDER BY, DISTINCT, AND, LIMIT, JOIN, LIKE, SUM, AVG, AS, CREATE VIEW, IN
```

{{% /notice %}}


## Concepts

SQLAlchemy provides tools for managing connections to a database, interacting with database queries and results, and construction of SQL statements in Python.

concept  |  description
---|---|
`sqlalchemy`      | high-level python library for managing all kinds of relational databases
`psycopg2`      |   low-level python library that actually manages the communication with a PostgreSQL DB
`create_engine()`      |   creates an `engine` that manages a conncetion to a DB
`'postgresql://<user>:<password>@<host>/<db>'` | the url, a string that contains all information needed to connect to a DB
`with engine.begin() as conn` | opens a database connection to read or write data
`conn.execute()` | submit arbitrary SQL statements to a DB
`df.to_sql(tablename, engine)` | write a pandas DataFrame into a table of a database
`pd.read_sql(query, engine)` | read a table as a DataFrame
`text()`  | to compose a textual statement to pass to the database


## Installation

Install the required libraries with `pip`:

```bash
pip install sqlalchemy
pip install psycopg2-binary
```

`sqlalchemy` is the generic high-level database interface for Python. You can use it to connect to many different relational databases. `psycopg2` is the low-level database driver specifically for Postgres. Usually `psycopg2` is not imported explicitly but is required by `sqlalchemy` when working with a Postgres Database Server. 


## Create a database connection

To access your database, SQLAlchemy needs a connection string. Connection strings consist of six parts:

part | description | default value
--- | --- | ---
dialect | The dialect/ flavour of the relational database | ...
host | IP address or name of the database server machine | localhost
port | network port on the host machine | 5432
database | the name of your database | postgres
user | the user name of the PostgreSQL Server | postgres
password | the password of the database user | ...

We will need following imports:
```python
from sqlalchemy import create_engine, text, types 
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.dialects.postgresql import JSON as postgres_json
```

A connection string follows this structure: 

`url = '<dialect>://<user>:<password>@<host>:<port>/<database>'`

and for postgresql could look like this:

```python
url = 'postgresql://postgres:mypassword123@34.159.127.75:5432/climate'
```

With a connection string we can create an engine. 

```python
engine = create_engine(url, echo=False)
```
The `engine` object manages connections to the database. It can be used to open new connections
or to handle several connections at once.

{{% notice tip "Logging" %}}

`sqlalchemy` and `psycopg2` translate python statements into SQL commands that a
database server can understand. When creating the engine, you can set `echo=True` 
to print out all the raw SQL queries that are actually sent to the server 
in the background and are usually hidden from the Python programmer! 

{{% /notice %}}


{{% notice tip "Database Credentials" %}}

It is not advisable to write your database user and password into a python file or into a Jupyter Notebook because it might end up in the wrong hands accidentally. To hide credentials from others you can use the `.env` file ([covered here](http://localhost:1313/07-analytical-engineering/intro_analytical_eng.html#env-files)).

In Python, you can read in the variables without showing their content:

```python
from dotenv import dotenv_values

config = dotenv_values()

host = config['POSTGRES_HOST'] # align the key label with your .env file !
password = config['POSTGRES_PASS']
db_name = config['POSTGRES_DB']

# and other environmental variables you need
```

{{% /notice %}}


## Run SQL statements

With an `engine` defined we can now send plain SQL statements to the server:

```python
with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE songs (
            id INT PRIMARY KEY,
            name VARCHAR,
            likes INTEGER
        )    
    """))
```

Connecting to a database works like opening a connection to a local file. The connection stays open within the `with` block and will be closed afterwards. 

The method `conn.execute` sends the SQL statement to the server and optionally returns a result set. Let's insert some data:

```python
with engine.begin() as conn:
    conn.execute(text("INSERT INTO songs VALUES (1, 'Radio Ga-Ga', 123)"))
```

### Transactions


Within a connection context we can send several statements at once:

```python
with engine.begin() as conn:
    conn.execute(text("INSERT INTO songs VALUES (2, 'Under Pressure', 2837)"))
    conn.execute(text("INSERT INTO songs VALUES (3, 'Who wants to live forever', 3998)"))
    conn.execute(text("INSERT INTO songs VALUES (4, 'Don't stop me now', 285)"))
```

The statements within the `with` block are executed as a *transaction*. A transaction bundles several SQL statements into a single atomic unit. If one of the statements fails the entire transaction fails and the state of the database stays unchanged. It’s all-or-nothing. This is called *atomicity* and is one of the key features of a relational database.

To send the statements as separate transactions use `engine.connect()` instead of `engine.begin()`.

{{% notice tip "engine.connect() vs engine.begin()" %}}

**engine.begin()**:  
All `conn.execute()` are treated as a single transaction. If any query fails (e.g., due to an error or constraint violation), the entire transaction is rolled back, and none of the queries take effect.

**engine.connect():**  
Each `conn.execute()` line is treated as a separate transaction. If a query fails, it doesn’t affect other queries executed earlier. You need to explicitly handle the transactions (commit or rollback) for each individual query.

{{% /notice %}}

### Reading data

We can also run `SELECT` statements and store the result in a variable `result`:


```python
with engine.begin() as conn:
    result = conn.execute(text("SELECT * FROM songs;"))
    data = result.all()
print(data)
```

The method `result.all()` reads all rows from the result object and returns a list
of tuples:

```txt
[(1, 'Radio Ga-Ga', 123),
 (2, 'Under Pressure', 2837),
 (3, 'Who wants to live forever', 3998),
 (4, "Don't stop me now", 285)]
```

The list of rows can then be converted into a `pd.DataFrame`:

```python
import pandas as pd

df = pd.DataFrame(data, columns=['id', 'name', 'likes'])
df.set_index('id')
```

### Reading and writing tables with pandas 

Pandas has some built-in tools to directly read data from a database into a DataFrame:

```python
songs = pd.read_sql(sql=text('SELECT * FROM songs;'), con=engine.connect(), index_col='id')
```

With a one-liner, you can also import new data into the database:

```python
songs.to_sql('songs', engine, if_exists='replace', index=True)
```

In the background, this creates a new table with column definitions and inserts
the data into the table. To get more control over the data types of the table 
you can run a `CREATE TABLE` statement before inserting data with pandas:

```python
with engine.begin() as conn:
    conn.execute(text("DROP TABLE IF EXISTS songs;"))
    conn.execute(text("""
        CREATE TABLE songs (
            id INT PRIMARY KEY,
            name VARCHAR,
            likes INTEGER)
        );
    """))
    songs.to_sql('songs', conn, if_exists='replace', index=True)
```

Alternatively we can define a dictionary with the data types and pass it to the pandas `.to_sql()` method. In this case would use the `engine` directly as we are not opening a connection within a `WITH` statement.

```python
dtype_dict = {'id' : types.INTEGER(), 
              'band_name' : types.VARCHAR(),
              'name' : types.VARCHAR(),
              'likes' : types.INTEGER(),
             }

songs.to_sql('songs', engine, if_exists='replace', index='id', dtype=dtype_dict)
```

### Creating Databases

There are multiple ways to create a database using interfaces... {{% expand "show me" %}}

interface  |  how-to
---|---|
psql shell | `CREATE DATABASE newname;` 
DBeaver in an existing connection  right-click on 'Databases' > 'Create New Database' |![](/images/dbt_db_dbeaver.png?width=200px)
in GCP interface: go to console, go to the SQL view, on the left select 'Databases'. Look for the **⊞ Create Database** button.|![](/images/dbt_db_gcp.png?width=200px)

{{% /expand %}}

But if we want to create a database **via python script** (without direct human interaction) we can use the [**SQLAlchemy-Utils**](https://pypi.org/project/SQLAlchemy-Utils/) package which is built on top of SQLAlchemy.

```python
pip install SQLAlchemy-Utils
```

In the following IF Statement the `database_exists(engine.url)` returns *True* if the database from the `url` exist and *False* if it doesn't.  

In case it is *not True* the `create_database(engine.url)` will connect to your instance and create the database 
```python
from sqlalchemy_utils import database_exists, create_database

if not database_exists(engine.url):
    create_database(engine.url)
```

## Project Challenges

{{% notice challenge "Initial Setup: Populating a New Database with Raw Data" %}}

To set up our dbt project, we need the following pre-steps:

- Create a new database.
- Make API requests for various locations and multiple days.
- Populate the database with the raw data retrieved from the API.

> Hint: keep the number of days and locations small until the data flows smoothly from the API to your database. Only then make the final "all locations and 365 days" run.

1. Update the `.env` file with your DB credentials
   ```python
   WEATHER_API = 'xxxxxxxxxxxxxxxxx'
   POSTGRES_USER = 'postgres'
   POSTGRES_PW = '123456789'
   POSTGRES_HOST = '00.000.000.00'
   POSTGRES_PORT = '5432'
   DB_CLIMATE = 'climate'
   ```
   
2. In a new notebook create the connection to your PostgreSQL instance
   - imports...
   
   ```python
   import pandas as pd
   from dotenv import load_dotenv
   from sqlalchemy import create_engine, types
   from sqlalchemy.dialects.postgresql import JSON as postgres_json
   from sqlalchemy_utils import database_exists, create_database
   ```  
   - load your `.env` file and read all variables you need for the db connection and for weather api
   
   - create the engine
   
   - make sure the database named `climate` exists
     (manually or via SQLAlchemy-Utils)
   
3. Add the [*code you developed in the previous encounter*](http://spiced-12-weeks-da.s3-website.eu-central-1.amazonaws.com/07-analytical-engineering/apis.html#:~:text=multiple%20api%20calls). 

4. After the `weather_dict` is saved as a json file (for backup), create a dataframe from it.
   ```python
   weather_dict_df = pd.DataFrame(weather_dict)
   ```
   
5. Define data types for the table in DB (this is why we imported `types` and `postgres_json`)
   ```python
   dtype_dict = {'extracted_at':types.DateTime, 'extracted_data':postgres_json}
   ```
   
6. Using pandas method `.to_sql` send the content of the dataframe to the table `weather_raw` in your `climate` database. Keep the format of the data as json (we will do some data modeling later).
   ```python
   weather_dict_df.to_sql('weather_raw', engine, if_exists='replace', dtype=dtype_dict)
   ```
7. Check if the database was poulated with timestamps and raw data like this
   <img src="/images/load_raw.png" style="zoom:60%;" /> 

8. Once you code is working the database is filled with a small date range, create a python file `extract_load.py` and copy all the necessary code from your notebook. In real life scenario this would be the Production file which can be run from a terminal or by automated systems without human interference.
 
{{% /notice %}}


{{% notice reading "Reading" %}}

- [The official SQL Alchemy tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- [Transactions](https://www.postgresql.org/docs/8.3/tutorial-transactions.html)
- [sqlalchemy types](https://docs.sqlalchemy.org/en/20/core/type_basics.html)

{{% /notice %}}

<br>

{{% notice copyright "Malte Bonart, Samuel McGuire, Alex Schirokow" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}