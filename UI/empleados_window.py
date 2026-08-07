import flet as ft
from DAO.empleado_dao import EmpleadoDAO
from UI.agregar_empleado_formulario import empleados_window_formulario


def empleados_window(page: ft.Page, actualizar_vista):

    # ? Instancia del DAO
    empleados_dao = EmpleadoDAO()
    registros = empleados_dao.cargar_datos()

    # ? Encabezado de la ventana
    page.title = "Empleados"
    page.window_width = 1920
    page.window_height = 1080
    page.padding = 0
    page.bgcolor = "#FFFFFF"

    campoBusqueda = ft.TextField(
        hint_text="Buscar",
        width=200,
        color="#000000",
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
        controls=[campoBusqueda],
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
            ft.DataColumn(
                ft.Text(
                    "Acción",
                    color="#FFFFFF",
                    weight=ft.FontWeight.BOLD
                )
            ),
        ],

        rows=[],

        heading_row_color="#C2355F",
        heading_row_height=50,
    )

    #? Editar empleado
    def editar_empleado(e, id_empleado):
        actualizar_vista(
            empleados_window_formulario(
                page,
                lambda: actualizar_vista(
                    empleados_window(page, actualizar_vista)
                ),
                id_empleado
            )
        )

    #? Desactivar empleado
    def desactivar_empleado(e, id_empleado):
        empleados_dao.cambiar_estado(id_empleado, "Inactivo")
        actualizar_vista(
            empleados_window(page, actualizar_vista)
        )

    #? Función para construir filas a partir de una lista de registros
    def construir_filas(lista_registros):
        filas = []

        for r in lista_registros:
            id_empleado = r[0]

            filas.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(r[0]), color="#000000")),
                        ft.DataCell(ft.Text(r[1], color="#000000")),
                        ft.DataCell(ft.Text(r[2], color="#000000")),
                        ft.DataCell(ft.Text(r[3], color="#000000")),
                        ft.DataCell(ft.Text(r[4], color="#000000")),
                        ft.DataCell(ft.Text(r[5], color="#000000")),
                        ft.DataCell(ft.Text(r[6], color="#000000")),
                        ft.DataCell(ft.Text(r[7], color="#000000")),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,
                                        icon_color="#5A1026",
                                        tooltip="Editar",
                                        on_click=lambda e, id=id_empleado: editar_empleado(e, id),
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.PERSON_OFF,
                                        icon_color="#C2355F",
                                        tooltip="Desactivar",
                                        on_click=lambda e, id=id_empleado: desactivar_empleado(e, id),
                                    ),
                                ],
                                spacing=0,
                            )
                        ),
                    ]
                )
            )

        return filas

    #? Filtrado según texto de búsqueda (nombre, apellidos, usuario)
    def buscar_empleados(e):
        texto = e.control.value.strip().lower()
        if texto == "":
            filtrados = registros
        else:
            filtrados = [
                r for r in registros
                if texto in str(r[1]).lower()   # nombre
                or texto in str(r[2]).lower()   # apellidos
                or texto in str(r[5]).lower()   # usuario
            ]
        tabla.rows = construir_filas(filtrados)
        page.update()

    campoBusqueda.on_change = buscar_empleados

    # ? Agregar registros
    tabla.rows = construir_filas(registros)

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
            on_click=lambda e: actualizar_vista(
                empleados_window_formulario(
                    page,
                    lambda: actualizar_vista (
                        empleados_window(page, actualizar_vista)
                    )
                )
            )
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