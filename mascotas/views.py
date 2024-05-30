from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def paginaMascotas(request):
    context = {
        'titulo': 'Este es el Portal de las Mascotas',
        'esAdmin': False,
        'nombre': 'Matias Bensan'
    }
    return render(request, 'mascotas.html', context)