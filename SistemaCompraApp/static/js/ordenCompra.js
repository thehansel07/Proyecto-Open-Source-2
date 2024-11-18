function getArticleAddForm() {
    $("#builtOrderAdd").modal("show");
  }
  
  function getArticleUpdateForm(id, descripcion, marca, unidadMedida,existencia, estado) {
    $("#builtUpdateArticle").modal("show");
    document.getElementById("txtIdArticulosUpdate").value = id;
    document.getElementById("txtDescripcionArticulosUpdate").value = descripcion;
    document.getElementById("txtMarcaArticulosUpdate").value = marca;
    document.getElementById("txtUnidadMedidaArticulosUpdate").value = unidadMedida;
    document.getElementById("txtExistenciaArticulosUpdate").value = existencia;
    document.getElementById("txtEstadoArticuloUpdate").checked = estado == "1" ? true : false;
  }
  
  function updateArticle() {
    const element = document.getElementById("myButtonUpdateArticle");
    var id = document.getElementById("txtIdArticulosUpdate").value
    var descripcion = document.getElementById("txtDescripcionArticulosUpdate").value;
    var marca = document.getElementById("txtMarcaArticulosUpdate").value;
    var unidadMedida = document.getElementById("txtUnidadMedidaArticulosUpdate").value;
    var existencia = document.getElementById("txtExistenciaArticulosUpdate").value;
    var estado = document.getElementById("txtEstadoArticuloUpdate").checked == true ? "1" : "0";;
    const csrftoken = getCookie("csrftoken");
  
    let validate = ValidateArticle(descripcion, unidadMedida, marca, existencia, estado, 1);
  
    if (validate) {
      element.setAttribute("data-dismiss", "modal");
      $.ajax({
        type: "POST",
        url: "/editarArticulos/",
        data: {
          txtIdArticulos: id,
          txtDescripcionArticulos: descripcion,
          txtMarcaArticulos: marca,
          txtUnidadMedidaArticulos: unidadMedida,
          txtExistenciaArticulos: existencia,
          txtEstadoArticulo: estado,
          csrfmiddlewaretoken: csrftoken,
        },
        beforeSend: function () {
          $("#loader").fadeIn();
        },
        success: function (data) {
           document.getElementById("txtIdArticulosUpdate").value = "";
           document.getElementById("txtDescripcionArticulosUpdate").value = "";
           document.getElementById("txtMarcaArticulosUpdate").value = "";
           document.getElementById("txtUnidadMedidaArticulosUpdate").value = "";
           document.getElementById("txtExistenciaArticulosUpdate").value = 0;
           document.getElementById("txtEstadoArticuloUpdate").checked = false;
          setTimeout(function () {
            $("#loader").fadeOut();
  
            Swal.fire({
              position: "center",
              icon: "success",
              title: "Articulo Actualizado correctamente...",
              showConfirmButton: false,
            });
  
            setTimeout(function () {
              location.reload();
            }, 3000);
          }, 3000);
        },
        error: function (xhr, status, error) {
          // Manejo de error si la solicitud falla
          Swal.fire({
            icon: "error",
            title: "Error",
            text: "Ocurrió un error. Inténtalo nuevamente.",
          });
  
          $("#loader").fadeOut();
        },
      });
    }
  }
  
  
  
  
  
  function printReport() {
    const csrftoken = getCookie("csrftoken");
    $.ajax({
      type: "POST",
      url: "/generateReport",
      data: {
        csrfmiddlewaretoken: csrftoken,
      },
      beforeSend: function () {
        $("#loader").fadeIn();
      },
      success: function (data) {
        setTimeout(function () {
          const decodedBytes = base85.decode(data); // Decodifica la cadena Base85 a bytes binarios
          var blob = new Blob([decodedBytes], { type: "application/pdf" });
          var pdfurl = window.URL.createObjectURL(blob);
          $("#pdfviewer").attr("data", pdfurl);
          $("#loader").fadeOut();
        }, 3000);
      },
      error: function (xhr, status, error) {
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "Ocurrió un error. Inténtalo nuevamente.",
        });
        $("#loader").fadeOut();
      },
    });
  }
  

  function saveRecordOrder() {
    const element = document.getElementById("myButtonAddingOrder");
    let fecha = document.getElementById("txtOrdenFecha").value;
    let idArticulo = document.getElementById("txtOrdenArticuloId").value;
    let cantidad = document.getElementById("txtOrdenCantidad").value;
    let idUnidadMedida = document.getElementById("txtOrdenUnidadMedida").value;
    let costoUnitario = document.getElementById("txtOrdenCostoUnitario").value;
    let idMarca = document.getElementById("txtOrdenMarcaId").value;
    let estado = document.getElementById("txtOrdenEstado").checked == true ? "1" : "0";
    const csrftoken = getCookie("csrftoken");
  
    let validate = ValidateOrder(fecha,idArticulo,cantidad,idUnidadMedida,costoUnitario,idMarca,estado,0);
  
    if (validate) {
      element.setAttribute("data-dismiss", "modal");
      $.ajax({
        type: "POST",
        url: "/registrarOrdenCompra/",
        data: {
          txtOrdenFecha: fecha,
          txtOrdenArticuloId: idArticulo,
          txtOrdenCantidad: cantidad,
          txtOrdenUnidadMedida: idUnidadMedida,
          txtOrdenCostoUnitario: costoUnitario,
          txtOrdenMarcaId:idMarca,
          txtOrdenEstado: estado,
          csrfmiddlewaretoken: csrftoken,
        },
        beforeSend: function () {
          $("#loader").fadeIn();
        },
        success: function (data) {
            document.getElementById("txtOrdenFecha").value = "";
            document.getElementById("txtOrdenArticuloId").value = "";
            document.getElementById("txtOrdenCantidad").value = "";
            document.getElementById("txtOrdenUnidadMedida").value = "";
            document.getElementById("txtOrdenCostoUnitario").value = "";
            document.getElementById("txtOrdenMarcaId").value = "";
            document.getElementById("txtOrdenEstado").checked = false;
          setTimeout(function () {
            $("#loader").fadeOut();
    
            Swal.fire({
              position: "center",
              icon: "success",
              title: "Orden de Compra Creada Correctamente...",
              showConfirmButton: false,
            });
    
            setTimeout(function () {
              location.reload();
            }, 3000);
          }, 3000);
        },
        error: function (xhr, status, error) {
          // Manejo de error si la solicitud falla
          Swal.fire({
            icon: "error",
            title: "Error",
            text: "Ocurrió un error. Inténtalo nuevamente.",
          });
  
          $("#loader").fadeOut();
        },
      });
    }
  }
  
  function ValidateOrder(fecha, idArticulo, cantidad, idUnidadMedida, idMarca, costoUnitario, estado, type) 
  {

    if(fecha == "" || fecha == null || fecha == "undefined")
    {
        Swal.fire({
            icon: "warning",
            title: "Oops...",
            text: "Favor de colocar la fecha",
          });

        return false;

    }


    if(idArticulo == "" || idArticulo == null || idArticulo == "undefined")
         {
            Swal.fire({
                icon: "warning",
                title: "Oops...",
                text: "Favor de colocar el articulo",
              });
    
            return false;
    
        }



        if(cantidad == "" || cantidad == null || cantidad == "undefined")
            {
               Swal.fire({
                   icon: "warning",
                   title: "Oops...",
                   text: "Favor de colocar la cantidad",
                 });
       
               return false;
       
           }


           if(idUnidadMedida == "" || idUnidadMedida == null || idUnidadMedida == "undefined")
            {
               Swal.fire({
                   icon: "warning",
                   title: "Oops...",
                   text: "Favor de colocar la unidad de medida",
                 });
       
               return false;
       
           }
  

           if(idMarca == "" || idMarca == null || idMarca == "undefined")
            {
               Swal.fire({
                   icon: "warning",
                   title: "Oops...",
                   text: "Favor de colocar la marca",
                 });
       
               return false;
       
           }


           
           if(costoUnitario == "" || costoUnitario == null || costoUnitario == "undefined")
            {
               Swal.fire({
                   icon: "warning",
                   title: "Oops...",
                   text: "Favor de colocar el costo unitario",
                 });
       
               return false;
       
           }


           if(estado == "" || estado == null || estado == "undefined")
            {
               Swal.fire({
                   icon: "warning",
                   title: "Oops...",
                   text: "Favor de colocar el estado",
                 });
       
               return false;
       
           }
           
    return true;
  }
  
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  