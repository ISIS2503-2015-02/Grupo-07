from django.db import models
from django.contrib.gis.db import models
from datetime import datetime, timedelta
from django.utils.translation import gettext as _
from django.utils import timezone
from usuarios.models import ReservaMobiBus
from math import sin, cos, atan2, sqrt, floor, radians
import operator

#Clase que modela un conductor de MoviBus de tcb

class ConductorMoviBus(models.Model):
    nombre = models.CharField(max_length = 200)
    cedula = models.CharField(max_length = 200, primary_key = True)
    calificacion = models.IntegerField(default = 0)
    fecha_ingreso_sistema = models.DateTimeField(auto_now_add=True)
    fecha_de_nacimiento = models.DateField(_("Fecha de Nacimiento"), blank=True, default = datetime(1980, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    movibus = models.ForeignKey('MoviBus',related_name='conductor')

    def kilometros_recorridos(self):
        kilometros = 0.0
        for recorrido in RecorridoMoviBus.objects.all():
            if recorrido.conductor.cedula == self.cedula:
                kilometros += recorrido.dar_kilometros()
        return kilometros

    def velocidad_promedio(self):
        velocidad = 0.0
        for recorrido in RecorridoMoviBus.objects.all():
            if recorrido.conductor.cedula == self.cedula:
                if velocidad > 0:
                    velocidad = (velocidad + recorrido.dar_velocidad())/2
                else:
                    velocidad = recorrido.dar_velocidad()
        return velocidad

    def generar_reporte(self):
        reporte = {}
        reporte['Nombre'] = str(self.nombre)
        reporte['Cedula'] = str(self.cedula)
        reporte['Kilometros Recorrdidos'] = str(self.kilometraje())
        reporte['Velocidad Promedio'] = str(self.velocidad_promedio())
        reporte['Fecha Nacimiento'] = self.fecha_de_nacimiento.strftime("%Y-%m-%d")
        reporte['Fecha Ingreso Sistema'] = self.fecha_ingreso_sistema.strftime("%Y-%m-%d")
        reporte['Movibuss manejados'] = "Movibus " + str(self.movibus)

        f = open('Reporte_Conductor_' + self.cedula + '.csv','w')
        f.write('Reporte Conductor ' + self.cedula + '\n' + '\n')
        f.write('')
        line = "\n".join("%s,%s" % (i, reporte[i]) for i in reporte)
        f.write(line)
        f.close()
        return ""

    def __unicode__(self):
        return self.nombre

#Clase que modela un MoviBus de tcb

class MoviBus(models.Model):
    placa = models.CharField(max_length = 200, primary_key = True)
    marca = models.CharField(max_length = 200)
    modelo = models.CharField(max_length = 200)
    fecha_fabricacion = models.DateField(_("Fecha de Fabricacion"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))
    cap_max = models.IntegerField()
    ruta = models.CharField(max_length = 1, blank = True)
    #objects = models.CharField(max_length = 200)
    estado_operativo = models.BooleanField(default=True)

    def kilometraje(self):
        kilometros = 0.0
        for recorrido in RecorridoMoviBus.objects.all():
            if recorrido.movibus.placa == self.placa:
                kilometros += recorrido.dar_kilometros()
        return kilometros

    def velocidad_promedio(self):
        velocidad = 0.0
        for recorrido in RecorridoMoviBus.objects.all():
            if recorrido.movibus.placa == self.placa:
                if velocidad > 0:
                    velocidad = (velocidad + recorrido.dar_velocidad())/2
                else:
                    velocidad = recorrido.dar_velocidad()
        return velocidad

    def mejor_conductor(self):
        contador = 0
        conductores = {}
        for recorrido in RecorridoMoviBus.objects.all():
            if recorrido.movibus.placa == self.placa:
                conductores[recorrido.conductor.cedula] = 0
        for recorrido in RecorridoMoviBus.objects.all():
            if recorrido.movibus.placa == self.placa:
                conductores[recorrido.conductor.cedula] += 1
        return conductores

    def generar_reporte(self):
        cedula = max(self.mejor_conductor().iteritems(), key=operator.itemgetter(1))[0]
        reporte = {}
        reporte['Placa'] = str(self.placa)
        reporte['Marca'] = str(self.marca)
        reporte['Modelo'] = str(self.modelo)
        reporte['Velocidad Promedio'] = str(self.velocidad_promedio())
        reporte['Kilometraje'] = str(self.kilometraje())
        reporte['Fecha Fabricacion'] = self.fecha_fabricacion.strftime("%Y-%m-%d")
        reporte['Capacidad Maxima'] = str(self.cap_max)
        for conductor in ConductorMoviBus.objects.all():
            if conductor.cedula == cedula:
                reporte['Conductor mas destacado'] = conductor.nombre

        f = open('Reporte_Movibus_' + self.placa + '.csv','w')
        f.write('Reporte Movibus ' + self.placa + '\n' + '\n')
        f.write('')
        line = "\n".join("%s,%s" % (i, reporte[i]) for i in reporte)
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
    recorrido = models.ForeignKey('RecorridoMoviBus', null=True, blank=True, default = None, related_name='coordena')

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
    identificador = models.CharField(max_length = 200, primary_key = True)
    inicio = models.DateTimeField(auto_now_add=True)
    fin = models.DateTimeField(auto_now_add=True)
    movibus = models.ForeignKey('MoviBus', related_name='recorrido')
    reserva = models.ForeignKey('usuarios.ReservaMobiBus', related_name='recorrido')
    conductor = models.ForeignKey('ConductorMoviBus', related_name='recorrido')

    def dar_kilometros(self):
        coordenadas_totales = []
        dis = 0.0
        for coordenada in CoordenadasMoviBus.objects.all():
            if coordenada.recorrido.identificador == self.identificador:
                coordenadas_totales.append(coordenada)
        cantidad = len(coordenadas_totales)
        while cantidad > 1:
            coordenada1 = coordenadas_totales.pop(0)
            coordenada2 = coordenadas_totales[0]

            lon1 = radians(coordenada1.longitud)
            lat1 = radians(coordenada1.latitud)
            lon2 = radians(coordenada2.longitud)
            lat2 = radians(coordenada2.latitud)
            dlat = (lat2 - lat1)/2.0
            dlon = (lon2 - lon1)/2.0
            a = (sin(dlat)*sin(dlat)) + cos(lat1) * cos(lat2) * (sin(dlon)*sin(dlon))
            b = 6371.0 * 2.0 * atan2(sqrt(a),sqrt(1.0-a))
            dis += b
            cantidad = cantidad - 1
        return dis

    def dar_velocidad(self):
        total = 0.0
        coordenadas_totales = []
        tiempo = [0, 0]
        diferencia = 0
        retorno = 0.0
        for coordenada in CoordenadasMoviBus.objects.all():
            if coordenada.recorrido.identificador == self.identificador:
                coordenadas_totales.append(coordenada)
        cantidad = len(coordenadas_totales)
        for i in range(cantidad-1):
            coordenada1 = coordenadas_totales[i]
            coordenada2 = coordenadas_totales[i+1]

            fecha1 = coordenada1.fecha
            fecha2 = coordenada2.fecha
            diferencia = fecha2 - fecha1
            timedelta(0,8,562000)
            actual = divmod(diferencia.days * 86400 + diferencia.seconds, 60)
            tiempo[1] += actual[1]
            if (tiempo[0] + actual[0] > 60):
                tiempo[1] += 1
            tiempo[0] = (tiempo[0] + actual[0]) % 60
            cantidad = cantidad - 1
        total += tiempo[0] + tiempo[1]/60.0
        if total > 0:
            return self.dar_kilometros()/total
        else:
            return 0

    def distancia(self):
        return str(round(self.dar_kilometros(),2)) + " km"

    def velocidad_promedio(self):
        return str(round(self.dar_velocidad(),2)) + " km/min"


    def __unicode__(self):
        return "Recorrido MoviBus No. " + self.identificador + " Usuario " + self.reserva.usuario.nombre + " - " + self.inicio.strftime("%Y-%m-%d %H:%M:%S")
