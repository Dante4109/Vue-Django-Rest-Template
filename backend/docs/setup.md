When setting up Django Rest Framework the first time it is necessary to run migrations individually.

Using CustomUser will result in the following error.

`django.db.utils.ProgrammingError: relation "users_customuser" does not exist`

`python manage.py makemigrations users`

`python manage.py makemigrations profile`

will resolve this issue. 

Then you can safely run 

`python manage.py migrate`

