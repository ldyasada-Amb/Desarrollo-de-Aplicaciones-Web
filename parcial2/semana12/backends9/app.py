from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

from database import obtener_conexion, crear_tablas


app = Flask(__name__)
app.secret_key = "lastcine_secret_key"


# ==========================================
# CONEXIÓN A LA BASE DE DATOS
# ==========================================

def conectar_db():
    return obtener_conexion()


# ==========================================
# INICIO
# ==========================================

@app.route("/")
def index():
    return render_template("index.html")


# ==========================================
# PELÍCULAS
# ==========================================

@app.route("/peliculas")
def peliculas():

    conexion = conectar_db()

    peliculas = conexion.execute("""
        SELECT *
        FROM peliculas
        ORDER BY id DESC
    """).fetchall()

    conexion.close()

    return render_template(
        "peliculas.html",
        peliculas=peliculas
    )


# ==========================================
# NUEVA PELÍCULA
# ==========================================

@app.route("/peliculas/nueva", methods=["GET", "POST"])
def nueva_pelicula():

    if request.method == "POST":

        titulo = request.form.get("titulo", "").strip()
        genero = request.form.get("genero", "").strip()

        try:
            precio = float(request.form.get("precio", 0))
            stock = int(request.form.get("stock", 0))

        except (ValueError, TypeError):
            flash(
                "Precio o stock inválido.",
                "danger"
            )

            return redirect(
                url_for("nueva_pelicula")
            )

        if not titulo or not genero:

            flash(
                "Todos los campos obligatorios deben completarse.",
                "danger"
            )

            return redirect(
                url_for("nueva_pelicula")
            )

        if precio < 0:

            flash(
                "El precio no puede ser negativo.",
                "danger"
            )

            return redirect(
                url_for("nueva_pelicula")
            )

        if stock < 0:

            flash(
                "El stock no puede ser negativo.",
                "danger"
            )

            return redirect(
                url_for("nueva_pelicula")
            )

        conexion = conectar_db()

        try:

            conexion.execute("""
                INSERT INTO peliculas
                (
                    titulo,
                    genero,
                    precio,
                    stock
                )
                VALUES (?, ?, ?, ?)
            """, (
                titulo,
                genero,
                precio,
                stock
            ))

            conexion.commit()

            flash(
                "Película agregada correctamente.",
                "success"
            )

        except sqlite3.IntegrityError:

            conexion.rollback()

            flash(
                "No se pudo agregar la película.",
                "danger"
            )

        finally:

            conexion.close()

        return redirect(
            url_for("peliculas")
        )

    return render_template(
        "formulario_pelicula.html"
    )


# ==========================================
# EDITAR PELÍCULA
# ==========================================

@app.route("/peliculas/editar/<int:id>", methods=["GET", "POST"])
def editar_pelicula(id):

    conexion = conectar_db()

    pelicula = conexion.execute("""
        SELECT *
        FROM peliculas
        WHERE id = ?
    """, (id,)).fetchone()

    if pelicula is None:

        conexion.close()

        flash(
            "Película no encontrada.",
            "danger"
        )

        return redirect(
            url_for("peliculas")
        )

    if request.method == "POST":

        titulo = request.form.get(
            "titulo",
            ""
        ).strip()

        genero = request.form.get(
            "genero",
            ""
        ).strip()

        try:

            precio = float(
                request.form.get(
                    "precio",
                    0
                )
            )

            stock = int(
                request.form.get(
                    "stock",
                    0
                )
            )

        except (ValueError, TypeError):

            conexion.close()

            flash(
                "Precio o stock inválido.",
                "danger"
            )

            return redirect(
                url_for(
                    "editar_pelicula",
                    id=id
                )
            )

        if not titulo or not genero:

            conexion.close()

            flash(
                "Todos los campos obligatorios deben completarse.",
                "danger"
            )

            return redirect(
                url_for(
                    "editar_pelicula",
                    id=id
                )
            )

        if precio < 0 or stock < 0:

            conexion.close()

            flash(
                "Precio y stock no pueden ser negativos.",
                "danger"
            )

            return redirect(
                url_for(
                    "editar_pelicula",
                    id=id
                )
            )

        try:

            conexion.execute("""
                UPDATE peliculas
                SET
                    titulo = ?,
                    genero = ?,
                    precio = ?,
                    stock = ?
                WHERE id = ?
            """, (
                titulo,
                genero,
                precio,
                stock,
                id
            ))

            conexion.commit()

            flash(
                "Película actualizada correctamente.",
                "success"
            )

        except sqlite3.IntegrityError:

            conexion.rollback()

            flash(
                "No se pudo actualizar la película.",
                "danger"
            )

        finally:

            conexion.close()

        return redirect(
            url_for("peliculas")
        )

    conexion.close()

    return render_template(
        "formulario_pelicula.html",
        pelicula=pelicula
    )


# ==========================================
# ELIMINAR PELÍCULA
# ==========================================

@app.route("/peliculas/eliminar/<int:id>")
def eliminar_pelicula(id):

    conexion = conectar_db()

    try:

        pelicula = conexion.execute("""
            SELECT id
            FROM peliculas
            WHERE id = ?
        """, (id,)).fetchone()

        if pelicula is None:

            flash(
                "Película no encontrada.",
                "danger"
            )

        else:

            conexion.execute("""
                DELETE FROM peliculas
                WHERE id = ?
            """, (id,))

            conexion.commit()

            flash(
                "Película eliminada correctamente.",
                "success"
            )

    except sqlite3.IntegrityError:

        conexion.rollback()

        flash(
            "No se puede eliminar esta película porque tiene facturas asociadas.",
            "danger"
        )

    finally:

        conexion.close()

    return redirect(
        url_for("peliculas")
    )


# ==========================================
# CLIENTES
# ==========================================

@app.route("/clientes")
def clientes():

    conexion = conectar_db()

    clientes = conexion.execute("""
        SELECT *
        FROM clientes
        ORDER BY id DESC
    """).fetchall()

    conexion.close()

    return render_template(
        "clientes.html",
        clientes=clientes
    )


# ==========================================
# NUEVO CLIENTE
# ==========================================

@app.route("/clientes/nuevo", methods=["GET", "POST"])
def nuevo_cliente():

    if request.method == "POST":

        nombre = request.form.get(
            "nombre",
            ""
        ).strip()

        apellido = request.form.get(
            "apellido",
            ""
        ).strip()

        cedula = request.form.get(
            "cedula",
            ""
        ).strip()

        telefono = request.form.get(
            "telefono",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        if not nombre or not apellido or not cedula:

            flash(
                "Nombre, apellido y cédula son obligatorios.",
                "danger"
            )

            return redirect(
                url_for("nuevo_cliente")
            )

        conexion = conectar_db()

        try:

            conexion.execute("""
                INSERT INTO clientes
                (
                    nombre,
                    apellido,
                    cedula,
                    telefono,
                    email
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                nombre,
                apellido,
                cedula,
                telefono,
                email
            ))

            conexion.commit()

            flash(
                "Cliente agregado correctamente.",
                "success"
            )

        except sqlite3.IntegrityError:

            conexion.rollback()

            flash(
                "La cédula ya está registrada.",
                "danger"
            )

        finally:

            conexion.close()

        return redirect(
            url_for("clientes")
        )

    return render_template(
        "formulario_cliente.html"
    )


# ==========================================
# EDITAR CLIENTE
# ==========================================

@app.route("/clientes/editar/<int:id>", methods=["GET", "POST"])
def editar_cliente(id):

    conexion = conectar_db()

    cliente = conexion.execute("""
        SELECT *
        FROM clientes
        WHERE id = ?
    """, (id,)).fetchone()

    if cliente is None:

        conexion.close()

        flash(
            "Cliente no encontrado.",
            "danger"
        )

        return redirect(
            url_for("clientes")
        )

    if request.method == "POST":

        nombre = request.form.get(
            "nombre",
            ""
        ).strip()

        apellido = request.form.get(
            "apellido",
            ""
        ).strip()

        cedula = request.form.get(
            "cedula",
            ""
        ).strip()

        telefono = request.form.get(
            "telefono",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        if not nombre or not apellido or not cedula:

            conexion.close()

            flash(
                "Nombre, apellido y cédula son obligatorios.",
                "danger"
            )

            return redirect(
                url_for(
                    "editar_cliente",
                    id=id
                )
            )

        try:

            conexion.execute("""
                UPDATE clientes
                SET
                    nombre = ?,
                    apellido = ?,
                    cedula = ?,
                    telefono = ?,
                    email = ?
                WHERE id = ?
            """, (
                nombre,
                apellido,
                cedula,
                telefono,
                email,
                id
            ))

            conexion.commit()

            flash(
                "Cliente actualizado correctamente.",
                "success"
            )

        except sqlite3.IntegrityError:

            conexion.rollback()

            flash(
                "La cédula ya pertenece a otro cliente.",
                "danger"
            )

        finally:

            conexion.close()

        return redirect(
            url_for("clientes")
        )

    conexion.close()

    return render_template(
        "formulario_cliente.html",
        cliente=cliente
    )


# ==========================================
# ELIMINAR CLIENTE
# ==========================================

@app.route("/clientes/eliminar/<int:id>")
def eliminar_cliente(id):

    conexion = conectar_db()

    try:

        cliente = conexion.execute("""
            SELECT id
            FROM clientes
            WHERE id = ?
        """, (id,)).fetchone()

        if cliente is None:

            flash(
                "Cliente no encontrado.",
                "danger"
            )

        else:

            conexion.execute("""
                DELETE FROM clientes
                WHERE id = ?
            """, (id,))

            conexion.commit()

            flash(
                "Cliente eliminado correctamente.",
                "success"
            )

    except sqlite3.IntegrityError:

        conexion.rollback()

        flash(
            "No se puede eliminar este cliente porque tiene facturas asociadas.",
            "danger"
        )

    finally:

        conexion.close()

    return redirect(
        url_for("clientes")
    )


# ==========================================
# PROVEEDORES
# ==========================================

@app.route("/proveedores")
def proveedores():

    conexion = conectar_db()

    proveedores = conexion.execute("""
        SELECT *
        FROM proveedores
        ORDER BY id DESC
    """).fetchall()

    conexion.close()

    return render_template(
        "proveedores.html",
        proveedores=proveedores
    )


# ==========================================
# NUEVO PROVEEDOR
# ==========================================

@app.route("/proveedores/nuevo", methods=["GET", "POST"])
def nuevo_proveedor():

    if request.method == "POST":

        nombre = request.form.get(
            "nombre",
            ""
        ).strip()

        telefono = request.form.get(
            "telefono",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        direccion = request.form.get(
            "direccion",
            ""
        ).strip()

        if not nombre:

            flash(
                "El nombre del proveedor es obligatorio.",
                "danger"
            )

            return redirect(
                url_for("nuevo_proveedor")
            )

        conexion = conectar_db()

        try:

            conexion.execute("""
                INSERT INTO proveedores
                (
                    nombre,
                    telefono,
                    email,
                    direccion
                )
                VALUES (?, ?, ?, ?)
            """, (
                nombre,
                telefono,
                email,
                direccion
            ))

            conexion.commit()

            flash(
                "Proveedor agregado correctamente.",
                "success"
            )

        except sqlite3.IntegrityError:

            conexion.rollback()

            flash(
                "No se pudo agregar el proveedor.",
                "danger"
            )

        finally:

            conexion.close()

        return redirect(
            url_for("proveedores")
        )

    return render_template(
        "formulario_proveedor.html"
    )


# ==========================================
# EDITAR PROVEEDOR
# ==========================================

@app.route("/proveedores/editar/<int:id>", methods=["GET", "POST"])
def editar_proveedor(id):

    conexion = conectar_db()

    proveedor = conexion.execute("""
        SELECT *
        FROM proveedores
        WHERE id = ?
    """, (id,)).fetchone()

    if proveedor is None:

        conexion.close()

        flash(
            "Proveedor no encontrado.",
            "danger"
        )

        return redirect(
            url_for("proveedores")
        )

    if request.method == "POST":

        nombre = request.form.get(
            "nombre",
            ""
        ).strip()

        telefono = request.form.get(
            "telefono",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        direccion = request.form.get(
            "direccion",
            ""
        ).strip()

        if not nombre:

            conexion.close()

            flash(
                "El nombre del proveedor es obligatorio.",
                "danger"
            )

            return redirect(
                url_for(
                    "editar_proveedor",
                    id=id
                )
            )

        try:

            conexion.execute("""
                UPDATE proveedores
                SET
                    nombre = ?,
                    telefono = ?,
                    email = ?,
                    direccion = ?
                WHERE id = ?
            """, (
                nombre,
                telefono,
                email,
                direccion,
                id
            ))

            conexion.commit()

            flash(
                "Proveedor actualizado correctamente.",
                "success"
            )

        except sqlite3.IntegrityError:

            conexion.rollback()

            flash(
                "No se pudo actualizar el proveedor.",
                "danger"
            )

        finally:

            conexion.close()

        return redirect(
            url_for("proveedores")
        )

    conexion.close()

    return render_template(
        "formulario_proveedor.html",
        proveedor=proveedor
    )


# ==========================================
# ELIMINAR PROVEEDOR
# ==========================================

@app.route("/proveedores/eliminar/<int:id>")
def eliminar_proveedor(id):

    conexion = conectar_db()

    try:

        proveedor = conexion.execute("""
            SELECT id
            FROM proveedores
            WHERE id = ?
        """, (id,)).fetchone()

        if proveedor is None:

            flash(
                "Proveedor no encontrado.",
                "danger"
            )

        else:

            conexion.execute("""
                DELETE FROM proveedores
                WHERE id = ?
            """, (id,))

            conexion.commit()

            flash(
                "Proveedor eliminado correctamente.",
                "success"
            )

    except sqlite3.IntegrityError:

        conexion.rollback()

        flash(
            "No se pudo eliminar el proveedor.",
            "danger"
        )

    finally:

        conexion.close()

    return redirect(
        url_for("proveedores")
    )


# ==========================================
# FACTURACIÓN
# ==========================================

@app.route("/facturacion")
def facturacion():

    conexion = conectar_db()

    facturas = conexion.execute("""
        SELECT
            facturacion.id,
            facturacion.cantidad,
            facturacion.total,
            facturacion.fecha,

            clientes.nombre || ' ' || clientes.apellido
                AS cliente,

            peliculas.titulo
                AS pelicula

        FROM facturacion

        INNER JOIN clientes
            ON facturacion.cliente_id = clientes.id

        INNER JOIN peliculas
            ON facturacion.pelicula_id = peliculas.id

        ORDER BY facturacion.id DESC
    """).fetchall()

    conexion.close()

    return render_template(
        "facturacion.html",
        facturas=facturas
    )


# ==========================================
# NUEVA FACTURA
# ==========================================

@app.route("/facturacion/nueva", methods=["GET", "POST"])
def nueva_factura():

    conexion = conectar_db()

    if request.method == "POST":

        cliente_id = request.form.get(
            "cliente_id"
        )

        pelicula_id = request.form.get(
            "pelicula_id"
        )

        try:

            cantidad = int(
                request.form.get(
                    "cantidad",
                    0
                )
            )

        except (ValueError, TypeError):

            conexion.close()

            flash(
                "La cantidad debe ser un número entero.",
                "danger"
            )

            return redirect(
                url_for("nueva_factura")
            )

        # ==================================
        # VALIDAR CLIENTE
        # ==================================

        cliente = conexion.execute("""
            SELECT *
            FROM clientes
            WHERE id = ?
        """, (cliente_id,)).fetchone()

        if cliente is None:

            conexion.close()

            flash(
                "El cliente seleccionado no existe.",
                "danger"
            )

            return redirect(
                url_for("nueva_factura")
            )

        # ==================================
        # VALIDAR PELÍCULA
        # ==================================

        pelicula = conexion.execute("""
            SELECT *
            FROM peliculas
            WHERE id = ?
        """, (pelicula_id,)).fetchone()

        if pelicula is None:

            conexion.close()

            flash(
                "La película seleccionada no existe.",
                "danger"
            )

            return redirect(
                url_for("nueva_factura")
            )

        # ==================================
        # VALIDAR CANTIDAD
        # ==================================

        if cantidad <= 0:

            conexion.close()

            flash(
                "La cantidad debe ser mayor que cero.",
                "danger"
            )

            return redirect(
                url_for("nueva_factura")
            )

        # ==================================
        # VALIDAR STOCK
        # ==================================

        if cantidad > pelicula["stock"]:

            conexion.close()

            flash(
                "No hay suficiente stock disponible.",
                "danger"
            )

            return redirect(
                url_for("nueva_factura")
            )

        # ==================================
        # CALCULAR TOTAL
        # ==================================

        total = pelicula["precio"] * cantidad

        try:

            # ==================================
            # REGISTRAR FACTURA
            # ==================================

            conexion.execute("""
                INSERT INTO facturacion
                (
                    cliente_id,
                    pelicula_id,
                    cantidad,
                    total
                )
                VALUES (?, ?, ?, ?)
            """, (
                cliente_id,
                pelicula_id,
                cantidad,
                total
            ))

            # ==================================
            # DESCONTAR STOCK
            # ==================================

            conexion.execute("""
                UPDATE peliculas
                SET stock = stock - ?
                WHERE id = ?
            """, (
                cantidad,
                pelicula_id
            ))

            conexion.commit()

            flash(
                "Factura registrada correctamente.",
                "success"
            )

        except sqlite3.IntegrityError:

            conexion.rollback()

            flash(
                "No se pudo registrar la factura.",
                "danger"
            )

        finally:

            conexion.close()

        return redirect(
            url_for("facturacion")
        )

    # ==========================================
    # CARGAR CLIENTES
    # ==========================================

    clientes = conexion.execute("""
        SELECT *
        FROM clientes
        ORDER BY nombre, apellido
    """).fetchall()

    # ==========================================
    # CARGAR PELÍCULAS
    # ==========================================

    peliculas = conexion.execute("""
        SELECT *
        FROM peliculas
        WHERE stock > 0
        ORDER BY titulo
    """).fetchall()

    conexion.close()

    return render_template(
        "formulario_facturacion.html",
        clientes=clientes,
        peliculas=peliculas
    )


# ==========================================
# EJECUTAR APLICACIÓN
# ==========================================

if __name__ == "__main__":

    # Crear tablas si todavía no existen
    crear_tablas()

    app.run(
        debug=True
    )
