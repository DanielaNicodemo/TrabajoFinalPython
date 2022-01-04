from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Contacto
from AppCoder.models import Producto
from AppCoder.models import Categoria
from AppCoder.forms import ContactoFormulario

# Create your views here.
def inicio(request):
   # return HttpResponse("Esto es una prueba del inicio")
   return render(request, "AppCoder/inicio.html")

def makeup(request):
   
   return render(request, "AppCoder/makeup.html")

def skincare(request):
   
   return render(request, "AppCoder/skincare.html")

def productos(request):
   productos = Producto.objects.all()

   context = {"productos": productos,
              }

   return render(request, "AppCoder/productos.html", context)

def detalles(request, producto_id):
   obj = Producto.objects.get(pk=producto_id)
   context = {"producto": obj}

   return render(request, "AppCoder/detalles.html", context)

def contacto(request):

   if request.method == "POST":

      miFormulario= ContactoFormulario(request.POST)
      if miFormulario.is_valid():
         informacion= miFormulario.cleaned_data

         contactoInsta = Contacto(nombre=informacion["nombre"], mail=informacion["mail"], telefono=informacion["telefono"], mensaje=informacion["mensaje"])
         contactoInsta.save()
         return render(request, "AppCoder/inicio.html")


   else:

      miFormulario= ContactoFormulario()   
   
   return render(request, "AppCoder/contacto.html", {"miFormulario": miFormulario})


