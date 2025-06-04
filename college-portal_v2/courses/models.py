from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    type = models.ForeignKey("CourseType", on_delete=models.CASCADE)

class CourseType(models.Model):
    name = models.CharField(max_length=50 , unique=True)

    def __str__(self):
        return self.name
