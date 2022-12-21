from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.


# def home(request):
#     student_data = Student.objects.all()
#     return render(request,'myapp/home.html',{'student':student_data})

'''
Simple model manger to get the deatils .
'''

# class home(View):

#     def get(self, request):
#         student_data = Student.students.all()
#         # student_data = Student.objects.all() 

#         return render(request,'myapp/home.html',{'student':student_data})



'''
Add extra manager methods :
'''

class home(View):

    def get(self, request):
        # student_data = Student.students.all()
        student_data = Student.students.get_stu_roll_range(1,3)
        return render(request,'myapp/home.html',{'student':student_data})


