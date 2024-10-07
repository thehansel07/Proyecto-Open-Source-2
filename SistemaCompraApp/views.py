from django.shortcuts import render, redirect
from .models import Marcas, UnidadesMedida, Proveedores
import sweetify # type: ignore

# Create your views here.

def index(request):
    return render(request, 'index.html')

def principalMarcas(request):
    listadoMarcas = Marcas.objects.all()
    return render(request, 'principalMarcas.html', {'marcas': listadoMarcas})

def principalUnidadesdeMedida(request):
    listadoUnidades = UnidadesMedida.objects.all()
    return render(request, 'principalUnidadesdeMedida.html', {'unidades': listadoUnidades})

def principalProveedores(request):
    listadoProveedor = Proveedores.objects.all()
    print(listadoProveedor)
    return render(request, 'principalProveedores.html', {'proovedor': listadoProveedor})

def registrarMarcas(request):
    descripcion = request.POST['txtdescripcionMarca']
    estado = request.POST['txtEstadoMarca']

    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Marcas.objects.create(descripcion=descripcion, estado=estado)
    sweetify.success(request, 'Marca Agregada Correctamente!!!')

    return redirect('/principalMarcas')

def registrarUnidadesdeMedida(request):
    descripcion = request.POST['txtdescripcionUnidadesdeMedida']
    estado = request.POST['txtEstadoUnidadesdeMedida']

    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    UnidadesMedida.objects.create(descripcion=descripcion, estado=estado)
    sweetify.success(request, 'Marca Agregada Correctamente!!!')

    return redirect('/principalUnidadesdeMedida')

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
    print(idunidadmedida)
    unidad.delete()
    sweetify.success(request, 'Unidades Eliminada Correctamente!!!')
    return redirect('/principalUnidadesdeMedida')

def eliminarProveedor(request,idproveedor):
    proveedor = Proveedores.objects.get(idproveedor=idproveedor)
    proveedor.delete()
    sweetify.success(request, 'Proveedor Eliminada Correctamente!!!')
    return redirect('/principalProveedores')

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

    marca = Marcas.objects.get(idmarca=idmarca)
    marca.descripcion = descripcion
    marca.estado =estado
    marca.save()

    sweetify.success(request, 'Marca Modificada Correctamente!!!')

    return redirect('/principalMarcas')

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

    if 'txtdescripcionUnidadesdeMedida' in request.POST:
        estado = request.POST['txtdescripcionUnidadesdeMedida']
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

 