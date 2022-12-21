from django.urls import path
from .views import *
urlpatterns = [
        path('sign_up/',sign_up, name='sign_up'),
        path('login/',User_login, name='login'),
        path('User_profile/',User_profile, name='user_profile'),
        path('user_logout/',User_logout, name='user_logout'),
        path('change_password/',ChangePassword, name='change_password'),
        path('user_details/<int:id>/',user_details, name='user_details'),
]