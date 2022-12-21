from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
# Create your views here.


def  thankyou(request):
    return render(request,'match_app/success.html')


def showFormData(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        print("post request")
        if fm.is_valid():
    #         # first way to get data, Always prefer this way to get data from forms

            # name = fm.cleaned_data['name']
            # email = fm.cleaned_data['email']
            # password = fm.cleaned_data['password']
            # repassword = fm.cleaned_data['repassword']
            print('Data is valid')
            print('name:',fm.cleaned_data['name'] )
            print('email:', fm.cleaned_data['email'])
            print('password:',fm.cleaned_data['password'])
            print('repassword:', fm.cleaned_data['repassword'])
    #         # return HttpResponseRedirect('/reg/success/')
            
            # return render(request,'match_app/success.html',{'nm':name})
            # return render(request, 'match_app/home.html', {'form': fm})

    else:
        fm = StudentRegistration()
        print('get request')
    return render(request,'match_app/home.html',{'form':fm})  