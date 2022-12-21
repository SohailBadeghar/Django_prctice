from django import forms

class UserResgistrationsForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'Please enter a name'})
    email = forms.EmailField()
    phone_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())    