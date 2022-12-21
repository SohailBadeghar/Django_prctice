from django import forms    

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    Mobile_No = forms.IntegerField()
    password = forms.CharField(max_length=100)