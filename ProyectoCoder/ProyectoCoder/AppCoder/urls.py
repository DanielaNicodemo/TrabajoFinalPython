from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('makeup', views.makeup, name= "makeup"),
    path('skincare', views.skincare, name= "skincare"),
    path('contacto', views.contacto, name= "contacto"),
    path('productos', views.productos, name= "productos"),
    path('detalles/<int:producto_id>/', views.detalles, name= "detalles"),
    
]