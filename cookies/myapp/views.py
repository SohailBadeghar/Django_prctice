import re
from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.



def setcookies(request):
    response =  render(request,'myapp/setcookies.html')
    response.set_cookie('name','Sohail is Good Programmer!') 
    # response.set_cookie('name','Sohail is Good Programmer!',expires=datetime.utcnow() + timedelta(days=2)) #it will set for days to expire cookies
    # response.set_cookie('name','Sohail is Good Programmer!' , max_age=15)  #it will set the  expire timig ex.this cookie will be set for 15sec only

    return response



def getcookies(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    name = request.COOKIES.get('name','Guest')
    return render(request,'myapp/getcookies.html',{'name':name})


def delcookies(request):
    response =  render(request,'myapp/delcookies.html')
    response.delete_cookie('name')
    return response