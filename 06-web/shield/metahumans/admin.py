from django.contrib import admin

from . import models

# Register your models here.

class PowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'level')


admin.site.register(models.Power, PowerAdmin)


class MetaHumanAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'active', 'level')
    list_filter = ('active', 'level', 'powers')

admin.site.register(models.MetaHuman, MetaHumanAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'headquarter')

admin.site.register(models.Team, TeamAdmin)
