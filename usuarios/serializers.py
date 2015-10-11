from rest_framework import serializers
from models import Usuario, ReservaMobiBus


class UsuarioSerializer(serializers.ModelSerializer):
    reserva = serializers.PrimaryKeyRelatedField(many=True, queryset=ReservaMobiBus.objects.all())
    class Meta:
        model = Usuario
        fields = ('nombre','login','contrasenia','direccion','telefono','email','fecha_nacimiento', 'reserva')

class ReservaMobiBusSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='Usuario.login')
    class Meta:
        model = ReservaMobiBus
        fields = ('fecha', 'usuario')
