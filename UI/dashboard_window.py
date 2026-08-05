import flet as ft
import flet_charts as fch
from DAO.dashboard_dao import *

def dashboard(page: ft.Page):

    #? creamos intantacia y metodos
    dao = DashboardDAO()

    ventas_hoy = dao.ventas_hoy()
    productos = dao.total_productos()
    stock_bajo = dao.stock_bajo()
    total_caja = dao.total_caja()
    productos_mas_vendidos = dao.productos_mas_vendidos()
    resumen_ventas = dao.resumen_ventas("Semana")

    #? textos para los targets
    txt_ventas_hoy = ft.Text(
        f"{ventas_hoy:,.2f}",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    txt_productos = ft.Text(
        f"{productos:,.2f}",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    txt_stock_bajo = ft.Text(
        f"{stock_bajo:,.2f}",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    txt_total_caja = ft.Text(
        f"{total_caja:,.2f}",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    filtro_ventas = ft.Dropdown(
        width=150,
        height=35,
        value="Semana",
        color = "#000",

        options=[
            ft.dropdown.Option("Semana"),
            ft.dropdown.Option("Mes"),
            ft.dropdown.Option("Año"),
            ft.dropdown.Option("Todo el tiempo")
        ],
    )

    filtro_ventas.on_text_change = lambda e: actualizar_resumen(e.control.value)

    #? productos mas vendidos
    if productos_mas_vendidos:

        max_ventas = productos_mas_vendidos[0][2]

        productos_porcentaje = []

        for nombre, imagen, ventas in productos_mas_vendidos:

            porcentaje = ventas / max_ventas if max_ventas > 0 else 0

            productos_porcentaje.append((nombre, imagen, ventas, porcentaje))

        #? Crear filas de la tabla
        filas_productos = []

        for nombre, imagen, ventas, porcentaje in productos_porcentaje:

            filas_productos.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(str(imagen), color="#000")
                        ),

                        ft.DataCell(
                            ft.Text(nombre, color="#000")
                        ),

                        ft.DataCell(
                            ft.Text(str(ventas), color="#000")
                        ),

                        ft.DataCell(
                            ft.Container(
                                width=120,
                                height=10,
                                bgcolor="#E5E5E5",
                                border_radius=5,
                                content=ft.Container(
                                    width=120 * porcentaje,
                                    height=10,
                                    bgcolor="#5A1026",
                                    border_radius=5
                                )
                            )
                        )
                    ],
                )
            )

    grafica_ventas = fch.LineChart(
        min_y=0,
        expand=True,
    )

    #? grafica
    def actualizar_resumen(filtro):

        datos = dao.resumen_ventas(filtro)

        puntos = []

        for i, dato in enumerate(datos):
            ventas = dato[1]

            puntos.append(
                fch.LineChartDataPoint(
                    i,
                    float(ventas)
                )
            )

        grafica_ventas.data_series = [
            fch.LineChartData(
                points=puntos,
                curved=True
            )
        ]

        page.update()

    #? titulo y subtitulo del contenido principal
    titulo = ft.Text(
        "Dashboard",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#5A1026"
    )

    subtitulo = ft.Text(
        "Resumen general del sistema",
        size=20,
        weight=ft.FontWeight.NORMAL,
        color="#5A1026"
    )

    #? tarjetas de stats
    targets = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    bgcolor="#D8A7B1",
                    height=200,
                    expand=True,
                    border=ft.Border.all(1, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Ventas de hoy",
                                color="#5A1026",
                                weight=ft.FontWeight.BOLD,
                                size=20
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
                    border=ft.Border.all(1, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Productos",
                                color="#5A1026",
                                weight=ft.FontWeight.BOLD,
                                size=20
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
                    border=ft.Border.all(1, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Stock bajo",
                                color="#5A1026",
                                weight=ft.FontWeight.BOLD,
                                size=20
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
                    border=ft.Border.all(1, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Total en caja",
                                color="#5A1026",
                                weight=ft.FontWeight.BOLD,
                                size=20
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

    #? targets de tabla y grafica
    actualizar_resumen("Semana")
    targets_bottom = ft.Container(
        content=ft.Row(
            controls=[

                #? Cuadro de productos más vendidos
                ft.Container(
                    height=350,
                    expand=8,
                    border=ft.Border.all(1, "#5A1026"),
                    padding=10,

                    content=ft.Column(
                        controls=[

                            #? Título
                            ft.Text(
                                "Productos más vendidos",
                                color="#5A1026",
                                weight=ft.FontWeight.BOLD,
                                size=20,
                            ),

                            #? Tabla
                            ft.DataTable(
                                columns=[
                                    ft.DataColumn(
                                        ft.Text(
                                            "Imagen",
                                            color="#FFFFFF",
                                            weight=ft.FontWeight.BOLD,
                                        )
                                    ),

                                    ft.DataColumn(
                                        ft.Text(
                                            "Nombre",
                                            color="#FFFFFF",
                                            weight=ft.FontWeight.BOLD,
                                        )
                                    ),

                                    ft.DataColumn(
                                        ft.Text(
                                            "Piezas vendidas",
                                            color="#FFFFFF",
                                            weight=ft.FontWeight.BOLD,
                                        )
                                    ),

                                    ft.DataColumn(
                                        ft.Text(
                                            "",
                                            color="#FFFFFF",
                                        )
                                    ),
                                ],

                                rows=filas_productos,
                                heading_row_color="#C2355F",
                            ),
                        ],
                    ),
                ),

                #? Cuadro de resumen de ventas
                ft.Container(
                    height=350,
                    expand=4,
                    border=ft.Border.all(1, "#5A1026"),
                    padding=10,

                    content=ft.Column(
                        controls=[

                            #? Título y dropdown
                            ft.Row(
                                controls=[

                                    ft.Text(
                                        "Resumen de ventas",
                                        color="#5A1026",
                                        weight=ft.FontWeight.BOLD,
                                        size=20,
                                    ),

                                    #? dropdown
                                    filtro_ventas,
                                ],

                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),

                            #? Gráfica
                            ft.Container(
                                height=250,
                                expand=True,
                                content=grafica_ventas,
                            ),
                        ],

                        spacing=10,
                    ),
                ),
            ],

            spacing=15,
        ),
    )

    #? contenido principal
    layout = ft.Container(
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

    return layout