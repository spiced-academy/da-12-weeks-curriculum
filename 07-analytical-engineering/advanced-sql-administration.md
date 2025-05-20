---
title: "Managing PostgreSQL users and roles"
weight: 95
---

![Chewbacca & friends](/images/star_wars_roles.jpg)
{{< credits >}}
Photo by Bonnie Burton on <a href="https://commons.wikimedia.org/wiki/File:Chewbacca_%26_friends.jpg">Wikimedia Commons</a> licensed under cc-by-2.0.
  
{{< /credits >}}

{{% notice warmup "A new database user" %}}

1. Log in to your database with `psql`. Run the following statement:

    ```postgresql
    CREATE USER obiwan WITH PASSWORD '12345';
    ```
2. Logout and try to login with the new user credentials. 
3. Which SQL commands can you execute? Which commands are blocked?

{{% /notice %}}


## Concepts

concept  |  description
---|---|
privileges      |   determine the authority that you must have to create or access your data store tables for SQL Server databases
role            |   named group of related privileges that can be granted to the user
user            |   specific person allowed access to database
schema          |   part of the database heiarchy used to divide access to data


## Privileges

## Roles

![postgresql users](/images/postgresql_users.svg)



## Users


## Access rights

![postgresql access](/images/postgresql_access.svg)




## Public schema and public role

On initialization PostgreSQL sets up an implicit role `PUBLIC` with `CREATE` 
privileges on the public schema. By default, all newly created users are implicitly 
assigned to this public role. Therefore every user is able to create tables
(and fill it with data) in the public schema. 

To secure the database it is good practice to revoke these usage rights on the database level (for the default database named `postgres`):

```postgresql
REVOKE ALL ON DATABASE postgres FROM PUBLIC;
```

and on the schema level:

```postgresql
REVOKE ALL ON SCHEMA public FROM PUBLIC;
```

If several database have already been created, these command need to be executed for all databases in place.


## Default Privileges 

For tables, database or schemas created in the future a set of default privileges is granted by default. This means that new tables might not be accessible by users because they have been only granted access to existing tables/ schemas/ databases.

To make sure that future tables are accessible one can `ALTER` the default privileges of a schema:

```sql
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema 
GRANT SELECT ON TABLES TO readonly;
```

{{% notice challenge "Dashboard user" %}}

- Create a `readonly` role with `SELECT` privileges on all tables in your database
- Create a `dashboard` user with a password
- Assign the role `readonly` to the new user
- Login with the new user and test it

{{% /notice %}}

{{% notice challenge "New user with write access" %}}

- Create a `readwrite` role with `SELECT`, `INSERT`, `UPDATE`, `DELETE` privileges on all tables in your database
- Create a new user with a password and assign the role to it
- Login with the new user and test it

{{% /notice %}}


{{% notice reading "Reading" %}}

- [List of Privileges](https://www.postgresql.org/docs/13/ddl-priv.html)
- [PostgreSQL Users and Roles - Guide](https://aws.amazon.com/blogs/database/managing-postgresql-users-and-roles/)

{{% /notice %}}

<br>

{{% notice copyright "Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}