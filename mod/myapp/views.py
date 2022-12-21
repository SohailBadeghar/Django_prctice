from django.shortcuts import render
from .models import *
# Create your views here.


def student_info(request):
   stud = StudentModel.objects.all()
   return render(request,'myapp/home.html',{'stu':stud})