from django.db import models

# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=50) # varchar 50
    age = models.IntegerField()
    gpa = models.DecimalField(max_digits=3 , decimal_places=2)
    gender = models.CharField(max_length=10,choices= [("m" , "male") , ("f" , "female")])
    
    def __str__(self):
        return self.name