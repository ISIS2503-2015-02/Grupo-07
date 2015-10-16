from django.db import models
from django.contrib.gis.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils import timezone
from django import forms
import time

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length = 200)
    login = models.CharField(max_length = 200, primary_key = True)
    contrasenia = models.CharField(max_length=200)
    direccion = models.CharField(max_length = 200, default = "")
    telefono = models.CharField(max_length = 200, default = "")
    email = models.EmailField(unique = True)
    fecha_nacimiento = models.DateField(_("Fecha de Nacimiento"), blank=True, default = datetime(1980, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))

    def __unicode__(self):
        return self.nombre

#Clase que modela una reserva de un usuario de moviBus

class ReservaMobiBus(models.Model):
    identificador = models.CharField(primary_key = True, max_length = 200)
    usuario = models.ForeignKey('Usuario', related_name='reserva')
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_programada = models.DateTimeField(default = datetime.now())

    def __unicode__(self):
        return "Reserva Usuario No. " + self.identificador + " - " + self.fecha.strftime("%Y-%m-%d %H:%M:%S")
