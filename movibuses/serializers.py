from rest_framework import serializers
from models import ConductorMoviBus, MoviBus, CoordenadasMoviBus, ReporteMoviBus


class ConductorMoviBusSerializer(serializers.HyperlinkedModelSerializer):
    movibus = serializers.ReadOnlyField(source='MoviBus.placa')
    class Meta:
        model = ConductorMoviBus
        fields = ('nombre', 'cedula', 'calificacion', 'kilometros_recorridos', 'fecha_ingreso_sistema', 'fecha_de_nacimiento','movibus')

class MoviBusSerializer(serializers.HyperlinkedModelSerializer):
    conductor = serializers.PrimaryKeyRelatedField(many=True, queryset=ConductorMoviBus.objects.all())
    coordenada = serializers.PrimaryKeyRelatedField(many=True, queryset=CoordenadasMoviBus.objects.all())
    reporte = serializers.PrimaryKeyRelatedField(many=True, queryset=ReporteMoviBus.objects.all())
    class Meta:
        model = MoviBus
        fields = ('placa','marca','modelo','kilometraje','fecha_fabricacion','ruta','cap_max','conductor','estado_operativo','coordenada','reporte')

class CoordenadasMoviBusSerializer(serializers.HyperlinkedModelSerializer):
    movibus = serializers.ReadOnlyField(source='MoviBus.placa')
    class Meta:
        model = CoordenadasMoviBus
        fields = ('fecha','latitud','longitud','movibus')

class ReporteMoviBusSerializer(serializers.HyperlinkedModelSerializer):
    movibus = serializers.ReadOnlyField(source='MoviBus.placa')
    class Meta:
        model = ReporteMoviBus
        fields = ('fecha','movibus')
