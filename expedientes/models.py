from django.db import models

class Expediente(models.Model):
    expendiente= models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField("Fecha de creacion")
    numero = models.IntegerField()
    letra = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
	
