function getProviderAddForm() {
    $("#builtProviderAdd").modal("show");
  }
  
  function getProviderUpdate(id, cedula, nombreComercial, estado) {
    $("#builtUpdateProvider").modal("show");
  
    document.getElementById("txtIdproveedor").value = id;
    document.getElementById("txtcedulaProveedorUpdate").value = cedula;
    document.getElementById("txtNombreComercialProveedorUpdate").value = nombreComercial;
    document.getElementById("txtEstadoProveedorUpdate").checked = estado == "1" ? true : false;
  }
  
  function updateProvider() {
      const element = document.getElementById("myButtonUpdate");
      let id = document.getElementById("txtIdproveedor").value;
      let nombreComercial = document.getElementById("txtNombreComercialProveedorUpdate").value;
      let cedula = document.getElementById("txtcedulaProveedorUpdate").value;
      let estado = document.getElementById("txtEstadoProveedorUpdate").checked == true ? 1: 0;
      const csrftoken = getCookie("csrftoken");
    
      let validate = ValidateEmployees(cedula, nombreComercial, estado, 1);
    
      if (validate) {
        element.setAttribute("data-dismiss", "modal");
        $.ajax({
          type: "POST",
          url: "/editarProveedor/",
          data: {
            txtIdproveedor: id,
            txtNombreComercialProveedor: nombreComercial,
            txtEstadoProveedor: estado,
            txtcedulaProveedor: cedula,
            csrfmiddlewaretoken: csrftoken,
          },
          beforeSend: function () {
            $("#loader").fadeIn();
          },
          success: function (data) {
            document.getElementById("txtIdproveedor").value= "";
            document.getElementById("txtNombreComercialProveedorUpdate").value = "";
            document.getElementById("txtcedulaProveedorUpdate").value = "";
            document.getElementById("txtEstadoProveedorUpdate").checked == false;
            setTimeout(function () {
              $("#loader").fadeOut();
    
              Swal.fire({
                position: "center",
                icon: "success",
                title: "Proveedor Actualizado Correctamente...",
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
  
  function saveProvider() {
    const element = document.getElementById("myButton");
    let nombreComercial = document.getElementById("txtNombreComercialProveedor").value;
    let cedula = document.getElementById("txtcedulaProveedor").value;
    let estado = document.getElementById("txtEstadoProveedor").checked == true ? "1" : "0";;
    const csrftoken = getCookie("csrftoken");
  
    let validate = ValidateEmployees(cedula, nombreComercial, estado, 0);
  
    if (validate) {
      element.setAttribute("data-dismiss", "modal");
      $.ajax({
        type: "POST",
        url: "/registrarProveedor/",
        data: {
          txtNombreComercialProveedor: nombreComercial,
          txtEstadoProveedor: estado,
          txtcedulaProveedor: cedula,
          csrfmiddlewaretoken: csrftoken,
        },
        beforeSend: function () {
          $("#loader").fadeIn();
        },
        success: function (data) {
              document.getElementById("txtNombreComercialProveedor").value= "";
              document.getElementById("txtcedulaProveedor").value = "";
              document.getElementById("txtEstadoProveedor").checked = false;
          setTimeout(function () {
            $("#loader").fadeOut();
  
            Swal.fire({
              position: "center",
              icon: "success",
              title: "Proveedor Agregado correctamente...",
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
  
  function ValidateEmployees(cedula, nombre, estado, type) {
  
      //Si se va actualizar validar si es una cedula valida
      if(type == 1){
          if (cedula == "" || cedula == "undefined" || cedula == null) {
              Swal.fire({
                icon: "warning",
                title: "Oops...",
                text: "Favor de colocar la cedula",
              });
              return false;
            } else {
              if (!validate_cedula(cedula)) {
                Swal.fire({
                  icon: "warning",
                  title: "Oops...",
                  text: "Cedula inválida favor de revisar y colocar nuevamente!!!",
                });
                return false;
              }
            }
      }
      else{
  
          if (cedula == "" || cedula == "undefined" || cedula == null) {
              Swal.fire({
                icon: "warning",
                title: "Oops...",
                text: "Favor de colocar la cedula",
              });
              return false;
            } else {
              if (!validate_cedula(cedula)) {
                Swal.fire({
                  icon: "warning",
                  title: "Oops...",
                  text: "Cedula inválida favor de revisar y colocar nuevamente!!!",
                });
                return false;
              }
            }
      
        if (nombre == "" || nombre == "undefined" || nombre == null) {
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
  
  function validate_cedula(ced) {
    var c = ced.replace(/-/g,'');  
    var cedula = c.substr(0, c.length - 1);  
    var verificador = c.substr(c.length - 1, 1); 
    var suma = 0;   
    var cedulaValida = 0;
    if (ced.length < 11) {
      return false;
    }
    for (i = 0; i < cedula.length; i++) {
      mod = "";
      if (i % 2 == 0) {
        mod = 1;
      } else {
        mod = 2;
      }
      res = cedula.substr(i, 1) * mod;
      if (res > 9) {
        res = res.toString();
        uno = res.substr(0, 1);
        dos = res.substr(1, 1);
        res = eval(uno) + eval(dos);
      }
      suma += eval(res);
    }
    el_numero = (10 - (suma % 10)) % 10;
    if (el_numero == verificador && cedula.substr(0, 3) != "000") {
      cedulaValida = true;
    } else {
      cedulaValida = false;
    }
    return cedulaValida;
  }
  