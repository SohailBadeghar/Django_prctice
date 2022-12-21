from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserResgistrationsForm
# Create your views here.


def  thankyou(request):
    return render(request,'myapp/success.html')


def showFormData(request):
    if request.method == 'POST':
        fm = UserResgistrationsForm(request.POST)
        print("post request")
        if fm.is_valid():
            # first way to get data, Always prefer this way to get data from forms

            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            phone_no = fm.cleaned_data['phone_no']
            password =  fm.cleaned_data['password']
            print('Data is valid')
            print('name:',name )
            print('email:', email)
            print('phone_no:', phone_no)
            print('password:',  password )
            return HttpResponseRedirect('/reg/success/')
            # return render(request,'myapp/success.html',{'nm':name})  

    else:
        fm = UserResgistrationsForm()
        print('get request')
    return render(request,'myapp/home.html',{'form':fm})  