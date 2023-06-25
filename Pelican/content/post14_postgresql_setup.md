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

### Setup Your Database Using Pyhton
Imagine you want to create a database to play with postgres. You can use this code as a skeleton for your app. 
This job needs 2 external dependencies: 
- psycopg2==2.9.6
- python-dotenv==0.21.1
Structure of 'module' looks as follows. 


```bash
.env
create_table.py
setup_db.py
```

Here is the first script to be executed: setup_db.py
```python
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

load_dotenv()
pw_pg, DATABASE_URL, mydb_name = [os.environ.get('pw_pg'), os.environ.get('DATABASE_URL'),os.environ.get('db_name')]

def check_database():
    connection = psycopg2.connect(host="localhost", user="postgres", password=pw_pg) 
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = connection.cursor()
    # Check if the database exists
    cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    dbs = cur.fetchall()
    if (mydb_name,) not in dbs:
        cur.execute(f"CREATE DATABASE {mydb_name};")
        return "Database created successfully"
    else:
        return "Database already exists"

def add_postgis():
    conn = psycopg2.connect(database=mydb_name, user="postgres", 
                            password=pw_pg, host="localhost", port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
    cur.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    print(mydb_name)
    check_database()
    add_postgis()
```
Second portion create_table.py besides creating tables, populates it with data.

```python

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv


load_dotenv()
pw_pg, DATABASE_URL, mydb_name = [os.environ.get('pw_pg'), os.environ.get('DATABASE_URL'),os.environ.get('db_name')]

def _create_table():
    conn = psycopg2.connect(database=mydb_name, user="postgres", 
                            password=pw_pg, host="localhost", port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Create a cursor
    cursor = conn.cursor()
    # Create the table if it does not already exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS capital_cities (
        id serial PRIMARY KEY,
        name varchar(255),
        geom geometry(Point, 4326)
    )
    """)
    # Commit, close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()



def insert_mock_data():
    # Connect to the database
    conn = psycopg2.connect(database=mydb_name, user="postgres", 
                            password=pw_pg, host="localhost", port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Create a cursor
    cursor = conn.cursor()
    # Select all rows from the capital_cities table
    cursor.execute("SELECT * FROM capital_cities")

    # Fetch the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Insert a row into the table
    cursor.execute("""
        INSERT INTO capital_cities (name, geom)
        VALUES (%s, ST_GeomFromText(%s, 4326))
    """, ('Paris', 'POINT(2.3522 48.8566)'))
    # Commit the changes
    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    _create_table()
    insert_mock_data()
```

### Sources 
1. Obe, Regina O.; Hsu, Leo S.. PostgreSQL: Up and Running. O'Reilly Media. Kindle Edition. 
2. https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a9e3. https://towardsdatascience.com/sending-data-from-a-flask-app-to-postgresql-database-889304964bf2
