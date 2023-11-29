from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .models import Informacion

# Create your views here.
def hola(request):
    return HttpResponse("hola")
def home(request):
    loco = open("cambios/templates/home.html")
    template = Template(loco. read ())
    loco.close()
    contexto = Context ()
    documento = template. render (contexto)
    return HttpResponse (documento)
def prueba(request):
    loco = open("cambios/templates/todo.html")
    template = Template(loco. read ())
    loco.close()
    contexto = Context ()
    documento = template. render (contexto)
    return HttpResponse (documento)
#error de algun dato, ya sea el registro o en el inicio de sesion
def error(request):
    return HttpResponse("<h1> error en algun dato </h1>")

#acciones
def registro(request): #registro
    if request.method!= "POST": return render(request, "sign-up.html")
    datos= dict(request.POST)
    nombre= datos["nombree"][0]
    contra= datos["contraseña"][0]
    email= datos["correo"][0]
    try:
        Informacion.objects.get(email=email)
        return redirect("/error")
    except:
        pass
    Informacion(nombre=nombre,contraseña= contra, email=email).save()
    return redirect("/home")
def sesion(request):
    if request.method!= "POST": return redirect("/error")
    datos= dict(request.POST)
    email= datos["email"][0]
    contra= datos["contraseña"][0]
    try:
        Informacion.objects.get(email=email, contraseña=contra)
        return redirect("/home")
    except:
        return redirect("/error")

def votacion(request):
    return(render(request,"votacion.html"))
        
    
    