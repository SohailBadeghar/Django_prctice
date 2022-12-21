from django.shortcuts import render
from .forms import StudentRegistration,TecherRegistration
# Create your views here.

def student_form(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRegistration()
    return render(request,'myapp/Student.html',{'form':fm})


def techer_form(request):
    if request.method == 'POST':
        fm = TecherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = TecherRegistration()
        return render(request,'myapp/techers.html',{'form':fm})
