from django.db import models
from django.contrib.gis.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils import timezone

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
