from rest_framework import serializers
from datetime import datetime
from models import ConductorTranvia, Tranvia, Linea, AlertaTranvia, CoordenadasTranvia, ReporteTranvia, RecorridoTranvia


class ConductorTranviaSerializer(serializers.ModelSerializer):
    fecha_ingreso_sistema = serializers.ReadOnlyField(default = datetime.now)
    recorrido = serializers.PrimaryKeyRelatedField(many = True, queryset=RecorridoTranvia.objects.all())
    class Meta:
        model = ConductorTranvia
        fields = ('nombre', 'cedula', 'calificacion', 'kilometros_recorridos', 'fecha_ingreso_sistema', 'fecha_de_nacimiento','tranvia', 'recorrido')

class LineaSerializer(serializers.ModelSerializer):
    recorrido = serializers.PrimaryKeyRelatedField(many=True, queryset=RecorridoTranvia.objects.all())
    tranvia = serializers.PrimaryKeyRelatedField(many=True, queryset=Tranvia.objects.all())
    class Meta:
        model = Linea
        fields = ('numero', 'estacion_llegada', 'estacion_salida', 'kilometros_totales','recorrido','tranvia')

class TranviaSerializer(serializers.ModelSerializer):
    conductor = serializers.PrimaryKeyRelatedField(many=True, queryset=ConductorTranvia.objects.all())
    coordenada = serializers.PrimaryKeyRelatedField(many=True, queryset=CoordenadasTranvia.objects.all())
    reporte = serializers.PrimaryKeyRelatedField(many=True, queryset=ReporteTranvia.objects.all())
    alerta = serializers.PrimaryKeyRelatedField(many=True, queryset=AlertaTranvia.objects.all())
    recorrido = serializers.PrimaryKeyRelatedField(many=True, queryset=RecorridoTranvia.objects.all())

    class Meta:
        model = Tranvia
        fields = ('placa','marca','modelo','kilometraje','fecha_fabricacion','cap_max','conductor','estado_operativo','coordenada','reporte', 'alerta', 'recorrido')

class CoordenadasTranviaSerializer(serializers.ModelSerializer):
    fecha = serializers.ReadOnlyField(default = datetime.now)
    class Meta:
        model = CoordenadasTranvia
        fields = ('fecha','latitud','longitud','tranvia','recorrido')

class AlertaTranviaSerializer(serializers.ModelSerializer):
    fecha = serializers.ReadOnlyField(default = datetime.now)

    class Meta:
        model = AlertaTranvia
        fields = ('fecha','descripcion','tranvia','solicita_reposicion')

class ReporteTranviaSerializer(serializers.ModelSerializer):
    fecha = serializers.ReadOnlyField(default = datetime.now)
    class Meta:
        model = ReporteTranvia
        fields = ('fecha','tranvia')

class RecorridoTranviaSerializer(serializers.ModelSerializer):
    inicio = serializers.ReadOnlyField(default = datetime.now)
    coordenada = serializers.PrimaryKeyRelatedField(many = True, queryset = CoordenadasTranvia.objects.all())
    class Meta:
        model = RecorridoTranvia
        fields = ('inicio','tranvia','linea','conductor','coordenada')
