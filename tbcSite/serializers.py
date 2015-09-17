from rest_framework import serializers
from usuarios.models import Usuario, ReservaMobiBus
from tranvias.models import ConductorTranvia, Tranvia, Linea, AlertaTranvia, CoordenadasTranvia
from movibuses.models import ConductorMoviBus, MoviBus, CoordenadasMoviBus
from vcubs.models import EstacionVcub, Vcub
from reportes.models import ReporteMoviBus, ReporteTranvia

class ConductorMoviBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConductorMoviBus
        fields = ('nombre', 'cedula', 'calificacion', 'kilometros_recorridos', 'fecha_ingreso_sistema', 'fecha_de_nacimiento')


class MoviBusSerializer(serializers.ModelSerializer):
    coordenada = serializers.PrimaryKeyRelatedField(many=True, queryset=CoordenadasMoviBus.objects.all())
    reporte = serializers.PrimaryKeyRelatedField(many=True, queryset=ReporteMoviBus.objects.all())
    reserva = serializers.PrimaryKeyRelatedField(many=True, queryset=ReservaMobiBus.objects.all())
    class Meta:
        model = MoviBus
        fields = ('placa','marca','modelo','kilometraje','fecha_fabricacion','cap_max','ruta','conductor','estado_operativo','coordenada','reporte','reserva')

class CoordenadasMoviBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordenadasMoviBus
        fields = ('fecha','latitud','longitud')

class ReporteMoviBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteMoviBus
        fields = ('fecha')

class ConductorTranviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConductorTranvia
        fields = ('nombre', 'cedula', 'calificacion', 'kilometros_recorridos', 'fecha_ingreso_sistema', 'fecha_de_nacimiento')

class LineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linea
        fields = ('numero', 'estacion_llegada', 'estacion_salida', 'kilometros_totales')

class TranviaSerializer(serializers.ModelSerializer):
    coordenada = serializers.PrimaryKeyRelatedField(many=True, queryset=CoordenadasTranvia.objects.all())
    reporte = serializers.PrimaryKeyRelatedField(many=True, queryset=ReporteTranvia.objects.all())
    alerta = serializers.PrimaryKeyRelatedField(many=True, queryset=AlertaTranvia.objects.all())

    class Meta:
        model = Tranvia
        fields = ('placa','marca','modelo','kilometraje','fecha_fabricacion','cap_max','ruta','conductor','estado_operativo','coordenada','reporte', 'alerta')

class CoordenadasTranviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordenadasTranvia
        fields = ('fecha','latitud','longitud')

class AlertaTranviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertaTranvia
        fields = ('fecha','solicita_reposicion')

class ReporteTranviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteTranvia
        fields = ('fecha')

class UsuarioSerializer(serializers.ModelSerializer):
    reserva = serializers.PrimaryKeyRelatedField(many=True, queryset=ReservaMobiBus.objects.all())
    class Meta:
        model = Usuario
        fields = ('nombre','login','contrasenia','direccion','telefono','email','fecha_nacimiento', 'reserva')

class ReservaMobiBusSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='Usuario.login')
    class Meta:
        model = ReservaMobiBus
        fields = ('fecha', 'usuario')

class EstacionVcubSerializer(serializers.ModelSerializer):
    vcubs = serializers.PrimaryKeyRelatedField(many=True, queryset=Vcub.objects.all())
    class Meta:
        model = EstacionVcub
        fields = ('nombre','fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo','vcubs')

class VcubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vcub
        fields = ('registro','marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo')
