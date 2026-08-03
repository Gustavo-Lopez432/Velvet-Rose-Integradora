import flet as ft

def ventas_window(page: ft.Page):

    #? encabezado de la ventana
    page.title = "Productos"
    page.window_width = 1920
    page.window_height = 1080
    page.padding = 0
    page.bgcolor = "#FFFFFF"

    #? titulo y subtitulo del contenido principal
    titulo = ft.Container(
        content=ft.Text(
            "Productos",
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
                    bgcolor="#EF82A2",
                    color="#000000",
                    width=180,
                    style=ft.ButtonStyle(text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
                ),
                
                ft.ElevatedButton(
                    "Productos",
                    bgcolor="#C2355F",
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
                        content=ft.Text("CODIGO DE BARRAS", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("MARCA", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("TALLA", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("COLOR", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("PRECIO", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("EXISTENCIA", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("STOCK", color="#FFFFFF"),
                        width=120,
                        height=50,
                        bgcolor="#C2355F",
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.all(5)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("IMAGEN", color="#FFFFFF"),
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
                                content=ft.Text("4684523", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("Iluion", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("M", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("Rosa", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("$40", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("Si", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text("20", color="#000000"),
                                width=120,
                                height=50,
                                alignment=ft.Alignment.CENTER,
                                padding=ft.Padding.all(5)
                            )
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Text(),
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
            "Agregar producto",
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