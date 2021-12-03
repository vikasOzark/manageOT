from django import forms
from django.db.models.base import Model
from django.forms import widgets
from .models import OverTime, Employee


class OverTimeAdd(forms.ModelForm):

    class Meta:
        model = OverTime
        fields = [
            'emp_user',
            'overTime',
            'reaion',
            'date_ot'
        ]

        widgets = {
            'overTime': forms.NumberInput(attrs={'class': 'time-field'}),
            'reaion': forms.TextInput(attrs={'class': 'time-field'}),
            'date_ot': forms.DateInput(attrs = {'class' : 'date_ot', 'placeholder' : ' YYYY-MM-DD'}),

        }

        labels = {
            'emp_user': 'Name of Employee',
            'OverTime': 'OT Time',
            'reaion': 'Reason',
            'date_ot' : 'Date',
        }


class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'emp_name',
            'emp_l_name',
            'emp_email',
            'emp_number',
        ]

        widgets = {
            'emp_name': forms.TextInput(attrs = {'class' : 'form-control'}),
            'emp_l_name': forms.TextInput(attrs = {'class' : 'form-control'}),
            'emp_email': forms.EmailInput(attrs = {'class' : 'form-control'}),
            'emp_number': forms.NumberInput(attrs = {'class' : 'form-control'})
        }

        labels = {
            'emp_name': 'Name',
            'emp_l_name': 'Last Name',
            'emp_email': 'Email',
            'emp_number': 'Phone Number',
        }
