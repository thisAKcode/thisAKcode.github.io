title: Setup a PostgreSQL db
date: 2022-04-12 12:00
author: Alex


### Install PostgreSQL

I donwnloaded installer from EDB and followed instructions from PostgreSQL Setup Wizard. 
Wizard suggest to install some additional applications (pgAdmin etc.), let you choose directory, suggest the port number to listen 5432 or to use something else for security or if you are running multiple PostgreSQL services on the same server. 
During the installation you also create a password for superadmin called **postgres**.

### Creating database
Okay when I launched Stack Builder I opted for installing some additional extensions included in PostGIS bundle. Then I also choosed to create a spatial database option from Stack Builder Wizard.

### Creating Login Roles 
After PostgreSQL installation and initial setup, a data cluster with a single login role called postgres is initialized, and database is also called postgres.
pgAdmin has a gui for creating user roles. Otherwise write following code:
```sql
CREATE ROLE alex LOGIN PASSWORD 'usesafeone' CREATEDB;
```
### Creating User, Managing Authentication
### Schemas 
Schemas is attribute of Postgresql where one schema may be shared by multiple tables.
That way several tables may be grouped into schemas. Schemas are nice cause otherwise you are froced to alwaya rely on public schema and run the risk of name clashes since objects within schema must be unique.
Schemas can be toherwise organized by roles.

### form URI
Here you can find an awesome article about connecting to postgresql using url. <https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING>
Your possible connection to dummy db may look like that. 
```pyhton 

# here is how your connection uri looks like
# postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
# followed by a concrete example
DATABASE_URL = "postgresql://postgres:my_super_hard_pw@localhost:5432/python_db"

```

### Sources 
1. Obe, Regina O.; Hsu, Leo S.. PostgreSQL: Up and Running. O'Reilly Media. Kindle Edition. 
2. https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a9e3. https://towardsdatascience.com/sending-data-from-a-flask-app-to-postgresql-database-889304964bf2
