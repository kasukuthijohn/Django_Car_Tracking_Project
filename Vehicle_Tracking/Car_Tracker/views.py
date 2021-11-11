from django.shortcuts import render
from .models import Station,Vehicles
# Create your views here.

def htmlfile1(request):
    data = Vehicles.objects.all()
    data2=Station.objects.all()
    return render(request,"htmlfile.html",{'data1':data,'data2':data2})

def data(request):
    return render(request,"data.html")

def Altroz_details(request):
    return render(request,'Altroz_details.html')
def Audi_details(request):
    return render(request,'Audi_details.html')
def Benz_details(request):
    return render(request,'Benz_details.html')
def bmw(request):
    return render(request,'bmw.html')
def Dacia(request):
    return render(request,'Dacia.html')
