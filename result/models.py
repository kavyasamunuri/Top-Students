from django.db import models

# Create your models here.
class student(models.Model):
    student_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    email_address=models.CharField(max_length=100)
    marks=models.CharField(max_length=5)
    grade=models.CharField(max_length=5)
    result=models.CharField(max_length=5)
    def __str__(self):
        return self.student_name