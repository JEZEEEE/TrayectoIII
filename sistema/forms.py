from django import forms
from .models import Persona, Usuario, Rol, Permiso
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinLengthValidator

#funciones de validacion del formulario de registro de la persona para el sistema
def validar_nombre_apellido(value):
    if len(value) < 2:
        raise ValidationError('Debe tener al menos 2 caracteres.')

def validar_contraseña(value):
    if len(value) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
    if not any(char.isdigit() for char in value):
        raise ValidationError('La contraseña debe contener al menos un número.')
    if not any(char.isalpha() for char in value):
        raise ValidationError('La contraseña debe contener al menos una letra.')

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    fky_rol = forms.ModelChoiceField(queryset=Rol.objects.all(), label='Rol')

    class Meta:
        model = Persona
        fields = ['nom_per', 'ape_per', 'cor_per', 'fky_rol', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels={
            'nom_per':'Nombre',
            'ape_per':'Apellido',
            'cor_per':'Correo',
            'fky_rol':'Rol'   
       }         
        error_messages = {
            'nom_per': {
                'required': 'Este campo es obligatorio.',
                'min_length': 'Debe tener al menos 2 caracteres.',
            },
            'ape_per': {
                'required': 'Este campo es obligatorio.',
                'min_length': 'Debe tener al menos 2 caracteres.',
            },
            'cor_per': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un correo electrónico válido.',
            },
            'password': {
                'required': 'Este campo es obligatorio.',
            },
            'fky_rol': {
                'required': 'Debe seleccionar un rol.',
            },
        }
    nom_per = forms.CharField(validators=[validar_nombre_apellido])
    ape_per = forms.CharField(validators=[validar_nombre_apellido])
    password= forms.CharField(validators=[validar_contraseña])
    cor_per = forms.EmailField(validators=[EmailValidator()])    
    
    def clean_cor_per(self):
        cor_per = self.cleaned_data.get('cor_per')
        if Persona.objects.filter(cor_per=cor_per).exists():
            raise ValidationError('Este correo electrónico ya está en uso.')
        return cor_per
    
    def save(self, commit=True):
        persona = super().save(commit=False)
        persona.est_per = 'A'  # Estado activo por defecto
        if commit:
            persona.save()
            usuario = Usuario(
                cor_usu=self.cleaned_data['cor_per'],
                con_usu=self.cleaned_data['password'],
                fky_per=persona,
                fky_rol=self.cleaned_data['fky_rol'],
                est_usu='A'  # Estado activo por defecto
            )
            usuario.save()
        return persona

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Contraseña')

class AsignarRolPermisosForm(forms.Form):
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), label='Rol')
    permisos = forms.ModelMultipleChoiceField(queryset=Permiso.objects.all(), widget=forms.CheckboxSelectMultiple, label='Permisos')

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario')
        super().__init__(*args, **kwargs)

    def save(self):
        rol = self.cleaned_data['rol']
        permisos = self.cleaned_data['permisos']
        self.usuario.fky_rol = rol
        self.usuario.save()
        # Asignar permisos (suponiendo que hay un campo M-M para permisos en el modelo Usuario)
        self.usuario.permisos.set(permisos)
        self.usuario.save()


class ModificarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cor_usu', 'con_usu', 'fky_per', 'fky_rol', 'est_usu']
        fky_per = forms.ModelChoiceField(queryset=Persona.objects.all(), to_field_name="cod_per")
        fky_rol = forms.ModelChoiceField(queryset=Rol.objects.all(),to_field_name="cod_rol")
        
