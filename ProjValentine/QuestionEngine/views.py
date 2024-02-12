from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "templates/home.html")

def Yes(request):
    return render(request, "templates/YesFirst.html")

def FirstNo(request):
    return render(request, "templates/NoFirst.html")

def SecondNo(request):
    return render(request, "templates/SecondNo.html")