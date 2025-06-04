from django.contrib import admin
from .models import Courses , CourseType

# Register your models here.
admin.site.register(Courses)
admin.site.register(CourseType)