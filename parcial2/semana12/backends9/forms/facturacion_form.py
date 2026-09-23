# ==========================================
# FORMULARIO DE FACTURACIÓN
# ==========================================


def validar_factura(cliente_id, pelicula_id, cantidad):
    """
    Valida los datos básicos de una factura.

    Retorna:
        (True, None) si los datos son correctos.
        (False, mensaje) si existe algún error.
    """

    # ==========================================
    # VALIDAR CLIENTE
    # ==========================================

    if not cliente_id:
        return False, "Debe seleccionar un cliente."

    try:
        cliente_id = int(cliente_id)
    except (ValueError, TypeError):
        return False, "El cliente seleccionado no es válido."

    if cliente_id <= 0:
        return False, "El cliente seleccionado no es válido."

    # ==========================================
    # VALIDAR PELÍCULA
    # ==========================================

    if not pelicula_id:
        return False, "Debe seleccionar una película."

    try:
        pelicula_id = int(pelicula_id)
    except (ValueError, TypeError):
        return False, "La película seleccionada no es válida."

    if pelicula_id <= 0:
        return False, "La película seleccionada no es válida."

    # ==========================================
    # VALIDAR CANTIDAD
    # ==========================================

    try:
        cantidad = int(cantidad)
    except (ValueError, TypeError):
        return False, "La cantidad debe ser un número entero."

    if cantidad <= 0:
        return False, "La cantidad debe ser mayor que cero."

    # ==========================================
    # DATOS CORRECTOS
    # ==========================================

    return True, None
