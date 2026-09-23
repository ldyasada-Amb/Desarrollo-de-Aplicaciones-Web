import sqlite3
import os


DATABASE = "data/lastcine.db"


# ==========================================
# CREAR CARPETA DATA
# ==========================================

os.makedirs("data", exist_ok=True)


# ==========================================
# FUNCIÓN PARA CONECTAR A LA BASE DE DATOS
# ==========================================

def obtener_conexion():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row

    # Activar claves foráneas
    conexion.execute("PRAGMA foreign_keys = ON")

    return conexion


# ==========================================
# CREAR TABLAS
# ==========================================

def crear_tablas():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # ==========================================
    # TABLA DE PELÍCULAS
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS peliculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            precio REAL NOT NULL CHECK(precio >= 0),
            stock INTEGER NOT NULL CHECK(stock >= 0)
        )
    """)

    # ==========================================
    # TABLA DE CLIENTES
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            cedula TEXT NOT NULL UNIQUE,
            telefono TEXT,
            email TEXT
        )
    """)

    # ==========================================
    # TABLA DE PROVEEDORES
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proveedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT,
            email TEXT,
            direccion TEXT
        )
    """)

    # ==========================================
    # TABLA DE FACTURACIÓN
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS facturacion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            pelicula_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL CHECK(cantidad > 0),
            total REAL NOT NULL CHECK(total >= 0),
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (cliente_id)
                REFERENCES clientes(id)
                ON DELETE RESTRICT,

            FOREIGN KEY (pelicula_id)
                REFERENCES peliculas(id)
                ON DELETE RESTRICT
        )
    """)

    conexion.commit()
    conexion.close()


# ==========================================
# INICIALIZAR BASE DE DATOS
# ==========================================

if __name__ == "__main__":

    crear_tablas()

    print("==========================================")
    print("Base de datos LastCine creada correctamente.")
    print(f"Ubicación: {DATABASE}")
    print("==========================================")
