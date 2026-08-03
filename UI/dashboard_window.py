import flet as ft
from DAO.dashboard_dao import *

def dashboard(page: ft.Page):

    #? creamos intantacia y metodos
    dao = DashboardDAO()

    ventas_hoy = dao.ventas_hoy()
    productos = dao.total_productos()
    stock_bajo = dao.stock_bajo()
    total_caja = dao.total_caja()
    productos_mas_vendidos = dao.productos_mas_vendidos()

    #? textos para los targets
    txt_ventas_hoy=ft.Text(
        f"{ventas_hoy:,.2f}",
        size=14,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    txt_productos=ft.Text(
        f"{productos:,.2f}",
        size=14,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    txt_stock_bajo=ft.Text(
            f"{stock_bajo:,.2f}",
            size=14,
            weight=ft.FontWeight.BOLD,
            color="#000000"
        )

    txt_total_caja=ft.Text(
            f"{total_caja:,.2f}",
            size=14,
            weight=ft.FontWeight.BOLD,
            color="#000000"
        )

    #? productos mas vendidos
    mayor = max(producto[2] for producto in productos_mas_vendidos)

    for producto in productos_mas_vendidos:
        porcentaje = producto[2] / mayor

    barra = ft.ProgressBar(
        value=porcentaje,
        width=180,
        color="#C2355F"
    )

    #? encabezado de la ventana
    page.title = "Dashboard"
    page.window_width = 1920
    page.window_height = 1080
    page.padding = 0
    page.bgcolor = "#FFFFFF"


    #? titulo y subtitulo del contenido principal
    titulo = ft.Text(
        "Dashboard",
        size=30,
        weight=ft.FontWeight.BOLD,
        color = "#5A1026"
    )

    subtitulo = ft.Text(
        "Resumen general del sistema",
        size=16,
        weight=ft.FontWeight.NORMAL,
        color = "#5A1026"
    )

    #? header
    header = ft.Container(
        bgcolor="#EF82A2",
        height=100,
        padding=20,
        content=ft.Row(
            controls=[
                ft.Image(
                    src="assets/Logo.png",
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
                        ft.Icon(ft.Icons.PERSON, color="#FFFFFF"),
                        ft.Text("Bienvenido", color="#FFFFFF")
                    ],
                    spacing=5
                    ),
                    bgcolor="#EF82A2"
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
    )

    #? sidebar del dashboard
    menu_lateral = ft.Container(
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
                    style=ft.ButtonStyle(text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
                ),
                
                ft.ElevatedButton(
                    "Ventas",
                    bgcolor="#EF82A2",
                    color="#000000",
                    width=180,
                    style=ft.ButtonStyle(text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
                ),
                
                ft.ElevatedButton(
                    "Productos",
                    bgcolor="#EF82A2",
                    color="#000000",
                    width=180,
                    style=ft.ButtonStyle(text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
                ),
                
                ft.ElevatedButton(
                    "Empleados",
                    bgcolor="#EF82A2",
                    color="#000000",
                    width=180,
                    style=ft.ButtonStyle(text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
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
                    style=ft.ButtonStyle(text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
                ),
                                
                ft.ElevatedButton(
                    "Reportes",
                    bgcolor="#EF82A2",
                    color="#000000",
                    width=180,
                    style=ft.ButtonStyle(text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
                ),
            ],
            spacing=15
        )
    )

    #? tarjetas de stats
    targets = ft.Container(
        content=ft.Row(
            controls = [
                ft.Container(
                    bgcolor="#D8A7B1",
                    height=200,
                    expand=True,
                    blur=10,
                    border=ft.Border.all(2, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Ventas de hoy",
                                color="#5A1026",
                                weight=ft.FontWeight.BOLD,
                                size=14
                            ),

                            ft.Container(
                                width=120,
                                content=ft.Divider(
                                    color="#C2355F",
                                )
                            ),

                            txt_ventas_hoy,

                            ft.Container(
                                width=120,
                                content=ft.Divider(
                                    color="#C2355F",
                                )
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=12
                    )
                ),

                ft.Container(
                    bgcolor="#D8A7B1",
                    height=200,
                    expand=True,
                    blur=10,
                    border=ft.Border.all(2, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Productos",
                                color="#5A1026",
                                weight=ft.FontWeight.BOLD,
                                size=14
                            ),

                            ft.Container(
                                width=120,
                                content=ft.Divider(
                                    color="#C2355F",
                                )
                            ),

                            txt_productos,

                            ft.Container(
                                width=120,
                                content=ft.Divider(
                                    color="#C2355F",
                                )
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=12
                    )
                ),

                ft.Container(
                    bgcolor="#D8A7B1",
                    height=200,
                    expand=True,
                    blur=10,
                    border=ft.Border.all(2, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Stock bajo",
                                color="#5A1026",
                                weight=ft.FontWeight.BOLD,
                                size=14
                            ),

                            ft.Container(
                                width=120,
                                content=ft.Divider(
                                    color="#C2355F",
                                )
                            ),

                            txt_stock_bajo,

                            ft.Container(
                                width=120,
                                content=ft.Divider(
                                    color="#C2355F",
                                )
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=12
                    )
                ),

                ft.Container(
                    bgcolor="#D8A7B1",
                    height=200,
                    expand=True,
                    blur=10,
                    border=ft.Border.all(2, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Total en caja",
                                color="#5A1026",
                                weight=ft.FontWeight.BOLD,
                                size=14
                            ),

                            ft.Container(
                                width=120,
                                content=ft.Divider(
                                    color="#C2355F",
                                )
                            ),

                            txt_total_caja,

                            ft.Container(
                                width=120,
                                content=ft.Divider(
                                    color="#C2355F",
                                )
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=12
                    )
                )
            ],
            spacing=20
        ),
        padding=5
    )

    #? tragets of table and grafic
    targets_bottom = ft.Container (
        content=ft.Row(
            controls=[
                ft.Container(
                    height=350,
                    expand=8,
                    blur=10,
                    border=ft.Border.all(2, "#5A1026"),
                    content=ft.Container(
                        ft.Text(
                            "Productos mas vendidos", 
                            color="#5A1026", 
                            weight=ft.FontWeight.BOLD, 
                            margin=10
                        ),

                        ft.Text(
                            barra
                        )
                    ),
                ),

                ft.Container(
                    height=350,
                    expand=4,
                    border=ft.Border.all(2, "#5A1026"),
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "Resumen de ventas",
                                color="#5A1026", 
                                weight=ft.FontWeight.BOLD,
                            ),

                            ft.Dropdown(
                                width=200,
                                height=35,
                                hint_text="Filtrar por",
                                color="#000000",
                                options=[
                                    ft.dropdown.Option("Día"),
                                    ft.dropdown.Option("Mes"),
                                    ft.dropdown.Option("Año"),
                                    ft.dropdown.Option("Todo el tiempo"),
                                ],
                            )
                        ],
                        align=ft.Alignment.TOP_CENTER,
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        margin=10
                    )
                ),
            ]
        )
    )

    #? contenido principal del layout (SIN header)
    contenido = ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                subtitulo,
                targets,
                targets_bottom
            ],
            spacing=10
        ),
        padding=30,
        expand=True
    )

    #? Row con sidebar y contenido (SIN header)
    layout_interno = ft.Row(
        controls=[menu_lateral, contenido],
        expand=True
    )

    #? Layout final: header arriba, row abajo
    layout = ft.Column(
        controls=[
            header,
            layout_interno
        ],
        spacing=0,
        expand=True
    )
    
    page.add(layout)

ft.app(target=dashboard)