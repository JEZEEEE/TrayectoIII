from django.db import models
from django.core.validators import RegexValidator

class TipoPersona(models.Model):
    cod_tip_per = models.AutoField(primary_key=True)  # Clave primaria
    nom_tip_per = models.CharField(max_length=50)  # Nombre del tipo de persona
    est_tip_per = models.CharField(max_length=1)  # Estado del tipo de persona

    def __str__(self):
        return self.nom_tip_per

class Persona(models.Model):
    cod_per = models.AutoField(primary_key=True)  # Clave primaria
    nom_per = models.CharField(max_length=50, validators=[
        RegexValidator(r'^[a-zA-Z ]+$', 'Solo se permiten letras y espacios.')
    ])
    ape_per = models.CharField(max_length=50, validators=[
        RegexValidator(r'^[a-zA-Z ]+$', 'Solo se permiten letras y espacios.')
    ])
    cor_per = models.EmailField(max_length=50, unique=True)  # Correo de la persona
    fky_tip_per = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)  # Clave foránea a tipo_persona
    est_per = models.CharField(max_length=1)  # Estado de la persona

    

    def __str__(self):
        return f"{self.nom_per} {self.ape_per}"
