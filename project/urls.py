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

from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from ejemplo.views import (buscar,
                             monstrar_familiares, mostrar_mascotas,
                            BuscarFamiliar, AltaFamiliar, ActualizarFamiliar,
                            BorrarFamiliar, BuscarMascota, AltaMascota, ActualizarMascota,BorrarMascota, pagina_principal,
                            mostrar_vehiculo, BuscarVehiculo, AltaVehiculo, ActualizarVehiculo, BorrarVehiculo, FamiliarList,
                            FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
from ejemplo_2.views import(index, PostList, PostCrear, 
                             PostBorrar, PostActualizar, PostDetalle,
                             UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar,
                             MensajeCrear, MensajeListar, MensajeDetalle)

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
    path('vehiculos/alta', AltaVehiculo.as_view()),
    path("vehiculos/actualizar/<int:pk>", ActualizarVehiculo.as_view()),
    path('vehiculos/borrar/<int:pk>' , BorrarVehiculo.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()), 
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('succes_update_message/', TemplateView.as_view(template_name= 'ejemplo/succes_update_message.html')),
    path('ejemplo-dos/', index, name='ejemplo-dos-index'),
    path('ejemplo-dos/listar/', PostList.as_view(), name='listar'),
    path('ejemplo-dos/crear/', PostCrear.as_view(), name='ejemplo-dos-crear'),
    path('ejemplo-dos/borrar/<int:pk>', PostBorrar.as_view(), name='borrar-2' ),
    path('ejemplo-dos/actualizar/<int:pk>', PostActualizar.as_view(), name='actualizar-2'),
    path('ejemplo-dos/<int:pk>/detalle/', PostDetalle.as_view(), name= 'ejemplo-dos-detalle'),
    path('ejemplo-dos/signup/',UserSignUp.as_view(), name= 'signup' ),
    path('ejemplo-dos/login/', UserLogin.as_view(), name='login'),
    path('ejemplo-dos/logout/', UserLogout.as_view(), name='logout'),
    path('ejemplo-dos/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name='avatar-actualizar'),
    path('ejemplo-dos/users/<int:pk>/actualizar/', UserActualizar.as_view(), name='user-actualizar' ),
    path('ejemplo-dos/mensajes/crear/', MensajeCrear.as_view(), name='crear-mensaje'),
    path('ejemplo-dos/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name='detalle-mensaje'),
    path('ejemplo-dos/mensajes/listar/', MensajeListar.as_view(), name='listar-mensaje'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





