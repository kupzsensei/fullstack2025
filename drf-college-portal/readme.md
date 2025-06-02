# Django Rest Framework

## 1. DRF Installation
```
pip install djangorestframework
```

> always use pip freeze > requirements.txt after pip install.

## 2. add `rest_framework` to your installed apps @ `settings.py`
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## 3. sample model
```python
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50 )
    middle_name = models.CharField(max_length=50 , blank=True , null=True)
    birth_date = models.DateField()
    address = models.TextField()
    gender = models.ForeignKey("Gender" , on_delete=models.CASCADE)
    email = models.EmailField()
    contact_number = models.IntegerField()
    emergency_contact = models.IntegerField()
    
    def __str__(self):
        return f'{self.last_name.title()}, {self.first_name.title()} {self.middle_name[0].title()}.'
    


class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name.title()
```

## 4. views.py
```python
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GenderSerializer , StudentSerializer
from .models import Gender, Student

# Create your views here.
class GenderView(APIView):

    def get(self,request):
        queryset = Gender.objects.all().order_by('-id')
        serializer = GenderSerializer(queryset , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = GenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self,request):
        try:
            instance = Gender.objects.get(id=request.data['id'])
        except:
            return Response({"detail": "Not found"}, status=404)
        else:
            serializer = GenderSerializer(instance, data=request.data )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def delete(self,request):
        try:
            instance = Gender.objects.get(id=request.data['id'])
        except:
            return Response({"detail": "Not found"}, status=404)
        else:
            instance.delete()
            return Response({"detail": "Deleted Successfully."})
            


class StudentView(APIView):     
    

    def get(self,request):
        students = Student.objects.all().order_by('last_name')
        serializer = StudentSerializer(students , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        pass

    def patch(self,request):
        pass

    def delete(self,request):
        pass

```

## 5. Serializers.py
```python
from rest_framework import serializers
from .models import Gender , Student

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    gender = GenderSerializer(read_only=True)
    # birth_date = serializers.DateField(write_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        # depth = 1
        # fields = [ 'first_name']
        # extra_kwargs = {
        #     'birth_date': {"write_only": True}
        # }
```

## 6. urls.py
```python
"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from student.views import GenderView , StudentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/gender/' , GenderView.as_view()),     # added
    path('api/student/' ,StudentView.as_view() ),   # i added this
]
```


