from django.db import models
from django.contrib.gis.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils import timezone
import time

#Clase que modela un conductor de tranvia de tcb

class ConductorTranvia(models.Model):
    nombre = models.CharField(max_length = 200)
    cedula = models.CharField(max_length = 200, unique = True)
    calificacion = models.IntegerField(default = 0)
    velocidad_promedio = models.FloatField(default = 0)
    kilometros_recorridos = models.FloatField(default = 0)
    fecha_ingreso_sistema = models.DateTimeField(auto_now_add=True)
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
    velocidad_promedio = models.FloatField(default = 0)
    fecha_fabricacion = models.DateField(_("Fecha de Fabricacion"),  default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    cap_max = models.IntegerField()
    linea = models.ForeignKey('Linea', related_name='tranvia')
    #objects = models.CharField(max_length = 200)
    estado_operativo = models.BooleanField(default = True)

    #Genera un reporte en un archivo txt

    def generar_reporte(self):

        reporte = {}
        reporte['Placa'] = str(self.placa)
        reporte['Marca'] = str(self.marca)
        reporte['Modelo'] = str(self.modelo)
        reporte['Kilometraje'] = str(self.kilometraje)
        reporte['Fecha Fabricacion'] = self.fecha_fabricacion.strftime("%Y-%m-%d")
        reporte['Capacidad Maxima'] = str(self.cap_max)
        reporte['Linea'] = str(self.linea.numero)

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
    fecha = models.DateTimeField(auto_now_add=True)
    latitud = models.FloatField(default = 1)
    longitud = models.FloatField(default = 1)
    recorrido = models.ForeignKey('RecorridoTranvia', null=True, blank=True, default = None, related_name='coordenada')

    class Meta:
        unique_together = ('tranvia', 'fecha')

    def __unicode__(self):
        return self.fecha.strftime("%Y-%m-%d %H:%M:%S") + ": " + self.tranvia.placa

#Clase que modela una alerta de tranvia

class AlertaTranvia(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tranvia = models.ForeignKey('Tranvia', related_name='alerta')
    descripcion = models.TextField(max_length= 200,null = True, default = "Alerta Tranvia")
    solicita_reposicion = models.BooleanField(default=False)

    class Meta:
        unique_together = ('tranvia', 'fecha')

    def __unicode__(self):
        return "Alerta - " + self.tranvia.placa

class ReporteTranvia(models.Model):
    tranvia = models.ForeignKey('Tranvia',related_name='reporte')
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('tranvia', 'fecha')

    def __unicode__(self):
        return "Reporte Tranvia " + self.tranvia.placa + ": " + self.fecha.strftime("%Y-%m-%d %H:%M:%S") + self.tranvia.generar_reporte()

class RecorridoTranvia(models.Model):
    inicio = models.DateTimeField(auto_now_add=True)
    fin = models.DateTimeField(auto_now_add=True)
    tranvia = models.ForeignKey('Tranvia',related_name='recorrido')
    linea = models.ForeignKey('Linea', related_name='recorrido')
    conductor = models.ForeignKey('ConductorTranvia', related_name='recorrido')

    def distancia(self):
        coordenadas_totales = []
        dis = vincenty((0,0),(0,0))
        for coordenada in CoordenadasTranvia.objects.all():
            if coordenada.inicio == self.inicio and coordenada.tranvia.placa == self.tranvia.placa:
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
        return "Recorrido Tranvia " + self.inicio.strftime("%Y-%m-%d %H:%M:%S") + ": Linea(" + self.linea.numero + ")"
