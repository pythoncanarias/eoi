from django.shortcuts import render

from .models import MetaHuman

# Create your views here.

def list_all_metahumans(request):
    items = MetaHuman.objects.all()
    return render(request, "metahumans/list_metahumans.html", {
        "items": items,
    })

    
