from django.db import models
from django.db.models.base import Model
# Create your models here.
class Producto(models.Model):
    nombre_pro =  models.CharField(max_length=50,default='')
    precio_pro = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre_pro

class Comuna(models.Model):
    nombre_c =  models.CharField(max_length=50,default='')
    def __str__(self):
        return self.nombre_c

class Cliente(models.Model):
    rut =  models.CharField(max_length=13)
    nombre_cli = models.CharField(max_length=50,default='')
    apellido_cli = models.CharField(max_length=50,default='')
    fecha_nac = models.DateTimeField('Fecha de nacimiento del cliente')
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100, default=' ')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, default=' ')
    contrasena = models.CharField(max_length=50)
    contrasena_val = models.CharField(max_length=50)
    def __str__(self):
        return self.rut

