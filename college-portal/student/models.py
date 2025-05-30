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