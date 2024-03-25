from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

from django.shortcuts import render
# Request: Para realizar peticiones
# HttpResponse: para enviar la respuesta usando el protocolo HTTP.

# Esto es una vista
def bienvenida(request):
    # Pasamos un objeto del tipo request como primer argumento 
    return HttpResponse("Bienvenido o bienvenida a este curso de Django. :)")

def bienvenidaRojo(request):
    # Pasamos un objeto del tipo request como primer argumento 
    return HttpResponse("<p style='color: red'>Bienvenido o bienvenida a este curso de Django. :)</p>")

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "Adultez"
    else:
        if edad < 10:
            categoria = "Infancia"
        else:
            categoria = "Adolescencia"
    
    resultado = "<h1>Categoría de la edad: %s</h1>" %categoria
    return HttpResponse(resultado)

def obtenerMomentoActual(request):
    # respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now())
    respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S'))
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
        <body>
            <p>Nombre: %s / Edad: %s</p>
        </body>
    </html>
    """ % (nombre, edad)
    
    return HttpResponse(contenido)

def miPlantilla(request):
    # abrimos el documento que contiene la plantilla
    plantillaExterna = open('./plantillas/plantilla.html')
    # Cargar el documente en una variable de tipo 'Template': 
    template = Template(plantillaExterna.read())
    # cerrar el documento por temas de seguridad y rendimiento
    plantillaExterna.close()
    # crear un contexto
    contexto = Context()
    # renderizamos el documento
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaParametros(request):
    nombre = "Engellundez"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", 'javascript', "java", "C#", "Kotlin"]
    # abrimos el documento que contiene la plantilla
    plantillaExterna = open('./plantillas/plantillaParametros.html')
    # Cargar el documente en una variable de tipo 'Template': 
    template = Template(plantillaExterna.read())
    # cerrar el documento por temas de seguridad y rendimiento
    plantillaExterna.close()
    # crear un contexto
    contexto = Context({'nombreCanal': nombre, 'fechaActual': fechaActual, 'lenguajes': lenguajes})
    # renderizamos el documento
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaCargador(request):
    nombre = "Engellundez"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", 'javascript', "java", "C#", "Kotlin", 'PHP']
    # Especificamos la carpeta donde están las plantillas en Settings 
    # TEMPLATES>Dir
    # e inicializamos el template ahora con el nombre de la plantilla
    plantillaExterna = get_template('plantillaParametros.html')
    # Renderizar el documento a renderizar
    documento = plantillaExterna.render({'nombreCanal': nombre, 'fechaActual': fechaActual, 'lenguajes': lenguajes})
    return HttpResponse(documento)

def plantillaShortcut(request):
    nombre = "Engellundez"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", 'Javascript', "Java", "C#", "Kotlin", 'PHP', 'C++']
    
    return render(request, 'plantillaParametros.html', {'nombreCanal': nombre, 'fechaActual': fechaActual, 'lenguajes': lenguajes})

def plantillaHija(request):    
    return render(request, 'plantillaHija.html',)

def plantillaHija2(request):    
    return render(request, 'plantillaHija2.html',)