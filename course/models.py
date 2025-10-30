from django.db import models

# Create your models here.
class Course (models.Model):
    code = models.AutoField(primary_key= True)
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
