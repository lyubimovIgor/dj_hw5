from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)

class Measurement(models.Model):
    sensor= models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    img_of_measurement = models.ImageField(null=True, blank=True)