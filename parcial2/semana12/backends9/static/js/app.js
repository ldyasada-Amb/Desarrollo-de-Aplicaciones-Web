/* ==========================================
   LASTCINE
   JAVASCRIPT GENERAL
   ========================================== */


/* ==========================================
   CUANDO CARGA LA PÁGINA
   ========================================== */

document.addEventListener("DOMContentLoaded", function () {

    inicializarConfirmaciones();

    inicializarValidaciones();

    inicializarFormularios();

    inicializarAnimaciones();

});


/* ==========================================
   CONFIRMAR ELIMINACIONES
   ========================================== */

function confirmarEliminacion(mensaje) {

    if (!mensaje) {

        mensaje =
            "¿Estás seguro de que deseas eliminar este registro?";

    }

    return window.confirm(mensaje);

}


function inicializarConfirmaciones() {

    const enlacesEliminar =
        document.querySelectorAll(
            ".btn-eliminar"
        );


    enlacesEliminar.forEach(function (enlace) {

        enlace.addEventListener(
            "click",
            function (event) {

                const mensaje =
                    enlace.dataset.mensaje ||
                    "¿Estás seguro de que deseas eliminar este registro?";


                if (!confirmarEliminacion(mensaje)) {

                    event.preventDefault();

                }

            }
        );

    });

}


/* ==========================================
   VALIDACIONES GENERALES
   ========================================== */

function inicializarValidaciones() {

    const formularios =
        document.querySelectorAll("form");


    formularios.forEach(function (formulario) {

        formulario.addEventListener(
            "submit",
            function (event) {

                if (!formulario.checkValidity()) {

                    event.preventDefault();

                    event.stopPropagation();

                }

                formulario.classList.add(
                    "was-validated"
                );

            }
        );

    });

}


/* ==========================================
   FORMULARIOS
   ========================================== */

function inicializarFormularios() {

    inicializarFormularioCliente();

    inicializarFormularioProveedor();

    inicializarFormularioPelicula();

    inicializarFormularioFacturacion();

}


/* ==========================================
   FORMULARIO CLIENTE
   ========================================== */

function inicializarFormularioCliente() {

    const formulario =
        document.querySelector(
            "#formCliente"
        );


    if (!formulario) {

        return;

    }


    const cedula =
        document.querySelector(
            "#cedula"
        );


    const telefono =
        document.querySelector(
            "#telefono"
        );


    if (cedula) {

        cedula.addEventListener(
            "input",
            function () {

                this.value =
                    this.value.replace(
                        /\D/g,
                        ""
                    );

            }
        );

    }


    if (telefono) {

        telefono.addEventListener(
            "input",
            function () {

                this.value =
                    this.value.replace(
                        /\D/g,
                        ""
                    );

            }
        );

    }

}


/* ==========================================
   FORMULARIO PROVEEDOR
   ========================================== */

function inicializarFormularioProveedor() {

    const formulario =
        document.querySelector(
            "#formProveedor"
        );


    if (!formulario) {

        return;

    }


    const telefono =
        document.querySelector(
            "#telefono"
        );


    if (telefono) {

        telefono.addEventListener(
            "input",
            function () {

                this.value =
                    this.value.replace(
                        /\D/g,
                        ""
                    );

            }
        );

    }

}


/* ==========================================
   FORMULARIO PELÍCULA
   ========================================== */

function inicializarFormularioPelicula() {

    const formulario =
        document.querySelector(
            "#formPelicula"
        );


    if (!formulario) {

        return;

    }


    const precio =
        document.querySelector(
            "#precio"
        );


    const stock =
        document.querySelector(
            "#stock"
        );


    if (precio) {

        precio.addEventListener(
            "input",
            function () {

                if (parseFloat(this.value) < 0) {

                    this.value = 0;

                }

            }
        );

    }


    if (stock) {

        stock.addEventListener(
            "input",
            function () {

                if (parseInt(this.value) < 0) {

                    this.value = 0;

                }

            }
        );

    }

}


/* ==========================================
   FORMULARIO FACTURACIÓN
   ========================================== */

function inicializarFormularioFacturacion() {

    const formulario =
        document.querySelector(
            "#formFactura"
        );


    if (!formulario) {

        return;

    }


    const peliculaSelect =
        document.querySelector(
            "#pelicula_id"
        );


    const cantidadInput =
        document.querySelector(
            "#cantidad"
        );


    const totalFactura =
        document.querySelector(
            "#totalFactura"
        );


    const precioUnitario =
        document.querySelector(
            "#precioUnitario"
        );


    const stockDisponible =
        document.querySelector(
            "#stockDisponible"
        );


    const informacionPelicula =
        document.querySelector(
            "#informacionPelicula"
        );


    function actualizarFactura() {

        if (!peliculaSelect) {

            return;

        }


        const opcion =
            peliculaSelect.options[
                peliculaSelect.selectedIndex
            ];


        if (!opcion || !opcion.value) {

            if (informacionPelicula) {

                informacionPelicula.classList.add(
                    "d-none"
                );

            }


            if (totalFactura) {

                totalFactura.textContent =
                    "$0.00";

            }

            return;

        }


        const precio =
            parseFloat(
                opcion.dataset.precio
            ) || 0;


        const stock =
            parseInt(
                opcion.dataset.stock
            ) || 0;


        let cantidad =
            parseInt(
                cantidadInput.value
            ) || 0;


        if (cantidad < 1) {

            cantidad = 1;

            cantidadInput.value = 1;

        }


        if (cantidad > stock) {

            cantidad = stock;

            cantidadInput.value = stock;

        }


        if (precioUnitario) {

            precioUnitario.textContent =
                "$" + precio.toFixed(2);

        }


        if (stockDisponible) {

            stockDisponible.textContent =
                stock;

        }


        if (informacionPelicula) {

            informacionPelicula.classList.remove(
                "d-none"
            );

        }


        const total =
            precio * cantidad;


        if (totalFactura) {

            totalFactura.textContent =
                "$" + total.toFixed(2);

        }

    }


    if (peliculaSelect) {

        peliculaSelect.addEventListener(
            "change",
            actualizarFactura
        );

    }


    if (cantidadInput) {

        cantidadInput.addEventListener(
            "input",
            actualizarFactura
        );

    }


    actualizarFactura();

}


/* ==========================================
   ANIMACIONES
   ========================================== */

function inicializarAnimaciones() {

    const elementos =
        document.querySelectorAll(
            ".card, .table-responsive"
        );


    elementos.forEach(function (elemento) {

        elemento.classList.add(
            "fade-in"
        );

    });

}


/* ==========================================
   AUTO CERRAR ALERTAS
   ========================================== */

function cerrarAlertasAutomaticamente() {

    const alertas =
        document.querySelectorAll(
            ".alert.alert-dismissible"
        );


    alertas.forEach(function (alerta) {

        setTimeout(function () {

            const boton =
                alerta.querySelector(
                    ".btn-close"
                );


            if (boton) {

                boton.click();

            }

        }, 5000);

    });

}


/* ==========================================
   FORMATEAR MONEDA
   ========================================== */

function formatearMoneda(valor) {

    const numero =
        Number(valor) || 0;


    return new Intl.NumberFormat(
        "es-EC",
        {
            style: "currency",
            currency: "USD"
        }
    ).format(numero);

}


/* ==========================================
   EXPORTAR FUNCIONES
   ========================================== */

window.confirmarEliminacion =
    confirmarEliminacion;

window.formatearMoneda =
    formatearMoneda;
