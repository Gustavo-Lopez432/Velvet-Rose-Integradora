import flet as ft
from DAO.producto_dao import ProductoDAO
from UI.agregar_producto_formulario import productos_window_formulario

def productos_window(page: ft.Page, actualizar_vista):

    #? Instancia del DAO
    producto_dao = ProductoDAO()
    registros = producto_dao.cargar_datos()

    campoBusqueda = ft.TextField(
        hint_text="Buscar",
        width=200,
        color="#000000",
    )

    #? Diálogo de confirmación para eliminar
    dialogo_confirmar = ft.AlertDialog(
        modal=True,
        title=ft.Text("Eliminar producto"),
        content=ft.Text("¿Seguro que quieres eliminar este producto? Esta acción no se puede deshacer."),
    )

    def cerrar_dialogo():
        dialogo_confirmar.open = False
        page.update()

    def confirmar_eliminar(id_producto):
        def eliminar_confirmado(e):
            try:
                producto_dao.delete(id_producto)
                cerrar_dialogo()
                actualizar_vista(productos_window(page, actualizar_vista))
            except Exception as ex:
                cerrar_dialogo()
                snack = ft.SnackBar(
                    content=ft.Text("No se puede eliminar: este producto ya tiene ventas registradas."),
                    bgcolor="#C62828",
                )
                page.overlay.append(snack)
                snack.open = True
                page.update()

        dialogo_confirmar.actions = [
            ft.TextButton("Cancelar", on_click=lambda e: cerrar_dialogo()),
            ft.TextButton("Eliminar", on_click=eliminar_confirmado),
        ]
        dialogo_confirmar.open = True
        page.overlay.append(dialogo_confirmar)
        page.update()

    #? Editar producto
    def editar_producto(e, id_producto):
        actualizar_vista(
            productos_window_formulario(
                page,
                lambda: actualizar_vista(
                    productos_window(page, actualizar_vista)
                ),
                id_producto
            )
        )

    #? Función para construir filas a partir de una lista de registros
    def construir_filas(lista_registros):
        filas = []

        for r in lista_registros:
            id_producto = r[0]

            filas.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(r[0]), color="#000000")),      # ID
                        ft.DataCell(ft.Text(r[1], color="#000000")),           # Código de barras
                        ft.DataCell(ft.Text(r[2], color="#000000")),           # Nombre
                        ft.DataCell(ft.Text(r[3], color="#000000")),           # Marca
                        ft.DataCell(ft.Text(r[4], color="#000000")),           # Talla
                        ft.DataCell(ft.Text(r[5], color="#000000")),           # Color
                        ft.DataCell(ft.Text(f"${float(r[7]):,.2f}", color="#000000")),  # Precio
                        ft.DataCell(ft.Text(str(r[9]), color="#000000")),      # Existencia
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,
                                        icon_color="#5A1026",
                                        tooltip="Editar",
                                        on_click=lambda e, id=id_producto: editar_producto(e, id),
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.DELETE_OUTLINE,
                                        icon_color="#C2355F",
                                        tooltip="Eliminar",
                                        on_click=lambda e, id=id_producto: confirmar_eliminar(id),
                                    ),
                                ],
                                spacing=0,
                            )
                        ),
                    ]
                )
            )

        return filas

    #? Título
    titulo = ft.Text(
        "Productos",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#5A1026",
    )

    #? Barra de búsqueda
    contenidoBusqueda = ft.Row(
        controls=[campoBusqueda],
        alignment=ft.MainAxisAlignment.END
    )

    #? Tabla de productos
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Código de barras", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Nombre", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Marca", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Talla", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Color", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Precio", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Existencia", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Acción", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
        ],
        rows=[],
        heading_row_color="#C2355F",
        heading_row_height=50,
    )

    #? Filtrado según texto de búsqueda
    def buscar_productos(e):
        texto = e.control.value.strip().lower()
        if texto == "":
            filtrados = registros
        else:
            filtrados = [
                r for r in registros
                if texto in str(r[1]).lower()
                or texto in str(r[2]).lower()
                or texto in str(r[3]).lower()
            ]
        tabla.rows = construir_filas(filtrados)
        page.update()

    campoBusqueda.on_change = buscar_productos

    #? Agregar registros
    tabla.rows = construir_filas(registros)

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
            "Agregar producto",
            bgcolor="#EF82A2",
            color="#000000",
            on_click=lambda e: actualizar_vista(
                productos_window_formulario(
                    page,
                    lambda: actualizar_vista(
                        productos_window(page, actualizar_vista)
                    )
                )
            )
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