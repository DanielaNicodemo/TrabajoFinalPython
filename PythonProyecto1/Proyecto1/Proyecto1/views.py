from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Daniiiiiii")

def segundaVista(request):
    return HttpResponse("<br><br>---------holaaaaaa----------")

def dia(request):
    variable= datetime.now()    
    return HttpResponse (f"Hoy es un gran dia<br> {variable}")

def apellido(request, ape):
    fecha= datetime.now()
    return HttpResponse (f"el profe de coder {ape}, es muy bueno..<br><br>,.. por lo menos hoy:->{fecha}")

def cuantosAnios(request, nac): 
    fecha=datetime.now() 
    edad= fecha.year - int(nac)
    return HttpResponse (f"tu edad es: {edad}")

def probandoTemplate(request):
    miHTML= open("C:/Users/osvaldo/Desktop/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")  
    plantilla= Template(miHTML.read())  
    miHTML.close()

    miContexto= Context()

    documento= plantilla.render(miContexto)

    return HttpResponse(documento)


