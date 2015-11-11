from rest_framework import serializers
from datetime import datetime
from models import ConductorTranvia, Tranvia, Linea, AlertaTranvia, CoordenadasTranvia, ReporteTranvia, RecorridoTranvia


class ConductorTranviaSerializer(serializers.ModelSerializer):
    fecha_ingreso_sistema = serializers.ReadOnlyField(default = datetime.now)
    calificacion = serializers.ReadOnlyField(default = 0)
    class Meta:
        model = ConductorTranvia
        fields = ('nombre', 'cedula', 'calificacion', 'fecha_ingreso_sistema', 'fecha_de_nacimiento','tranvia',)

class LineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linea
        fields = ('numero', 'estacion_llegada', 'estacion_salida', 'kilometros_totales',)

class TranviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tranvia
        fields = ('placa','marca','modelo','fecha_fabricacion','cap_max','linea','estado_operativo',)

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
    class Meta:
        model = RecorridoTranvia
        fields = ('identificador','inicio','tranvia','linea','conductor',)
