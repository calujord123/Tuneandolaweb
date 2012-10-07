#! /usr/bin/python
# -*- coding: UTF-8 -*-

# +-----------------------------------------------------------------------------+
# |                                                                             |
# |     Nombre archivo:         view_home.py                                    |
# |     Autor:                  Carlos Jordán Murillo                           |
# |                                                                             |
# |     Descripción:                                                            |
# |     Es todo lo que se va a mostrar en la interfaz del usuario.              |
# |                                                                             |
# +-----------------------------------------------------------------------------+

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import *
from django.utils.translation import ngettext
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt

from backend.models import *




# Clase formulario


#    id                  = models.AutoField(primary_key=True)
#    cedula              = models.CharField(max_length=10)
#    numero_matricula    = models.CharField(max_length=15)
#    nombre_estudiante   = models.CharField(max_length=200)
#    apellido_estudiante = models.CharField(max_length=200)
#    telefono            = models.CharField(max_length=10)
#    direccion           = models.TextField()
#    numero_materias_aprobadas   = models.FloatField()
#    promedio_estudiante         = models.FloatField()


class EstudianteForm(forms.Form):
    cedula  = forms.RegexField(help_text="Número de cédula", label=("Cédula o Pasaporte"),max_length=10, regex=r"[0-9]+$", error_message = ("Sólo se permiten números"))
    nombre_estudiante = forms.RegexField(label=("Nombre del Estudiante"), max_length=300, regex= r'[A-Z a-z]+$', error_message= ("Sólo se permiten caracteres"))
    apellido_estudiante= forms.RegexField(label=("apellido del Estudiante"), max_length=300, regex= r'[A-Z a-z]+$', error_message= ("Sólo se permiten caracteres"))
    




def home(request):
    usuario = Inscripcion.objects.all()
    return render_to_response("index.html", {"lista":usuario})


@csrf_exempt
def registrar_estudiante(request):
    formulario = EstudianteForm()
    if request.method == "POST":
        
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            return render_to_response("formulario/registrar_estudiante.html", {"titulo_page":"Registro estudiante exitoso", "formulario":EstudianteForm()})
    return render_to_response("formulario/registrar_estudiante.html", {"titulo_page":"Registro estudiante", "formulario":formulario})


def consultar_estudiantes(request):
    
    lista_estudiante = Estudiante.objects.all()
    return render_to_response("formulario/lista_estudiantes.html",{"titulo_page":"Esto es una prueba con herencia","lista_estudiante":lista_estudiante})
    
    