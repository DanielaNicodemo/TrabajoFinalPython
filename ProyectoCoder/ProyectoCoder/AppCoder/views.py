from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
   # return HttpResponse("Esto es una prueba del inicio")
   return render(request, "AppCoder/inicio.html")

def makeup(request):
   
   return render(request, "AppCoder/makeup.html")

def skincare(request):
   
   return render(request, "AppCoder/skincare.html")