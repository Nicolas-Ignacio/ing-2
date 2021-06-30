from django import forms
from django.forms import ModelForm, fields
from .models import Ropa
 
class ropaForm(ModelForm):
    class Meta:
        model = Ropa
        fields = ['idRopa', 'marcaRopa', 'precioRopa', 'descripcionRopa', 'imagenRopa','categoriaRopa']
