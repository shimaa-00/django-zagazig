from django.db import models
from course.models import Course
# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=50) # varchar 50
    age = models.IntegerField()
    gpa = models.DecimalField(max_digits=3 , decimal_places=2)
    gender = models.CharField(max_length=10,choices= [("m" , "male") , ("f" , "female")])
    # media/students/imagename
    img = models.ImageField(upload_to='students/' , null = True , blank=True)
    status = models.BooleanField(default=True )
    courses = models.ManyToManyField(Course , through='StudentCourses' )

    def __str__(self):
        return self.name
class StudentCourses (models.Model):
    student = models.ForeignKey (Student , on_delete=models.CASCADE , verbose_name='student' , db_column='student_id' , null=True)
    course= models.ForeignKey (Course , on_delete=models.CASCADE , verbose_name='course' , db_column= 'course_code' , null=True)
    grade = models.DecimalField(max_digits=4 , decimal_places=2)
    def __str__ (self):
        return f"student {self.student.name} in course {self.course.name} with grade {self.grade}"
    



class StudentMTMCourses (models.Model):
    name = models.CharField(max_length=50) # varchar 50
    age = models.IntegerField()
    gpa = models.DecimalField(max_digits=3 , decimal_places=2)
    gender = models.CharField(max_length=10,choices= [("m" , "male") , ("f" , "female")])
    # media/students/imagename
    img = models.ImageField(upload_to='students/' , null = True , blank=True)
    status = models.BooleanField(default=True )
    courses = models.ManyToManyField(Course  )