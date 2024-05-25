from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(req):
    return HttpResponse('<h1>Hola Mundo!!</h1>')

def chao(req):
    return HttpResponse('<h1>Chao pescado!!</h1>')

def saludar(req, nombre = 'Amigo'):
    return HttpResponse(f'<h3>Hola {nombre}</h3>')

def poliglota(req, nombre, idioma):
    # Saluda a la persona en el idioma ingresa
    idiomas = {
        'ingles': 'Hello, how are you!', 
        'sueco': 'Hejsan, hur är det!',
        'aleman': 'Hallo, wie geht es du!'
    }
    
    if idioma in idiomas.keys():
        return HttpResponse(f'{idiomas[idioma]}, {nombre.capitalize()}')
    else:
        return HttpResponse('No entiendo el idioma')
