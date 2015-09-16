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
    coordenadas = serializers.StringRelatedField(many=True)
    reportes = serializers.StringRelatedField(many=True)
    reserva = serializers.StringRelatedField(many=True)
    class Meta:
        model = MoviBus
        fields = ('placa','marca','modelo','kilometraje','fecha_fabricacion','cap_max','ruta','conductor','estado_operativo','coordenada','reporte')

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
    coordenadas = serializers.StringRelatedField(many=True)
    reportes = serializers.StringRelatedField(many=True)
    alerta = serializers.StringRelatedField(many=True)
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
    reserva = serializers.StringRelatedField(many=True)
    class Meta:
        model = Usuario
        fields = ('nombre','login','contrasenia','direccion','telefono','email','fecha_nacimiento')

class ReservaMobiBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaMobiBus
        fields = ('fecha')
