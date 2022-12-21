from django.urls import path
from myapp import views

urlpatterns = [
    
    path('func/',views.func_based , name='func_based'),

    path('cl/',views.Fucn_based.as_view(), name='func_based.as_view'),

    path('subcl/',views.Fucn_basedchild.as_view(), name='func_basedchild'),

    path('homecl/',views.HomeView.as_view(), name='homeview'),

    path('Aboutview/',views.AboutClassView.as_view(), name='AboutClassView'),

    path('contactfun/',views.contactfun, name='contactfun'),

    path('contactcl/',views.ContactClassView.as_view(), name='contactcl'),



]

