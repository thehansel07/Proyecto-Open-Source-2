from django.shortcuts import render, redirect
from .models import Departamentos, Empleados
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



def registrarDepartamentos(request):
    nombre = request.POST['txtNombreDepartamento']
    estado = request.POST['txtEstadoDepartamento']

    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Departamentos.objects.create(nombre=nombre, estado=estado)
    sweetify.success(request, 'Departamento Agregada Correctamente!!!')

    return redirect('/principalDepartamentos')



def registrarEmpleado(request):
    cedula = request.POST['txtEmpleadoCedula']
    nombre = request.POST['txtEmpleadoNombre']
    estado = request.POST['txtEmpleadoEstado']
    iddepartamento = request.POST['txtDepartamentoId']

    intance_Departamento = Departamentos.objects.get(iddepartamento = iddepartamento)



    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Empleados.objects.create(cedula = cedula, nombre=nombre, estado=estado, departamento = intance_Departamento)
    sweetify.success(request, 'Empleado Agregada Correctamente!!!')

    return redirect('/principalEmpleados')


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

    departamento = Departamentos.objects.get(iddepartamento=iddepartamento)
    departamento.nombre = nombre
    departamento.estado = estado
    departamento.save()

    sweetify.success(request, 'Departamento Modificado Correctamente!!!')

    return redirect('/principalDepartamentos')






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

    empleado = Empleados.objects.get(idempleado=idempleado)
    empleado.nombre = nombre
    empleado.cedula = cedula
    empleado.departamento = intance_Departamento
    empleado.estado = estado
    empleado.save()

    sweetify.success(request, 'Departamento Modificado Correctamente!!!')

    return redirect('/principalEmpleados')