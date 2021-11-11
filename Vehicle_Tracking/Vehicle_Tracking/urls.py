"""Vehicle_Tracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Car_Tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.htmlfile1),
    path('Altroz_details',views.Altroz_details),
    path('Benz_details',views.Benz_details),
    path('Audi_details',views.Audi_details),
    path('bmw',views.bmw),
    path('Dacia',views.Dacia),
]
