
from django.contrib import admin

from django.urls import path
from SistemaCompraApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('principalDepartamentos',views.principalDepartamentos),
    path('principalEmpleados',views.principalEmpleados),
    path('principalArticulos',views.principalArticulos),
    path('principalMarcas', views.principalMarcas, name='principalMarcas'),
    path('principalUnidadesdeMedida', views.principalUnidadesdeMedida, name='principalUnidadesdeMedida'),
    path('principalProveedores', views.principalProveedores, name='principalProveedores'),
    



    path('edicionDepartamento/<iddepartamento>', views.edicionDepartamento, name='edicionDepartamento'),
    path('edicionEmpleados/<idempleado>', views.edicionEmpleados, name='edicionEmpleados'),
    path('edicionArticulos/<idarticulo>', views.edicionArticulos, name='edicionArticulos'),

    path('editarDepartamento/', views.editarDepartamento, name='editarDepartamento'),
    path('editarEmpleado/', views.editarEmpleado, name='editarEmpleado'),
    path('editarArticulos/', views.editarArticulos, name='editarArticulos'),



    path('registrarDepartamentos/', views.registrarDepartamentos),
    path('registrarEmpleado/', views.registrarEmpleado),
    path('registrarArticulo/', views.registrarArticulo),

    path('eliminarEmpleado/<idempleado>',views.eliminarEmpleado, name='eliminarEmpleado'),
    path('eliminarDepartamento/<iddepartamento>',views.eliminarDepartamento, name='eliminarDepartamento'),
    path('eliminarArticulo/<idarticulo>',views.eliminarArticulo, name='eliminarArticulo'),




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
