// Selección de elementos
const formContainer = document.createElement("section");
formContainer.className = "container my-5";

formContainer.innerHTML = `
  <h3 class="mb-3 text-center">Agregar nueva película</h3>
  <form id="movieForm" class="p-3 border rounded bg-light">
    <div class="mb-3">
      <label for="nombre" class="form-label">Nombre de la película</label>
      <input type="text" id="nombre" class="form-control" placeholder="Ej: Matrix">
    </div>
    <div class="mb-3">
      <label for="descripcion" class="form-label">Descripción</label>
      <textarea id="descripcion" class="form-control" rows="3" placeholder="Breve sinopsis"></textarea>
    </div>
    <div class="mb-3">
      <label for="categoria" class="form-label">Categoría</label>
      <select id="categoria" class="form-select">
        <option value="">Seleccione una categoría</option>
        <option value="Terror">Terror</option>
        <option value="Animación">Animación</option>
        <option value="Acción">Acción</option>
      </select>
    </div>
    <button type="submit" class="btn btn-primary w-100">Agregar película</button>
  </form>
  <div id="mensaje" class="mt-3"></div>
  <h4 class="mt-4">Películas agregadas:</h4>
  <ul id="listaPeliculas" class="list-group"></ul>
  <p class="mt-3 fw-bold">Total de registros: <span id="total">0</span></p>
`;

document.body.appendChild(formContainer);

// Variables
const movieForm = document.getElementById("movieForm");
const mensaje = document.getElementById("mensaje");
const listaPeliculas = document.getElementById("listaPeliculas");
const total = document.getElementById("total");

let contador = 0;

// Función para mostrar mensajes
function mostrarMensaje(texto, tipo = "danger") {
  mensaje.innerHTML = "";
  const alert = document.createElement("div");
  alert.className = `alert alert-${tipo}`;
  alert.textContent = texto;
  mensaje.appendChild(alert);
}

// Evento submit
movieForm.addEventListener("submit", function (e) {
  e.preventDefault();

  const nombre = document.getElementById("nombre").value.trim();
  const descripcion = document.getElementById("descripcion").value.trim();
  const categoria = document.getElementById("categoria").value.trim();

  if (!nombre || !descripcion || !categoria) {
    mostrarMensaje("Todos los campos son obligatorios", "danger");
    return;
  }

  mostrarMensaje("Película agregada correctamente", "success");

  // Crear elemento dinámico
  const li = document.createElement("li");
  li.className = "list-group-item d-flex justify-content-between align-items-center";

  const contenido = document.createElement("div");
  contenido.innerHTML = `<strong>${nombre}</strong> - ${categoria}<br><small>${descripcion}</small>`;

  const btnEliminar = document.createElement("button");
  btnEliminar.className = "btn btn-sm btn-danger ms-3";
  btnEliminar.textContent = "Eliminar";

  btnEliminar.addEventListener("click", function () {
    listaPeliculas.removeChild(li);
    contador--;
    total.textContent = contador;
    mostrarMensaje("Película eliminada", "warning");
  });

  li.appendChild(contenido);
  li.appendChild(btnEliminar);
  listaPeliculas.appendChild(li);

  contador++;
  total.textContent = contador;

  // Resetear formulario
  movieForm.reset();
});
