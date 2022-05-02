from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(self):
    curso=Curso(nombre="Curso de django",comision=12345)
    curso.save()
    texto=f"curso: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)


def inicio(request):
    return HttpResponse(request, "AppCoder/inicio.html")

def profesores(request):
    return HttpResponse(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return HttpResponse("Esta es la pagina de estudiantes")

def cursos(request):
    return HttpResponse("Esta es la pagina de cursos")

def entregables(request):
    return HttpResponse("Esta es la pagina de profesores")
