from django.db import models
 
class Informacion(models.Model):
    nombre=models.CharField(null=False, max_length=50)
    contraseña=models.CharField(null=False, max_length=50)
    email=models.EmailField(null=False, max_length=30, default="default@gmail.com")
     
# Create your models here.
