from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class EstudianteS(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    emails = models.EmailField

class Profesor(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    emails = models.EmailField
    profesion = models.CharField(max_length=100)

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()   
