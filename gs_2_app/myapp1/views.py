from django.shortcuts import render,HttpResponse

# Create your views here.

def fun1(request):
    return HttpResponse("<h1> Hello This is myapp1</h1>")