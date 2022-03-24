from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

def inicio(request): #función que permite acceder a la vista
    return render(request, 'paginas/inicio.html')

def acerca(request):#Renderizar documento html
    return render(request, 'paginas/acerca.html')
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

def editar(request, id):
    #Creamos la consulta de libro a través del método get
    libro = Libro.objects.get(id=id)
    #Pasamos esa consulta al formulario para que muestre los datos
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')
