from appcoder.models import Curso, Profesor
from django.http import HttpResponse
from django.shortcuts import render
from appcoder.forms import ProfesorFormulario



def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

 
def creacion_curso(request):
   
    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]
              
        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()

    return render(request, "appcoder/curso_formulario.html")
    

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")



def creacion_profesores(request):

    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        # validamos que el formulario no tenga problemas 
        if formulario.is_valid():
            #recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])

            profesor.save()


    formulario = ProfesorFormulario()   
    contexto = {"formulario": formulario}    
    return render(request, "appcoder/profesores_formularios.html", contexto)    







def buscar_curso(request):

    return render(request, "appcoder/busqueda_cursos.html")
    

def resultados_busqueda_cursos(request):
    nombre_curso = request.GET["nombre_curso"]

    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)

    return render(request, "appcoder/resultados_busqueda_cursos.html", {"cursos": cursos})
    pass







def entregables(request):
    return render(request, "appcoder/entregables.html")