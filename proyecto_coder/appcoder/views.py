from appcoder.models import Curso
from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request,"appcoder/index.html")

def cursos(request):
    return HttpResponse("Estás en cursos")

def estudiantes(request):
    return HttpResponse("Estás en estudiantes")

def profesores(request):
    return HttpResponse("Estás en profesores")

def entregables(request):
    return HttpResponse("Estás en entregables")
