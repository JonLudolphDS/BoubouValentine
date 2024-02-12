from django.urls import path
from . import views

urlpatterns = [
    path("alo/", views.home, name='home'),
    path("Shesaidyes/", views.Yes, name='yes'),
    path("Shesaidno/", views.FirstNo, name='no1'),
    path("noagain/", views.SecondNo, name='no2'),
]