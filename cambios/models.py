from django.db import models
 
class Informacion(models.Model):
    nombre=models.CharField(null=False, max_length=50)
    contraseña=models.CharField(null=False, max_length=50)
    email=models.EmailField(null=False, max_length=30, default="default@gmail.com")
     
# Create your models here.
class Votaciones(models.Model):
    creador=models.CharField(null=False, max_length=50)
    ciudad=models.CharField(null=False, max_length=50)
    direccion=models.CharField(null=False, max_length=50)
    radio=models.DecimalField(null=False,max_digits=3, decimal_places=0)
    descripcion=models.CharField(null=False, max_length=10)