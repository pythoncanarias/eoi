from django.shortcuts import render

from .models import MetaHuman, Team

# Create your views here.

def list_all_metahumans(request):
    items = MetaHuman.objects.all()
    return render(request, "metahumans/list_metahumans.html", {
        "items": items,
    })

    
def list_all_teams(request):
    items = Team.objects.all()
    return render(request, "metahumans/list_teams.html", {
        "items": items,
    })

