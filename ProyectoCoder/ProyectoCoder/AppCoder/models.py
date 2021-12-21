from django.db import models

# Create your models here.

class FormContacto(models.Model):
    nombre = models.CharField(max_length=40)
    telefono= models.IntegerField()
    mail = models.CharField(max_length=40)
    mensaje= models.CharField(max_length=180)



class Labiales(models.Model):
    nombre = models.CharField(max_length=40)
    stock= models.IntegerField()
    precio= models.IntegerField()


class Cremas(models.Model):
    nombre = models.CharField(max_length=40)
    stock= models.IntegerField()
    precio= models.IntegerField()

    def __str__(self):

       return f"CREMA: {self.nombre} STOCK: {self.stock} PRECIO: {self.precio}"    
    