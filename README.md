# Python - APIs - Create REST APIs II

## Validation and Sanitization in DRF

2nd exercise for creating REST APIs with DRF

## Exercise Instructions

- For this exercise, we will be using the Django/DRF project created for the last exercise and will check validation and sanitize the incoming data.

- You can find this project in the `dciproject` folder.

Here is the folder tree structure:

```
python-apis-create-II
├─ README.md
└─ dciproject
    ├─ env
    ├  ├─ lib/
    │  ├─ bin/
    │  └─ pyvenv.cfg
    │  └─ pyvenv.cfg
    └─ my_project
      ├─ customer
      │  ├─ __init__.py
      │  ├─ __pycache__/
      │  ├─ admin.py
      │  ├─ apps.py
      │  ├─ migrations
      │  │  ├─ 0001_initial.py
      │  │  ├─ __init__.py
      │  │  └─ __pycache__/
      │  ├─ models.py
      │  ├─ serializers.py
      │  ├─ tests.py
      │  ├─ urls.py
      │  └─ views.py
      ├─ db.sqlite3
      ├─ manage.py
      ├─ my_project
      │  ├─ __init__.py
      │  ├─ __pycache__/
      │  ├─ asgi.py
      │  ├─ settings.py
      │  ├─ urls.py
      │  └─ wsgi.py
      └─ product
         ├─ __init__.py
         ├─ __pycache__/
         ├─ admin.py
         ├─ apps.py
         ├─ migrations
         │  ├─ 0001_initial.py
         │  ├─ __init__.py
         │  └─ __pycache__/
         ├─ serializers.py
         ├─ tests.py
         ├─ urls.py
         └─ views.py

```

- In order to start the `my_project` app, run the following in your terminal:

```
$ cd dciproject & cd my_project
```

Activate the virtual environment

```
$ source env/bin/activate
```

Run the Django server

```
(env)$ python3 manage.py runserver
```

- Please follow the steps below.

### 0. Add a model level validator to the customer REST APIs so that no Customer is created with the same name in the same year.

### 1. Add a model level validator to the product REST APIs such that no product is created with the same name and image.

### 2. Check validations for Product API using `python3 manage.py` shell command and then the `repr()` command (as done in lecture).

### 3. Check validations for Customer API using `python3 manage.py` shell command and then the `repr()` command (as done in lecture).

### 4. Add sanitization using the [Django-htmlsanitizer](https://pypi.org/project/django-html_sanitizer/) to the product APIs such that it only accepts input from 'a', 'p' and 'input' HTML tags

### 5. Add sanitization using the [Django-htmlsanitizer](https://pypi.org/project/django-html_sanitizer/) to the customer APIs such that it only accepts input from 'a', 'p' and 'input' HTML tags.
