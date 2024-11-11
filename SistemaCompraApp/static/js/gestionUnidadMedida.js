function getAddMeasurementForm() {
    $("#builtMeasurementAdd").modal("show");
  }
  
  function getMeasurementUpdate(id, descripcion, estado) {
    $("#builtMeasurementUpdate").modal("show");
    document.getElementById("txtIdunidadUpdate").value = id;
    document.getElementById("txtdescripcionUnidadesdeMedidaUpdate").value = descripcion;
    document.getElementById("txtEstadoUnidadesdeMedidaUpdate").checked = estado == "1" ? true : false;
  }
  
  function updateMeasurement() {
    const element = document.getElementById("myButtonUpdateMesurement");
    let id = document.getElementById("txtIdunidadUpdate").value;
    let descripcion = document.getElementById("txtdescripcionUnidadesdeMedidaUpdate").value;
    let estado =document.getElementById("txtEstadoUnidadesdeMedidaUpdate").checked == true ? 1: 0;
    const csrftoken = getCookie("csrftoken");
  
    element.setAttribute("data-dismiss", "modal");
    $.ajax({
      type: "POST",
      url: "/editarUnidades/",
      data: {
        txtIdunidad: id,
        txtdescripcionUnidadesdeMedida: descripcion,
        txtEstadoUnidadesdeMedida: estado,
        csrfmiddlewaretoken: csrftoken,
      },
      beforeSend: function () {
        $("#loader").fadeIn();
      },
      success: function (data) {
        document.getElementById("txtdescripcionUnidadesdeMedidaUpdate").value = "";
        document.getElementById("txtEstadoUnidadesdeMedidaUpdate").checked = false;
        setTimeout(function () {
          $("#loader").fadeOut();
  
          Swal.fire({
            position: "center",
            icon: "success",
            title: "Departamento Actualizando correctamente...",
            showConfirmButton: false,
          });
  
          setTimeout(function () {
            location.reload();
          }, 3000);
        }, 3000);
      },
      error: function (xhr, status, error) {
        // Manejo de error si la solicitud fall
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "Ocurrió un error. Inténtalo nuevamente.",
        });
        $("#loader").fadeOut();
      },
    });
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
  
  function saveMeasurementRecord() {
    const element = document.getElementById("myButtonMeasurement");
    var descripcion = document.getElementById("txtdescripcionUnidadesdeMedida").value;
    var estado = document.getElementById("txtEstadoUnidadesdeMedida").checked == true ? 1 : 0;
    const csrftoken = getCookie("csrftoken");
  
    let validate = ValidateMeasurement(descripcion, estado);
  
    if (validate) {
      element.setAttribute("data-dismiss", "modal");
      $.ajax({
        type: "POST",
        url: "/registrarUnidadesdeMedida/",
        data: {
          txtdescripcionUnidadesdeMedida: descripcion,
          txtEstadoUnidadesdeMedida: estado,
          csrfmiddlewaretoken: csrftoken,
        },
        beforeSend: function () {
          $("#loader").fadeIn();
        },
        success: function (data) {
            document.getElementById("txtdescripcionUnidadesdeMedida").value = "";
            document.getElementById("txtEstadoUnidadesdeMedida").checked = false;
          setTimeout(function () {
            $("#loader").fadeOut();
    
            Swal.fire({
              position: "center",
              icon: "success",
              title: "Unidad de Medida Agregada correctamente...",
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
  
  function ValidateMeasurement(descripcion, estado) {
    if (descripcion == "" || descripcion == "undefined" || descripcion == null) {
      Swal.fire({
        icon: "warning",
        title: "Oops...",
        text: "Favor de colocar el nombre",
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
  