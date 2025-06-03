# DRF Generics API VIEWS

`views.py`

```python
from django.shortcuts import render
from rest_framework import generics # new import
from .models import Gender, Student
from .serializers import StudentGetSerializer , GenderSerializer , StudentPostSerializer

# Create your views here.
class StudentListCreateView(generics.ListCreateAPIView): # handle List and create or Get and POST http method.
    # student = Student.objects.all()
    # serializer = StudentSerializer(student , many=True)
    # return Response(serializer.data)
    queryset = Student.objects.all() 
    serializer_class = StudentPostSerializer # serializer 

    def get_serializer_class(self):
        if self.request.method == "GET": # check if the http method is GET
            return StudentGetSerializer
        return super().get_serializer_class()

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentPostSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentGetSerializer
        return super().get_serializer_class()


class GenderListCreateView(generics.ListCreateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

```

> Thank you!