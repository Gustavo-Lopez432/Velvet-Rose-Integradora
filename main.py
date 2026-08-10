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

    #? Guardamos aquí los datos del empleado que inició sesión.
    sesion = {"id_empleado": None, "nombre": None, "rol": None}

    def actualizar_vista(vista):
        contenido.content = vista
        page.update()

    def mostrar_dashboard(id_empleado, nombre, rol):

        sesion["id_empleado"] = id_empleado
        sesion["nombre"] = nombre
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

                    #? Texto informativo, ya no es un botón clicable
                    ft.Container(
                        padding=ft.Padding.symmetric(horizontal=15, vertical=8),
                        border_radius=8,
                        bgcolor="#C2355F",
                        content=ft.Row(
                            controls=[
                                ft.Icon(
                                    ft.Icons.PERSON,
                                    color="#FFFFFF"
                                ),
                                ft.Text(
                                    f"Bienvenido, {sesion['nombre']}",
                                    color="#FFFFFF",
                                    weight=ft.FontWeight.BOLD,
                                )
                            ],
                            spacing=8
                        ),
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

        botones_menu = {}

        def marcar_activo(nombre_boton):
            for clave, boton in botones_menu.items():
                if clave == nombre_boton:
                    boton.bgcolor = COLOR_ACTIVO_BG
                    boton.color = COLOR_ACTIVO_TEXTO
                else:
                    boton.bgcolor = COLOR_NORMAL_BG
                    boton.color = COLOR_NORMAL_TEXTO
            page.update()

        def ir_a(nombre_boton, vista):
            marcar_activo(nombre_boton)
            actualizar_vista(vista)

        boton_dashboard = ft.ElevatedButton(
            "Dashboard",
            icon=ft.Icons.DASHBOARD,
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
            icon=ft.Icons.POINT_OF_SALE,
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
            icon=ft.Icons.INVENTORY_2,
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
            icon=ft.Icons.BADGE,
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
            icon=ft.Icons.POINT_OF_SALE_OUTLINED,
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
            icon=ft.Icons.BAR_CHART,
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

        def cerrar_sesion(e):
            sesion["id_empleado"] = None
            sesion["nombre"] = None
            sesion["rol"] = None
            mostrar_login()

        boton_cerrar_sesion = ft.ElevatedButton(
            "Cerrar sesión",
            icon=ft.Icons.LOGOUT,
            bgcolor="#C62828",
            color="#FFFFFF",
            width=180,
            on_click=cerrar_sesion,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    weight=ft.FontWeight.BOLD
                )
            )
        )

        sideBar = ft.Container(
            width=220,
            bgcolor="#EF82A2",
            padding=20,

            content=ft.Column(
                controls=[
                    ft.Column(
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
                    ),

                    boton_cerrar_sesion,
                ],

                spacing=15,
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
                        expand=True,
                        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
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