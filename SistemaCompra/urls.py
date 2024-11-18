
from django.contrib import admin

from django.urls import path
from SistemaCompraApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index1, name='index1'),
    path('index',views.index, name='index'),


    # Section of report
    path('generateReportDepartment',views.generateReportDepartment, name='generateReportDepartment'),
    path('generateReportEmpleados',views.generateReportEmpleados, name='generateReportEmpleados'),
    path('generateReportBrand',views.generateReportBrand, name='generateReportBrand'),
    path('generateReportMeasurement',views.generateReportMeasurement, name='generateReportMeasurement'),
    path('generateReportProvider',views.generateReportProvider, name='generateReportProvider'),
    path('generateReportArticle',views.generateReportArticle, name='generateReportArticle'),
    path('generateReportOrder',views.generateReportOrder, name='generateReportOrder'),

    path('principalDepartamentos',views.principalDepartamentos, name='principalDepartamentos'),
    path('principalEmpleados',views.principalEmpleados),
    path('principalArticulos',views.principalArticulos),
    path('principalMarcas', views.principalMarcas, name='principalMarcas'),
    path('principalUnidadesdeMedida', views.principalUnidadesdeMedida, name='principalUnidadesdeMedida'),
    path('principalProveedores', views.principalProveedores, name='principalProveedores'),
    path('lista_departametos', views.lista_departametos, name='lista_departametos'),
    path('principalOrdenCompra', views.principalOrdenCompra, name='principalOrdenCompra'),




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
    path('eliminarOrdenCompra/<idordencompra>',views.eliminarOrdenCompra, name='eliminarOrdenCompra'),




    path('registrarMarcas/', views.registrarMarcas, name='registrarMarcas'),
    path('registrarUnidadesdeMedida/', views.registrarUnidadesdeMedida, name='registrarUnidadesdeMedida'),
    path('registrarProveedor/', views.registrarProveedor, name='registrarProveedor'),
    path('registrarOrdenCompra/', views.registrarOrdenCompra, name='registrarOrdenCompra'),

    path('eliminarMarcas/<idmarca>', views.eliminarMarcas, name='eliminarMarcas'),
    path('eliminarUnidades/<idunidadmedida>', views.eliminarUnidades, name='eliminarUnidades'),
    path('eliminarProveedor/<idproveedor>', views.eliminarProveedor, name='eliminarProveedor'),

    path('edicionMarcas/<idmarca>', views.edicionMarcas, name='edicionMarcas'),
    path('edicionUnidades/<idunidadmedida>', views.edicionUnidades, name='edicionUnidades'),

    path('edicionProveedor/<idproveedor>', views.edicionProveedor, name='edicionProveedor'),

    path('editarMarcas/', views.editarMarcas, name='editarMarcas'),
    path('editarUnidades/', views.editarUnidades, name='editarUnidades'),
    path('editarProveedor/', views.editarProveedor, name='editarProveedor'),

    path('logout/', views.signout, name='logout'), 
    path('signin/',views.signin, name="signin"),
    path('signup/', views.signup, name='signup')



]
