from django.shortcuts import render
from .forms import *
from django.contrib import messages
# Create your views here.


def reg(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,"Your Account has been successfully registered!!!")
            messages.info(request," now you can login to your account")
    else:
        fm = StudentRegistration()
    return render(request, 'myapp/index.html', {'form':fm})