(function (){

    const btnEliminacion = document.querySelectorAll('.btnEliminacion');
       btnEliminacion.forEach(btn=>{
          btn.addEventListener('click', (e)=>{
          const confirmacion = confirm('Estas seguro que desea eliminar este registro?');
        if (!confirmacion){
            e.preventDefault();
        }
    });
});
})();







function getAddBrandForm() {
    $("#builtBrandAdd").modal("show");
  }
  
  function getBrandUpdate(id, descripcion, estado) 
  {
    $("#builtBrandUpdate").modal("show");
    document.getElementById("txtIdMarcaUpdate").value = id;
    document.getElementById("txtdescripcionMarcaUpdate").value = descripcion;
    document.getElementById("txtEstadoMarcaUpdate").checked = estado == "1" ? true : false;
  }
  
  function updateBrand() {
    const element = document.getElementById("myButtonUpdateBrand");
    let id = document.getElementById("txtIdMarcaUpdate").value;
    let descripcion = document.getElementById("txtdescripcionMarcaUpdate").value;
    let estado = document.getElementById("txtEstadoMarcaUpdate").checked == true ? 1: 0;
    const csrftoken = getCookie("csrftoken");
  
    element.setAttribute("data-dismiss", "modal");
    $.ajax({
      type: "POST",
      url: "/editarMarcas/",
      data: {
        txtIdmarca: id,
        txtdescripcionMarca: descripcion,
        txtEstadoMarcas: estado,
        csrfmiddlewaretoken: csrftoken,
      },
      beforeSend: function () {
        $("#loader").fadeIn();
      },
      success: function (data) {
        document.getElementById("txtdescripcionMarcaUpdate").value = "";
        document.getElementById("txtEstadoMarcaUpdate").checked = false;
        setTimeout(function () {
          $("#loader").fadeOut();
  
          Swal.fire({
            position: "center",
            icon: "success",
            title: "Marca Actualizando correctamente...",
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
  
  function saveBrandRecord() {
    const element = document.getElementById("myButtonBrand");
    var descripcion = document.getElementById("txtdescripcionMarca").value;
    var estado = document.getElementById("txtEstadoMarca").checked;
    const csrftoken = getCookie("csrftoken");
  
    let validate = ValidateBrand(descripcion, estado);
  
    if (validate) {
      element.setAttribute("data-dismiss", "modal");
      $.ajax({
        type: "POST",
        url: "/registrarMarcas/",
        data: {
            txtdescripcionMarca: descripcion,
            txtEstadoMarca: estado,
            csrfmiddlewaretoken: csrftoken,
        },
        beforeSend: function () {
          $("#loader").fadeIn();
        },
        success: function (data) {
          document.getElementById("txtdescripcionMarca").value = "";
          document.getElementById("txtEstadoMarca").checked = false;
          setTimeout(function () {
            $("#loader").fadeOut();
    
            Swal.fire({
              position: "center",
              icon: "success",
              title: "Marca Agregada correctamente...",
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
  
  function ValidateBrand(descripcion, estado) {
    if (descripcion == "" || descripcion == "undefined" || descripcion == null) {
      Swal.fire({
        icon: "warning",
        title: "Oops...",
        text: "Favor de colocar la descripcion",
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
  