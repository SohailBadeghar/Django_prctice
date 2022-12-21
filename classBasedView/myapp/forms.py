from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(max_length=255)