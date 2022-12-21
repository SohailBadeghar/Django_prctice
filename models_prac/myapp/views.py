from django.shortcuts import render
from .models import *   

# Create your views here.

def musicians(request):
    musician_list = Musician.objects.all()
    albums_info = Album.objects.all()
    data = {
        'mt':musician_list,
        'at':albums_info
        }
    return render(request, 'myapp/music.html',  data)


# def albums_details(request):
#     albums_info = Album.objects.all()
#     print('albums_details',albums_info)
#     return render(request, 'myapp/music.html',{'at':albums_info})