# Django Step by Step Guide

1. ## create a directory/folder.
```
mkdir <name_of_folder>
```

2. ## go inside that directory/folder.
```
cd <name_of_folder>
```

3. ## create virtual env.
```
python3 -m venv venv    # linux
python -m venv venv     # windows
```

4. ## activate virtual env.
```
source venv/bin/activate    # linux
venv\Scripts\activate       # windows
```

5. ## install django
```
pip install django
```

6. ## check the dependencies
```
pip freeze
```

7. ## save the dependencies into requirements.txt
```
pip freeze > requirements.txt
```

8. ## create django project
```
django-admin startproject core .
```

9. ## migrate the database
```
python manage.py migrate
```

10. ## create admin user
```
python manage.py createsuperuser
```

11. ## create django app
```
python manage.py startapp <name_of_app>
```

12. ## register your app into `settings.py`
    - add your app name inside the list of `INSTALLED_APPS`
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'student', # new app
    ]
    ```

13. ## create a model
`models.py`
```python
from django.db import models

# Create your models here.

class Gender(models.Model):
    name = models.CharField(max_length=15 , unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    address = models.TextField()
    birth_date = models.DateField()
    gender = models.ForeignKey(Gender , on_delete=models.CASCADE)
    email = models.EmailField()
    contact = models.IntegerField()
    emergency_contact = models.IntegerField()

    def __str__(self):
        return f'{self.last_name}, {self.first_name} {self.middle_name}'
    
class College(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    description = models.TextField()
    college = models.ForeignKey(College , on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudentCourse(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} - {self.course}'
```

14. ## register your model to admin panel.
`admin.py`
```python
from django.contrib import admin
from .models import Student ,Gender , Course , College , StudentCourse

# Register your models here.
admin.site.register(Student)
admin.site.register(Gender)
admin.site.register(Course)
admin.site.register(College)
admin.site.register(StudentCourse)
```

15. ## create a migration file
```
python manage.py makemigrations
```

16. ## apply changes to database
```
python manage.py migrate
```

17. ## run server
```
python manage.py runserver
```

18. ## goto 127.0.0.1:8000/admin

### congrats