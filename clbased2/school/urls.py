from django.urls import path
from .views import *
urlpatterns = [
    path('homefun/',homefun,name='homefun'),   #for FunctionBased views urlpatterns
    path('cl/',HomeClassView.as_view(),name='homeclassview'), #for class based views urlpatterns

    ################################################################
    path('About/',AboutFun,name='aboutfun'), #for fun views urlpatterns

    path('About_class/',AboutClassView.as_view(),name='aboutclassview'),   #for class based views urlpatterns

    ################################################################################################


    path('contactfun/',contactfun,name='contactfun'), # for functions based views urlpatterns

    path('contactclass/',ContactClassView.as_view(), name='contactclass'), # for classBased views urlpatterns
]