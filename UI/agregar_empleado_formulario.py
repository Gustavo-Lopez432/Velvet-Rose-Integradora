import re
import flet as ft
from DAO.empleado_dao import EmpleadoDAO
from models.empleado import Empleado

def empleados_window_formulario(page: ft.Page, cancelar, id_empleado=None):

    #? instancias
    empleado_dao = EmpleadoDAO()

    #? si hay id, buscamos al empleado para precargar sus datos (modo edición)
    empleado_actual = None
    if id_empleado is not None:
        todos = empleado_dao.cargar_datos()
        for r in todos:
            if r[0] == id_empleado:
                empleado_actual = r
                break

    page.title = "Editar empleado" if empleado_actual else "Registrar empleado"
    page.bgcolor = "#F9F3F4"
    page.padding = 0

    puestos = ["Vendedor", "Administrador"]

    ancho_campo = 250

    #? Patrón simple de correo, suficiente para atrapar texto sin formato
    #? (evita depender de una librería externa)
    patron_correo = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    nombre = ft.TextField(
        label="Nombre",
        width=ancho_campo,
        value=empleado_actual[1] if empleado_actual else ""
    )

    apellidos = ft.TextField(
        label="Apellidos",
        width=ancho_campo,
        value=empleado_actual[2] if empleado_actual else ""
    )

    telefono = ft.TextField(
        label="Teléfono",
        width=ancho_campo,
        keyboard_type=ft.KeyboardType.PHONE,
        value=empleado_actual[3] if empleado_actual else ""
    )

    correo = ft.TextField(
        label="Correo electrónico",
        width=ancho_campo,
        keyboard_type=ft.KeyboardType.EMAIL,
        value=empleado_actual[4] if empleado_actual else ""
    )

    usuario = ft.TextField(
        label="Usuario",
        width=ancho_campo,
        value=empleado_actual[5] if empleado_actual else ""
    )

    contrasena = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=ancho_campo,
        value=empleado_actual[6] if empleado_actual else ""
    )

    puesto = ft.Dropdown(
        label="Puesto",
        width=ancho_campo,
        options=[ft.dropdown.Option(p) for p in puestos],
        value=empleado_actual[7] if empleado_actual else None
    )

    mensaje = ft.Text(
        "",
        color=ft.Colors.RED,
        text_align=ft.TextAlign.CENTER,
        width=ancho_campo,
    )

    def limpiar_mensaje(e=None):
        if mensaje.value:
            mensaje.value = ""
            page.update()

    nombre.on_change = limpiar_mensaje
    apellidos.on_change = limpiar_mensaje
    telefono.on_change = limpiar_mensaje
    correo.on_change = limpiar_mensaje
    usuario.on_change = limpiar_mensaje
    contrasena.on_change = limpiar_mensaje
    puesto.on_change = limpiar_mensaje

    def cancelar_formulario(e):
        cancelar()

    def guardar_empleado(e):

        errores = []

        if not nombre.value or not nombre.value.strip():
            errores.append("Nombre")

        if not apellidos.value or not apellidos.value.strip():
            errores.append("Apellidos")

        #? Teléfono: solo dígitos (se aceptan espacios/guiones, se limpian antes de validar)
        telefono_limpio = (telefono.value or "").replace(" ", "").replace("-", "")
        if not telefono_limpio:
            errores.append("Teléfono")
        elif not telefono_limpio.isdigit():
            errores.append("Teléfono (solo números)")
        elif len(telefono_limpio) < 10:
            errores.append("Teléfono (mínimo 10 dígitos)")

        if not correo.value or not correo.value.strip():
            errores.append("Correo")
        elif not patron_correo.match(correo.value.strip()):
            errores.append("Correo (formato inválido)")

        if not usuario.value or not usuario.value.strip():
            errores.append("Usuario")

        if not contrasena.value:
            errores.append("Contraseña")

        if not puesto.value:
            errores.append("Puesto")

        if errores:
            mensaje.value = f"Faltan campos por completar: {', '.join(errores)}"
            mensaje.color = ft.Colors.RED
            page.update()
            return

        try:
            if empleado_actual:
                empleado = Empleado(
                    id=id_empleado,
                    nombre=nombre.value.strip(),
                    apellidos=apellidos.value.strip(),
                    telefono=telefono_limpio,
                    correo=correo.value.strip(),
                    usuario=usuario.value.strip(),
                    contrasena=contrasena.value,
                    puesto=puesto.value,
                    estado=empleado_actual[8]
                )
                empleado_dao.update(empleado)
                mensaje.value = f"Empleado '{nombre.value}' actualizado correctamente."
            else:
                empleado = Empleado(
                    id=None,
                    nombre=nombre.value.strip(),
                    apellidos=apellidos.value.strip(),
                    telefono=telefono_limpio,
                    correo=correo.value.strip(),
                    usuario=usuario.value.strip(),
                    contrasena=contrasena.value,
                    puesto=puesto.value
                )
                empleado_dao.insert(empleado)
                mensaje.value = f"Empleado '{nombre.value}' agregado correctamente."

            mensaje.color = ft.Colors.GREEN
            page.update()
            cancelar()

        except Exception:
            #? Cualquier error inesperado (ej. usuario duplicado en la BD)
            #? se muestra de forma controlada en vez de tronar la app
            mensaje.value = "No se pudo guardar el empleado. Verifica que el usuario no esté repetido."
            mensaje.color = ft.Colors.RED
            page.update()

    btn_agregar = ft.ElevatedButton(
        "Guardar cambios" if empleado_actual else "Agregar",
        icon=ft.Icons.SAVE if empleado_actual else ft.Icons.ADD_CIRCLE_OUTLINE,
        bgcolor="#EF82A2",
        color="#000000",
        width=ancho_campo,
        height=45,
        on_click=guardar_empleado,
    )

    btn_cancelar = ft.ElevatedButton(
        "Cancelar",
        icon=ft.Icons.CANCEL_OUTLINED,
        bgcolor="#EF82A2",
        color="#000000",
        width=ancho_campo,
        height=45,
        on_click=cancelar_formulario,
    )

    #? filas de 3 columnas, mismo patrón que el formulario de productos
    fila_1 = ft.Row(
        controls=[nombre, apellidos, telefono],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    fila_2 = ft.Row(
        controls=[correo, usuario, contrasena],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    fila_3 = ft.Row(
        controls=[puesto],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    fila_botones = ft.Row(
        controls=[btn_agregar, btn_cancelar],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    #? Tarjeta ancha al estilo del formulario de productos: blanca, borde
    #? rosa, radio 15, campos en filas de 3 columnas
    formulario = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Editar empleado" if empleado_actual else "Registre un empleado",
                    size=20,
                    color="#000000",
                    weight=ft.FontWeight.BOLD,
                ),
                fila_1,
                fila_2,
                fila_3,
                fila_botones,
                mensaje,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
        ),
        width=850,
        padding=30,
        alignment=ft.Alignment.CENTER,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        border=ft.Border.all(3, "#EF82A2"),
    )

    return ft.Container(
        content=ft.Column(
            controls=[formulario],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=True,
        alignment=ft.Alignment.CENTER,
        padding=30,
    )