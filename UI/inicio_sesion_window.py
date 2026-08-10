import flet as ft
from DAO.inicio_sesion_dao import InicioSesionDAO

def inicio_sesion_window(page: ft.Page, ir_al_dashboard):

    dao = InicioSesionDAO()

    usuario = ft.TextField(
        label="Usuario",
        prefix_icon=ft.Icons.PERSON,
        color="#000000",
        width=300,
    )

    contrasena = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        color="#000000",
        width=300,
    )

    mensaje = ft.Text(
        "",
        color=ft.Colors.RED,
    )

    def iniciar_sesion(e):

        usuario_ingresado = usuario.value
        contrasena_ingresada = contrasena.value

        if not usuario_ingresado or not contrasena_ingresada:
            mensaje.value = "Completa todos los campos"
            mensaje.color = ft.Colors.RED
            page.update()
            return

        resultado = dao.validar_usuario(usuario_ingresado, contrasena_ingresada)

        if resultado == "INACTIVO":
            mensaje.value = "Este usuario ha sido desactivado"
            mensaje.color = ft.Colors.RED
            page.update()
            return

        if resultado:
            id_empleado = resultado[0]
            nombre = resultado[1]
            rol = resultado[4]

            mensaje.value = "Inicio de sesión exitoso"
            mensaje.color = ft.Colors.GREEN
            page.update()

            ir_al_dashboard(id_empleado, nombre, rol)

        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            mensaje.color = ft.Colors.RED
            page.update()

    boton = ft.ElevatedButton(
        "Iniciar sesión",
        bgcolor="#EF82A2",
        color="#000000",
        width=300,
        height=50,
        on_click=iniciar_sesion,
    )

    formulario = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Iniciar sesión",
                    size=20,
                    color="#000000",
                    weight=ft.FontWeight.BOLD,
                ),

                usuario,
                contrasena,
                boton,
                mensaje,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),

        width=400,
        padding=30,
        alignment=ft.Alignment.CENTER,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        border=ft.Border.all(3, "#EF82A2"),
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(
                    src="assets/Logo.png",
                    width=300,
                    height=250,
                ),
                formulario,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        expand=True,
        alignment=ft.Alignment.CENTER,
    )