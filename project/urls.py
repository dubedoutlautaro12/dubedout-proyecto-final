"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ejemplo.views import (buscar,
                             monstrar_familiares, mostrar_mascotas,
                            BuscarFamiliar, AltaFamiliar, ActualizarFamiliar,
                            BorrarFamiliar, BuscarMascota, AltaMascota, ActualizarMascota,BorrarMascota, pagina_principal,
                            mostrar_vehiculo, BuscarVehiculo, AltaVehiculo)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buscar/', buscar),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>',ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mascotas/', mostrar_mascotas),
    path('mascotas/buscar', BuscarMascota.as_view()),
    path('mascotas/alta', AltaMascota.as_view()),
    path('mascotas/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('mascotas/borrar/<int:pk>', BorrarMascota.as_view()),
    path('pagina-principal/', pagina_principal),
    path('vehiculos/', mostrar_vehiculo),
    path('vehiculos/buscar', BuscarVehiculo.as_view()),
    path('vehiculos/alta', AltaVehiculo.as_view())
]





