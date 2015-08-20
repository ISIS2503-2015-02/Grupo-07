from django.db import models

# Represents a transport object.
class Transport(models.Model):
	driver_name = models.CharField(max_length=30)
	license_plate = models.CharField(max_length=10)
	transport_type = models.IntegerField()
	transport_status = models.IntegerField()

# Represents historic data.
class Historic(models.Model):
	transport_pk = models.ForeignKey(Transport)
	latitude_pos = models.CharField(max_length=20)
	longitude_pos = models.CharField(max_length=20)
	transport_speed = models.IntegerField()
