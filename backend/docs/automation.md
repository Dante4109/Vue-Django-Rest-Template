The following will need to be performed for the cookie cutter automated script to setup a new webapp django RF backend. The settings file is created via a generator. 

Requirements

Python >= 3.12  
PIP
VS Code

1. Create a virtual environment.
2. Run `pip install requirements.txt`
3. Input Database questions in setup script.
4. Generate settings file based on database input.
5. Run `python manage.py makemigrations users`
6. Run `python manage.py makemigrations profile`
7. Run `python manage.py migrate`

## Database Input Request Types

### Postgresql:

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "",
        "HOST": "localhost",
        "USER": "postgres",
        "PASSWORD": "",
        "PORT": 5432,
    }
}
```

### SQLLite:

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

