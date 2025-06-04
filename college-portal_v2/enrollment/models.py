from django.db import models
from courses.models import Courses
# Create your models here.
class Enrollment(models.Model):
    type = models.ForeignKey("EnrollmentType" , on_delete=models.CASCADE)
    status = models.ForeignKey("EnrollmentStatus", on_delete=models.CASCADE)
    mode_of_learning = models.ForeignKey("ModeOfLearning" , on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=10)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    # scholarship


class EnrollmentType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # documents
    
    def __str__(self):
        return self.name

class EnrollmentStatus(models.Model):
    name = models.CharField(max_length=50 , unique=True)

    def __str__(self):
        return self.name

class ModeOfLearning(models.Model):
    name = models.CharField(max_length=50 , unique=True)

    def __str__(self):
        return self.name
    
class RequiredDocuments(models.Model):
    enrollment = models.ForeignKey(Enrollment , on_delete=models.CASCADE , related_name="documents")
    psa = models.BooleanField(default=False)
    tor = models.BooleanField(default=False)
    transfer_credential = models.BooleanField(default=False)
    good_moral = models.BooleanField(default=False)
    photos_2x2 = models.BooleanField(default=False)
    med_cert = models.BooleanField(default=False)
    vaccination_card = models.BooleanField(default=False)
    valid_id = models.BooleanField(default=False)
    
