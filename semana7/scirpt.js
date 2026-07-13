// Variables
const movieForm = document.getElementById("movieForm");
const mensaje = document.getElementById("mensaje");
const listaPeliculas = document.getElementById("listaPeliculas");
const total = document.getElementById("total");

const nombre = document.getElementById("nombre");
const descripcion = document.getElementById("descripcion");
const categoria = document.getElementById("categoria");

let contador = 0;

// Función para mostrar mensajes generales
function mostrarMensaje(texto, tipo = "danger") {
  mensaje.innerHTML = "";
  const alert = document.createElement("div");
  alert.className = `alert alert-${tipo}`;
  alert.textContent = texto;
  mensaje.appendChild(alert);
}

// Función para mostrar error debajo de cada campo
function mostrarError(campo, mensaje) {
  let feedback = campo.nextElementSibling;
  feedback.textContent = mensaje;
  campo.classList.add("is-invalid");
  campo.classList.remove("is-valid");
}

function mostrarValido(campo) {
  let feedback = campo.nextElementSibling;
  feedback.textContent = "";
  campo.classList.remove("is-invalid");
  campo.classList.add("is-valid");
}

// Validaciones
function validarNombre() {
  if (nombre.value.trim().length < 3) {
    mostrarError(nombre, "El nombre debe tener al menos 3 caracteres.");
    return false;
  }
  mostrarValido(nombre);
  return true;
}

function validarDescripcion() {
  if (descripcion.value.trim().length < 10) {
    mostrarError(descripcion, "La descripción debe ser más detallada (mínimo 10 caracteres).");
    return false;
  }
  mostrarValido(descripcion);
  return true;
}

function validarCategoria() {
  if (!categoria.value.trim()) {
    mostrarError(categoria, "Debe seleccionar una categoría.");
    return false;
  }
  mostrarValido(categoria);
  return true;
}

// Eventos en tiempo real
nombre.addEventListener("input", validarNombre);
descripcion.addEventListener("input", validarDescripcion);
categoria.addEventListener("blur", validarCategoria);

// Evento submit
movieForm.addEventListener("submit", function (e) {
  e.preventDefault();

  const validoNombre = validarNombre();
  const validoDescripcion = validarDescripcion();
  const validoCategoria = validarCategoria();

  if (!validoNombre || !validoDescripcion || !validoCategoria) {
    mostrarMensaje("Corrige los errores antes de registrar la película.", "danger");
    return;
  }

  mostrarMensaje("Película agregada correctamente", "success");

  // Crear tarjeta dinámica con Bootstrap
  const card = document.createElement("div");
  card.className = "card mb-3";

  const cardBody = document.createElement("div");
  cardBody.className = "card-body";

  cardBody.innerHTML = `
    <h5 class="card-title">${nombre.value}</h5>
    <h6 class="card-subtitle mb-2 text-muted">${categoria.value}</h6>
    <p class="card-text">${descripcion.value}</p>
  `;

  const btnEliminar = document.createElement("button");
  btnEliminar.className = "btn btn-sm btn-danger";
  btnEliminar.textContent = "Eliminar";

  btnEliminar.addEventListener("click", function () {
    listaPeliculas.removeChild(card);
    contador--;
    total.textContent = contador;
    mostrarMensaje("Película eliminada", "warning");
  });

  cardBody.appendChild(btnEliminar);
  card.appendChild(cardBody);
  listaPeliculas.appendChild(card);

  contador++;
  total.textContent = contador;

  // Resetear formulario y clases
  movieForm.reset();
  nombre.classList.remove("is-valid");
  descripcion.classList.remove("is-valid");
  categoria.classList.remove("is-valid");
});


