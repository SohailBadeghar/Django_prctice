from django.shortcuts import render
from .forms import EmployeeRegistrationForm
# Create your views here.

def ShowFromData(request):
    fm = EmployeeRegistrationForm()
    return render(request, 'myapp/home.html',{'form':fm})