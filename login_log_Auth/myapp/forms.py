from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label = 'confirm Password (again)',widget=forms.PasswordInput)
    # first_Name = forms.CharField(label='First Name ', min_length=4, max_length=150)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
        labels = {'email':'Email'}