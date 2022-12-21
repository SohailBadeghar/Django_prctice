from django.shortcuts import render

# Create your views here.
def dynamic(request):
    return render(request,'myapp/dynamic.html')


# def show(request,my_id):
#     return render(request,'myapp/home.html',{'id':my_id})

def show(request,my_id):
    if my_id == 1:
        student = {'id':my_id, 'name':'sohail'}
    if my_id == 2:
        student = {'id':my_id, 'name':'sonal'}
    if my_id == 3:
        student = {'id':my_id, 'name':'maddy'}
    return render(request,'myapp/home.html',student)