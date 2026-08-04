import flet as ft
from DAO.venta_dao import VentaDAO

def ventas_window(page: ft.Page):

    #? instacias de los objetos 
    venta_dao = VentaDAO()
    registros = venta_dao.cargar_datos()


    #? encabezado de la ventana
    page.title = "Ventas"
    page.window.full_screen = True
    page.padding = 0
    page.bgcolor = "#FFFFFF"

    #? titulo y subtitulo del contenido principal
    titulo = ft.Container(
        content=ft.Text(
            "Ventas",
            size=30,
            weight=ft.FontWeight.BOLD,
            color="#5A1026",
        ),
        height=120,
        width=200,
    )

    #?barra de busqueda y dropdown
    contenidoBusqueda = ft.Row(
        controls=[
            ft.TextField(
                hint_text="Buscar",
                width=200,
                height=120,
                color="#000000",
            ),
            ft.Dropdown(
                width=200,
                height=120,
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
        spacing=10,
        alignment=ft.MainAxisAlignment.END
    )

    #?tabla de ventas
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Fecha", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Folio", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Empleado", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Subtotal", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("IVA", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Total", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
        ],

        rows=[],
        heading_row_color="#C2355F",
        heading_row_height=50,
    )

    for registro in registros:
        tabla.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(registro[0]), color="#000000")),
                    ft.DataCell(ft.Text(registro[1], color="#000000")),
                    ft.DataCell(ft.Text(str(registro[2]), color="#000000")),
                    ft.DataCell(ft.Text(registro[3], color="#000000")),
                    ft.DataCell(ft.Text(str(registro[4]), color="#000000")),
                    ft.DataCell(ft.Text(str(registro[5]), color="#000000")),
                    ft.DataCell(ft.Text(str(registro[6]), color="#000000")),
                ]
            )
        )

    tablaHorizontal = ft.Row (
        controls=[
            tabla
        ],
        scroll=ft.ScrollMode.AUTO,
    )

    tablaScroll = ft.Column(
        controls=[
            tablaHorizontal
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    contenedorTabla = ft.Container(
        content=tablaScroll,
        expand=True
    )

    #? boton para agragar mas ventas
    botonAgregar = ft.Container(
        content=ft.ElevatedButton(
            "Agregar venta",
            bgcolor="#EF82A2",
            color="#000000",
        ),
        alignment=ft.Alignment.CENTER_RIGHT,
        padding=ft.Padding.all(10)
    )

    #? contenido principal del layout (SIN header)
    contenido = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        titulo,
                        ft.Container(expand=True),
                        contenidoBusqueda,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                contenedorTabla,
                botonAgregar,
            ],
            spacing=10
        ),
        padding=30,
        expand=True
    )

    #? Row con sidebar y contenido (SIN header)
    layout_interno = ft.Row(
        controls=[contenido],
        expand=True
    )

    #? Layout final: header arriba, row abajo
    layout = ft.Column(
        controls=[
            layout_interno
        ],
        spacing=0,
        expand=True
    )
    
    return layout