from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

# Create your views here.

# blogs/
def index(req):
    return render(req, 'blogs.html')

# blogs/create
def new(req):
    return HttpResponse('placeholder para mostrar un nuevo formulario para crear un nuevo blog')

# blogs/create
def create(req):
    return redirect('/')

# blogs/<number>
def show(req, number):
    return HttpResponse(f'placeholder para mostrar el blog número: {number}')

# blogs/<number>
def edit(req, number):
        return HttpResponse(f'placeholder para editar el blog número: {number}')

# blogs/<number>/delete
def destroy(req, number):
        return redirect('/blogs')

# blogs/json
def json_req(req):
    data = {
        'title': 'Mi Blog',
        'author': 'Autor del Blog',
        'content': 'Este es el contenido de ejemplo del blog.',
        'published': True
    }
    return JsonResponse(data)