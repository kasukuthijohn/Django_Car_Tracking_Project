from django.db import models

# Create your models here.
class Station(models.Model):
    StationName=models.CharField(max_length=234)
    StationLocation=models.CharField(max_length=234)

    def __str__(self):
        return self.StationName;

class Vehicles(models.Model):
    Car_Number=models.CharField(max_length=20)
    Car_model=models.CharField(max_length=234)
    Car_Mileage=models.IntegerField()
    stations=models.ManyToManyField(Station)

    def __str__(self):
        return self.Car_model;
