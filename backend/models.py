#! /usr/bin/python
# -*- coding: UTF-8 -*-

from django.db import models

# Create your models here.

class Inscripcion(models.Model):
    id                  = models.AutoField(primary_key=True)
    cedula              = models.CharField(max_length=10, help_text="Sólo 10 caracteres")
    nombre              = models.CharField(max_length=120, help_text="Ingrese nombre")
    apellido            = models.CharField(max_length=120, help_text="Ingresar apellido")
    email               = models.EmailField()
    nombre_archivo      = models.ImageField(upload_to='./', blank=False)
    
    def __unicode__(self):
        return self.nombre
    


class Estudiante(models.Model):
    id                  = models.AutoField(primary_key=True)
    cedula              = models.CharField(max_length=10)
    numero_matricula    = models.CharField(max_length=15)
    nombre_estudiante   = models.CharField(max_length=200)
    apellido_estudiante = models.CharField(max_length=200)
    telefono            = models.CharField(max_length=10)
    direccion           = models.TextField()
    numero_materias_aprobadas   = models.FloatField()
    promedio_estudiante         = models.FloatField()
    
    def __unicode__(self):
        return self.apellido_estudiante +" "+self.nombre_estudiante
    
    
