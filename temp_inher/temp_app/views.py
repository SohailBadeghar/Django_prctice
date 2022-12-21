from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'temp_app/Home.html')   

def About(request):
    return render(request,'temp_app/about.html')    