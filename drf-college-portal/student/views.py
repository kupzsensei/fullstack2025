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

