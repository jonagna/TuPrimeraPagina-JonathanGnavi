from django.shortcuts import render
from .models import Marca, Auto, Cliente

def home(request):
    return render(request, "autos/home.html")
