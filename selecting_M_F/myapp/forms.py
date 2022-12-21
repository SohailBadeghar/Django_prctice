from django import forms
from .models import Employee


class EmployeeRegistrationForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['Name','email','Mobile_no']
        # fields = '__all__'




