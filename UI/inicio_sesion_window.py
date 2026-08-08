import flet as ft


def main(page: ft.Page):

    page.theme = ft.Theme(
        font_family="Dinsical"
    )

    page.title = "Velvet Rose - Inicio de sesión"
    page.bgcolor = "#FFFFFF"
    page.padding = 0

    # HEADER
    header = ft.Container(
        bgcolor="#EF82A2",
        height=100,
        padding=20,
        content=ft.Row(
            controls=[
                ft.Text(
                    "BIENVENIDO!!",
                    size=30,
                    color="#FFFFFF",
                    weight=ft.FontWeight.BOLD,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

    # CAMPOS
    usuario = ft.TextField(
        label="Usuario",
        prefix_icon=ft.Icons.PERSON,
        width=300,
    )

    contrasena = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=300,
    )

    mensaje = ft.Text(
        "",
        color=ft.Colors.RED,
    )


    # =========================
    # FUNCIÓN LOGIN
    # =========================

    def iniciar_sesion(e):

        user = usuario.value
        password = contrasena.value

        if user == "admin" and password == "1234":

            mensaje.value = "Inicio de sesión exitoso"
            mensaje.color = ft.Colors.GREEN

        else:

            mensaje.value = "Usuario o contraseña incorrectos"
            mensaje.color = ft.Colors.RED

        page.update()

    # BOTÓN
    boton = ft.ElevatedButton(
        "Iniciar sesión",
        bgcolor="#EF82A2",
        color="#000000",
        width=300,
        height=50,
        on_click=iniciar_sesion,
    )

    # TARJETA DEL LOGIN
    container = ft.Container(
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
        padding=0,
        alignment=ft.Alignment.CENTER,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        border=ft.Border.all(3, "#EF82A2"),
    )

    # CONTENIDO PRINCIPAL
    contenido = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(
                    src="assets/Logo.png",
                    width=300,
                    height=250,
                ),

                container,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),

        expand=True,
        alignment=ft.Alignment.CENTER,
    )
    # PÁGINA
    page.add(
        ft.Column(
            controls=[
                header,
                contenido,
            ],
            spacing=0,
            expand=True,
        )
    )


ft.app(target=main)