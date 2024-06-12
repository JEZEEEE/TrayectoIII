from django.db import models

class Rol(models.Model):
    cod_rol = models.AutoField(primary_key=True)
    nom_rol = models.CharField(max_length=50)
    est_rol = models.CharField(max_length=1)

    def __str__(self):
        return self.nom_rol

class Permiso(models.Model):
    cod_perm = models.AutoField(primary_key=True)
    nom_perm = models.CharField(max_length=50)
    des_perm = models.CharField(max_length=220)
    est_perm = models.CharField(max_length=1)

    def __str__(self):
        return self.nom_perm

class Persona(models.Model):
    cod_per = models.AutoField(primary_key=True)
    nom_per = models.CharField(max_length=50)
    ape_per = models.CharField(max_length=50)
    cor_per = models.EmailField(unique=True)
    fky_rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    est_per = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.nom_per} {self.ape_per}"

class Usuario(models.Model):
    cod_usu = models.AutoField(primary_key=True)
    cor_usu = models.EmailField(unique=True)
    con_usu = models.CharField(max_length=50)
    fky_per = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fky_rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    est_usu = models.CharField(max_length=1)

    def __str__(self):
        return self.cor_usu

