from django.db import models
from django.contrib.gis.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils import timezone
from usuarios.models import ReservaMobiBus

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
    reserva = models.ForeignKey('usuarios.ReservaMobiBus', related_name='recorrido')
    conductor = models.ForeignKey('ConductorMoviBus', related_name='recorrido')

    def __unicode__(self):
        return "Recorrido MoviBus " + self.inicio.strftime("%Y-%m-%d %H:%M:%S") + ": " + self.reserva.usuario.nombre
