import flet as ft
from DAO.empleado_dao import EmpleadoDAO

def empleados_window(page: ft.Page):

    #? Instancia del DAO
    empleados_dao = EmpleadoDAO()
    registros = empleados_dao.cargar_datos()

    #? Título
    titulo = ft.Text(
        "Empleados",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#5A1026",
    )

    #? Barra de búsqueda
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

    #? Tabla de empleados
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(
                ft.Text("ID", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Nombre", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Apellidos", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Teléfono", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Correo", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Usuario", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Contraseña", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Rol", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
        ],
        rows=[],
        heading_row_color="#C2355F",
        heading_row_height=50,
    )

    #? Agregar registros
    for registro in registros:

        tabla.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(registro[0]), color="#000000")),
                    ft.DataCell(ft.Text(registro[1], color="#000000")),
                    ft.DataCell(ft.Text(registro[2], color="#000000")),
                    ft.DataCell(ft.Text(registro[3], color="#000000")),
                    ft.DataCell(ft.Text(registro[4], color="#000000")),
                    ft.DataCell(ft.Text(registro[5], color="#000000")),
                    ft.DataCell(ft.Text(registro[6], color="#000000")),
                    ft.DataCell(ft.Text(registro[7], color="#000000")),
                ]
            )
        )

    #? Scroll de la tabla
    tablaHorizontal = ft.Row(
        controls=[tabla],
        scroll=ft.ScrollMode.AUTO,
    )

    tablaScroll = ft.Column(
        controls=[tablaHorizontal],
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    #? Botón agregar
    botonAgregar = ft.Container(
        content=ft.ElevatedButton(
            "Agregar empleado",
            bgcolor="#EF82A2",
            color="#000000",
        ),
        alignment=ft.Alignment.CENTER_RIGHT,
        padding=10
    )

    #? Contenido de la vista
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