
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserResgistrationsForm
from .models import *
# Create your views here.


def  thankyou(request):
    return render(request,'myapp/success.html')


def showFormData(request):
    if request.method == 'POST':
        fm = UserResgistrationsForm(request.POST)
        print("post request")
        if fm.is_valid():
            # first way to get data, Always prefer this way to get data from forms

            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pn = fm.cleaned_data['phone_no']
            ps =  fm.cleaned_data['password']
            rps = fm.cleaned_data['repassword']

            reg = Student(  name=nm,email=em,phone_no=pn,password=ps,repassword=rps)
            reg.save()
            
            # print('Data is valid')
            # print('name:',nm )
            # print('email:', em)
            # print('phone_no:', pn)
            # print('password:',  ps )
            # print('password:',  rps )

            return HttpResponseRedirect('/reg/success/')
            # return render(request,'myapp/success.html',{'nm':name})  

    else:
        fm = UserResgistrationsForm()
        print('get request')
    return render(request,'myapp/home.html',{'form':fm})  