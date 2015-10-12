from django.contrib import admin
from vcubs.models import EstacionVcub, Vcub
from usuarios.models import Usuario, ReservaMobiBus
from movibuses.models import MoviBus, ConductorMoviBus, ReporteMoviBus, RecorridoMoviBus, CoordenadasMoviBus
from tranvias.models import Tranvia, ConductorTranvia, ReporteTranvia, RecorridoTranvia, CoordenadasTranvia, Linea, AlertaTranvia


################################################################################
#                                 ChoiceInLine
################################################################################

#VCUBS
class VcubEstacion(admin.TabularInline):
    model = Vcub
    choice = 0
    extra = 0

#USUARIOS
class ReservaUsuario(admin.TabularInline):
    model = ReservaMobiBus
    choice = 0
    extra = 0

class RecoReserva(admin.TabularInline):
    model = RecorridoMoviBus
    choice = 0
    extra = 0

#MOVIBUSES
class CondMovibus(admin.TabularInline):
    model = ConductorMoviBus
    choice = 0
    extra = 0

class ReporteMovi(admin.TabularInline):
    model = ReporteMoviBus
    choice = 0
    extra = 0

class RecCondMovibus(admin.TabularInline):
    model = RecorridoMoviBus
    choice = 0
    extra = 1

class CoordRecMov(admin.TabularInline):
    model = CoordenadasMoviBus
    choice = 0
    extra = 0

#TRANVIAS

class CondTranvia(admin.TabularInline):
    model = ConductorTranvia
    choice = 0
    extra = 0

class ReporteTran(admin.TabularInline):
    model = ReporteTranvia
    choice = 0
    extra = 0

class AlertaTran(admin.TabularInline):
    model = AlertaTranvia
    choice = 0
    extra = 0

class RecTranvia(admin.TabularInline):
    model = RecorridoTranvia
    choice = 0
    extra = 0

class RecCondTranvia(admin.TabularInline):
    model = RecorridoTranvia
    choice = 0
    extra = 1

class CoorRecTra(admin.TabularInline):
    model = CoordenadasTranvia
    choice = 0
    extra = 0

class TranviaLinea(admin.TabularInline):
    model = Tranvia
    choice = 0
    extra = 0

################################################################################
#                                    Vcubs
################################################################################

class EstacionVcubAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        ('Informacion', {'fields': ['fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo'], 'classes': ['collapse']}),
    ]
    inlines = [VcubEstacion]
    list_display = ('nombre','estacion','fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo','necesita_refill',)
    list_filter = ['nombre','estacion','fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo','necesita_refill',]
    search_fields = ['nombre','estacion','fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo','necesita_refill',]

class VcubAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['registro']}),
        ('Informacion', {'fields': ['marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo'], 'classes': ['collapse']}),
    ]
    list_display = ('registro','marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo',)
    list_filter = ['registro','marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo',]
    search_fields = ['registro','marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo',]


################################################################################
#                                    MOVIBUSES
################################################################################

class MoviBusAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['placa']}),
        ('Informacion', {'fields': ['marca','modelo','kilometraje','fecha_fabricacion','cap_max'], 'classes': ['collapse']}),
    ]
    inlines = [CondMovibus,ReporteMovi]
    list_display = ('placa','marca','modelo','kilometraje','velocidad_promedio','fecha_fabricacion','cap_max',)
    list_filter = ['placa','marca','modelo','kilometraje','velocidad_promedio','fecha_fabricacion','cap_max',]
    search_fields =['placa','marca','modelo','kilometraje','velocidad_promedio','fecha_fabricacion','cap_max',]

class ConductorMoviBusAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_ingreso_sistema',)
    fieldsets = [
        (None,               {'fields': ['cedula']}),
        ('Informacion', {'fields': ['nombre','fecha_de_nacimiento'], 'classes': ['collapse']}),
    ]
    inlines = [RecCondMovibus]
    list_display = ('nombre','fecha_de_nacimiento','calificacion','kilometros_recorridos','velocidad_promedio','fecha_ingreso_sistema','movibus',)
    list_filter = ['nombre','fecha_de_nacimiento','calificacion','kilometros_recorridos','velocidad_promedio','fecha_ingreso_sistema','movibus',]
    search_fields =['nombre','fecha_de_nacimiento','calificacion','kilometros_recorridos','velocidad_promedio','fecha_ingreso_sistema','movibus',]

class ReporteMoviBusAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    fieldsets = []
    list_display = ('movibus','fecha',)
    list_filter = ['movibus','fecha',]
    search_fields = ['movibus','fecha',]

class RecorridoMoviBusAdmin(admin.ModelAdmin):
    readonly_fields = ('inicio',)
    fieldsets = []
    inlines = [CoordRecMov]
    list_display = ('inicio','fin','reserva','conductor',)
    list_filter = ['inicio','fin','reserva','conductor',]
    search_fields = ['inicio','fin','reserva','conductor',]

################################################################################
#                                    USUARIOS
################################################################################

class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['login']}),
        ('Informacion', {'fields': ['nombre','contrasenia','direccion','telefono','email','fecha_nacimiento'], 'classes': ['collapse']}),
    ]
    inlines = [ReservaUsuario]
    list_display = ('nombre','contrasenia','direccion','telefono','email','fecha_nacimiento',)
    list_filter = ['nombre','contrasenia','direccion','telefono','email','fecha_nacimiento',]
    search_fields =['nombre','contrasenia','direccion','telefono','email','fecha_nacimiento',]


class ReservaMoviBusAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    fieldsets = []
    inlines = [RecoReserva]
    list_display = ('fecha','usuario',)
    list_filter = ['fecha','usuario',]
    search_fields =['fecha','usuario',]

################################################################################
#                                    TRANVIAS
################################################################################

class LineaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['numero']}),
        ('Informacion', {'fields': ['estacion_llegada','estacion_salida','kilometros_totales'], 'classes': ['collapse']}),
    ]
    inlines = [TranviaLinea]
    list_display = ('numero','estacion_llegada','estacion_salida','kilometros_totales',)
    list_filter = ['numero','estacion_llegada','estacion_salida','kilometros_totales',]
    search_fields =['numero','estacion_llegada','estacion_salida','kilometros_totales',]


class TranviaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['placa']}),
        ('Informacion', {'fields': ['marca','modelo','kilometraje','fecha_fabricacion','cap_max'], 'classes': ['collapse']}),
    ]
    inlines = [CondTranvia, ReporteTran, AlertaTran, RecTranvia]
    list_display = ('placa','marca','modelo','kilometraje','velocidad_promedio','fecha_fabricacion','cap_max','linea',)
    list_filter = ['placa','marca','modelo','kilometraje','velocidad_promedio','fecha_fabricacion','cap_max','linea',]
    search_fields =['placa','marca','modelo','kilometraje','velocidad_promedio','fecha_fabricacion','cap_max','linea',]


class ConductorTranviaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_ingreso_sistema',)
    fieldsets = [
        (None,               {'fields': ['cedula']}),
        ('Informacion', {'fields': ['nombre','fecha_de_nacimiento'], 'classes': ['collapse']}),
    ]
    inlines = [RecCondTranvia]
    list_display = ('nombre','fecha_de_nacimiento','calificacion','kilometros_recorridos','velocidad_promedio','fecha_ingreso_sistema','tranvia',)
    list_filter = ['nombre','fecha_de_nacimiento','calificacion','kilometros_recorridos','velocidad_promedio','fecha_ingreso_sistema','tranvia',]
    search_fields =['nombre','fecha_de_nacimiento','calificacion','kilometros_recorridos','velocidad_promedio','fecha_ingreso_sistema','tranvia',]

class ReporteTranviaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    fieldsets = []
    list_display = ('tranvia','fecha',)
    list_filter = ['tranvia','fecha',]
    search_fields = ['tranvia','fecha',]

class RecorridoTranviaAdmin(admin.ModelAdmin):
    readonly_fields = ('inicio',)
    inlines = [CoorRecTra]
    list_display = ('inicio','tranvia','linea','conductor',)
    list_filter = ['inicio','tranvia','linea','conductor',]
    search_fields = ['inicio','tranvia','linea','conductor',]


admin.site.register(EstacionVcub, EstacionVcubAdmin)
admin.site.register(Vcub, VcubAdmin)
admin.site.register(MoviBus,MoviBusAdmin)
admin.site.register(ConductorMoviBus,ConductorMoviBusAdmin)
admin.site.register(ReporteMoviBus,ReporteMoviBusAdmin)
admin.site.register(RecorridoMoviBus,RecorridoMoviBusAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ReservaMobiBus,ReservaMoviBusAdmin)
admin.site.register(Linea,LineaAdmin)
admin.site.register(Tranvia,TranviaAdmin)
admin.site.register(ConductorTranvia,ConductorTranviaAdmin)
admin.site.register(ReporteTranvia,ReporteTranviaAdmin)
admin.site.register(RecorridoTranvia,RecorridoTranviaAdmin)
