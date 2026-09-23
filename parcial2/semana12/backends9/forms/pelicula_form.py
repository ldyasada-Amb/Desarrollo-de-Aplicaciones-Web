# ==========================================
# FORMULARIO DE PELÍCULAS
# ==========================================


def validar_pelicula(titulo, genero, precio, stock):
    """
    Valida los datos de una película.

    Retorna:
        (True, None) si los datos son correctos.
        (False, mensaje) si existe algún error.
    """

    titulo = titulo.strip()
    genero = genero.strip()

    # ==========================================
    # VALIDAR CAMPOS OBLIGATORIOS
    # ==========================================

    if not titulo:
        return False, "El título de la película es obligatorio."

    if not genero:
        return False, "El género de la película es obligatorio."

    # ==========================================
    # VALIDAR PRECIO
    # ==========================================

    try:
        precio = float(precio)
    except (ValueError, TypeError):
        return False, "El precio debe ser un número válido."

    if precio < 0:
        return False, "El precio no puede ser negativo."

    # ==========================================
    # VALIDAR STOCK
    # ==========================================

    try:
        stock = int(stock)
    except (ValueError, TypeError):
        return False, "El stock debe ser un número entero."

    if stock < 0:
        return False, "El stock no puede ser negativo."

    # ==========================================
    # DATOS CORRECTOS
    # ==========================================

    return True, None
