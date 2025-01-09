from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'salvando_patas/index.html')

def organization(request):
    '''Muestra mision, nombre, logo,vision, etc...'''
    objetos = Organization.objects.all()
    context = {'objetos':objetos}
    return render(request,'salvando_patas/organizacion.html',context)