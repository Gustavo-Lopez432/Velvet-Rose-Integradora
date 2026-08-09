import flet as ft
from DAO.reportes_dao import ReportesDAO


def reportes_window(page: ft.Page, actualizar_vista=None):

    reportes_dao = ReportesDAO()

    titulo = ft.Text(
        "Reportes",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#5A1026",
    )

    #? Área donde se pintan las tres tablas, vacía hasta que se generen
    resultado = ft.Column(
        controls=[],
        spacing=25,
    )

    def construir_tabla(columnas, filas):
        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(c, color="#FFFFFF", weight=ft.FontWeight.BOLD))
                for c in columnas
            ],
            rows=filas,
            heading_row_color="#EF82A2",
            heading_row_height=45,
            column_spacing=30,
        )

    def generar_reporte(e):

        #? --- Ventas por fecha (últimos 30 días) ---
        ventas_fecha = reportes_dao.ventas_por_rango(30)
        filas_ventas_fecha = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(dia), color="#000000")),
                ft.DataCell(ft.Text(str(num_ventas), color="#000000")),
                ft.DataCell(ft.Text(f"${float(total):,.2f}", color="#000000")),
            ])
            for dia, num_ventas, total in ventas_fecha
        ]

        #? --- Productos más vendidos ---
        top_productos = reportes_dao.productos_mas_vendidos()
        filas_top_productos = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(nombre), color="#000000")),
                ft.DataCell(ft.Text(str(total_vendido), color="#000000")),
            ])
            for nombre, total_vendido in top_productos
        ]

        #? --- Ventas por empleado ---
        ventas_empleado = reportes_dao.ventas_por_empleado()
        filas_ventas_empleado = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(empleado), color="#000000")),
                ft.DataCell(ft.Text(str(num_ventas), color="#000000")),
                ft.DataCell(ft.Text(f"${float(total):,.2f}", color="#000000")),
            ])
            for empleado, num_ventas, total in ventas_empleado
        ]

        def seccion(titulo_seccion, tabla, mensaje_vacio):
            contenido_tabla = tabla if tabla.rows else ft.Text(mensaje_vacio, color="#66727C")
            return ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(titulo_seccion, size=18, weight=ft.FontWeight.BOLD, color="#000000"),
                        ft.Row(controls=[contenido_tabla], scroll=ft.ScrollMode.AUTO),
                    ],
                    spacing=10,
                ),
                width=850,
                padding=20,
                bgcolor=ft.Colors.WHITE,
                border_radius=15,
                border=ft.Border.all(3, "#EF82A2"),
            )

        resultado.controls = [
            seccion(
                "Ventas de los últimos 30 días",
                construir_tabla(["Día", "Ventas", "Total"], filas_ventas_fecha),
                "No hay ventas registradas en los últimos 30 días."
            ),
            seccion(
                "Productos más vendidos",
                construir_tabla(["Producto", "Piezas vendidas"], filas_top_productos),
                "Aún no hay ventas con detalle registrado."
            ),
            seccion(
                "Ventas por empleado",
                construir_tabla(["Empleado", "Ventas", "Total"], filas_ventas_empleado),
                "No hay empleados registrados."
            ),
        ]
        page.update()

    boton_generar = ft.ElevatedButton(
        "Generar reporte",
        icon=ft.Icons.BAR_CHART,
        bgcolor="#EF82A2",
        color="#000000",
        height=45,
        on_click=generar_reporte,
    )

    contenido = ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                boton_generar,
                ft.Column(
                    controls=[resultado],
                    scroll=ft.ScrollMode.AUTO,
                    expand=True,
                ),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        padding=30,
        expand=True,
    )

    return contenido