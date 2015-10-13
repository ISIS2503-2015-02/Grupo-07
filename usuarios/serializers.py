from rest_framework import serializers
from datetime import datetime
from models import Usuario, ReservaMobiBus
from movibuses.models import RecorridoMoviBus


class UsuarioSerializer(serializers.ModelSerializer):
    reserva = serializers.PrimaryKeyRelatedField(many=True, queryset=ReservaMobiBus.objects.all())
    class Meta:
        model = Usuario
        fields = ('nombre','login','contrasenia','direccion','telefono','email','fecha_nacimiento', 'reserva')

class ReservaMobiBusSerializer(serializers.ModelSerializer):
    fecha = serializers.ReadOnlyField(default = datetime.now)
    recorrido = serializers.PrimaryKeyRelatedField(many=True,queryset = RecorridoMoviBus.objects.all())
    class Meta:
        model = ReservaMobiBus
        fields = ('fecha', 'usuario','fecha_programada','recorrido')
