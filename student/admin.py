from django.contrib import admin

# Register your models here.
from .models import Student , StudentCourses , StudentMTMCourses
admin.site.register(Student)
admin.site.register(StudentCourses)
admin.site.register(StudentMTMCourses)