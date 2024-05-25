from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(req):
    return HttpResponse('<h1>Hola Mundo!!</h1>')

def chao(req):
    return HttpResponse('<h1>Chao pescado!!</h1>')

def saludar(req, nombre = 'Amigo'):
    return HttpResponse(f'<h3>Hola {nombre}</h3>')