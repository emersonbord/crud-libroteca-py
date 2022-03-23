#Las rutas que maneja djnago, permiten ingresar y determinar si el usuario escribe algo en la url del navegador
from django.urls import path
from . import views

urlpatterns = [ #El  usuario accede a la vista. Redireccionamiento
    path('', views.inicio, name='inicio'),
]