from django.shortcuts import render
from rest_framework import generics
from .models import Gender, Student
from .serializers import StudentGetSerializer , GenderSerializer , StudentPostSerializer

# Create your views here.
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentPostSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
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
