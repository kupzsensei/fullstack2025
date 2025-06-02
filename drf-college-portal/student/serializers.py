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