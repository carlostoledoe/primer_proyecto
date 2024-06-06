from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
mascotas = [
    {
        'id': 1,
        'nombre': 'Pelusa',
        'especie': 'gato',
        'texto': 'Es un gato feliz, gordo y peludo.',
        'url': 'https://images.ctfassets.net/denf86kkcx7r/1PKz6sDJvJXhONBEMzPQIY/48a700dc59e7f4fa64bff5ef5477ee2f/gato_gordo_santevet-83',
        'vacunas': ['octuple']
    },
    {
        'id': 2,
        'nombre': 'Rocky',
        'especie': 'perro',
        'texto': 'Fue un perro muy bravo, pero cariñoso',
        'url': 'https://t2.uc.ltmcdn.com/es/posts/5/3/2/como_evitar_que_mi_perro_sea_agresivo_30235_orig.jpg',
        'vacunas': ['octuple', 'antirrabica']
    },
    {
        'id': 3,
        'nombre': 'Nemo',
        'especie': 'pez',
        'texto': 'Es un pez fome, no hace nada.',
        'url': 'https://www.webconsultas.com/sites/default/files/styles/wch_image_schema/public/temas/el-pez-rojo_0.jpg',
        'vacunas': ['antibioticos', 'melipass']
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

def detalleMascota(request, id):
    id = int(id)  # Ya que las cosas viajan como string
    masc_encontarda = None
    for masc in mascotas:
        if masc['id'] == id:
            masc_encontarda = masc
            break # Para que no siga buscando
    context = {
        'mascota': masc_encontarda
    }
    
    return render(request, 'detalle.html', context)

def crear_mascota(request):
    print(request.POST)
    print(request.POST['nombre'])
    print(request.POST['especie'])
    return redirect('/pets')
