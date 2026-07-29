import flet as ft

def dashboard(page: ft.Page):

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
                ft.Text(""),
                ft.Text(
                    "Velvet Rose",
                    size=30,
                    color="#FFFFFF"
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
                    "Usuarios",
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
                    "Productos",
                    bgcolor="#EF82A2",
                    color="#000000",
                    width=180,
                    style=ft.ButtonStyle(text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
                ),
                                
                ft.ElevatedButton(
                    "Usuarios",
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
                    height=140, 
                    expand=True, 
                    blur = 10,
                    border=ft.Border.all(2, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text("Ventas de hoy", color="#5A1026", weight=ft.FontWeight.BOLD, align=ft.Alignment.CENTER),
                            ft.Divider(color="#C2355F"),
                            ft.Text(),
                            ft.Text(),
                            ft.Divider(color="#C2355F"),
                        ]
                    )
                ),

                ft.Container(
                    bgcolor="#D8A7B1", 
                    height=140, 
                    expand=True, 
                    blur = 10,
                    border=ft.Border.all(2, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text ("Productos", color="#5A1026", weight=ft.FontWeight.BOLD, align=ft.Alignment.CENTER),
                            ft.Divider(color="#C2355F"),
                            ft.Text (""),
                            ft.Text (""),
                            ft.Divider(color="#C2355F"),
                        ]
                    )
                ),

                ft.Container(
                    bgcolor="#D8A7B1", 
                    height=140, 
                    expand=True,
                    blur = 10,
                    border=ft.Border.all(2, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text("Stock Bajo", color="#5A1026", weight=ft.FontWeight.BOLD, align=ft.Alignment.CENTER),
                            ft.Divider(color="#C2355F"),
                            ft.Text(""),
                            ft.Text(""),
                            ft.Divider(color="#C2355F"),
                        ]
                    )
                ),

                ft.Container(
                    bgcolor="#D8A7B1", 
                    height=140, 
                    expand=True, 
                    blur = 10,
                    border=ft.Border.all(2, "#5A1026"),
                    content=ft.Column(
                        controls=[
                            ft.Text("Total en caja", color="#5A1026", weight=ft.FontWeight.BOLD, align=ft.Alignment.CENTER),
                            ft.Divider(color="#C2355F"),
                            ft.Text(""),
                            ft.Text(""),
                            ft.Divider(color="#C2355F"),
                        ]
                    )
                ),
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
                    bgcolor = "#fff000"
                )
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