from rest_framework import serializers
from models import EstacionVcub, Vcub

class EstacionVcubSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstacionVcub
        fields = ('nombre','fecha_construccion','cap_actual','cap_max','lon','lat','estado_operativo',)

class VcubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vcub
        fields = ('registro','marca','modelo','fecha_fabricacion','estacion','en_transito','estado_operativo')
