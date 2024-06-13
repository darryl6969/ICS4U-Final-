from django.db import models

class WeatherInfo(models.Model):
    Year = models.IntegerField()
    Month = models.IntegerField()
    Date = models.CharField(max_length = 15)
    Temperature = models.FloatField()
    meteorologicalConditions = models.CharField(max_length = 300)
    windSpeedInKM = models.IntegerField()
    sunriseInAM = models.IntegerField()
    sunsetInPM = models.IntegerField()