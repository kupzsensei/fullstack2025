from django.contrib import admin
from .models import Enrollment , EnrollmentStatus , EnrollmentType , ModeOfLearning

# Register your models here.
admin.site.register(Enrollment)
admin.site.register(EnrollmentStatus)
admin.site.register(EnrollmentType)
admin.site.register(ModeOfLearning)