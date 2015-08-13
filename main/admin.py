from django.contrib import admin
from .models import ConductorTranvia, ConductorMoviBus, Tranvia, MoviBus

# Register your models here.

class ConductorTranviaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        ('Informacion', {'fields': ['cedula','fecha_de_nacimiento'], 'classes': ['collapse']}),
    ]
    list_display = ('nombre', 'cedula', 'fecha_de_nacimiento')
    search_fields = ['cedula']

class ConductorMoviBusAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        ('Informacion', {'fields': ['cedula','fecha_de_nacimiento'], 'classes': ['collapse']}),
    ]
    list_display = ('nombre', 'cedula', 'fecha_de_nacimiento')
    search_fields = ['cedula']

class TranviaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['placa']}),
        ('Informacion', {'fields': ['marca','modelo','fecha_fabricacion','cap_max','linea','lon','lat','conductor','estado_operativo'], 'classes': ['collapse']}),
    ]
    list_display = ('placa','marca', 'modelo','fecha_fabricacion','cap_max','linea','lon','lat','conductor','estado_operativo')
    list_filter = ['marca','linea',]
    search_fields = ['placa']

class MoviBusAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['placa']}),
        ('Informacion', {'fields': ['marca','modelo','fecha_fabricacion','cap_max','ruta','lon','lat','conductor','estado_operativo'], 'classes': ['collapse']}),
    ]
    list_display = ('placa','marca', 'modelo','fecha_fabricacion','cap_max','ruta','lon','lat','conductor','estado_operativo')
    list_filter = ['marca','ruta',]
    search_fields = ['placa']

admin.site.register(ConductorTranvia, ConductorTranviaAdmin)
admin.site.register(ConductorMoviBus, ConductorMoviBusAdmin)
admin.site.register(Tranvia, TranviaAdmin)
admin.site.register(MoviBus, MoviBusAdmin)
