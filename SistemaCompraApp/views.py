from django.shortcuts import render, redirect
from .models import Departamentos, Empleados,Marcas, UnidadesMedida, Proveedores,Articulos
import sweetify # type: ignore

# Create your views here.

def index(request):
    return render(request, 'index.html')


def principalDepartamentos(request):
    departamentos = Departamentos.objects.all()

    return render(request, 'principalDepartamentos.html',{
        'departamentos':departamentos
    })


def principalEmpleados(request):
    empleados = Empleados.objects.all()
    departamentos = Departamentos.objects.all()

    return render(request, 'principalEmpleados.html',{
        'empleados':empleados,
        'departamentos':departamentos
    })


def principalMarcas(request):
    listadoMarcas = Marcas.objects.all()
    return render(request, 'principalMarcas.html', {'marcas': listadoMarcas})

def principalUnidadesdeMedida(request):
    listadoUnidades = UnidadesMedida.objects.all()
    return render(request, 'principalUnidadesdeMedida.html', {'unidades': listadoUnidades})

def principalProveedores(request):
    listadoProveedor = Proveedores.objects.all()
    return render(request, 'principalProveedores.html', {'proovedor': listadoProveedor})



def principalArticulos(request):
    listadoArticulos = Articulos.objects.all()
    listadoMarcas = Marcas.objects.all()
    listadoUnidadMedida = UnidadesMedida.objects.all()

    return render(request, 'principalArticulos.html', {'articulos': listadoArticulos, 
                                                       'marcas':listadoMarcas,
                                                       'unidadMedidas':listadoUnidadMedida})




def edicionArticulos(request, idarticulo):
    articulo = Articulos.objects.get(idarticulo = idarticulo)
    marca = Marcas.objects.all()
    unidadMedida = UnidadesMedida.objects.all()

    return render(request,'edicionArticulos.html', {'articulo': articulo, 'marcas':marca, 'unidadMedida':unidadMedida})





def editarArticulos(request):
    idarticulo = request.POST['txtIdArticulos']
    descripcion = request.POST['txtDescripcionArticulos']
    id_unidadmedida = request.POST['txtUnidadMedidaArticulos']
    existencia = request.POST['txtExistenciaArticulos']
    idmarca = request.POST['txtMarcaArticulos']


    instance_marca = Marcas.objects.get(idmarca = idmarca)
    instance_unidadMedida = UnidadesMedida.objects.get(idunidadmedida = id_unidadmedida)

    if 'txtEstadoArticulo' in request.POST:
        estado = request.POST['txtEstadoArticulo']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    articulo = Articulos.objects.get(idarticulo = idarticulo)
    articulo.estado = estado
    articulo.descripcion = descripcion
    articulo.existencia = existencia
    articulo.marca = instance_marca
    articulo.unidadmedida = instance_unidadMedida
    articulo.save()

    return redirect('/principalArticulos')


def registrarDepartamentos(request):
    nombre = request.POST['txtNombreDepartamento']
    estado = request.POST['txtEstadoDepartamento']

  #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Departamentos.objects.create(nombre = nombre, estado = estado)
    sweetify.success(request, 'Departamento Agregada Correctamente!!!')
    
    
    return redirect('/principalDepartamentos')




def registrarArticulo(request):
    descripcion = request.POST['txtDescripcionArticulos']
    id_unidadmedida = request.POST['txtUnidadMedidaArticulos']
    existencia = request.POST['txtExistenciaArticulos']
    idmarca = request.POST['txtMarcaArticulos']
    estado = request.POST['txtEstadoArticulo']




    instance_marca = Marcas.objects.get(idmarca = idmarca)
    instance_unidadMedida = UnidadesMedida.objects.get(idunidadmedida = id_unidadmedida)


    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Articulos.objects.create(descripcion=descripcion,
                            marca=instance_marca,
                            unidadmedida=instance_unidadMedida,
                            existencia = existencia,
                            estado = estado)
    

    sweetify.success(request, 'Articulo Agregado Correctamente!!!')

    return redirect('/principalArticulos')









def registrarMarcas(request):
    descripcion = request.POST['txtdescripcionMarca']
    estado = request.POST['txtEstadoMarca']

    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Marcas.objects.create(descripcion=descripcion, estado=estado)
    sweetify.success(request, 'Marcas Agregada Correctamente!!!')

    return redirect('/principalMarcas')



def registrarEmpleado(request):
    cedula = request.POST['txtEmpleadoCedula']
    nombre = request.POST['txtEmpleadoNombre']
    estado = request.POST['txtEmpleadoEstado']
    iddepartamento = request.POST['txtDepartamentoId']

    intance_Departamento = Departamentos.objects.get(iddepartamento = iddepartamento)


    Empleados.objects.create(cedula = cedula, nombre=nombre, departamento=intance_Departamento, estado=estado)
    sweetify.success(request, 'Marca Agregada Correctamente!!!')

    return redirect('/principalEmpleados')

def registrarUnidadesdeMedida(request):
    descripcion = request.POST['txtdescripcionUnidadesdeMedida']
    estado = request.POST['txtEstadoUnidadesdeMedida']

    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    UnidadesMedida.objects.create(descripcion = descripcion, estado=estado)
    sweetify.success(request, 'Unidad Medida Agregada Correctamente!!!')

    return redirect('/principalUnidadesdeMedida')


def eliminarDepartamento(request,iddepartamento):
    departamentos = Departamentos.objects.get(iddepartamento=iddepartamento)
    departamentos.delete()
    sweetify.success(request, 'Departamento Eliminada Correctamente!!!')
    return redirect('/principalDepartamentos')


def eliminarEmpleado(request,idempleado):
    empleado = Empleados.objects.get(idempleado=idempleado)
    empleado.delete()
    sweetify.success(request, 'Empleado Eliminado Correctamente!!!')
    return redirect('/principalEmpleados')




def edicionEmpleados(request, idempleado):
    empleado = Empleados.objects.get(idempleado=idempleado)
    departamento = Departamentos.objects.all()
    return render(request, 'edicionEmpleado.html', {'empleado': empleado,
                                                    'departamentos':departamento})



def edicionDepartamento(request, iddepartamento):
    departamento = Departamentos.objects.get(iddepartamento=iddepartamento)
    return render(request, 'edicionDepartamento.html', {'departamento': departamento})


def editarDepartamento(request):
    iddepartamento  = request.POST['txtIdDepartamento']
    nombre = request.POST['txtNombreDepartamento']


    if 'txtEstadoDepartamento' in request.POST:
        estado = request.POST['txtEstadoDepartamento']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    departamento = Departamentos.objects.get(iddepartamento = iddepartamento)
    departamento.estado = estado
    departamento.nombre = nombre
    departamento.save()

    return redirect('/principalDepartamentos')

def registrarProveedor(request):
    cedularnc = request.POST['txtcedulaProveedor']
    nombrecomercial = request.POST['txtNombreComercialProveedor']
    estado = request.POST['txtEstadoProveedor']

    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Proveedores.objects.create(nombrecomercial=nombrecomercial, cedularnc=cedularnc, estado=estado)
    sweetify.success(request, 'Marca Agregada Correctamente!!!')

    return redirect('/principalProveedores')

def eliminarMarcas(request,idmarca):
    marca = Marcas.objects.get(idmarca=idmarca)
    marca.delete()
    sweetify.success(request, 'Marca Eliminada Correctamente!!!')
    return redirect('/principalMarcas')

def eliminarUnidades(request,idunidadmedida):
    unidad = UnidadesMedida.objects.get(idunidadmedida=idunidadmedida)
    unidad.delete()
    sweetify.success(request, 'Unidades Eliminada Correctamente!!!')
    return redirect('/principalUnidadesdeMedida')

def eliminarProveedor(request,idproveedor):
    proveedor = Proveedores.objects.get(idproveedor=idproveedor)
    proveedor.delete()
    sweetify.success(request, 'Proveedor Eliminada Correctamente!!!')
    return redirect('/principalProveedores')

def eliminarArticulo(request,idarticulo):
    articulo = Articulos.objects.get(idarticulo=idarticulo)
    articulo.delete()
    sweetify.success(request, 'Articulo Eliminado Correctamente!!!')
    return redirect('/principalArticulos')


def editarMarcas(request):
    idmarca = request.POST['txtIdmarca']
    descripcion = request.POST['txtdescripcionMarca']

    if 'txtEstadoMarcas' in request.POST:
        estado = request.POST['txtEstadoMarcas']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    marcas = Marcas.objects.get(idmarca=idmarca)
    marcas.descripcion = descripcion
    marcas.estado = estado
    marcas.save()

    sweetify.success(request, 'Marcas Modificado Correctamente!!!')

    return redirect('/principalMarcas')

def editarEmpleado(request):
    idempleado  = request.POST['txtEmpleadoId']
    nombre = request.POST['txtEmpleadoNombre']
    cedula = request.POST['txtEmpleadoCedula']
    iddepartamento = request.POST['txtDepartamentoId']
    intance_Departamento = Departamentos.objects.get(iddepartamento = iddepartamento)

    if 'txtEmpleadoEstado' in request.POST:
        estado = request.POST['txtEmpleadoEstado']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    empledo = Empleados.objects.get(idempleado = idempleado)
    empledo.cedula = cedula
    empledo.estado = estado
    empledo.departamento = intance_Departamento
    empledo.nombre = nombre
    empledo.save()

    sweetify.success(request, 'Empleado Modificado Correctamente!!!')

    return redirect('/principalEmpleados')

def editarProveedor(request):
    idproveedor = request.POST['txtIdproveedor']
    cedularnc = request.POST['txtcedulaProveedor']
    nombrecomercial = request.POST['txtNombreComercialProveedor']

    if 'txtEstadoProovedor' in request.POST:
        estado = request.POST['txtEstadoProveedor']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    proveedor = Proveedores.objects.get(idproveedor=idproveedor)
    proveedor.cedularnc = cedularnc
    proveedor.nombrecomercial = nombrecomercial
    proveedor.estado =estado
    proveedor.save()

    sweetify.success(request, 'Proveedor Modificada Correctamente!!!')

    return redirect('/principalProveedores')

def editarUnidades(request):
    idunidadmedida = request.POST['txtIdunidad']
    descripcion = request.POST['txtdescripcionUnidadesdeMedida']

    if 'txtEstadoUnidadesdeMedida' in request.POST:
        estado = request.POST['txtEstadoUnidadesdeMedida']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    unidad = UnidadesMedida.objects.get(idunidadmedida=idunidadmedida)
    unidad.descripcion = descripcion
    unidad.estado =estado
    unidad.save()

    sweetify.success(request, 'Marca Modificada Correctamente!!!')

    return redirect('/principalUnidadesdeMedida')


def edicionUnidades(request, idunidadmedida):
    unidad = UnidadesMedida.objects.get(idunidadmedida=idunidadmedida)
    return render(request, 'edicionUnidades.html', {'unidad': unidad})

def edicionMarcas(request, idmarca):
    marca = Marcas.objects.get(idmarca=idmarca)
    return render(request, 'edicionMarcas.html', {'marca': marca})

def edicionProveedor(request, idproveedor):
    proveedor = Proveedores.objects.get(idproveedor=idproveedor)
    return render(request, 'edicionProveedor.html', {'proveedor': proveedor})

 
