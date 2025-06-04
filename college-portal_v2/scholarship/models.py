from django.db import models
from enrollment.models import Enrollment

# Create your models here.
class Scholarship(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE , related_name="scholarship")
    provider = models.CharField(max_length=50)
    ref_code = models.CharField(max_length=50 , blank=True , null=True)

    def __str__(self):
        return f"{self.enrollment} , {self.provider}"