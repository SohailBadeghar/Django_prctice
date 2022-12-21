from django import forms

class UserResgistrationsForm(forms.Form):
    # name = forms.CharField(min_length=5,max_length=20, error_messages={'required': 'Please enter a name'})
    name = forms.CharField()
    email = forms.EmailField()
    phone_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())    
    #cleaning and validating fields
    def clen_name(self):
        valname = self.cleaned_data['name']
        print(valname)  
        if len(valname) < 4:
            raise forms.ValidationError('Enter more than 4 characters or equal to 4')
        return valname      