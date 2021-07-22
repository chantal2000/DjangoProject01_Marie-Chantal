from django.db import models

from django.db.models.fields import PositiveBigIntegerField

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    Age=models.PositiveSmallIntegerField()
    Roll_number=models.CharField(max_length=5)
    student_id=models.PositiveSmallIntegerField()
    National_Id=models.CharField(max_length=16)
    CHOICES=(
        ('F',"Female"),
        ('M',"Male")
    )
    Gender=models.CharField(max_length=10,choices=CHOICES)
    Guardian_name=models.CharField(max_length=40)
    Email_address=models.EmailField(max_length=30)
    Country=models.CharField(max_length=30)
    profile_image=models.CharField(max_length=20)
    Grade=models.CharField(max_length=2)
    Medical_report=models.FileField(upload_to='uploads',blank=True)
    date_Of_enrollment=models.DateField()
    course_name=models.CharField(max_length=30)
    Laptop_number=models.CharField(max_length=7)
    # Languages=models.ListField()
    # phone_number=models.Phone


    
   