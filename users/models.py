from django.db import models
from django.contrib.gis.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils import timezone
from django import forms
from movibuses.models import MoviBus

# Create your models here.

class Usuario(models.Model):
    login = models.CharField(max_length = 200, unique = True)
    contrasenia = forms.CharField(max_length = 200)
    nombre = models.CharField(max_length = 200)
    fecha_nacimiento = models.DateField(_("Fecha de Nacimiento"), blank=True, default = datetime(1980, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))

    def __unicode__(self):
        return nombre

#Clase que modela una reserva de un usuario de moviBus

class ReservaMobiBus(models.Model):
    usuario = models.OneToOneField(Usuario, null = True)
    movi_bus = models.OneToOneField(MoviBus, null = True)
    fecha = models.DateField(_("Fecha de Reserva"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))

    def __unicode__(self):
        return "Usuario - " + self.fecha
