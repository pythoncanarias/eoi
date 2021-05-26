from django.shortcuts import render

from .models import Metahumano

# Create your views here.

def detalle(request, pk):
    metahuman = Metahumano.objects.get(id=pk)
    return render(request, 'metahumans/detalle.html', {
        "mh": metahuman, 
    })


def listado_metahumans(request):
    filas = Metahumano.objects.all()
    return render(request, 'metahumans/listado.html', {
        "filas": filas,
    })
