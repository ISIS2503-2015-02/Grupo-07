from django.db import models

# Create your models here.
class BusPrueba(models.Model):
    msg = models.CharField(max_length = 100)