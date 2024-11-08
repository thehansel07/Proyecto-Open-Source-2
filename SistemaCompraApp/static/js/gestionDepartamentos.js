

function getBuiltyUpdateForm() {
    $('#builtyUpdateModal').modal('show');
}


function getDepartmentUpdate(id, nombre, estado)
{
    $('#updateDepartment').modal('show');
    document.getElementById("txtIdDepartamentoUpdate").value = id;
    document.getElementById("txtNombreDepartamentoUpdate").value = nombre;
    document.getElementById("txtEstadoDepartamentoUpdate").checked = estado;
}


function updateDepartment()
{
    const element = document.getElementById("myButtonUpdate");
    var id = document.getElementById("txtIdDepartamentoUpdate").value;
    var nombre = document.getElementById("txtNombreDepartamentoUpdate").value;
    var estado = document.getElementById("txtEstadoDepartamentoUpdate").checked == true ? 1 : 0;
    const csrftoken = getCookie('csrftoken');


     element.setAttribute("data-dismiss", "modal");
     $.ajax({
         type: "POST",
         url: '/editarDepartamento/',
         data: 
         {
         
         txtIdDepartamento: id,    
         txtNombreDepartamento: nombre,
         txtEstadoDepartamento: estado,
         csrfmiddlewaretoken: csrftoken,
         },
         beforeSend: function() {
             $("#loader").fadeIn();
         },
         success: function(data) {
             document.getElementById("txtNombreDepartamento").value = '';
             document.getElementById("txtEstadoDepartamento").checked = false
             setTimeout(function() {
                 $("#loader").fadeOut();
                 location.reload()
                 Swal.fire({
                     position: "center",
                     icon: "success",
                     title: "Departamento Actualizando correctamente...",
                     showConfirmButton: false,
                     timer: 1500
                   })
             }, 3000); 
             
         }
         ,
       error: function(xhr, status, error) {
         // Manejo de error si la solicitud fall
         Swal.fire({
             icon: "error",
             title: "Error",
             text: "Ocurrió un error. Inténtalo nuevamente.",
           })
         $("#loader").fadeOut(); 
       }
     });
}
    



    function saveRecord() {

        const element = document.getElementById("myButton");
        var nombre = document.getElementById("txtNombreDepartamento").value;
        var estado = document.getElementById("txtEstadoDepartamento").checked;
        const csrftoken = getCookie('csrftoken');

        let validate = ValidateDepartaments(nombre, estado);

        if(validate)
        {
            element.setAttribute("data-dismiss", "modal");
            $.ajax({
                type: "POST",
                url: '/registrarDepartamentos/',
                data: 
                {
                txtNombreDepartamento: nombre,
                txtEstadoDepartamento: estado,
                csrfmiddlewaretoken: csrftoken,
                },
                beforeSend: function() {
                    $("#loader").fadeIn();
                },
                success: function(data) {
                    document.getElementById("txtNombreDepartamento").value = '';
                    document.getElementById("txtEstadoDepartamento").checked = false;

                    setTimeout(function() {
                        $("#loader").fadeOut();
                        location.reload();

                        Swal.fire({
                            position: "center",
                            icon: "success",
                            title: "Departamento guardado correctamente...",
                            showConfirmButton: false,
                            timer: 1500
                          });

                    }, 3000); 
                    
                }
                ,
              error: function(xhr, status, error) {
                // Manejo de error si la solicitud falla

                Swal.fire({
                    icon: "error",
                    title: "Error",
                    text: "Ocurrió un error. Inténtalo nuevamente.",
                  });

                $("#loader").fadeOut(); 
    
              }
            });
        }
        
    }

    function ValidateDepartaments(nombre, estado)
    {
        if(nombre== '' || nombre =='undefined' || nombre == null)
        {
            Swal.fire({
                icon: "warning",
                title: "Oops...",
                text: "Favor de colocar el nombre",
              });

              return false
        } 
        
        
        if(estado== '' || estado =='undefined' || estado == null)
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
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }