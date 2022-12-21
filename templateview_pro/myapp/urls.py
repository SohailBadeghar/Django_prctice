from django.urls import path
from .views import *
urlpatterns = [
    # path('',TemplateView.as_view(template_name = 'myapp/home.html'), name = 'home')

    # path('',Hometemplateview.as_view(), name = 'home')

     path('',Hometemplateview.as_view(extra_context = {'courses':'Django'}), name = 'home'),

      path('About/<int:roll>',Hometemplateview.as_view(), name = 'About')
]

