from django.db import models
from django.contrib.gis.db import models
from datetime import datetime, timedelta
from django.utils.translation import gettext as _
from django.utils import timezone
from usuarios.models import ReservaMobiBus
from math import sin, cos, atan2, sqrt, floor
from geopy.distance import vincenty

#Clase que modela un conductor de MoviBus de tcb

class ConductorMoviBus(models.Model):
    nombre = models.CharField(max_length = 200)
    cedula = models.CharField(max_length = 200, unique = True)
    calificacion = models.IntegerField(default = 0)
    kilometros_recorridos = models.FloatField(default = 0)
    velocidad_promedio = models.FloatField(default = 0)
    fecha_ingreso_sistema = models.DateTimeField(auto_now_add=True)
    fecha_de_nacimiento = models.DateField(_("Fecha de Nacimiento"), blank=True, default = datetime(1980, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    movibus = models.ForeignKey('MoviBus',related_name='conductor')

    def dar_kilometros_recorridos(self):
        return self.kilometros_recorridos

    def __unicode__(self):
        return self.nombre

#Clase que modela un MoviBus de tcb

class MoviBus(models.Model):
    placa = models.CharField(max_length = 200, unique = True)
    marca = models.CharField(max_length = 200)
    modelo = models.CharField(max_length = 200)
    velocidad_promedio = models.FloatField(default = 0)
    kilometraje = models.FloatField(blank=True, default = 1)
    fecha_fabricacion = models.DateField(_("Fecha de Fabricacion"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    cap_max = models.IntegerField()
    ruta = models.CharField(max_length = 1, blank = True)
    #objects = models.CharField(max_length = 200)
    estado_operativo = models.BooleanField(default=True)

    #Genera un reporte en un archivo txt

    def generar_reporte(self):
        reporte = {}
        reporte['Placa'] = str(self.placa)
        reporte['Marca'] = str(self.marca)
        reporte['Modelo'] = str(self.modelo)
        reporte['Kilometraje'] = str(self.kilometraje)
        reporte['Fecha Fabricacion'] = self.fecha_fabricacion.strftime("%Y-%m-%d")
        reporte['Capacidad Maxima'] = str(self.cap_max)
        reporte['Ruta'] = str(self.ruta)

        f = open('Reporte_MoviBus_' + self.placa + '.txt','w')
        f.write('Reporte MoviBus ' + self.placa + '\n' + '\n')
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

class CoordenadasMoviBus(models.Model):
    movibus = models.ForeignKey('MoviBus', related_name='coordenada')
    fecha = models.DateTimeField(auto_now_add=True)
    latitud = models.FloatField(default = 1)
    longitud = models.FloatField(default = 1)
    recorrido = models.ForeignKey('RecorridoMoviBus', null=True, blank=True, default = None, related_name='coordenada')

    class Meta:
        unique_together = ('movibus', 'fecha')

    def __unicode__(self):
        return self.movibus.placa

class ReporteMoviBus(models.Model):
    movibus = models.ForeignKey('MoviBus',related_name='reporte')
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movibus', 'fecha')

    def __unicode__(self):
        return "Reporte MoviBus " + self.movibus.placa + ": " + self.fecha.strftime("%Y-%m-%d %H:%M:%S") + self.movibus.generar_reporte()

class RecorridoMoviBus(models.Model):
    inicio = models.DateTimeField(auto_now_add=True)
    fin = models.DateTimeField(auto_now_add=True)
    movibus = models.ForeignKey('MoviBus', related_name='recorrido')
    reserva = models.ForeignKey('usuarios.ReservaMobiBus', related_name='recorrido')
    conductor = models.ForeignKey('ConductorMoviBus', related_name='recorrido')

    def velocidad_promedio(self):
        coordenadas_totales = []
        tiempo = 0
        diferencia = 0
        for coordenada in CoordenadasMoviBus.objects.all():
            if coordenada.recorrido.reserva == self.reserva:
                coordenadas_totales.append(coordenada)
        cantidad = len(coordenadas_totales)
        while cantidad > 1:
            coordenada2 = coordenadas_totales.pop(0)
            coordenada1 = coordenadas_totales.pop(0)
            coordenadas_totales.append(coordenada2)

            fecha1 = coordenada1.fecha
            fecha2 = coordenada2.fecha
            diferencia = fecha2 - fecha1
            timedelta(0,8,562000)
            tiempo = divmod(diferencia.days * 86400 + diferencia.seconds, 60)
            cantidad = cantidad - 1
        return tiempo

    def distancia(self):
        coordenadas_totales = []
        dis = vincenty((0,0),(0,0))
        for coordenada in CoordenadasMoviBus.objects.all():
            if coordenada.recorrido.reserva == self.reserva:
                coordenadas_totales.append(coordenada)
        cantidad = len(coordenadas_totales)
        while cantidad > 1:
            coordenada1 = coordenadas_totales.pop(0)
            coordenada2 = coordenadas_totales.pop(0)
            coordenadas_totales.append(coordenada2)

            lon1 = coordenada1.longitud
            lat1 = coordenada1.latitud
            lon2 = coordenada2.longitud
            lat2 = coordenada2.latitud
            dis = dis + vincenty((lat1,lon1),(lat2,lon2))
            cantidad = cantidad - 1
        return dis

    def __unicode__(self):
        return "Recorrido MoviBus " + self.inicio.strftime("%Y-%m-%d %H:%M:%S") + ": " + self.reserva.usuario.nombre
