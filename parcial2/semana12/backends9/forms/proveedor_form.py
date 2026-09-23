# ==========================================
# FORMULARIO DE PROVEEDORES
# ==========================================


def validar_proveedor(nombre, telefono="", email="", direccion=""):
    """
    Valida los datos de un proveedor.

    Retorna:
        (True, None) si los datos son correctos.
        (False, mensaje) si existe algún error.
    """

    nombre = nombre.strip()
    telefono = telefono.strip()
    email = email.strip()
    direccion = direccion.strip()

    # ==========================================
    # VALIDAR NOMBRE
    # ==========================================

    if not nombre:
        return False, "El nombre del proveedor es obligatorio."

    # ==========================================
    # VALIDAR TELÉFONO
    # ==========================================

    if telefono:

        if not telefono.isdigit():
            return False, "El teléfono debe contener únicamente números."

        if len(telefono) < 7 or len(telefono) > 10:
            return False, "El teléfono debe tener entre 7 y 10 dígitos."

    # ==========================================
    # VALIDAR CORREO
    # ==========================================

    if email:

        if "@" not in email or "." not in email:
            return False, "El correo electrónico no tiene un formato válido."

    # ==========================================
    # VALIDAR DIRECCIÓN
    # ==========================================

    if len(direccion) > 200:
        return False, "La dirección no puede superar los 200 caracteres."

    # ==========================================
    # DATOS CORRECTOS
    # ==========================================

    return True, None
