from django.db import models
from django.core.exceptions import ValidationError
import re

# Modelo de Categoría
class Categoria(models.Model):
    ESTADO_CHOICES = [
    ('A', 'Activo'),
    ('I', 'Inactivo'),
    ]
    cod_cat = models.AutoField(primary_key=True)
    nom_cat = models.CharField(max_length=50)
    est_cat = models.CharField(max_length=1, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.nom_cat

# Modelo de Marca
class Marca(models.Model):
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]
    
    cod_mar = models.AutoField(primary_key=True)
    nom_mar = models.CharField(max_length=50)
    est_mar = models.CharField(max_length=1, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.nom_mar

# Modelo de Producto
class Producto(models.Model):
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]

    cod_prod = models.AutoField(primary_key=True)
    nom_prod = models.CharField(max_length=50)
    pre_prod = models.DecimalField(max_digits=10, decimal_places=2)
    fky_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fky_mar = models.ForeignKey(Marca, on_delete=models.CASCADE)
    est_prod = models.CharField(max_length=1, choices=ESTADO_CHOICES)  # Se agregan las opciones

    def __str__(self):
        return self.nom_prod

# Modelo intermedio para Producto-Categoría
class ProductoCategoria(models.Model):
    cod_prod_cat = models.AutoField(primary_key=True)
    fky_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fky_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    est_prod_cat = models.CharField(max_length=1)

    class Meta:
        unique_together = (('fky_prod', 'fky_cat'),)

    def __str__(self):
        return f'{self.fky_prod} - {self.fky_cat}'

# Modelo intermedio para Producto-Marca
class ProductoMarca(models.Model):
    cod_prod_mar = models.AutoField(primary_key=True)
    fky_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fky_mar = models.ForeignKey(Marca, on_delete=models.CASCADE)
    est_prod_mar = models.CharField(max_length=1)

    class Meta:
        unique_together = (('fky_prod', 'fky_mar'),)

    def __str__(self):
        return f'{self.fky_prod} - {self.fky_mar}'
