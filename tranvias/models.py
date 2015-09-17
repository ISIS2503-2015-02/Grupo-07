from django.db import models
from django.contrib.gis.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils import timezone

#Clase que modela un conductor de tranvia de tcb

class ConductorTranvia(models.Model):
    nombre = models.CharField(max_length = 200)
    cedula = models.CharField(max_length = 200, unique = True)
    calificacion = models.IntegerField(default = 0)
    kilometros_recorridos = models.FloatField(default = 0)
    fecha_ingreso_sistema = models.DateField(_("Fecha de ingreso al sistema"), blank=True, default = datetime(1980, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    fecha_de_nacimiento = models.DateField(_("Fecha de Nacimiento"), blank=True, default = datetime(1980, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    tranvia = models.ForeignKey('Tranvia',related_name='conductor')

    def dar_kilometros_recorridos(self):
        return self.kilometros_recorridos

    def __unicode__(self):
        return self.nombre

#Clase que modela una linea de tranvia

class Linea(models.Model):
    numero = models.CharField(unique = True, max_length = 200)
    estacion_llegada = models.CharField(max_length = 200, null = True)
    estacion_salida = models.CharField(max_length = 200, null = True)
    kilometros_totales = models.FloatField(default = 0)

    def __unicode__(self):
        return self.numero

#Clase que modela un tranvia de tcb

class Tranvia(models.Model):
    placa = models.CharField(max_length = 200, unique = True)
    marca = models.CharField(max_length = 200)
    modelo = models.CharField(max_length = 200)
    kilometraje = models.FloatField(default = 1)
    fecha_fabricacion = models.DateField(_("Fecha de Fabricacion"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    cap_max = models.IntegerField()
    linea = models.ForeignKey(Linea, null = True, blank = True)
    objects = models.CharField(max_length = 200)
    estado_operativo = models.BooleanField(default = True)

    #Genera un reporte en un archivo txt

    def generar_reporte(self):
        reporte = {}
        reporte['Placa'] = str(self.placa)
        reporte['Marca'] = str(self.marca)
        reporte['Modelo'] = str(self.modelo)
        reporte['Kilometraje'] = str(self.kilometraje)
        reporte['Fecha Fabricacion'] = str(self.fecha_fabricacion)
        reporte['Capacidad Maxima'] = str(self.cap_max)
        reporte['Linea'] = str(self.linea.__unicode__)

        f = open('Reporte_Tranvia_' + self.placa + '.txt','w')
        f.write('Reporte Tranvia ' + self.placa + '\n' + '\n')
        f.write('')
        line = "\n".join("%s\t%s" % (i, reporte[i]) for i in reporte)
        f.write(line)
        f.close()

        return ""

    generar_reporte.admin_order_field = 'generar_reporte'
    generar_reporte.short_description = 'Generar Reporte'

    def __unicode__(self):
        return self.placa

#Clase que guarda las coordenadas de los movibuses

class CoordenadasTranvia(models.Model):
    tranvia = models.ForeignKey('Tranvia',related_name='coordenada')
    fecha = models.DateField(_("Fecha"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    latitud = models.FloatField(default = 1)
    longitud = models.FloatField(default = 1)

    class Meta:
        unique_together = ('tranvia', 'fecha')

    def __unicode__(self):
        return self.fecha + ": " + self.tranvia.placa

#Clase que modela una alerta de tranvia

class AlertaTranvia(models.Model):
    fecha = models.DateField(_("Fecha de Alerta"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    tranvia =  models.ForeignKey('Tranvia', related_name='alerta')
    solicita_reposicion = models.BooleanField(default=True)

    class Meta:
        unique_together = ('tranvia', 'fecha')

    def __unicode__(self):
        return "Alerta - " + self.tranvia.placa

class ReporteTranvia(models.Model):
    tranvia = models.ForeignKey('Tranvia',related_name='reporte')
    fecha = models.DateField(_("Fecha"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))

    class Meta:
        unique_together = ('tranvia', 'fecha')

    def __unicode__(self):
        return "Reporte Tranvia " + self.tranvia.placa + ": " + str(self.fecha) + self.tranvia.generar_reporte()
