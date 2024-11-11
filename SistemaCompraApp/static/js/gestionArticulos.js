function getArticleAddForm() {
  $("#builtArticleAdd").modal("show");
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


function saveArticleNewDos() {
   
   const element = document.getElementById("myButtonAddingArticle");
   let descripcion = document.getElementById("txtDescripcionArticulos").value;
   let unidadMedida = document.getElementById("txtUnidadMedidaArticulos").value;
   let marca = document.getElementById("txtMarcaArticulos").value;
   let existencia = document.getElementById("txtExistenciaArticulos").value;
   let estado = document.getElementById("txtEstadoArticulo").checked == true ? "1" : "0";
   const csrftoken = getCookie("csrftoken");


    let validate = ValidateArticle(descripcion,unidadMedida,marca,existencia,estado,0);

  alert("Probando nuevamente");

}

function saveRecordArticle() {
  const element = document.getElementById("myButtonAddingArticle");
  let descripcion = document.getElementById("txtDescripcionArticulos").value;
  let unidadMedida = document.getElementById("txtUnidadMedidaArticulos").value;
  let marca = document.getElementById("txtMarcaArticulos").value;
  let existencia = document.getElementById("txtExistenciaArticulos").value;
  let estado = document.getElementById("txtEstadoArticulo").checked == true ? "1" : "0";
  const csrftoken = getCookie("csrftoken");

  let validate = ValidateArticle(descripcion,unidadMedida,marca,existencia,estado,0);

  if (validate) {
    element.setAttribute("data-dismiss", "modal");
    $.ajax({
      type: "POST",
      url: "/registrarArticulo/",
      data: {
        txtDescripcionArticulos: descripcion,
        txtUnidadMedidaArticulos: unidadMedida,
        txtExistenciaArticulos: existencia,
        txtMarcaArticulos: marca,
        txtEstadoArticulo: estado,
        csrfmiddlewaretoken: csrftoken,
      },
      beforeSend: function () {
        $("#loader").fadeIn();
      },
      success: function (data) {
        document.getElementById("txtDescripcionArticulos").value = "";
        document.getElementById("txtUnidadMedidaArticulos").value ="";
        document.getElementById("txtMarcaArticulos").value = "";
        document.getElementById("txtExistenciaArticulos").value= "";
        document.getElementById("txtEstadoArticulo").checked = false
        setTimeout(function () {
          $("#loader").fadeOut();
  
          Swal.fire({
            position: "center",
            icon: "success",
            title: "Articulo Agregado correctamente...",
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

function ValidateArticle(descripcion,unidadMedida,marca,existencia,estado,type) 
{

  if (type == 0) {

    if (descripcion == "" || descripcion == "undefined" || descripcion == null) 
    {
        Swal.fire({
          icon: "warning",
          title: "Oops...",
          text: "Favor de colocar la descripcion",
        });
  
      return false;
    }

    if (Math.sign(existencia) == -1 || existencia == 0) {
      Swal.fire({
        icon: "warning",
        title: "Oops...",
        text: "Favor de colocar cantidad valida, no se acepta 0 ni valor negativo...",
      });

      return false;
    }

    if (
      unidadMedida == "" ||
      unidadMedida == "undefined" ||
      unidadMedida == null
    ) {
      Swal.fire({
        icon: "warning",
        title: "Oops...",
        text: "Favor de colocar la Unidad De Medida",
      });

      return false;
    }

    if (marca == "" || marca == "undefined" || marca == null) {
      Swal.fire({
        icon: "warning",
        title: "Oops...",
        text: "Favor de colocar la marca",
      });

      return false;
    }

    if (estado == "" || estado == "undefined" || estado == null) {
      Swal.fire({
        icon: "warning",
        title: "Oops...",
        text: "Favor de colocar el estado",
      });

      return false;
    }
  } 
  else 
  {
    if (Math.sign(existencia) == -1 || existencia == 0) 
      {
         Swal.fire({
           icon: "warning",
           title: "Oops...",
           text: "Favor de colocar cantidad valida, no se acepta 0 ni valor negativo...",
         });

      return false;
    }
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
