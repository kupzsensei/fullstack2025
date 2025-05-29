# create a directory/folder

1. go to that folder
```
cd name_of_folder
```

2. create a virtual env.
    - for windows
    venv\Scripts\activate
    - for linux
    source venv/bin/activate

3. install django
```
pip install django
```

4. create django project
```
django-admin startproject core .
```

5. run django server
```
python manage.py runserver
```

6. migrate database
```
python manage.py migrate
```

7. create a admin account
```
python manage.py createsuperuser
```

8. create django apps
```
python manage.py startapp products
```

9. update Database
```
python manage.py makemigrations
python manage.py migrate
```

