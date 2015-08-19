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
    #kilometraje = models.FloatField(default = 1)
    fecha_fabricacion = models.DateField(_("Fecha de Fabricacion"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    cap_max = models.IntegerField()
    linea = models.CharField(max_length = 1, blank = True)
    lon = models.FloatField()
    lat = models.FloatField()
    objects = models.GeoManager()
    conductor = models.OneToOneField(ConductorTranvia, null = True)
    estado_operativo = models.BooleanField(default = True)

    def generar_reporte(self):
        reporte = {}
        reporte['Placa'] = str(self.placa)
        reporte['Marca'] = str(self.marca)
        reporte['Modelo'] = str(self.modelo)
        #reporte['Kilometraje'] = str(self.kilometraje)
        reporte['Fecha Fabricacion'] = str(self.fecha_fabricacion)
        reporte['Capacidad Maxima'] = str(self.cap_max)
        reporte['Linea'] = str(self.linea)
        reporte['Ubicacion Actual'] = "Lon: " + str(self.lon) + " -  Lat: " + str(self.lat)
        reporte['Conductor Actual'] = str(self.conductor)

        f = open('reporte_tranvia.txt','w')
        f.write('Reporte Tranvia ' + self.placa + '\n' + '\n')
        f.write('')
        line = "\n".join("%0s\t%15s" % (i, reporte[i]) for i in reporte)
        f.write(line)
        f.close()

    def __unicode__(self):
        return self.placa

#Clase que modela un MoviBus de tcb

class MoviBus(models.Model):
    placa = models.CharField(max_length = 200, unique = True)
    marca = models.CharField(max_length = 200)
    modelo = models.CharField(max_length = 200)
    kilometraje = models.FloatField(blank=True)
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
    estacion = models.ForeignKey(EstacionVcub, null = True, blank = True)
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

    def __unicode__(self):
        return "Usuario - " + self.fecha

#Clase que modela una alerta de tranvia

class AlertaTranvia(models.Model):
    fecha = models.DateField(_("Fecha de Alerta"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    tranvia =  models.ForeignKey(Tranvia, null = True)
    solicita_reposicion = models.BooleanField(default=True)

    def __unicode__(self):
        return "Alerta - " + self.tranvia.placa
