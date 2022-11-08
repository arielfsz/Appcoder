from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

from datetime import datetime



def vista_saludo(request):

    return HttpResponse("""
        <h1>Hola coders! :) </h1>
        <p style='color:red' >Esto es una prueba</p>
        """)



def iniciar_sesion(request):

    return HttpResponse("Pasame tu usuario y password por whatsapp ;) ")



def dia_hoy(request, nombre):

    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenido {nombre}"

    return HttpResponse(respuesta)



def anio_nacimiento(request, edad):

    edad = int(edad)

    anio_nac = datetime.now().year - edad

    return HttpResponse(f"Naciste en {anio_nac}")



def vista_plantilla(request):

    #abrimos el archivo
    archivo = open(r"C:\Users\crari\OneDrive\Escritorio\Python\Curso Coder\proyecto_coder\proyecto_coder\templates\plantilla_bonita.html")
    
    #creamos el objeto "plantilla" (template)
    plantilla = Template(archivo.read())

    #cerramos el archivo para liberar recursos 
    archivo.close()

    #diccionario con datos para la plantilla
    datos = {"nombre": "Ariel", "fecha": datetime.now(), "apellido": "Fernández"}

    #creamos el contexto 
    contexto = Context(datos)

    #renderizamos la plantilla para crear la respuesta  
    documento = plantilla.render(contexto)

    #retornamos la respuesta 
    return HttpResponse(documento)



def vista_listado_alumnos(request):

    archivo = open(r"C:\Users\crari\OneDrive\Escritorio\Python\Curso Coder\proyecto_coder\proyecto_coder\templates\listado_alumnos.html")

    plantilla = Template(archivo.read())

    archivo.close()

    listado_alumnos = ["Luis Suarez","Sergio Rochet","Felipe Carballo","Camilo Candido","Jose Luis Rodriguez"]
   
    datos = {"tecnologia": "React", "listado_alumnos": listado_alumnos}

    contexto = Context(datos)
    
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)



def vista_listado_alumnos2(request):

    listado_alumnos = ["Luis Suarez","Sergio Rochet","Felipe Carballo","Camilo Candido","Jose Luis Rodriguez"]
   
    datos = {"tecnologia": "React", "listado_alumnos": listado_alumnos}
  
    plantilla = loader.get_template("listado_alumnos.html")
    
    documento = plantilla.render(datos)

    return HttpResponse(documento)



    