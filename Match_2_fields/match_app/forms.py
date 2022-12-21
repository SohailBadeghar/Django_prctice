from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    repassword1 = forms.CharField(label = 'Password(again)',widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        new1 = self.cleaned_data['name']
        new2 = self.cleaned_data['email']
        val = self.cleaned_data['password1']
        val2 = self.cleaned_data['repassword1']  

        if val != val2:
            raise forms.ValidationError("Password Does Not Match")