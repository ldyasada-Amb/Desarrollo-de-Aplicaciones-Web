# ==========================================
# FORMULARIO DE CLIENTES
# ==========================================


def validar_cliente(nombre, apellido, cedula, telefono="", email=""):
    """
    Valida los datos de un cliente.

    Retorna:
        (True, None) si los datos son correctos.
        (False, mensaje) si existe algún error.
    """

    nombre = nombre.strip()
    apellido = apellido.strip()
    cedula = cedula.strip()
    telefono = telefono.strip()
    email = email.strip()

    # ==========================================
    # VALIDAR CAMPOS OBLIGATORIOS
    # ==========================================

    if not nombre:
        return False, "El nombre del cliente es obligatorio."

    if not apellido:
        return False, "El apellido del cliente es obligatorio."

    if not cedula:
        return False, "La cédula del cliente es obligatoria."

    # ==========================================
    # VALIDAR CÉDULA
    # ==========================================

    if not cedula.isdigit():
        return False, "La cédula debe contener únicamente números."

    if len(cedula) != 10:
        return False, "La cédula debe tener 10 dígitos."

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
    # DATOS CORRECTOS
    # ==========================================

    return True, None
