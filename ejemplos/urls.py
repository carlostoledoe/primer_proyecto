from django.urls import path
from ejemplos.views import * # usar * no es muy buena práctica xq se pierde trasabilida

urlpatterns = [
    path('', hola), # Las dos comillas toma la ruta por defecto
    path('chao/', chao),
    path('saludar/<nombre>', saludar), #Ruta variable, recibe parámetro
    path('saludar/', saludar), 
    path('poliglota/<nombre>/<idioma>', poliglota),
    path('mascotasapp/', mascotasapp)
]