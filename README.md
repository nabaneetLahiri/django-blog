<h1>Basic blog app using django.</h1>
https://blogged-basic.herokuapp.com/

<h3>Problem using sqlite.</h4>
After the dyno, in heroku, sleeps the data base gets reset. Solution for this is using postgresql.
<ul>
  <li><h4>Step 1:<h4> We need to change setting.py file:
       postgres local system config:
    <span data-selectable-paragraph>
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
   </span>    
