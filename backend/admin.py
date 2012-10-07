#! /usr/bin/python
# -*- coding: UTF-8 -*-
from backend.models import *
from django.contrib import admin

class AdminInscripcion(admin.ModelAdmin):
    list_display = ("id","cedula","nombre" )
    
class AdminEstudiante(admin.ModelAdmin):
    list_display = ("id","nombre_estudiante","apellido_estudiante", "cedula")
    
admin.site.register(Inscripcion, AdminInscripcion)
admin.site.register(Estudiante, AdminEstudiante)



