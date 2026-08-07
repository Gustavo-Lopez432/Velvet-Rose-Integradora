import flet as ft
import flet_charts as fch
from DAO.dashboard_dao import DashboardDAO
from datetime import date, datetime

def dashboard_window(page: ft.Page):

    #? creamos intantacia y metodos
    dao = DashboardDAO()

    ventas_hoy = dao.ventas_hoy()
    productos = dao.total_productos()
    stock_bajo = dao.stock_bajo()
    total_caja = dao.total_caja()
    productos_mas_vendidos = dao.productos_mas_vendidos()

    #? textos para los targets
    txt_ventas_hoy = ft.Text(
        f"${ventas_hoy:,.2f}",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    txt_productos = ft.Text(
        f"{productos:,.0f}",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    txt_stock_bajo = ft.Text(
        f"{stock_bajo:,.0f}",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    txt_total_caja = ft.Text(
        f"${total_caja:,.2f}",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    #? productos mas vendidos
    if productos_mas_vendidos:

        max_ventas = float(productos_mas_vendidos[0][2])

        productos_porcentaje = []

        for nombre, imagen, ventas in productos_mas_vendidos:

            ventas = float(ventas)
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
                            ft.Container(
                                content=ft.Text(str(int(ventas)), color="#000"),
                                alignment=ft.Alignment.CENTER,
                                width=120,
                            )
                        ),
                    ],
                )
            )

    grafica_ventas = fch.LineChart(
        min_y=0,
        expand=True,
        border=ft.Border.all(1, "#000000"),
        horizontal_grid_lines=fch.ChartGridLines(
            color="#FFFFFF",
            width=1,
        ),
        left_axis=fch.ChartAxis(
            label_size=40,
        ),
        bottom_axis=fch.ChartAxis(
            label_size=30,
        ),
    )

    def formatear_etiqueta(fecha_hora):
        return fecha_hora.strftime("%H:%M")

    contenedor_grafica = ft.Container(
        height=250,
        width=350,
        content=grafica_ventas,
    )

    #? funcion para actualizar el estado de la grafica
    def actualizar_resumen():

        datos = dao.resumen_ventas_hoy()

        if not datos:
            contenedor_grafica.content = ft.Column(
                controls=[
                    ft.Icon(ft.Icons.SHOW_CHART, size=40, color="#C2355F"),
                    ft.Text(
                        "Sin ventas registradas hoy",
                        color="#5A1026",
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
            page.update()
            return

        contenedor_grafica.content = grafica_ventas

        puntos = []
        etiquetas = []
        valores_ventas = []

        for i, dato in enumerate(datos):
            etiqueta = formatear_etiqueta(dato[0])
            ventas = float(dato[1])

            puntos.append(
                fch.LineChartDataPoint(i, ventas)
            )

            etiquetas.append(
                fch.ChartAxisLabel(
                    value=i,
                    label=ft.Container(
                        content=ft.Text(str(etiqueta), size=10, color="#000000"),
                        padding=5,
                    )
                )
            )

            valores_ventas.append(ventas)

        grafica_ventas.data_series = [
            fch.LineChartData(
                points=puntos,
                curved=True,
                color="#C2355F",
                stroke_width=3,
            )
        ]

        grafica_ventas.bottom_axis.labels = etiquetas
        grafica_ventas.max_x = max(len(puntos) - 1, 1)

        max_venta = max(valores_ventas) if valores_ventas else 0
        max_venta = max_venta if max_venta > 0 else 100

        pasos = 5
        intervalo = max_venta / pasos

        etiquetas_y = []
        for i in range(pasos + 1):
            valor = round(intervalo * i)
            etiquetas_y.append(
                fch.ChartAxisLabel(
                    value=valor,
                    label=ft.Container(
                        content=ft.Text(f"${valor:,.0f}", size=10, color="#000000"),
                        padding=5,
                    )
                )
            )

        grafica_ventas.left_axis.labels = etiquetas_y
        grafica_ventas.max_y = (intervalo * pasos) * 1.15
        grafica_ventas.horizontal_grid_lines.interval = intervalo if intervalo > 0 else 1

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
    actualizar_resumen()
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
                                ],

                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),

                            #? Gráfica
                            ft.Container(
                                expand=True,
                                alignment=ft.Alignment.BOTTOM_CENTER,
                                content=contenedor_grafica,
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