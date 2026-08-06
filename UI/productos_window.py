import flet as ft
from DAO.producto_dao import ProductoDAO
from UI.agregar_producto_formulario import productos_window_formulario


def productos_window(page: ft.Page, actualizar_vista):

    #? Instancia del DAO
    producto_dao = ProductoDAO()
    registros = producto_dao.cargar_datos()

    #? Título
    titulo = ft.Text(
        "Productos",
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

    #? Tabla de productos
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Código de barras", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Nombre", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Marca", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Talla", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Color", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Imagen", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Precio", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Proveedor", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Existencia", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Max stock", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Min stock", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
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
                    ft.DataCell(ft.Text(str(registro[7]), color="#000000")),
                    ft.DataCell(ft.Text(registro[8], color="#000000")),
                    ft.DataCell(ft.Text(str(registro[9]), color="#000000")),
                    ft.DataCell(ft.Text(str(registro[10]), color="#000000")),
                    ft.DataCell(ft.Text(str(registro[11]), color="#000000")),
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