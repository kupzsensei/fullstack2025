from django.contrib import admin
from .models import Student ,Gender , Course , College , StudentCourse

# Register your models here.
admin.site.register(Student)
admin.site.register(Gender)
admin.site.register(Course)
admin.site.register(College)
admin.site.register(StudentCourse)