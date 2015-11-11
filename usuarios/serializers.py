from rest_framework import serializers
from datetime import datetime
from models import Usuario, ReservaMobiBus
from movibuses.models import RecorridoMoviBus


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre','login','contrasenia','direccion','telefono','email','fecha_nacimiento',)

class ReservaMobiBusSerializer(serializers.ModelSerializer):
    fecha = serializers.ReadOnlyField(default = datetime.now)
    class Meta:
        model = ReservaMobiBus
        fields = ('identificador','fecha', 'usuario','fecha_programada',)
