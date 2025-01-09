from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'salvando_patas/index.html')

def organization(request):
    '''Muestra mision, nombre, logo,vision, etc...'''
    objetos = Organization.objects.all()
    context = {'objetos':objetos}
    return render(request,'salvando_patas/organizacion.html',context)

def miembros(request):
    objetos = TeamMember.objects.all()
    context = {'objetos':objetos}
    return render(request,'salvando_patas/miembros.html',context)

def actividades(request):
    objetos = Activity.objects.all()
    context = {'objetos':objetos}
    return render(request,'salvando_patas/actividades.html',context)

def problematica(request):
    objetos = Issue.objects.all()
    context = {'objetos':objetos}
    return render(request,'salvando_patas/problematica.html',context)

def como_ayudar(request):
    objetos = HelpOption.objects.all()
    context = {'objetos':objetos}
    return render(request,'salvando_patas/como_ayudar.html',context)

def recursos(request):
    objetos = Resource.objects.all()
    context = {'objetos':objetos}
    return render(request,'salvando_patas/recursos.html',context)

def donacion(request):
    objetos = Donation.objects.all()
    context = {'objetos':objetos}
    return render(request,'salvando_patas/donacion.html',context)