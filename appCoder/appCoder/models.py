from django.db import models # llamo al paquete para crear las clases
#c
class Familiares(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    parentezco=models.CharField(max_length=40)
    enRelacion=models.BooleanField()

class Integrantes(models.Model):
    nombre=models.CharField(max_length=40)
    fecha=models.TimeField()