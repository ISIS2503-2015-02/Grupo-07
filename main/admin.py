from django.contrib import admin
from .models import ConductorTranvia, ConductorMoviBus, Tranvia, MoviBus, EstacionVcub, Vcub

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Vcub
    choice = 0

class Alerta(admin.TabularInline):
    model = AlertaTranvia
    choice = 0

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
    inlines = [Alerta]
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

class VcubAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['registro']}),
        ('Informacion', {'fields': ['marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo'], 'classes': ['collapse']}),
    ]
    list_display = ('registro','marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo')
    list_filter = ['marca','estacion',]
    search_fields = ['registro']

class EstacionVcubAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        ('Informacion', {'fields': ['fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('nombre','fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo')
    list_filter = ['fecha_construccion']
    search_fields = ['nombre']

admin.site.register(ConductorTranvia, ConductorTranviaAdmin)
admin.site.register(ConductorMoviBus, ConductorMoviBusAdmin)
admin.site.register(Tranvia, TranviaAdmin)
admin.site.register(MoviBus, MoviBusAdmin)
admin.site.register(Vcub, VcubAdmin)
admin.site.register(EstacionVcub, EstacionVcubAdmin)
