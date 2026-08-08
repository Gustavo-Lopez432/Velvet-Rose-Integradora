import flet as ft
from DAO.venta_dao import VentaDAO
from UI.agegar_venta_formulario import agregar_venta_formulario
from DAO.detalle_venta_dao import DetalleVentaDAO

def ventas_window(page: ft.Page, actualizar_vista):

    #? Instancia del DAO
    venta_dao = VentaDAO()
    registros = venta_dao.cargar_datos()
    detalle_venta_dao = DetalleVentaDAO()

    #? Título
    titulo = ft.Text(
        "Ventas",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#5A1026",
    )

    #? Barra de búsqueda y filtro
    campoBusqueda = ft.TextField(
        hint_text="Buscar por empleado o fecha",
        width=250,
        color="#000000",
    )

    contenidoBusqueda = ft.Row(
        controls=[
            campoBusqueda,

        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.END
    )

    #? Tabla de ventas
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(
                ft.Text("ID", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Fecha", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Folio", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Empleado", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Subtotal", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("IVA", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Total", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text("Acción", color="#FFFFFF", weight=ft.FontWeight.BOLD)
            ),
        ],
        rows=[],
        heading_row_color="#C2355F",
        heading_row_height=50,
    )


    #? Diálogo de confirmación para eliminar
    dialogo_confirmar = ft.AlertDialog(
        modal=True,
        title=ft.Text("Eliminar venta"),
        content=ft.Text("¿Seguro que quieres eliminar esta venta? Esta acción no se puede deshacer."),
    )

    def cerrar_dialogo():
        dialogo_confirmar.open = False
        page.update()

    def confirmar_eliminar(id_venta):
        def eliminar_confirmado(e):
            detalles = detalle_venta_dao.cargar_datos(id_venta)
            for detalle in detalles:
                detalle_venta_dao.delete(detalle[0])  # detalle[0] es el id del detalle

            venta_dao.delete(id_venta)
            cerrar_dialogo()
            actualizar_vista(ventas_window(page, actualizar_vista))

        dialogo_confirmar.actions = [
            ft.TextButton("Cancelar", on_click=lambda e: cerrar_dialogo()),
            ft.TextButton("Eliminar", on_click=eliminar_confirmado),
        ]
        dialogo_confirmar.open = True
        page.overlay.append(dialogo_confirmar)
        page.update()

    #? Función para construir filas a partir de una lista de registros
    def construir_filas(lista_registros):
        filas = []

        for registro in lista_registros:
            id_venta = registro[0]

            filas.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(registro[0]), color="#000000")),
                        ft.DataCell(ft.Text(registro[1], color="#000000")),
                        ft.DataCell(ft.Text(str(registro[2]), color="#000000")),
                        ft.DataCell(ft.Text(registro[3], color="#000000")),
                        ft.DataCell(ft.Text(str(registro[4]), color="#000000")),
                        ft.DataCell(ft.Text(str(registro[5]), color="#000000")),
                        ft.DataCell(ft.Text(str(registro[6]), color="#000000")),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_color="#C2355F",
                                tooltip="Eliminar venta",
                                on_click=lambda e, id=id_venta: confirmar_eliminar(id),
                            )
                        ),
                    ]
                )
            )

        return filas

    #? Filtrado según texto de búsqueda (empleado o fecha)
    def buscar_ventas(e):
        texto = e.control.value.strip().lower()
        if texto == "":
            filtrados = registros
        else:
            filtrados = [
                r for r in registros
                if texto in str(r[3]).lower()   # empleado
                or texto in str(r[1]).lower()   # fecha
            ]
        tabla.rows = construir_filas(filtrados)
        page.update()

    campoBusqueda.on_change = buscar_ventas

    #? Agregar registros a la tabla
    tabla.rows = construir_filas(registros)

    #? Scroll horizontal y vertical de la tabla
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
            "Agregar venta",
            bgcolor="#EF82A2",
            color="#000000",
            on_click=lambda e: actualizar_vista(
                agregar_venta_formulario(
                    page,
                    lambda: actualizar_vista(
                        ventas_window(page, actualizar_vista)
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