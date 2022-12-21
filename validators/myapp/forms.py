from django import forms
from django.core import validators

#custome Validators 
def start_with_s(value):
    if value[0] != 'S' :
        raise forms.ValidationError('Name should start with S')

class UserResgistrationsForm(forms.Form):
    name = forms.CharField(validators=[start_with_s])
    
    #This is built-in validationError
    # name = forms.CharField(validators=[validators.MaxLengthValidator(5)]) 
    email = forms.EmailField()
   