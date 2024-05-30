from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
mascotas = [
    {
        'id': 1,
        'nombre': 'Pelusa',
        'especie': 'gato'
    },
    {
        'id': 2,
        'nombre': 'Rocky',
        'especie': 'perro'
    },
    {
        'id': 3,
        'nombre': 'Nemo',
        'especie': 'pez'
    },
]


def paginaMascotas(request):
    context = {
        'titulo': 'Este es el Portal de las Mascotas',
        'esAdmin': True,
        'nombre': 'Matias Bensan', 
        'mascotas': mascotas
    }
    return render(request, 'mascotas.html', context)