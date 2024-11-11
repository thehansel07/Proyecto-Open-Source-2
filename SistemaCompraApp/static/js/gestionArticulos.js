function getArticleAddForm() {
    $("#builtArticleAdd").modal("show");
  }
  
  function getArticleUpdateForm(id, cedula, nombre, iddepartamento, estado) {
    $("#builtUpdateEmployees").modal("show");
  
    document.getElementById("txtIdEmpleadoUpdate").value = id
    document.getElementById("txtCedulaEmpleadoUpdate").value = cedula;
    document.getElementById("txtNombreEmpleadoUpdate").value = nombre;
    document.getElementById("txtDepartamentoIdUpdate").value = iddepartamento;
    document.getElementById("txtEstadoEmpleadoUpdate").checked = estado == "1" ? true : false;
  }
  
  function updateEmployees() {
      const element = document.getElementById("myButtonUpdate");
      let id = document.getElementById("txtIdEmpleadoUpdate").value;
      let nombre = document.getElementById("txtNombreEmpleadoUpdate").value;
      let cedula = document.getElementById("txtCedulaEmpleadoUpdate").value;
      let iddepartamento = document.getElementById("txtDepartamentoIdUpdate").value;
      let estado = document.getElementById("txtEstadoEmpleadoUpdate").checked == true ? 1: 0; ;
      const csrftoken = getCookie("csrftoken");
    
      let validate = ValidateEmployees(cedula, nombre, iddepartamento, estado, 1);
    
      if (validate) {
        element.setAttribute("data-dismiss", "modal");
        $.ajax({
          type: "POST",
          url: "/editarEmpleado/",
          data: {
            txtEmpleadoId: id,
            txtEmpleadoNombre: nombre,
            txtEmpleadoEstado: estado,
            txtEmpleadoCedula: cedula,
            txtDepartamentoId: iddepartamento,
            csrfmiddlewaretoken: csrftoken,
          },
          beforeSend: function () {
            $("#loader").fadeIn();
          },
          success: function (data) {
              document.getElementById("txtNombreEmpleadoUpdate").value = "";
              document.getElementById("txtCedulaEmpleadoUpdate").value = "";
              document.getElementById("txtDepartamentoIdUpdate").value = "";
              document.getElementById("txtEstadoEmpleadoUpdate").checked = "";
            setTimeout(function () {
              $("#loader").fadeOut();
    
              Swal.fire({
                position: "center",
                icon: "success",
                title: "Empleado Actualizado correctamente...",
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
  
  function saveArticle() {
    const element = document.getElementById("myButtonAddingArticle");
    let descripcion = document.getElementById("txtDescripcionArticulos").value;
    let unidadMedida = document.getElementById("txtUnidadMedidaArticulos").value;
    let marca = document.getElementById("txtMarcaArticulos").value;
    let existencia = document.getElementById("txtExistenciaArticulos").value;
    let estado = document.getElementById("txtEstadoArticulo").checked == true ? "1" : "0";;
    const csrftoken = getCookie("csrftoken");
  
    let validate = ValidateArticle(descripcion, unidadMedida, marca, existencia, estado, 0);
  
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
            document.getElementById("txtUnidadMedidaArticulos").value = "";
            document.getElementById("txtMarcaArticulos").value = "";
            document.getElementById("txtExistenciaArticulos").value = "";
            document.getElementById("txtEstadoArticulo").checked == true ? "1" : "0";;
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
  
  function ValidateArticle(descripcion, unidadMedida, marca, existencia, estado, type) 
  {
  
    if (descripcion == "" || descripcion == "undefined" || descripcion == null) {
        Swal.fire({
          icon: "warning",
          title: "Oops...",
          text: "Favor de colocar la descripcion",
        });
    
        return false;
      }

    if(Math.sign(existencia) == -1 || existencia == 0 )
        {
        Swal.fire({
            icon: "warning",
            title: "Oops...",
            text: "Favor de colocar cantidad valida, no se acepta 0 ni valor negativo...",
          });
      
          return false;
        
    }

    if (unidadMedida == "" || unidadMedida == "undefined" || unidadMedida == null) {
        Swal.fire({
          icon: "warning",
          title: "Oops...",
          text: "Favor de colocar la Unidad De Medida",
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
  