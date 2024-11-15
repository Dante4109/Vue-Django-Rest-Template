Django server: 

### Start Django Server

`python manage.py runserver`

### Create all migrations

`python manage.py makemigrations`

### Update tables in DB via migration files

`python manage.py migrate`

### Create migrations for a single app

`python manage.py makemigrations --name app_name --empty` *creates empty

*migration to be coded manually*

`python manage.py startapp *app_name* ./backend/*app_name*`

### Create super user 

python manage.py createsuperuser

## Default example 

user:admin@example.com
pw:password