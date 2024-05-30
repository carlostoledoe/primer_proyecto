from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def paginaMascotas(request):
    return render(request, 'mascotas.html')