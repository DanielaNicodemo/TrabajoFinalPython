from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name= "Inicio"),
    path('makeup', views.makeup, name= "Makeup"),
    path('skincare', views.skincare, name= "Skincare"),
    path('contacto', views.contacto, name= "Contacto"),
    
    
]