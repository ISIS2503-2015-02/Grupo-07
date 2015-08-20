from django.db import models
from django.contrib.gis.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils import timezone
from movibuses.models import MoviBus
from tranvias.models import Tranvia

class ReporteMoviBus(models.Model):
    movibus = models.OneToOneField(MoviBus, null = True)
    fecha = models.DateField(_("Fecha"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))

    def __unicode__(self):
        return "Reporte MoviBus " + self.movibus.placa + ": " + str(self.fecha) + self.movibus.generar_reporte()

class ReporteTranvia(models.Model):
    tranvia = models.OneToOneField(Tranvia, null = True)
    fecha = models.DateField(_("Fecha"), blank=True, default = datetime(2010, 1, 1, 13, 0, 0, 775217,tzinfo = timezone.get_current_timezone()))

    def __unicode__(self):
        return "Reporte Tranvia " + self.tranvia.placa + ": " + str(self.fecha) + self.tranvia.generar_reporte()
