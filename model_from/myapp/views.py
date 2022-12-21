
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import *
# Create your views here.


def  thankyou(request):
    return render(request,'myapp/success.html')


def showFormData(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        print("post request")
        if fm.is_valid():
            # first way to get data, Always prefer this way to get data from forms

            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pn = fm.cleaned_data['phone_no']
            ps =  fm.cleaned_data['password']
            rps = fm.cleaned_data['repassword']

            #for save the data to the database
            Result = Student(name=nm, email=em, phone_no=pn, password=ps, repassword=rps)
            Result.save()

            #for update in db
            # Result = Student(id = 1,name=nm, email=em, phone_no=pn, password=ps, repassword=rps)
            # Result.save()

            # Result = Student(id = 1)
            # Result.delete()

            # print('Data is valid')
            # print('name:',nm )
            # print('email:', em)
            # print('phone_no:', pn)
            # print('password:',  ps )
            # print('password:',  rps )

            return HttpResponseRedirect('/reg/success/')
            # return render(request,'myapp/success.html',{'nm':name})  

    else:
        fm = StudentRegistration()
        print('get request')
    return render(request,'myapp/home.html',{'form':fm})  