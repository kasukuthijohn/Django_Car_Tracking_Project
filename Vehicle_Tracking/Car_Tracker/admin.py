from django.contrib import admin

# Register your models here.
from Car_Tracker.models import Station,Vehicles

admin.site.register(Station)
admin.site.register(Vehicles)
