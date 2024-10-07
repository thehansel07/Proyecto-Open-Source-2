"""
URL configuration for SistemaCompra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from SistemaCompraApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('principalMarcas', views.principalMarcas, name='principalMarcas'),
    path('principalUnidadesdeMedida', views.principalUnidadesdeMedida, name='principalUnidadesdeMedida'),
    path('principalProveedores', views.principalProveedores, name='principalProveedores'),
    
    path('registrarMarcas/', views.registrarMarcas, name='registrarMarcas'),
    path('registrarUnidadesdeMedida/', views.registrarUnidadesdeMedida, name='registrarUnidadesdeMedida'),
    path('registrarProveedor/', views.registrarProveedor, name='registrarProveedor'),

    path('eliminarMarcas/<idmarca>', views.eliminarMarcas, name='eliminarMarcas'),
    path('eliminarUnidades/<idunidadmedida>', views.eliminarUnidades, name='eliminarUnidades'),
    path('eliminarProveedor/<idproveedor>', views.eliminarProveedor, name='eliminarProveedor'),

    path('edicionMarcas/<idmarca>', views.edicionMarcas, name='edicionMarcas'),
    path('edicionUnidades/<idunidadmedida>', views.edicionUnidades, name='edicionUnidades'),
    path('edicionProveedor/<idproveedor>', views.edicionProveedor, name='edicionProveedor'),

    path('editarMarcas/', views.editarMarcas, name='editarMarcas'),
    path('editarUnidades/', views.editarUnidades, name='editarUnidades'),
    path('editarProveedor/', views.editarProveedor, name='editarProveedor')

]
