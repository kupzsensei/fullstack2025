from rest_framework import serializers
from .models import Student , Gender , EducationalBackground

class StudentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        depth = 1
        fields = [
            'id',
            'first_name', 
            'last_name',
            'middle_name', 
            'birth_date', 
            'gender', 
            'nationality' , 
            'religion' , 
            'contact_number' , 
            'email' , 
            'address' , 
            'birth_place' , 
            'lrn_number',
            'educational_background',
        ]

class StudentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # depth = 1
        fields = [
            'id',
            'first_name', 
            'last_name',
            'middle_name', 
            'birth_date', 
            'gender', 
            'nationality' , 
            'religion' , 
            'contact_number' , 
            'email' , 
            'address' , 
            'birth_place' , 
            'lrn_number',
        ]



class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"