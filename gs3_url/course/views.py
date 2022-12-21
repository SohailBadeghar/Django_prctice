from django.shortcuts import render,HttpResponse
# Create your views here.

def show(request):
    return HttpResponse("Hello World!")

def render_page(request):
    return render(request, 'course/home.html')
