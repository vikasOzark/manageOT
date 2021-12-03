from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    emp_name = models.CharField(max_length = 250, default = '')
    emp_l_name = models.CharField(max_length = 250, default = '')
    emp_email = models.EmailField(max_length = 250, default = '')
    emp_number = models.IntegerField()
    emp_profile = models.ImageField(upload_to = 'profiles', blank = True)

    def __str__(self):
        return self.emp_name
    
class OverTime(models.Model):
    emp_user = models.ForeignKey(Employee, null = True, on_delete = models.CASCADE)
    overTime = models.FloatField( blank = True, null=True)
    reaion = models.CharField(max_length = 250, blank = True, null=True)
    date_ot = models.DateField(null = True, blank = True)


    def __str__(self):
        return str(self.overTime)