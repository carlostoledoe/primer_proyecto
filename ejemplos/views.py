from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(req):
    return render(req, 'hola.html')

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

def mascotasapp(req):
    return HttpResponse('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mascotas App</title>
</head>
<body>
    <h1>Mascotas App</h1>
    <h2>Las mejores mascotas del mundo mundial</h2>
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cumque voluptatem aliquid distinctio adipisci nobis veniam reprehenderit architecto cupiditate natus tempora earum in ducimus minima, fugiat similique eum maxime nisi.</p>
    <img src="https://www.hola.com/imagenes/mascotas/20190215137141/razas-perro-pequenos-gt/0-645-998/perros-miniatura-m.jpg?im=Resize=(300)" alt="completo01">
    <img src="https://img.huffingtonpost.es/files/image_720_480/uploads/2023/06/22/un-perro-de-raza-labrador.jpeg">
</body>
</html>
''')