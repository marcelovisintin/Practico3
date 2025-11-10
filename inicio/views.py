from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Maquina

def principal(request):
   
    return render (request, 'inicio.html')

def paradas(request):
    return render (request, 'paradas.html')

def crear_maquina(request,marca, proceso, descripcion):
    maquina=Maquina(marca=marca, proceso=proceso, descripcion=descripcion)
    maquina.save()
    
    return render (request, 'crear_maquina.html', {'maquina_cargada':maquina})   

def listado_maquinas(request):
    
    maquinas = Maquina.objects.all()
    
    return render (request, 'listado_maquinas.html',{'listado_de_maquinas':maquinas})