from django.urls import path
from .views import *
urlpatterns = [
    path('studentList/',StudentListView.as_view(),name="StudentListView"), # ListView

    path('studentDetail/<int:pk>',StudentDetailView.as_view(),name="StudentDetailView")# DetailView

]
