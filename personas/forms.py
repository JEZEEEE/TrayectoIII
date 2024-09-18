from django import forms
from .models import Persona
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinLengthValidator
import re
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nom_per', 'ape_per', 'cor_per', 'fky_tip_per', 'est_per']
        widgets = {
            'est_per': forms.TextInput(attrs={'maxlength': 1}),
        }


def validar_nombre_apellido(value):
        if len(value) < 2:
            raise ValidationError('Debe tener al menos 2 caracteres.')
        if not re.match("^[a-zA-ZÀ-ÿ\u00f1\u00d1\s]+$", value):
            raise ValidationError('El nombre solo debe contener letras.')

        nom_per = forms.CharField(validators=[validar_nombre_apellido])
        ape_per = forms.CharField(validators=[validar_nombre_apellido])
        cor_per = forms.EmailField(validators=[EmailValidator()])