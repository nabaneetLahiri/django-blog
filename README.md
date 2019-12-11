<h1>Basic blog app using django.</h1>
https://blogged-basic.herokuapp.com/

<h3>Problem using sqlite.</h3>
After the dyno, in heroku, sleeps the data base gets reset. Solution for this is using postgresql.
<h4>Step 1: We need to change setting.py file:</h4>
postgres local system config:

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

postgres heroku config:

```python
import psycopg2 #need to install
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

import dj_database_url #need to install
DATABASES={}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

```
