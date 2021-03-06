from django.contrib import admin
from vcubs.models import EstacionVcub, Vcub
from usuarios.models import ReservaMobiBus
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

class CoordRecMov(admin.TabularInline):
    model = CoordenadasMoviBus
    choice = 0
    extra = 0

#TRANVIAS

class CondTranvia(admin.TabularInline):
    model = ConductorTranvia
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
        ('Informacion', {'fields': ['fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo']}),
    ]
    inlines = [VcubEstacion]
    list_display = ('nombre','fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo','necesita_refill',)
    list_filter = ['nombre','fecha_construccion','cap_actual','cap_max','lon','lat',]
    search_fields = ['nombre','fecha_construccion','cap_actual','cap_max','lon','lat',]

class VcubAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['registro']}),
        ('Informacion', {'fields': ['marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo']}),
    ]
    list_display = ('registro','estacion','marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo',)
    list_filter = ['registro','estacion','marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo',]
    search_fields = ['registro','estacion','marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo',]


################################################################################
#                                    MOVIBUSES
################################################################################

class MoviBusAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['placa']}),
        ('Informacion', {'fields': ['marca','modelo','fecha_fabricacion','cap_max']}),
    ]
    inlines = [CondMovibus]
    list_display = ('placa','marca','modelo','kilometraje','velocidad_promedio','fecha_fabricacion','estado_operativo','cap_max',)
    list_filter = ['placa','marca','modelo','fecha_fabricacion','cap_max',]
    search_fields =['placa','marca','modelo','kilometraje','velocidad_promedio','fecha_fabricacion','cap_max',]

class ConductorMoviBusAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_ingreso_sistema',)
    fieldsets = [
        (None,               {'fields': ['cedula']}),
        ('Informacion', {'fields': ['nombre','fecha_de_nacimiento','movibus']}),
    ]
    list_display = ('nombre','fecha_de_nacimiento','kilometros_recorridos','velocidad_promedio','fecha_ingreso_sistema','movibus',)
    list_filter = ['nombre','fecha_de_nacimiento','fecha_ingreso_sistema','movibus',]
    search_fields =['nombre','fecha_de_nacimiento','kilometros_recorridos','velocidad_promedio','fecha_ingreso_sistema','movibus',]

class ReporteMoviBusAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    fieldsets = [('Informacion', {'fields': ['movibus',]}),]
    list_display = ('movibus','fecha',)
    list_filter = ['movibus','fecha',]
    search_fields = ['movibus','fecha',]

class RecorridoMoviBusAdmin(admin.ModelAdmin):
    readonly_fields = ('inicio',)
    fieldsets = [   (None,               {'fields': ['identificador']}),
                    ('Informacion', {'fields': ['reserva','movibus','conductor',]}),]
    inlines = [CoordRecMov]
    list_display = ('identificador','inicio','reserva','movibus','conductor','distancia','velocidad_promedio')
    list_filter = ['identificador','inicio','reserva','movibus','conductor',]
    search_fields = ['identificador','inicio','reserva','movibus','conductor',]

################################################################################
#                                    USUARIOS
################################################################################

# class UsuarioAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['usuario']}),
#         ('Informacion', {'fields': ['usuario','nombre','direccion','telefono','fecha_nacimiento','tipo_usuario']}),
#     ]
#     inlines = [ReservaUsuario]
#     list_display = ('usuario','nombre','direccion','telefono','fecha_nacimiento','tipo_usuario')
#     list_filter = ['usuario','nombre','direccion','telefono','fecha_nacimiento','tipo_usuario']
#     search_fields =['usuario','nombre','direccion','telefono','fecha_nacimiento','tipo_usuario']


class ReservaMoviBusAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    fieldsets = [      (None,               {'fields': ['identificador']}),
                    ('Informacion', {'fields': ['usuario','fecha_programada',]}),]
    inlines = [RecoReserva]
    list_display = ('identificador','fecha','usuario',)
    list_filter = ['identificador','fecha','usuario',]
    search_fields =['identificador','fecha','usuario',]

################################################################################
#                                    TRANVIAS
################################################################################

class LineaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['numero']}),
        ('Informacion', {'fields': ['estacion_llegada','estacion_salida','kilometros_totales']}),
    ]
    inlines = [TranviaLinea]
    list_display = ('numero','estacion_llegada','estacion_salida','kilometros_totales',)
    list_filter = ['numero','estacion_llegada','estacion_salida','kilometros_totales',]
    search_fields =['numero','estacion_llegada','estacion_salida','kilometros_totales',]


class TranviaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['placa']}),
        ('Informacion', {'fields': ['marca','modelo','fecha_fabricacion','cap_max','estado_operativo','linea']}),
    ]
    inlines = [CondTranvia]
    list_display = ('placa','marca','modelo','kilometraje','velocidad_promedio','fecha_fabricacion','cap_max','linea')
    list_filter = ['placa','marca','modelo','fecha_fabricacion','cap_max','linea',]
    search_fields =['placa','marca','modelo','kilometraje','velocidad_promedio','fecha_fabricacion','cap_max','linea',]


class ConductorTranviaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_ingreso_sistema',)
    fieldsets = [
        (None,               {'fields': ['cedula']}),
        ('Informacion', {'fields': ['nombre','fecha_de_nacimiento','tranvia']}),
    ]
    list_display = ('nombre','fecha_de_nacimiento','calificacion','kilometros_recorridos','velocidad_promedio','fecha_ingreso_sistema','tranvia',)
    list_filter = ['nombre','fecha_de_nacimiento','fecha_ingreso_sistema','tranvia',]
    search_fields =['nombre','fecha_de_nacimiento','calificacion','kilometros_recorridos','velocidad_promedio','fecha_ingreso_sistema','tranvia',]

class ReporteTranviaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    fieldsets = [        ('Informacion', {'fields': ['tranvia',]}),]
    list_display = ('tranvia','fecha',)
    list_filter = ['tranvia','fecha',]
    search_fields = ['tranvia','fecha',]

class RecorridoTranviaAdmin(admin.ModelAdmin):
    readonly_fields = ('inicio',)
    fieldsets = [   (None,               {'fields': ['identificador']}),
                    ('Informacion', {'fields': ['tranvia','linea','conductor',]}),]
    inlines = [CoorRecTra]
    list_display = ('identificador','inicio','tranvia','linea','conductor','distancia','velocidad_promedio')
    list_filter = ['identificador','inicio','tranvia','linea','conductor',]
    search_fields = ['identificador','inicio','tranvia','linea','conductor',]


admin.site.register(EstacionVcub, EstacionVcubAdmin)
admin.site.register(Vcub, VcubAdmin)
admin.site.register(MoviBus,MoviBusAdmin)
admin.site.register(ConductorMoviBus,ConductorMoviBusAdmin)
admin.site.register(ReporteMoviBus,ReporteMoviBusAdmin)
admin.site.register(RecorridoMoviBus,RecorridoMoviBusAdmin)
# admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ReservaMobiBus,ReservaMoviBusAdmin)
admin.site.register(Linea,LineaAdmin)
admin.site.register(Tranvia,TranviaAdmin)
admin.site.register(ConductorTranvia,ConductorTranviaAdmin)
admin.site.register(ReporteTranvia,ReporteTranviaAdmin)
admin.site.register(RecorridoTranvia,RecorridoTranviaAdmin)
