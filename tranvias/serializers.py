from rest_framework import serializers
from models import ConductorTranvia, Tranvia, Linea, AlertaTranvia, CoordenadasTranvia, ReporteTranvia


class ConductorTranviaSerializer(serializers.ModelSerializer):
    tranvia = serializers.ReadOnlyField(source='Tranvia.placa')
    class Meta:
        model = ConductorTranvia
        fields = ('nombre', 'cedula', 'calificacion', 'kilometros_recorridos', 'fecha_ingreso_sistema', 'fecha_de_nacimiento','tranvia')

class LineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linea
        fields = ('numero', 'estacion_llegada', 'estacion_salida', 'kilometros_totales')

class TranviaSerializer(serializers.ModelSerializer):
    conductor = serializers.PrimaryKeyRelatedField(many=True, queryset=ConductorTranvia.objects.all())
    coordenada = serializers.PrimaryKeyRelatedField(many=True, queryset=CoordenadasTranvia.objects.all())
    reporte = serializers.PrimaryKeyRelatedField(many=True, queryset=ReporteTranvia.objects.all())
    alerta = serializers.PrimaryKeyRelatedField(many=True, queryset=AlertaTranvia.objects.all())

    class Meta:
        model = Tranvia
        fields = ('placa','marca','modelo','kilometraje','fecha_fabricacion','cap_max','conductor','estado_operativo','coordenada','reporte', 'alerta')

class CoordenadasTranviaSerializer(serializers.ModelSerializer):
    tranvia = serializers.ReadOnlyField(source='Tranvia.placa')
    class Meta:
        model = CoordenadasTranvia
        fields = ('fecha','latitud','longitud','tranvia')

class AlertaTranviaSerializer(serializers.ModelSerializer):
    tranvia = serializers.ReadOnlyField(source='Tranvia.placa')
    class Meta:
        model = AlertaTranvia
        fields = ('fecha','solicita_reposicion','tranvia')

class ReporteTranviaSerializer(serializers.ModelSerializer):
    tranvia = serializers.ReadOnlyField(source='Tranvia.placa')
    class Meta:
        model = ReporteTranvia
        fields = ('fecha','tranvia')
