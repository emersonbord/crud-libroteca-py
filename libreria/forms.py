from django import forms
from .models import Libro

#
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        #creamos la lectura y el mapeado de nuestro modelo a partir de la declaración del formulario
        fields = '__all__'