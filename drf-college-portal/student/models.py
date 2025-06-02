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
