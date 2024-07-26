from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Courses(models.Model):
    Course_Name = models.CharField( max_length=250)
    Course_Fee = models.IntegerField(null=True)
    
    def __str__(self):
        return self.Course_Name

class Student(models.Model):
    Stu_Lname = models.CharField( max_length=250)
    Stu_Fname = models.CharField( max_length=250)
    Stu_Age = models.IntegerField(null=True)
    Stu_Email = models.EmailField(null=True, max_length=254)
    Stu_Number = models.CharField( max_length=250)
    Stu_Address = models.TextField(null=True)
    Stu_Course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    

    



class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    Teach_Age = models.IntegerField(null=True)
    Teach_Number = models.CharField( max_length=250)
    Teach_Address = models.TextField(null=True)
    Teach_Image = models.ImageField(null=True, upload_to='Image/', height_field=None, width_field=None, max_length=None)

    