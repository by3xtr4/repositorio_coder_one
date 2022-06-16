from django.template import Template, Context, loader  #va si o si
from django.http import HttpResponse
from appCoder.models import Familiares, Integrantes # traigo las clases que necesito
import datetime # va si o si, importantisimo para llamar a la fecha y parametros del estilo

#defino acciones, 
def familia(self):
    familia=Familiares(nombre="Lucas", apellido="Gandini", parentezco="Primo", enRelacion="False")
    familia.save()
    return HttpResponse(f"Integrandes de la Familia<br> {familia.nombre} {familia.apellido}, parentezco: {familia.parentezco}, Actualmente en relación?: {familia.enRelacion}")

def integrantes(self):
    integra=["Lucas Gandini", "Mario Gandini", "Fernando Gandini", "Paula Gandini"]
    for i in integra:
        integrante=Integrantes(nombre=i, fecha=datetime.datetime.now())
        integrante.save()
    return HttpResponse(f"Integrantes almacenados")

#test servidor
def saludar(request):
    texto="Hola Man!"
    return HttpResponse(texto)