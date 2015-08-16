from django.db import models
from django.contrib.gis.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils import timezone

#Hola
#Clase que modela un conductor de tranvia de tcb

class ConductorTranvia(models.Model):
    nombre = models.CharField(max_length = 200)
    cedula = models.CharField(max_length = 200, unique = True)
    fecha_de_nacimiento = models.DateField(_("Fecha de Nacimiento"), blank=True, default = datetime(1980, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))

    def __unicode__(self):
        return self.nombre

#Clase que modela un conductor de MoviBus de tcb

class ConductorMoviBus(models.Model):
    nombre = models.CharField(max_length = 200)
    cedula = models.CharField(max_length = 200, unique = True)
    fecha_de_nacimiento = models.DateField(_("Fecha de Nacimiento"), blank=True, default = datetime(1980, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))

    def __unicode__(self):
        return self.nombre

#Clase que modela un tranvia de tcb

class Tranvia(models.Model):
    placa = models.CharField(max_length = 200, unique = True)
    marca = models.CharField(max_length = 200)
    modelo = models.CharField(max_length = 200)
    fecha_fabricacion = models.DateField(_("Fecha de Fabricacion"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    cap_max = models.IntegerField()
    linea = models.CharField(max_length = 1, blank = True)
    lon = models.FloatField()
    lat = models.FloatField()
    objects = models.GeoManager()
    conductor = models.OneToOneField(ConductorTranvia, null = True)
    estado_operativo = models.BooleanField(default = True)

    def __unicode__(self):
        return self.placa

#Clase que modela un MoviBus de tcb

class MoviBus(models.Model):
    placa = models.CharField(max_length = 200, unique = True)
    marca = models.CharField(max_length = 200)
    modelo = models.CharField(max_length = 200)
    fecha_fabricacion = models.DateField(_("Fecha de Fabricacion"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    cap_max = models.IntegerField()
    ruta = models.CharField(max_length = 1, blank = True)
    lon = models.FloatField()
    lat = models.FloatField()
    objects = models.GeoManager()
    conductor = models.OneToOneField(ConductorMoviBus, null = True)
    estado_operativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.placa

#Clase que modela una estacion de vcub de tcb

class EstacionVcub(models.Model):
    nombre = models.CharField(max_length = 200, unique = True)
    fecha_construccion = models.DateField(_("Fecha de Construccion"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    cap_actual = models.IntegerField()
    cap_max = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    objects = models.GeoManager()
    estado_operativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre

#Clase que modela una vcub de tcb

class Vcub(models.Model):
    registro = models.CharField(max_length = 200, unique = True)
    marca = models.CharField(max_length = 200)
    modelo = models.CharField(max_length = 200)
    fecha_fabricacion = models.DateField(_("Fecha de Fabricacion"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    estacion = models.ForeignKey(EstacionVcub, null = True)
    objects = models.GeoManager()
    en_transito = models.BooleanField(default=True)
    estado_operativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.registro

#Clase que modela una reserva de un usuario de moviBus

class ReservaMobiBus(models.Model):
    #usuario = ForeignKey(Usuario)
    movi_bus = models.OneToOneField(MoviBus, null = True)
    fecha = models.DateField(_("Fecha de Reserva"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))

#Clase que modela una alerta de tranvía
class AlertaTranvia(models.Model):
    fecha = models.DateField(_("Fecha de Reserva"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    tranvia =  ForeignKey(Tranvia)
    solicits_reposicion = models.BooleanField(default=True)
