from django.shortcuts import render,HttpResponse

# Create your views here.

def fun2(request):
    return HttpResponse("<h1> Hello This is myapp2</h1>")
