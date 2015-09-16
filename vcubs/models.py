from django.db import models
from django.contrib.gis.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils import timezone

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

    def necesita_refill(self):
        return self.cap_actual <= (self.cap_max*0.1)

    def __unicode__(self):
        return self.nombre

    necesita_refill.admin_order_field = 'necesita_refill'
    necesita_refill.boolean = True
    necesita_refill.short_description = 'Ordenar Refill?'

#Clase que modela una vcub de tcb

class Vcub(models.Model):
    registro = models.CharField(max_length = 200, unique = True)
    marca = models.CharField(max_length = 200)
    modelo = models.CharField(max_length = 200)
    fecha_fabricacion = models.DateField(_("Fecha de Fabricacion"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    estacion = models.ForeignKey(EstacionVcub, null = True, blank = True, related_name='vcubs')
    objects = models.GeoManager()
    en_transito = models.BooleanField(default=True)
    estado_operativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.registro
