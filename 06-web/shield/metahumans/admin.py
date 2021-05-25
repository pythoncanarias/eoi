from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import Equipo, Poder, Metahumano

class PoderAdmin(admin.ModelAdmin):
    search_fields = (
        'nombre',
    )
    list_display = ('id', 'nombre')


admin.site.register(Poder, PoderAdmin)


class EquipoAdmin(admin.ModelAdmin):
    search_fields = (
        'nombre',
        'cuartel',
    )
    list_display = ('id', 'nombre', 'cuartel')

admin.site.register(Equipo, EquipoAdmin)


class MetahumanoAdmin(admin.ModelAdmin):
    search_fields = (
        'nombre',
        'identidad',
        'equipo__nombre',
    )
    list_display = (
        'id',
        'nombre',
        'num_poderes',
        'peligrosidad',
        'en_equipo',
        'foto',
    )
    list_filter = (
        'equipo',
        'nivel',
    )
    exclude = ('activo',)

    def peligrosidad(self, mh):
        if mh.nivel <= 50:
            return format_html(f"<strong>{mh.nivel}</strong>")
        else:
            return str(mh.nivel)

    def en_equipo(self, mh):
        if mh.equipo:
            return True
        else:
            return False

    en_equipo.boolean = True

admin.site.register(Metahumano, MetahumanoAdmin)

