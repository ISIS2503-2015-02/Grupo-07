from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.contrib.auth.models import User
from models import ReservaMobiBus
from movibuses.models import RecorridoMoviBus

class UsuarioSerializer(serializers.ModelSerializer):
    #reserva = serializers.PrimaryKeyRelatedField(many=True, queryset=ReservaMobiBus.objects.all())

    def create(self, validated_data):
    	validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')

class ReservaMobiBusSerializer(serializers.ModelSerializer):
    fecha = serializers.ReadOnlyField(default = datetime.now)
    #recorrido = serializers.PrimaryKeyRelatedField(many=True,queryset = RecorridoMoviBus.objects.all())
    class Meta:
        model = ReservaMobiBus
        fields = ('identificador','fecha', 'usuario','fecha_programada',)
