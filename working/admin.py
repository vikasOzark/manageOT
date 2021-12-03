from typing import List
from django.contrib import admin
from .models import Employee, OverTime

# Register your models here.

@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = [ 'id' , 'user', 'emp_name', 'emp_l_name', 'emp_email', 'emp_number']

@admin.register(OverTime)
class OverTimeModelAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'emp_user', 'overTime', 'reaion', 'date_ot']