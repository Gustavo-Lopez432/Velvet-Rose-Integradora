import flet as ft
from DAO.empleado_dao import EmpleadoDAO


def empleados_window(page: ft.Page):

    # ? Instancia del DAO
    empleados_dao = EmpleadoDAO()
    registros = empleados_dao.cargar_datos()

    # ? Encabezado de la ventana
    page.title = "Empleados"
    page.window_width = 1920
    page.window_height = 1080
    page.padding = 0
    page.bgcolor = "#FFFFFF"

    # ? Header
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

    # ? Sidebar del dashboard
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
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(
                            weight=ft.FontWeight.BOLD
                        )
                    )
                ),

                ft.ElevatedButton(
                    "Empleados",
                    bgcolor="#C2355F",
                    color="#000000",
                    width=180,
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

    # ? Título
    titulo = ft.Text(
        "Empleados",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#5A1026"
    )

    # ? Barra de búsqueda
    contenidoBusqueda = ft.Row(
        controls=[
            ft.TextField(
                hint_text="Buscar",
                width=200,
                color="#000000",
            ),
        ],
        alignment=ft.MainAxisAlignment.END
    )

    # ? Tabla de empleados
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(
                ft.Text(
                    "ID",
                    color="#FFFFFF",
                    weight=ft.FontWeight.BOLD
                )
            ),
            ft.DataColumn(
                ft.Text(
                    "Nombre",
                    color="#FFFFFF",
                    weight=ft.FontWeight.BOLD
                )
            ),
            ft.DataColumn(
                ft.Text(
                    "Apellidos",
                    color="#FFFFFF",
                    weight=ft.FontWeight.BOLD
                )
            ),
            ft.DataColumn(
                ft.Text(
                    "Teléfono",
                    color="#FFFFFF",
                    weight=ft.FontWeight.BOLD
                )
            ),
            ft.DataColumn(
                ft.Text(
                    "Correo",
                    color="#FFFFFF",
                    weight=ft.FontWeight.BOLD
                )
            ),
            ft.DataColumn(
                ft.Text(
                    "Usuario",
                    color="#FFFFFF",
                    weight=ft.FontWeight.BOLD
                )
            ),
            ft.DataColumn(
                ft.Text(
                    "Contraseña",
                    color="#FFFFFF",
                    weight=ft.FontWeight.BOLD
                )
            ),
            ft.DataColumn(
                ft.Text(
                    "Rol",
                    color="#FFFFFF",
                    weight=ft.FontWeight.BOLD
                )
            ),
        ],

        rows=[],

        heading_row_color="#C2355F",
        heading_row_height=50,
    )

    # ? Agregar registros
    for registro in registros:

        tabla.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(
                            str(registro[0]),
                            color="#000000"
                        )
                    ),

                    ft.DataCell(
                        ft.Text(
                            registro[1],
                            color="#000000"
                        )
                    ),

                    ft.DataCell(
                        ft.Text(
                            registro[2],
                            color="#000000"
                        )
                    ),

                    ft.DataCell(
                        ft.Text(
                            registro[3],
                            color="#000000"
                        )
                    ),

                    ft.DataCell(
                        ft.Text(
                            registro[4],
                            color="#000000"
                        )
                    ),

                    ft.DataCell(
                        ft.Text(
                            registro[5],
                            color="#000000"
                        )
                    ),

                    ft.DataCell(
                        ft.Text(
                            registro[6],
                            color="#000000"
                        )
                    ),

                    ft.DataCell(
                        ft.Text(
                            registro[7],
                            color="#000000"
                        )
                    ),
                ]
            )
        )

    # ? Scroll horizontal de la tabla
    tablaHorizontal = ft.Row(
        controls=[tabla],
        scroll=ft.ScrollMode.AUTO,
    )

    # ? Scroll vertical de la tabla
    tablaScroll = ft.Column(
        controls=[tablaHorizontal],
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    # ? Botón agregar
    botonAgregar = ft.Container(
        content=ft.ElevatedButton(
            "Agregar empleado",
            bgcolor="#EF82A2",
            color="#000000",
        ),
        alignment=ft.Alignment.CENTER_RIGHT,
        padding=10
    )

    # ? Contenido de la vista
    contenido = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        titulo,
                        ft.Container(expand=True),
                        contenidoBusqueda,
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),

                tablaScroll,

                botonAgregar,
            ],
            spacing=10,
        ),
        padding=30,
        expand=True
    )

    return contenido