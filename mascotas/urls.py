from django.urls import path
from mascotas.views import paginaMascotas, detalleMascota, crear_mascota

urlpatterns = [
    path('', paginaMascotas),
    path('home/', paginaMascotas),
    path('<id>/', detalleMascota),
    path('create', crear_mascota)
]