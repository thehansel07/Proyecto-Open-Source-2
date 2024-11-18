from django.shortcuts import render, redirect
from .models import Departamentos, Empleados, Marcas, UnidadesMedida, Proveedores, Articulos, Ordencompra
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
from datetime import datetime


# Create your views here.


def index(request):
    return render(request, 'index.html')


def principalDepartamentos(request):
    query = request.GET.get('q', '')
    lista_departametos = Departamentos.objects.all()


    if query != '':
        lista_departametos = lista_departametos.filter(nombre__icontains=query) 
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


def principalOrdenCompra(request):
    query = request.GET.get('q', '')


    if(query != ''):
            query_date = datetime.strptime(query, "%Y-%m-%d").date()


    lista_OrdenCompra = Ordencompra.objects.all()
    listado_articulos = Articulos.objects.all()
    listado_marcas = Marcas.objects.all()
    listado_unidad_medida= UnidadesMedida.objects.all()


    if query != '':
        lista_OrdenCompra = list(filter(lambda x: x.fecha <= query_date, lista_OrdenCompra))
        query = ''

    paginator = Paginator(lista_OrdenCompra, 5) 

    page_number = request.GET.get('page')

    try:
        lista_OrdenCompra = paginator.page(page_number)

    except PageNotAnInteger:
        lista_OrdenCompra = paginator.page(1)

    except EmptyPage:
        lista_OrdenCompra = paginator.page(paginator.num_pages)

    return render(request, 'principalOrdenCompra.html', {
        'page_obj': lista_OrdenCompra,
        'query': query,
        'listado_articulos': listado_articulos,
        'listado_marcas': listado_marcas,
        'listado_unidad_medida': listado_unidad_medida
    })




def principalEmpleados(request):
    query = request.GET.get('q', '')
    lista_empleados = Empleados.objects.all()
    lista_departametos = Departamentos.objects.all()


    if query != '':
        lista_empleados = lista_empleados.filter(nombre__icontains=query) 
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
    query = request.GET.get('q', '')
    lista_marcas = Marcas.objects.all()


    if query != '':
        lista_marcas = lista_marcas.filter(descripcion__icontains=query) 
        query = ''

    paginator = Paginator(lista_marcas, 5) 

    page_number = request.GET.get('page')

    try:
        lista_marcas = paginator.page(page_number)

    except PageNotAnInteger:
        lista_marcas = paginator.page(1)

    except EmptyPage:
        lista_marcas = paginator.page(paginator.num_pages)

    return render(request, 'principalMarcas.html', {
        'page_obj': lista_marcas,
        'query': query,
    })

def principalUnidadesdeMedida(request):
    query = request.GET.get('q', '')
    lista_unidades_medidas = UnidadesMedida.objects.all()

    if query != '':
        lista_unidades_medidas = lista_unidades_medidas.filter(descripcion__icontains=query) 
        query = ''

    paginator = Paginator(lista_unidades_medidas, 5) 

    page_number = request.GET.get('page')

    try:
        lista_unidades_medidas = paginator.page(page_number)

    except PageNotAnInteger:
        lista_unidades_medidas = paginator.page(1)

    except EmptyPage:
        lista_unidades_medidas = paginator.page(paginator.num_pages)

    return render(request, 'principalUnidadesdeMedida.html', {
        'page_obj': lista_unidades_medidas,
        'query': query,
    })


def principalProveedores(request):
    query = request.GET.get('q', '')
    lista_proveedores = Proveedores.objects.all()

    if query != '':
        lista_proveedores = lista_proveedores.filter(nombrecomercial__icontains=query) 
        query = ''

    paginator = Paginator(lista_proveedores, 5) 

    page_number = request.GET.get('page')

    try:
        lista_proveedores = paginator.page(page_number)

    except PageNotAnInteger:
        lista_proveedores = paginator.page(1)

    except EmptyPage:
        lista_proveedores = paginator.page(paginator.num_pages)

    return render(request, 'principalProveedores.html', {
        'page_obj': lista_proveedores,
        'query': query,
    })


def principalArticulos(request):
    query = request.GET.get('q', '')
    listado_articulos = Articulos.objects.all()
    listado_marcas = Marcas.objects.all()
    listado_unidad_medida = UnidadesMedida.objects.all()

    if query != '':
        listado_articulos = listado_articulos.filter(descripcion__icontains=query) 
        query = ''

    paginator = Paginator(listado_articulos, 5) 

    page_number = request.GET.get('page')

    try:
        listado_articulos = paginator.page(page_number)

    except PageNotAnInteger:
        listado_articulos = paginator.page(1)

    except EmptyPage:
        listado_articulos = paginator.page(paginator.num_pages)

    return render(request, 'principalArticulos.html', {
        'page_obj': listado_articulos,
        'listado_marcas': listado_marcas,
        'listado_unidad_medida': listado_unidad_medida,
        'query': query,
    })
    


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
    estado = request.POST['txtEstadoArticulo']

    instance_marca = Marcas.objects.get(idmarca=idmarca)
    instance_unidadMedida = UnidadesMedida.objects.get(idunidadmedida=id_unidadmedida)

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


    Articulos.objects.create(descripcion=descripcion,
                             marca=instance_marca,
                             unidadmedida=instance_unidadMedida,
                             existencia=existencia,
                             estado=estado)

    return redirect('/principalArticulos')


def registrarMarcas(request):
    descripcion = request.POST['txtdescripcionMarca']
    estado = request.POST['txtEstadoMarca']

    Marcas.objects.create(descripcion=descripcion, estado=estado)

    return redirect('/principalMarcas')


def registrarEmpleado(request):
    cedula = request.POST['txtEmpleadoCedula']
    nombre = request.POST['txtEmpleadoNombre']
    estado = request.POST['txtEmpleadoEstado']
    iddepartamento = request.POST['txtDepartamentoId']

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
    UnidadesMedida.objects.create(descripcion=descripcion,estado=estado)
    sweetify.success(request, 'Unidad Medida Agregada Correctamente!!!')

    return redirect('/principalUnidadesdeMedida')



def registrarOrdenCompra(request):
    fecha = request.POST['txtOrdenFecha']
    idArticulo = request.POST['txtOrdenArticuloId']
    cantidad = request.POST['txtOrdenCantidad']
    idUnidadMedida = request.POST['txtOrdenUnidadMedida']
    costoUnitario = request.POST['txtOrdenCostoUnitario']
    idMarca = request.POST['txtOrdenMarcaId']
    estado = request.POST['txtOrdenEstado']

    instance_marca = Marcas.objects.get(idmarca=idMarca)
    instance_unidad_medida = UnidadesMedida.objects.get(idunidadmedida=idUnidadMedida)
    instance_articulo = Articulos.objects.get(idarticulo=idArticulo)



    Ordencompra.objects.create(fecha=fecha,
                              idarticulo = instance_articulo,
                              cantidad = cantidad,
                              idunidadmedida= instance_unidad_medida,
                              idmarca = instance_marca,
                              costounitario = costoUnitario,
                              estado=estado)
    

    existencia = int(instance_articulo.existencia) + int(cantidad)
    instance_articulo.existencia = existencia
    instance_articulo.save()

    return redirect('/principalOrdenCompra')


def eliminarDepartamento(request, iddepartamento):
    departamentos = Departamentos.objects.get(iddepartamento=iddepartamento)
    departamentos.delete()
    sweetify.success(request, 'Departamento Eliminado Correctamente!!!')
    return redirect('/lista_departametos')


def eliminarOrdenCompra(request, idordencompra):
    departamentos = Ordencompra.objects.get(idordencompra=idordencompra)
    departamentos.delete()
    sweetify.success(request, 'Orden De Compra Eliminada Correctamente!!!')
    return redirect('/principalOrdenCompra')



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

    Proveedores.objects.create(nombrecomercial=nombrecomercial, cedularnc=cedularnc, estado=estado)

    return redirect('/principalProveedores')


def eliminarMarcas(request, idmarca):
    marca = Marcas.objects.get(idmarca=idmarca)
    marca.delete()
    return redirect('/principalMarcas')


def eliminarUnidades(request, idunidadmedida):
    unidad = UnidadesMedida.objects.get(idunidadmedida=idunidadmedida)
    unidad.delete()
    sweetify.success(request, 'Unidades Eliminada Correctamente!!!')
    return redirect('/principalUnidadesdeMedida')


def eliminarProveedor(request, idproveedor):
    proveedor = Proveedores.objects.get(idproveedor=idproveedor)
    proveedor.delete()
    return redirect('/principalProveedores')


def eliminarArticulo(request, idarticulo):
    articulo = Articulos.objects.get(idarticulo=idarticulo)
    articulo.delete()
    return redirect('/principalArticulos')


def editarMarcas(request):
    idmarca = request.POST['txtIdmarca']
    descripcion = request.POST['txtdescripcionMarca']
    estado = request.POST['txtEstadoMarcas']

    marcas = Marcas.objects.get(idmarca=idmarca)
    marcas.descripcion = descripcion
    marcas.estado = estado
    marcas.save()

    return redirect('/principalMarcas')


def editarEmpleado(request):
    idempleado = request.POST['txtEmpleadoId']
    nombre = request.POST['txtEmpleadoNombre']
    cedula = request.POST['txtEmpleadoCedula']
    iddepartamento = request.POST['txtDepartamentoId']
    estado =  request.POST['txtEmpleadoEstado']

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
    estado = request.POST['txtEstadoProveedor']

    proveedor = Proveedores.objects.get(idproveedor=idproveedor)
    proveedor.cedularnc = cedularnc
    proveedor.nombrecomercial = nombrecomercial
    proveedor.estado = estado
    proveedor.save()

    return redirect('/principalProveedores')


def editarUnidades(request):
    idunidadmedida = request.POST['txtIdunidad']
    descripcion = request.POST['txtdescripcionUnidadesdeMedida']
    estado= request.POST['txtEstadoUnidadesdeMedida']

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
                return redirect('/index')
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
            return redirect('/index')


def index1(request):
    return render(request, 'index1.html')


# lista paginada en Python
def lista_departametos(request):

    query = request.GET.get('q', '')
    lista_departametos = Departamentos.objects.all()


    if query != '':
        lista_departametos = list(filter(lambda d: query.lower() in d['nombre'].lower(), lista_departametos))
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





def generateReportBrand(request):
    # Obtén todos los departamentos
    marcas = Marcas.objects.all()

    # Preparar los datos para la tabla
    data = []
    # Encabezado de la tabla
    data.append(['ID Marca', 'Nombre', 'Estado'])

    for mar in marcas:
        # Definir el estado de forma legible (Activo/Inactivo)
        if mar.estado == "1":
            estado = "Activo"

        else:
            estado = "Inactivo"

        # Añadir la fila con los datos del departamento
        data.append([mar.idmarca, mar.descripcion, estado])

    # Crear un buffer en memoria para almacenar el PDF
    buffer = io.BytesIO()

    # Crear el documento PDF
    document = SimpleDocTemplate(buffer, pagesize=letter)

    # Crear el estilo para el título
    styles = getSampleStyleSheet()
    # Usamos un estilo predefinido para el título
    title_style = styles['Title']

    # Crear el título como un párrafo (esto nos permite formatearlo fácilmente)
    title = Paragraph("Reporte de Marcas", title_style)

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
    return FileResponse(buffer, as_attachment=True, filename="reporteMarcas.pdf")


def generateReportMeasurement(request):
    # Obtén todos los departamentos
    unidades = UnidadesMedida.objects.all()

    # Preparar los datos para la tabla
    data = []
    # Encabezado de la tabla
    data.append(['ID Marca', 'Nombre', 'Estado'])

    for unidad in unidades:
        # Definir el estado de forma legible (Activo/Inactivo)
        if unidad.estado == "1":
            estado = "Activo"

        else:
            estado = "Inactivo"

        # Añadir la fila con los datos del departamento
        data.append([unidad.idunidadmedida, unidad.descripcion, estado])

    # Crear un buffer en memoria para almacenar el PDF
    buffer = io.BytesIO()

    # Crear el documento PDF
    document = SimpleDocTemplate(buffer, pagesize=letter)

    # Crear el estilo para el título
    styles = getSampleStyleSheet()
    # Usamos un estilo predefinido para el título
    title_style = styles['Title']

    # Crear el título como un párrafo (esto nos permite formatearlo fácilmente)
    title = Paragraph("Reporte de Unidades de Medidas", title_style)

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
    return FileResponse(buffer, as_attachment=True, filename="reporteUnidadMedida.pdf")





def generateReportProvider(request):
    # Obtén todos los departamentos
    proveedores = Proveedores.objects.all()

    # Preparar los datos para la tabla
    data = []
    # Encabezado de la tabla
    data.append(['ID Provedor', 'Cedula/RNC', 'Nombre Comercial', 'Estado'])

    for unidad in proveedores:
        # Definir el estado de forma legible (Activo/Inactivo)
        if unidad.estado == "1":
            estado = "Activo"

        else:
            estado = "Inactivo"

        # Añadir la fila con los datos del departamento
        data.append([unidad.idproveedor, unidad.cedularnc,unidad.nombrecomercial, estado])

    # Crear un buffer en memoria para almacenar el PDF
    buffer = io.BytesIO()

    # Crear el documento PDF
    document = SimpleDocTemplate(buffer, pagesize=letter)

    # Crear el estilo para el título
    styles = getSampleStyleSheet()
    # Usamos un estilo predefinido para el título
    title_style = styles['Title']

    # Crear el título como un párrafo (esto nos permite formatearlo fácilmente)
    title = Paragraph("Reporte de Unidades De Proveedores", title_style)

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
    return FileResponse(buffer, as_attachment=True, filename="reporteProveedor.pdf")





def generateReportArticle(request):
    # Obtén todos los departamentos
    articulos = Articulos.objects.all()

    # Preparar los datos para la tabla
    data = []
    # Encabezado de la tabla
    data.append(['ID Articulo', 'Descripcion', 'Marca', 'Unidad Medida', 'existencia', 'estado'])

    for unidad in articulos:
        # Definir el estado de forma legible (Activo/Inactivo)
        if unidad.estado == "1":
            estado = "Activo"

        else:
            estado = "Inactivo"

        # Añadir la fila con los datos del departamento
        data.append([unidad.idarticulo, unidad.descripcion,unidad.marca.descripcion,unidad.unidadmedida.descripcion,unidad.existencia, estado])

    # Crear un buffer en memoria para almacenar el PDF
    buffer = io.BytesIO()

    # Crear el documento PDF
    document = SimpleDocTemplate(buffer, pagesize=letter)

    # Crear el estilo para el título
    styles = getSampleStyleSheet()
    # Usamos un estilo predefinido para el título
    title_style = styles['Title']

    # Crear el título como un párrafo (esto nos permite formatearlo fácilmente)
    title = Paragraph("Reporte De Articulos", title_style)

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
    return FileResponse(buffer, as_attachment=True, filename="reporteArticulo.pdf")



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
