from django.shortcuts import render
# from .models import Empleados, Departamentos

# Create your views here.

def index(request):
    return render(request, 'index.html')

 