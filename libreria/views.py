from django.shortcuts import render
from django.http import HttpResponse

def inicio(request): #función que permite acceder a la vista
    return render(request, 'paginas/inicio.html')
def nosotros(request):#Renderizar documento html
    return render(request, 'paginas/nosotros.html')
def libros(request):
    return render(request, 'libros/index.html')
def crear(request):
    return render(request, 'libros/crear.html')

