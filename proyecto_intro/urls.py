"""
URL configuration for proyecto_intro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cambios.views import hola
from cambios.views import home
from cambios.views import prueba
from cambios.views import error
from cambios.views import registro,sesion,votar,ciudad,guardar_datos,completado
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hola),
    path("home/", home),
    path("entero/",prueba),
    path("error", error),
    path("registrar/",registro ),
    path("validar_usuario",sesion),
    path("votar/",votar),
    path("ciudad/",ciudad),
    path("votacion/",guardar_datos),
    path("completado/", completado)
]