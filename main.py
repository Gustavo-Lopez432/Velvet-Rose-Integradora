import flet as ft
from UI.inicio_sesion_window import inicio_sesion_window
from UI.dashboard_window import dashboard_window
from UI.ventas_window import ventas_window
from UI.productos_window import productos_window
from UI.empleados_window import empleados_window

def main(page: ft.Page):

    page.fonts = {
        "Dinsical": "assets/fonts/Dinsical-Regular.ttf"
    }

    page.theme = ft.Theme(
        font_family="Dinsical"
    )
    page.bgcolor = "#FFFFFF"
    page.padding = 0
    page.window.full_screen = True

    contenido = ft.Container(
        expand=True
    )

    def actualizar_vista(vista):
        contenido.content = vista
        page.update()

    def mostrar_dashboard():

        # Header
        header = ft.Container(
            bgcolor="#EF82A2",
            height=100,
            padding=20,
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="assets/rosa.png",
                        width=200,
                        height=150,
                    ),

                    ft.Text(
                        "Velvet Rose",
                        size=30,
                        color="#FFFFFF",
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.ElevatedButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(
                                    ft.Icons.PERSON,
                                    color="#FFFFFF"
                                ),
                                ft.Text(
                                    "Bienvenido",
                                    color="#FFFFFF"
                                )
                            ],
                            spacing=5
                        ),
                        bgcolor="#EF82A2"
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
        )

        sideBar = ft.Container(
            width=220,
            bgcolor="#EF82A2",
            padding=20,

            content=ft.Column(
                controls=[

                    ft.Text(
                        "Módulos principales",
                        size=16,
                        color="#000000",
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Divider(color="#000000"),

                    ft.ElevatedButton(
                        "Dashboard",
                        bgcolor="#C2355F",
                        color="#FFFFFF",
                        width=180,
                        on_click=lambda e:
                            actualizar_vista(
                                dashboard_window(page)
                            ),
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD
                            )
                        )
                    ),

                    ft.ElevatedButton(
                        "Ventas",
                        bgcolor="#EF82A2",
                        color="#000000",
                        width=180,
                        on_click=lambda e:
                            actualizar_vista(
                                ventas_window(
                                    page,
                                    actualizar_vista
                                )
                            ),
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD
                            )
                        )
                    ),

                    ft.ElevatedButton(
                        "Productos",
                        bgcolor="#EF82A2",
                        color="#000000",
                        width=180,
                        on_click=lambda e:
                            actualizar_vista(
                                productos_window(
                                    page,
                                    actualizar_vista
                                )
                            ),
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD
                            )
                        )
                    ),

                    ft.ElevatedButton(
                        "Empleados",
                        bgcolor="#EF82A2",
                        color="#000000",
                        width=180,
                        on_click=lambda e:
                            actualizar_vista(
                                empleados_window(
                                    page,
                                    actualizar_vista
                                )
                            ),
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD
                            )
                        )
                    ),

                    ft.Divider(color="#000000"),

                    ft.Text(
                        "Operaciones",
                        size=16,
                        color="#000000",
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.ElevatedButton(
                        "Corte de caja",
                        bgcolor="#EF82A2",
                        color="#000000",
                        width=180,
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD
                            )
                        )
                    ),

                    ft.ElevatedButton(
                        "Reportes",
                        bgcolor="#EF82A2",
                        color="#000000",
                        width=180,
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD
                            )
                        )
                    ),
                ],

                spacing=15
            )
        )

        page.controls.clear()

        page.add(
            ft.Column(
                controls=[
                    header,

                    ft.Row(
                        controls=[
                            sideBar,
                            contenido
                        ],
                        expand=True
                    )
                ],

                spacing=0,
                expand=True
            )
        )

        actualizar_vista(
            dashboard_window(page)
        )

    def mostrar_login():

        page.controls.clear()

        page.add(
            inicio_sesion_window(
                page,
                mostrar_dashboard
            )
        )

        page.update()

    mostrar_login()

ft.app(target=main)