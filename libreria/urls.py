#Las rutas que maneja djnago, permiten ingresar y determinar si el usuario escribe algo en la url del navegador
from django.urls import path
from . import views

urlpatterns = [ #El  usuario accede a la vista. Redireccionamiento
    path('inicio', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
]