<h1>Basic blog app using django.</h1>
https://blogged-basic.herokuapp.com/

<h3>Problem using sqlite.</h3>
After the dyno, in heroku, sleeps the data base gets reset. Solution for this is using postgresql.
<h4>Step 1: We need to change setting.py file:</h4>
postgresql local system config:

```python
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME','webedureka'),
        'USER': os.environ.get('DB_USER','postgres'),
        'PASSWORD':os.environ.get('DB_PASS','postgres'),
        'HOST':'localhost',
        'PORT':'5432',
    }
}

```

postgresql heroku config:

```python
import psycopg2 #need to install
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

import dj_database_url #need to install
DATABASES={}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

```
<h4>Step 2: Upload the local postgresql databse onto heroku</h4>
Install postgresql.<br>
During instlallation remember the password that is asked for postgres user let this be 'PassWord'<br>
Add the bin and lib folder of postgresql to path<br>

```cli
Control Panel
  All Control Panel Items
    System
      Advanced System Settings
        Environment Variables
          from the System Variables box select "PATH"
              Edit...
    
   ;C:\Program Files\PostgreSQL\9.2\bin;C:\Program Files\PostgreSQL\9.2\lib
```

Create a database in postgresql
<br><br>
<img src="https://github.com/nabaneetLahiri/django-blog/blob/master/readme%20img/db1.PNG">
<br><br>
Name of new database is website
<br><br>
<img src="https://github.com/nabaneetLahiri/django-blog/blob/master/readme%20img/db2.PNG">
<br><br>
Open anaconda promt run

```cli
heroku login
heroku pg:info -a blogged-basic
```
blogged-basic is the name of app in heroku
<br><br>
```cli
=== DATABASE_URL
Plan:                  Hobby-dev
Status:                Available
Connections:           2/20
PG Version:            11.6
Created:               2019-12-06 14:15 UTC
Data Size:             9.0 MB
Tables:                13
Rows:                  64/10000 (In compliance)
Fork/Follow:           Unsupported
Rollback:              Unsupported
Continuous Protection: Off
Add-on:                postgresql-convex-45212
```
Take note of value in 'Addon' field this is the heroku database let this be 'postgresql-convex-45212'
<br><br>
run 

```cli
SET PGUSER=postgres
SET PGPASSWORD=PassWord
heroku pg:push postgres://localhost/website  postgresql-convex-45212
```
here localhost can be replaced by name_of_host, website can be replaced by name_of_local_database and postgresql-convex-45212 replaced by nameOfHerokuDB in general the command will look like.

```cli
heroku pg:push postgres://name_of_host/name_of_local_database nameOfHerokuDB
```
