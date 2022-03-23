from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

def inicio(request): #función que permite acceder a la vista
    return render(request, 'paginas/inicio.html')

def nosotros(request):#Renderizar documento html
    return render(request, 'paginas/nosotros.html')
def libros(request):
    #obtenemos todos los libros
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request):
    return render(request, 'libros/editar.html')

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')
