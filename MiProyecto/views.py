from django.http import HttpResponse, response

import datetime

from django.template import Template,Context

from django.template.loader import get_template

from django.shortcuts import render



def bienvenida(request):
     return HttpResponse("Bienvenido a este curso django")
 


def bienvenidaAzul(request):
     return HttpResponse("<p style='color:darkblue'> Bienvenido en Color Azul Oscuro en Django  </p>")
 
 
def categoriaEdad(request,edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera Edad"
        else:
            categoria = "Adultez"
        
    else: 
         if edad < 10:
             categoria = "Infancia"
         else:
             categoria = "Adolescencia"
             
             
             
    resultado = "<h1> Categoría de la edad %s </h1>" %categoria
    return HttpResponse(resultado)


def momentoActual(request):
    respuesta = "<h1> Momento Actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)


def contenidoHTML(request,nombre,edad):
     contenido = """
     <html>
     <body>
     <p> Nombre: %s /Edad: %s </p>
     </body>
     </html>
     """ %(nombre,edad)
     
     return HttpResponse(contenido)
 
 

 
def miPrimeraPlantilla(request):
     plantillaExterna = open("C:/Users/USER/Documents/Sebas/django/MiProyecto/MiProyecto/plantillas/miPrimeraPlantilla.html")
     template = Template(plantillaExterna.read())
     plantillaExterna.close()
     contexto = Context()
     documento = template.render(contexto)
     return HttpResponse(documento)
      
def plantillaParametro(request):
     nombre = "evidenciajs"
     lenguajes = ["Python","Ruby","PHP","JavaScript","C#","Java"]
     fechaActual = datetime.datetime.now()
     plantillaExterna = open("C:/Users/USER/Documents/Sebas/django/MiProyecto/MiProyecto/plantillas/plantillaParametros.html")
     template = Template(plantillaExterna.read())
     plantillaExterna.close()
     contexto = Context({"nombreCanal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
     documento = template.render(contexto)
     return HttpResponse(documento)
 
 
def plantillaCargador(request):
     nombre = "evidenciajs"
     lenguajes = ["Python","Ruby","PHP","Kotlin","JavaScript","C#","Java"]
     fechaActual = datetime.datetime.now()
     plantillaExterna = get_template("plantillaParametros.html")
     documento = plantillaExterna.render({"nombreCanal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
     return HttpResponse(documento)
 
def plantillaShortCut(request):
     nombre = "evidenciajs"
     lenguajes = ["Python","Ruby","PHP","Kotlin","JavaScript","C#","Java","C++"]
     fechaActual = datetime.datetime.now()
     return render(request,'plantillaParametros.html',{"nombreCanal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
 
def plantillaHija1(request):
    return render(request,"plantillaHija_1.html",{})

def plantillaHija2(request):
    return render(request,'plantillaHija_2.html',{})