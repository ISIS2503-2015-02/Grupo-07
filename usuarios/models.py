from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from datetime import datetime, date
from django.utils.translation import gettext as _
from django.utils import timezone
from django import forms
import time

#Clase que modela una reserva de un usuario de moviBus

class ReservaMobiBus(models.Model):
    identificador = models.CharField(primary_key = True, max_length = 200)
    usuario = models.ForeignKey(User, related_name='reserva')
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_programada = models.DateTimeField(default = datetime.now())

    def __unicode__(self):
        return "Reserva Usuario No. " + self.identificador + " - " + self.fecha.strftime("%Y-%m-%d %H:%M:%S")
