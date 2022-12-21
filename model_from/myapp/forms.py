from django import forms
# from django.core import validators
from .models import *

class StudentRegistration(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name','email', 'phone_no', 'password', 'repassword'] 
       
        # we can do all the modifictions here in modelform 

        # you can chnage the name to show in template by labeling the existing name
        labels = {'name':'Enter Name','phone_no':'Enter Phone Number','password':'Enter Password','repassword':'Renter Password'}  
       

        #for Showing Error Messages in template by overriding django error

        error_messages = {
            'name':{'required':'Please enter a name'},
            'email':{'required':'Please enter a email address'},
            'phone_no':{'required':'Please enter a phone_number'},

        }


        widgets = {
            'password':forms.PasswordInput,
            'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter your Name '}),
        }
                


