from django.urls import path
from ejercicios_ruteo.views import index, new, create, show, edit, destroy, json_req

urlpatterns = [
    path('blogs/', index),
    path('blogs/new', new),
    path('blogs/create', create),
    path('blogs/json', json_req), # Las rutas más específicas deben ser definidas antes que las rutas que usan parámetros variables
    path('blogs/<number>', show),
    path('blogs/<number>/edit', edit),
    path('blogs/<number>/delete', destroy),
]