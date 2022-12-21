import email
from django import forms

class UserResgistrationsForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(label = 'Password(again)',widget=forms.PasswordInput)
