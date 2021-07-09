"""MiProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from MiProyecto.views import bienvenida, bienvenidaAzul, categoriaEdad, contenidoHTML, miPrimeraPlantilla, momentoActual, plantillaCargador, plantillaHija1, plantillaHija2, plantillaParametro, plantillaShortCut
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('bienvenidaAzul/', bienvenidaAzul),
    path('categoriaEdad/<int:edad>', categoriaEdad),
    path('momentoActual', momentoActual), 
    path('contenidoHTML/<nombre>/<int:edad>', contenidoHTML), 
    path('miPrimeraPlantilla', miPrimeraPlantilla), 
    path('plantillaParametros', plantillaParametro), 
    path('plantillaCargador', plantillaCargador),
    path('plantillaShortCut', plantillaShortCut),
    path('plantillaHija1', plantillaHija1),
    path('plantillaHija2', plantillaHija2),
    
]
