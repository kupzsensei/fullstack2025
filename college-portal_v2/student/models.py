from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50) # unique together with lastname and middle name
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True , null=True)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    address = models.TextField()
    birth_place = models.CharField(max_length=50)
    lrn_number = models.CharField(max_length=20)
    gender = models.ForeignKey("Gender" , on_delete=models.CASCADE)
    # educational_background
    # degree
    # guardian

    def __str__(self):
        return f"{self.last_name} , {self.first_name} {self.middle_name[0].upper()}."

class Gender(models.Model):
    name = models.CharField(max_length=50 , unique=True)

    def __str__(self):
        return self.name
    
class EducationalBackground(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE , related_name='educational_background')
    highschool_name = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    year_graduated = models.IntegerField()
    general_average = models.DecimalField(max_digits=10 , decimal_places=2, blank=True, null=True)
    school_address = models.TextField()

    def __str__(self):
        return f"{self.highschool_name} , {self.student}"

class Degree(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE , related_name='degree')
    school_attended = models.CharField(max_length=50)
    degree_earned = models.CharField(max_length=50)
    year_graduated = models.CharField(max_length=50)
    latin_honors = models.CharField(max_length=50, null=True , blank=True)
    thesis_title = models.CharField(max_length=50)
    school_address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.student} , {self.degree_earned}'
    

class GuardianInformation(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE , related_name="guardian")
    full_name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    relationship = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return f"{self.student} , {self.full_name}"