from rest_framework import serializers
from datetime import datetime
from usuarios.models import ReservaMobiBus
from models import ConductorMoviBus, MoviBus, CoordenadasMoviBus, ReporteMoviBus, RecorridoMoviBus


class ConductorMoviBusSerializer(serializers.ModelSerializer):
    fecha_ingreso_sistema = serializers.ReadOnlyField(default = datetime.now)
    recorrido = serializers.PrimaryKeyRelatedField(many=True, queryset=RecorridoMoviBus.objects.all())
    class Meta:
        model = ConductorMoviBus
        fields = ('nombre', 'cedula', 'calificacion', 'kilometros_recorridos', 'fecha_ingreso_sistema', 'fecha_de_nacimiento','movibus','recorrido')

class MoviBusSerializer(serializers.ModelSerializer):
    conductor = serializers.PrimaryKeyRelatedField(many=True, queryset=ConductorMoviBus.objects.all())
    coordenada = serializers.PrimaryKeyRelatedField(many=True, queryset=CoordenadasMoviBus.objects.all())
    reporte = serializers.PrimaryKeyRelatedField(many=True, queryset=ReporteMoviBus.objects.all())
    class Meta:
        model = MoviBus
        fields = ('placa','marca','modelo','kilometraje','fecha_fabricacion','ruta','cap_max','conductor','estado_operativo','coordenada','reporte')

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
    coordenada = serializers.PrimaryKeyRelatedField(many=True, queryset=CoordenadasMoviBus.objects.all())
    class Meta:
        model = RecorridoMoviBus
        fields = ('inicio', 'coordenada','reserva','conductor')
