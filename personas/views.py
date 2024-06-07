from django.http import HttpResponse
from django.shortcuts import render, redirect
from personas.forms import PersonaForm

# Create your views here.
def home(request):
    if request.method == 'GET':
        form = PersonaForm()
        context = {'form': form}
        return render(request, 'personas.html', context)
    else:
        form = PersonaForm(request.POST)
        if form.is_valid():
            return redirect('/personas/exito')
        context = {'form': form}
    return render(request, 'personas.html', context)

def exito(request):
    return HttpResponse('Eeexito!!')