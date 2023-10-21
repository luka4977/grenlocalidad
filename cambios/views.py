from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
def hola(request):
    return HttpResponse("hola")
def home(request):
    loco = open("cambios/templates/inicio.html")
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