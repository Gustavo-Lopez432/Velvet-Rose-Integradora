import flet as ft

def ventas_window(page: ft.Page):

    #? encabezado de la ventana
    page.title = "Ventas"
    page.window_width = 1920
    page.window_height = 1080
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
                    bgcolor="#EF82A2",
                    color="#000000",
                    width=180,
                    style=ft.ButtonStyle(text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
                ),
                
                ft.ElevatedButton(
                    "Ventas",
                    bgcolor="#C2355F",
                    color="#FFFFFF",
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
    contenidoTabla = ft.Container(
        ft.DataTable(
            columns=[
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("ID", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("Fecha", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("Folio", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("ID del empleado", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("Subtotal", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("IVA", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("Total", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("1", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("28/07/2026", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("VBN323", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("1", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("30", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("16%", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("34.8", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                    ]
                )
            ],
            column_spacing=1,
            horizontal_lines=None,
            border=None
        ),
        alignment=ft.Alignment.CENTER
    )

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
                contenidoTabla,
                botonAgregar,
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

ft.app(target=ventas_window)