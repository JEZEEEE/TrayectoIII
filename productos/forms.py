from django import forms
from .models import Producto, Categoria, Marca
from .validators import validate_only_letters
import re

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nom_prod', 'pre_prod', 'fky_cat', 'fky_mar', 'est_prod']

    # Filtramos las categorías y marcas con estado 'A' (activo)
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        
        # Filtrar solo las categorías activas
        self.fields['fky_cat'].queryset = Categoria.objects.filter(est_cat='A')
        
        # Filtrar solo las marcas activas
        self.fields['fky_mar'].queryset = Marca.objects.filter(est_mar='A')

    # Validación personalizada para 'nom_prod'
    def clean_nom_prod(self):
        nom_prod = self.cleaned_data.get('nom_prod')
        validate_only_letters(nom_prod)  # Usa la función de validación
        return nom_prod

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nom_cat', 'est_cat']
        labels = {
            'nom_cat': 'Nombre de la Categoría',
            'est_cat': 'Estado',
        }
        error_messages = {
            'nom_cat': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'Máximo 50 caracteres permitidos.',
            },
            'est_cat': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'Máximo 1 carácter permitido.',
            },
        }
        
    def clean_nom_cat(self):
        nom_cat = self.cleaned_data.get('nom_cat')
        validate_only_letters(nom_cat)  # Usa la función de validación
        return nom_cat
    
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nom_mar', 'est_mar']
        labels = {
            'nom_mar': 'Nombre de la Marca',
            'est_mar': 'Estado',
        }
        error_messages = {
            'nom_mar': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'Máximo 50 caracteres permitidos.',
            },
            'est_mar': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'Máximo 1 carácter permitido.',
            },
        }
        
    def clean_nombre_marca(self):
        nom_mar = self.cleaned_data.get('nom_mar')
        validate_only_letters(nom_mar)  # Usa la función de validación
        return nom_mar