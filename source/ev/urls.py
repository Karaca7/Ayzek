

from django.urls import path
from django.views.generic import TemplateView

from ev.views import ev,cıkıs,silici,silici2
from django.urls import include
from django.contrib.auth.views import LogoutView









urlpatterns = [


    path("",ev,name='ev'),


    path("cıkıs/",cıkıs , name='cıkıs'),
    path("silici/<int:id>",silici,name='silici'),
    path("silici2/<int:id>",silici2,name='silici2'),

]



