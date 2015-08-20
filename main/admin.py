from django.contrib import admin
from usuarios.models import Usuario, ReservaMobiBus
from tranvias.models import ConductorTranvia, Tranvia, Linea, AlertaTranvia, CoordenadasTranvia
from movibuses.models import ConductorMoviBus, MoviBus, CoordenadasMoviBus
from vcubs.models import EstacionVcub, Vcub
from reportes.models import ReporteMoviBus, ReporteTranvia

# Register your models here.

class ChoiceInLineCoordTranvia(admin.TabularInline):
    model = CoordenadasTranvia
    choice  = 0
    extra = 1

class ChoiceInLineReservaMoviBus(admin.TabularInline):
    model = ReservaMobiBus
    choice  = 0
    extra = 0

class ChoiceInLineCoordMoviBus(admin.TabularInline):
    model = CoordenadasMoviBus
    choice  = 0
    extra = 1

class ChoiceInlineEstacion(admin.TabularInline):
    model = Vcub
    choice = 0
    extra = 0

class ChoiceInLineAlerta(admin.TabularInline):
    model = AlertaTranvia
    choice = 0
    extra = 0

class ConductorTranviaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        ('Informacion', {'fields': ['cedula','fecha_de_nacimiento', 'fecha_ingreso_sistema','calificacion'], 'classes': ['collapse']}),
    ]
    list_display = ('nombre', 'cedula', 'fecha_de_nacimiento','fecha_ingreso_sistema','calificacion','dar_kilometros_recorridos')
    list_filter = ['calificacion']
    search_fields = ['cedula']

class ConductorMoviBusAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        ('Informacion', {'fields': ['cedula','fecha_de_nacimiento', 'fecha_ingreso_sistema','calificacion'], 'classes': ['collapse']}),
    ]
    list_display = ('nombre', 'cedula', 'fecha_de_nacimiento','fecha_ingreso_sistema','calificacion','dar_kilometros_recorridos')
    list_filter = ['calificacion']
    search_fields = ['cedula']

class TranviaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['placa']}),
        ('Informacion', {'fields': ['marca','modelo','fecha_fabricacion','cap_max','linea','conductor','estado_operativo'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLineAlerta, ChoiceInLineCoordTranvia]
    list_display = ('placa','marca', 'modelo','fecha_fabricacion','cap_max','linea','conductor','estado_operativo')
    list_filter = ['marca','linea',]
    search_fields = ['placa']

class MoviBusAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['placa']}),
        ('Informacion', {'fields': ['marca','modelo','fecha_fabricacion','cap_max','ruta','conductor','estado_operativo'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLineCoordMoviBus]
    list_display = ('placa','marca', 'modelo','fecha_fabricacion','cap_max','ruta','conductor','estado_operativo')
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
    inlines = [ChoiceInlineEstacion]
    list_display = ('nombre','fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo','necesita_refill')
    list_filter = ['fecha_construccion']
    search_fields = ['nombre']

class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['email','login','contrasenia']}),
        ('Informacion', {'fields': ['nombre','fecha_nacimiento', 'direccion', 'telefono'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLineReservaMoviBus]
    list_display = ('nombre','login','fecha_nacimiento', 'direccion', 'telefono', 'email')
    list_filter = ['nombre','login','fecha_nacimiento', 'direccion', 'telefono', 'email']
    search_fields = ['nombre','login','fecha_nacimiento', 'direccion', 'telefono', 'email']

class ReporteMoviBusAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['movibus','fecha']}),
    ]
    list_display = ('movibus','fecha')
    list_filter = ['movibus','fecha']
    search_fields = ['movibus','fecha']

class ReporteTranviaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['tranvia','fecha']}),
    ]
    list_display = ('tranvia','fecha')
    list_filter = ['tranvia','fecha']
    search_fields = ['tranvia','fecha']

admin.site.register(ConductorTranvia, ConductorTranviaAdmin)
admin.site.register(ConductorMoviBus, ConductorMoviBusAdmin)
admin.site.register(Tranvia, TranviaAdmin)
admin.site.register(MoviBus, MoviBusAdmin)
admin.site.register(Vcub, VcubAdmin)
admin.site.register(EstacionVcub, EstacionVcubAdmin)
admin.site.register(Linea)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ReporteMoviBus, ReporteMoviBusAdmin)
admin.site.register(ReporteTranvia, ReporteTranviaAdmin)
