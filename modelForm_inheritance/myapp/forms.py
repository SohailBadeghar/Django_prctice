from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_name', 'email', 'password']

class TecherRegistration(forms.ModelForm):
    class Meta(StudentRegistration.Meta):
        fields = ['techers_name', 'email', 'password']
