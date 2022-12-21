from django.shortcuts import render
from    datetime import datetime
# Create your views here.
def Dyanamic_template(request):
    c_name = "djnago"
    duration = '4 months'
    seats = "30"
    # d = datetime.now()
    course_details = {'cn':c_name, 'dt':duration,'st':seats}
    return render(request, 'myapp/home.html', course_details) 

def datetime(request):
    d = datetime.now()
    return render(request, 'myapp/home.html', {'dm':d}) 