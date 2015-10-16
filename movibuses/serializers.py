from rest_framework import serializers
from datetime import datetime
from usuarios.models import ReservaMobiBus
from models import ConductorMoviBus, MoviBus, CoordenadasMoviBus, ReporteMoviBus, RecorridoMoviBus


class ConductorMoviBusSerializer(serializers.ModelSerializer):
    fecha_ingreso_sistema = serializers.ReadOnlyField(default = datetime.now)
    calificacion = serializers.ReadOnlyField(default = 0)
    #recorrido = serializers.PrimaryKeyRelatedField(many=True, queryset=RecorridoMoviBus.objects.all())
    class Meta:
        model = ConductorMoviBus
        fields = ('nombre', 'cedula', 'calificacion', 'fecha_ingreso_sistema', 'fecha_de_nacimiento','movibus',)

class MoviBusSerializer(serializers.ModelSerializer):
    #conductor = serializers.PrimaryKeyRelatedField(many=True, queryset=ConductorMoviBus.objects.all())
    #coordenada = serializers.PrimaryKeyRelatedField(many=True, queryset=CoordenadasMoviBus.objects.all())
    #reporte = serializers.PrimaryKeyRelatedField(many=True, queryset=ReporteMoviBus.objects.all())
    #recorrido = serializers.PrimaryKeyRelatedField(many=True, queryset=RecorridoMoviBus.objects.all())
    class Meta:
        model = MoviBus
        fields = ('placa','marca','modelo','fecha_fabricacion','ruta','cap_max','estado_operativo')

class CoordenadasMoviBusSerializer(serializers.ModelSerializer):
    fecha = serializers.ReadOnlyField(default = datetime.now)
    class Meta:
        model = CoordenadasMoviBus
        fields = ('fecha','latitud','longitud','movibus', 'recorrido')

class ReporteMoviBusSerializer(serializers.ModelSerializer):
    fecha = serializers.ReadOnlyField(default = datetime.now)
    class Meta:
        model = ReporteMoviBus
        fields = ('fecha','movibus')

class RecorridoMoviBusSerializer(serializers.ModelSerializer):
    inicio = serializers.ReadOnlyField(default = datetime.now)
    class Meta:
        model = RecorridoMoviBus
        fields = ('identificador','inicio','reserva','movibus','conductor')
