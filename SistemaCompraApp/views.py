from django.shortcuts import render, redirect
from .models import Departamentos, Empleados, Marcas, UnidadesMedida, Proveedores, Articulos
import sweetify  # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Create your views here.


def index(request):
    return render(request, 'index.html')


def principalDepartamentos(request):
    query = request.GET.get('q', '')
    lista_departametos = Departamentos.objects.all()


    if query != '':
        lista_departametos = lista_departametos.filter(nombre=query) 
        query = ''

    paginator = Paginator(lista_departametos, 5) 

    page_number = request.GET.get('page')

    try:
        lista_departametos = paginator.page(page_number)

    except PageNotAnInteger:
        lista_departametos = paginator.page(1)

    except EmptyPage:
        lista_departametos = paginator.page(paginator.num_pages)

    return render(request, 'principalDepartamentos.html', {
        'page_obj': lista_departametos,
        'query': query
    })



def principalEmpleados(request):
    query = request.GET.get('q', '')
    lista_empleados = Empleados.objects.all()
    lista_departametos = Departamentos.objects.all()


    if query != '':
        lista_empleados = lista_empleados.filter(nombre=query) 
        query = ''


    paginator = Paginator(lista_empleados, 5) 

    page_number = request.GET.get('page')

    try:
        lista_empleados = paginator.page(page_number)

    except PageNotAnInteger:
        lista_empleados = paginator.page(1)

    except EmptyPage:
        lista_empleados = paginator.page(paginator.num_pages)

    return render(request, 'principalEmpleados.html', {
        'page_obj': lista_empleados,
        'query': query,
        'departamentos': lista_departametos
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
                                                       'marcas': listadoMarcas,
                                                       'unidadMedidas': listadoUnidadMedida})


def edicionArticulos(request, idarticulo):
    articulo = Articulos.objects.get(idarticulo=idarticulo)
    marca = Marcas.objects.all()
    unidadMedida = UnidadesMedida.objects.all()

    return render(request, 'edicionArticulos.html', {'articulo': articulo, 'marcas': marca, 'unidadMedida': unidadMedida})


def editarArticulos(request):
    idarticulo = request.POST['txtIdArticulos']
    descripcion = request.POST['txtDescripcionArticulos']
    id_unidadmedida = request.POST['txtUnidadMedidaArticulos']
    existencia = request.POST['txtExistenciaArticulos']
    idmarca = request.POST['txtMarcaArticulos']

    instance_marca = Marcas.objects.get(idmarca=idmarca)
    instance_unidadMedida = UnidadesMedida.objects.get(
        idunidadmedida=id_unidadmedida)

    if 'txtEstadoArticulo' in request.POST:
        estado = request.POST['txtEstadoArticulo']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    articulo = Articulos.objects.get(idarticulo=idarticulo)
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

  # Valid if estado is on or off#
    if estado:
        estado = 1
    else:
        estado = 0

    Departamentos.objects.create(nombre=nombre, estado=estado)

    return redirect('/principalEmpleados')


def registrarArticulo(request):
    descripcion = request.POST['txtDescripcionArticulos']
    id_unidadmedida = request.POST['txtUnidadMedidaArticulos']
    existencia = request.POST['txtExistenciaArticulos']
    idmarca = request.POST['txtMarcaArticulos']
    estado = request.POST['txtEstadoArticulo']

    instance_marca = Marcas.objects.get(idmarca=idmarca)
    instance_unidadMedida = UnidadesMedida.objects.get(
        idunidadmedida=id_unidadmedida)

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Articulos.objects.create(descripcion=descripcion,
                             marca=instance_marca,
                             unidadmedida=instance_unidadMedida,
                             existencia=existencia,
                             estado=estado)

    sweetify.success(request, 'Articulo Agregado Correctamente!!!')

    return redirect('/principalArticulos')


def registrarMarcas(request):
    descripcion = request.POST['txtdescripcionMarca']
    estado = request.POST['txtEstadoMarca']

    # Valid if estado is on or off#
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
    
    
    #Valid if estado is on or off#
    if estado:
        estado = 1
    else:
        estado = 0
    
    intance_Departamento = Departamentos.objects.get(iddepartamento=iddepartamento)

    Empleados.objects.create(cedula=cedula,
                             nombre=nombre,
                             departamento=intance_Departamento,
                             estado=estado)
        
    return redirect('/principalEmpleados')


# def validar_cedula(cedula):
  # La cédula debe tener 11 dígitos
    if len(cedula) != 11:
        return False
    if (int(cedula[0:3]) != 402 and int(cedula[0:3]) > 121 and int(cedula[0:3]) < 1):
        return False

    suma = 0
    verificador = 0

    for i, n in enumerate(cedula):
        # No ejecutar el ultimo digito
        if (i == len(cedula)-1):
            break
        # Los dígitos pares valen 2 y los impares 1
        multiplicador = 1 if (int(i) % 2) == 0 else 2
        # Se multiplica cada dígito por su paridad
        digito = int(n)*int(multiplicador)
        # Si la multiplicación da de dos dígitos, se suman entre sí
        digito = digito//10 + digito % 10 if (digito > 9) else digito

        # Y se va haciendo la acumulación de esa suma
        suma = suma + digito

    # Al final se obtiene el verificador con la siguiente fórmula
    verificador = (10 - (suma % 10)) % 10

    # Se comprueba el verificador
    return (verificador == int(cedula[-1:]))


def registrarUnidadesdeMedida(request):
    descripcion = request.POST['txtdescripcionUnidadesdeMedida']
    estado = request.POST['txtEstadoUnidadesdeMedida']

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    UnidadesMedida.objects.create(descripcion=descripcion, estado=estado)
    sweetify.success(request, 'Unidad Medida Agregada Correctamente!!!')

    return redirect('/principalUnidadesdeMedida')


def eliminarDepartamento(request, iddepartamento):
    departamentos = Departamentos.objects.get(iddepartamento=iddepartamento)
    departamentos.delete()
    sweetify.success(request, 'Departamento Eliminado Correctamente!!!')
    return redirect('/lista_departametos')


def eliminarEmpleado(request, idempleado):
    empleado = Empleados.objects.get(idempleado=idempleado)
    empleado.delete()
    sweetify.success(request, 'Empleado Eliminado Correctamente!!!')
    return redirect('/principalEmpleados')


def edicionEmpleados(request, idempleado):
    empleado = Empleados.objects.get(idempleado=idempleado)
    departamento = Departamentos.objects.all()
    return render(request, 'edicionEmpleado.html', {'empleado': empleado,
                                                    'departamentos': departamento})


def edicionDepartamento(request, iddepartamento):
    departamento = Departamentos.objects.get(iddepartamento=iddepartamento)
    return render(request, 'edicionDepartamento.html', {'departamento': departamento})


def editarDepartamento(request):
    iddepartamento = request.POST['txtIdDepartamento']
    nombre = request.POST['txtNombreDepartamento']
    estado = request.POST['txtEstadoDepartamento']

    departamento = Departamentos.objects.get(iddepartamento=iddepartamento)
    departamento.nombre = nombre
    departamento.estado = estado
    departamento.save()

    return redirect('/principalDepartamentos')


def registrarProveedor(request):
    cedularnc = request.POST['txtcedulaProveedor']
    nombrecomercial = request.POST['txtNombreComercialProveedor']
    estado = request.POST['txtEstadoProveedor']

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Proveedores.objects.create(
        nombrecomercial=nombrecomercial, cedularnc=cedularnc, estado=estado)
    sweetify.success(request, 'Marca Agregada Correctamente!!!')

    return redirect('/principalProveedores')


def eliminarMarcas(request, idmarca):
    print(request.POST['content'])
    print(request.POST['nombre'])

    print(idmarca)

    marca = Marcas.objects.get(idmarca=idmarca)
    marca.delete()
    sweetify.success(request, 'Marca Eliminada Correctamente!!!')
    return redirect('/principalMarcas')


def eliminarUnidades(request, idunidadmedida):
    unidad = UnidadesMedida.objects.get(idunidadmedida=idunidadmedida)
    unidad.delete()
    sweetify.success(request, 'Unidades Eliminada Correctamente!!!')
    return redirect('/principalUnidadesdeMedida')


def eliminarProveedor(request, idproveedor):
    proveedor = Proveedores.objects.get(idproveedor=idproveedor)
    proveedor.delete()
    sweetify.success(request, 'Proveedor Eliminada Correctamente!!!')
    return redirect('/principalProveedores')


def eliminarArticulo(request, idarticulo):
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
    idempleado = request.POST['txtEmpleadoId']
    nombre = request.POST['txtEmpleadoNombre']
    cedula = request.POST['txtEmpleadoCedula']
    iddepartamento = request.POST['txtDepartamentoId']
    estado =  request.POST['txtEmpleadoEstado']

    if estado:
        estado = 1
    else:
        estado = 0

    #Intance of Department Empleado
    intance_Departamento = Departamentos.objects.get(iddepartamento=iddepartamento)


    empledo = Empleados.objects.get(idempleado=idempleado)
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
    proveedor.estado = estado
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
    unidad.estado = estado
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


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': "Username already exists"
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': "Password do not match"
        })


def signout(request):
    logout(request)
    return redirect('index1')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })

        else:
            login(request, user)
            return redirect('/')


def index1(request):
    return render(request, 'index1.html')


# lista paginada en Python
def lista_departametos(request):

    query = request.GET.get('q', '')
    lista_departametos = Departamentos.objects.all()


    if query != '':
        lista_departametos = lista_departametos.filter(nombre=query) 
        query = ''


    paginator = Paginator(lista_departametos, 5) 

    page_number = request.GET.get('page')

    try:
        lista_departametos = paginator.page(page_number)

    except PageNotAnInteger:
        lista_departametos = paginator.page(1)

    except EmptyPage:
        lista_departametos = paginator.page(paginator.num_pages)

    return render(request, 'lista_departametos.html', {
        'page_obj': lista_departametos,
        'query': query
    })


# Reportes

def generateReportDepartment(request):
    # Obtén todos los departamentos
    departamentos = Departamentos.objects.all()

    # Preparar los datos para la tabla
    data = []
    # Encabezado de la tabla
    data.append(['ID Departamento', 'Nombre', 'Estado'])

    for dep in departamentos:
        # Definir el estado de forma legible (Activo/Inactivo)
        if dep.estado == "1":
            estado = "Activo"

        else:
            estado = "Inactivo"

        # Añadir la fila con los datos del departamento
        data.append([dep.iddepartamento, dep.nombre, estado])

    # Crear un buffer en memoria para almacenar el PDF
    buffer = io.BytesIO()

    # Crear el documento PDF
    document = SimpleDocTemplate(buffer, pagesize=letter)

    # Crear el estilo para el título
    styles = getSampleStyleSheet()
    # Usamos un estilo predefinido para el título
    title_style = styles['Title']

    # Crear el título como un párrafo (esto nos permite formatearlo fácilmente)
    title = Paragraph("Reporte de Departamentos", title_style)

    # Crear la tabla
    table = Table(data)

    # Estilo de la tabla
    style = TableStyle([
        # Fondo gris para el encabezado
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        # Texto blanco para el encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        # Centrar texto en todas las celdas
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        # Usar Helvetica en negrita para el encabezado
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        # Usar Helvetica normal para el cuerpo
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        # Espaciado debajo del encabezado
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Rejilla de la tabla
    ])

    # Asignar el estilo a la tabla
    table.setStyle(style)

    # Elementos del documento (agregar el título y la tabla)
    elements = [title, table]

    # Construir el PDF en el buffer
    document.build(elements)

    # Hacer que el cursor del buffer esté al principio
    buffer.seek(0)

    # Devolver la respuesta con el PDF como un archivo adjunto
    return FileResponse(buffer, as_attachment=True, filename="reporteDepartamentos.pdf")





def generateReportEmpleados(request):

    empleados = Empleados.objects.all()

    # Preparar los datos para la tabla
    data = []
    # Encabezado de la tabla
    data.append(['ID Empleados', 'Cedula', 'Nombre','Departamento', 'Estado'])

    for dep in empleados:
        # Definir el estado de forma legible (Activo/Inactivo)
        if dep.estado == "1":
            estado = "Activo"

        else:
            estado = "Inactivo"

        # Añadir la fila con los datos del departamento
        data.append([dep.idempleado, dep.cedula, dep.nombre,dep.departamento.nombre, estado])

    # Crear un buffer en memoria para almacenar el PDF
    buffer = io.BytesIO()

    # Crear el documento PDF
    document = SimpleDocTemplate(buffer, pagesize=letter)

    # Crear el estilo para el título
    styles = getSampleStyleSheet()
    # Usamos un estilo predefinido para el título
    title_style = styles['Title']

    # Crear el título como un párrafo (esto nos permite formatearlo fácilmente)
    title = Paragraph("Reporte de Empleados", title_style)

    # Crear la tabla
    table = Table(data)

    # Estilo de la tabla
    style = TableStyle([
        # Fondo gris para el encabezado
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        # Texto blanco para el encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        # Centrar texto en todas las celdas
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        # Usar Helvetica en negrita para el encabezado
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        # Usar Helvetica normal para el cuerpo
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        # Espaciado debajo del encabezado
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Rejilla de la tabla
    ])

    # Asignar el estilo a la tabla
    table.setStyle(style)

    # Elementos del documento (agregar el título y la tabla)
    elements = [title, table]

    # Construir el PDF en el buffer
    document.build(elements)

    # Hacer que el cursor del buffer esté al principio
    buffer.seek(0)

    # Devolver la respuesta con el PDF como un archivo adjunto
    return FileResponse(buffer, as_attachment=True, filename="reporteEmpleados.pdf")




# def principalDepartamentos(request):
#     departamentos = Departamentos.objects.all()
#     page = request.Get.get('page', 1)

#     try:
#         paginator = Paginator(departamentos, 3)
#         departamentos = paginator.page(page)

#     except:
#         raise Http404


#     return render(request, 'principalDepartamentos.html',{
#         'departamentos':departamentos
#     })
