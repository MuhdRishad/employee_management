from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name = models.CharField(max_length=120)
    profile_pic = models.ImageField(upload_to="profilepics",null=True)
    emp_email = models.EmailField(unique=True)
    emp_designation = models.CharField(max_length=120)
    emp_experience = models.PositiveIntegerField(default=0)    # OR (null = 0)
    emp_salary = models.PositiveIntegerField()
    emp_place = models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.emp_name
