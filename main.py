import flet as ft
from UI.inicio_sesion_window import inicio_sesion_window
from UI.dashboard_window import dashboard_window
from UI.ventas_window import ventas_window
from UI.productos_window import productos_window
from UI.empleados_window import empleados_window
from UI.reportes_window import reportes_window
from UI.corteCaja_window import corte_caja_window

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

    #? Guardamos aquí el id del empleado que inició sesión.
    #? Usamos un diccionario para poder modificarlo desde funciones internas.
    sesion = {"id_empleado": None, "rol": None}

    def actualizar_vista(vista):
        contenido.content = vista
        page.update()

    def mostrar_dashboard(id_empleado, rol):

        sesion["id_empleado"] = id_empleado
        sesion["rol"] = rol

        es_admin = rol == "Administrador"

        #? Header
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

        #? Colores para el botón activo (los mismos que ya tenía "Dashboard")
        COLOR_ACTIVO_BG = "#C2355F"
        COLOR_ACTIVO_TEXTO = "#FFFFFF"
        COLOR_NORMAL_BG = "#EF82A2"
        COLOR_NORMAL_TEXTO = "#000000"

        #? Diccionario para poder recorrer todos los botones del menú y
        #? resetear sus colores antes de marcar el activo
        botones_menu = {}

        def marcar_activo(nombre):
            for clave, boton in botones_menu.items():
                if clave == nombre:
                    boton.bgcolor = COLOR_ACTIVO_BG
                    boton.color = COLOR_ACTIVO_TEXTO
                else:
                    boton.bgcolor = COLOR_NORMAL_BG
                    boton.color = COLOR_NORMAL_TEXTO
            page.update()

        def ir_a(nombre, vista):
            marcar_activo(nombre)
            actualizar_vista(vista)

        boton_dashboard = ft.ElevatedButton(
            "Dashboard",
            bgcolor="#C2355F",
            color="#FFFFFF",
            width=180,
            on_click=lambda e:
                ir_a(
                    "dashboard",
                    dashboard_window(page, sesion["id_empleado"], sesion["rol"])
                ),
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    weight=ft.FontWeight.BOLD
                )
            )
        )

        boton_ventas = ft.ElevatedButton(
            "Ventas",
            bgcolor="#EF82A2",
            color="#000000",
            width=180,
            on_click=lambda e:
                ir_a(
                    "ventas",
                    ventas_window(
                        page,
                        actualizar_vista,
                        sesion["id_empleado"]
                    )
                ),
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    weight=ft.FontWeight.BOLD
                )
            )
        )

        boton_productos = ft.ElevatedButton(
            "Productos",
            bgcolor="#EF82A2",
            color="#000000",
            width=180,
            on_click=lambda e:
                ir_a(
                    "productos",
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
        )

        boton_empleados = ft.ElevatedButton(
            "Empleados",
            bgcolor="#EF82A2",
            color="#000000",
            width=180,
            disabled=not es_admin,
            on_click=lambda e:
                ir_a(
                    "empleados",
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
        )

        boton_corte_caja = ft.ElevatedButton(
            "Corte de caja",
            bgcolor="#EF82A2",
            color="#000000",
            width=180,
            on_click=lambda e:
                ir_a(
                    "corte_caja",
                    corte_caja_window(
                        page,
                        actualizar_vista,
                        sesion["id_empleado"]
                    )
                ),
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    weight=ft.FontWeight.BOLD
                )
            )
        )

        boton_reportes = ft.ElevatedButton(
            "Reportes",
            bgcolor="#EF82A2",
            color="#000000",
            width=180,
            disabled=not es_admin,
            on_click=lambda e:
                ir_a(
                    "reportes",
                    reportes_window(
                        page,
                        actualizar_vista
                    )
                ),
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    weight=ft.FontWeight.BOLD
                )
            )
        )

        botones_menu["dashboard"] = boton_dashboard
        botones_menu["ventas"] = boton_ventas
        botones_menu["productos"] = boton_productos
        botones_menu["empleados"] = boton_empleados
        botones_menu["corte_caja"] = boton_corte_caja
        botones_menu["reportes"] = boton_reportes

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

                    boton_dashboard,
                    boton_ventas,
                    boton_productos,
                    boton_empleados,

                    ft.Divider(color="#000000"),

                    ft.Text(
                        "Operaciones",
                        size=16,
                        color="#000000",
                        weight=ft.FontWeight.BOLD
                    ),

                    boton_corte_caja,
                    boton_reportes,
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

        marcar_activo("dashboard")
        actualizar_vista(
            dashboard_window(page, sesion["id_empleado"], sesion["rol"])
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