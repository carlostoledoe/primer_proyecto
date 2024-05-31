from django.urls import path
from mascotas.views import paginaMascotas, detalleMascota

urlpatterns = [
    path('', paginaMascotas),
    path('<id>/', detalleMascota),
    
]