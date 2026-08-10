import flet as ft
from DAO.corte_caja_dao import CorteCajaDAO


def corte_caja_window(page: ft.Page, actualizar_vista, id_empleado):

    corte_caja_dao = CorteCajaDAO()

    def es_decimal_valido(valor):
        if valor is None or not valor.strip():
            return False
        try:
            float(valor)
            return True
        except ValueError:
            return False

    def recargar():
        actualizar_vista(corte_caja_window(page, actualizar_vista, id_empleado))

    titulo = ft.Text(
        "Corte de caja",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#5A1026",
    )

    #? ===================== Historial de cortes (tabla) =====================
    dialogo_confirmar = ft.AlertDialog(
        modal=True,
        title=ft.Text("Eliminar corte"),
        content=ft.Text("¿Seguro que quieres eliminar este corte de caja? Esta acción no se puede deshacer."),
    )
    page.overlay.append(dialogo_confirmar)

    def cerrar_dialogo():
        dialogo_confirmar.open = False
        page.update()

    def confirmar_eliminar(id_corte):
        def eliminar_confirmado(e):
            corte_caja_dao.delete(id_corte)
            cerrar_dialogo()
            recargar()

        dialogo_confirmar.actions = [
            ft.TextButton("Cancelar", on_click=lambda e: cerrar_dialogo()),
            ft.TextButton("Eliminar", on_click=eliminar_confirmado),
        ]
        dialogo_confirmar.open = True
        page.update()

    def construir_tabla_historial():
        registros = corte_caja_dao.cargar_datos()

        filas = []
        for id_c, fecha_c, apertura_c, cierre_c, m_inicial, m_final, empleado_c, total_c in registros:
            filas.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(fecha_c), color="#000000")),
                    ft.DataCell(ft.Text(str(apertura_c), color="#000000")),
                    ft.DataCell(ft.Text(str(cierre_c) if cierre_c else "Turno abierto", color="#000000")),
                    ft.DataCell(ft.Text(f"${float(m_inicial):,.2f}", color="#000000")),
                    ft.DataCell(ft.Text(f"${float(m_final):,.2f}" if m_final is not None else "-", color="#000000")),
                    ft.DataCell(ft.Text(str(empleado_c), color="#000000")),
                    ft.DataCell(ft.Text(f"${float(total_c):,.2f}" if total_c is not None else "-", color="#000000")),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            icon_color="#C62828",
                            tooltip="Eliminar corte",
                            on_click=lambda e, id_corte=id_c: confirmar_eliminar(id_corte),
                        )
                    ),
                ])
            )

        tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(c, color="#FFFFFF", weight=ft.FontWeight.BOLD))
                for c in ["Fecha", "Apertura", "Cierre", "Monto inicial", "Monto final", "Empleado", "Total ventas", "Acciones"]
            ],
            rows=filas,
            heading_row_color="#C2355F",
            heading_row_height=45,
            column_spacing=25,
        )

        contenido_tabla = tabla if filas else ft.Text("Aún no hay cortes registrados.", color="#66727C")

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Historial de cortes", size=18, weight=ft.FontWeight.BOLD, color="#000000"),
                    ft.Row(controls=[contenido_tabla], scroll=ft.ScrollMode.AUTO),
                ],
                spacing=10,
            ),
            width=900,
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            border=ft.Border.all(3, "#EF82A2"),
        )

    corte_abierto = corte_caja_dao.obtener_corte_abierto(id_empleado)

    #? ===================== NO HAY TURNO ABIERTO: mostrar botón de apertura =====================
    if corte_abierto is None:

        mensaje_apertura = ft.Text("", color=ft.Colors.RED)

        def abrir_turno(e):
            corte_caja_dao.abrir_turno(id_empleado, monto_inicial=0)
            recargar()

        tarjeta = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("No tienes un turno abierto", size=20, weight=ft.FontWeight.BOLD, color="#000000"),
                    ft.Text(
                        "Abre un turno para empezar a registrar tu corte de caja del día.",
                        color="#66727C",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.ElevatedButton(
                        "Abrir turno",
                        icon=ft.Icons.LOCK_OPEN,
                        bgcolor="#EF82A2",
                        color="#000000",
                        height=45,
                        width=250,
                        on_click=abrir_turno,
                    ),
                    mensaje_apertura,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=16,
            ),
            width=450,
            padding=30,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            border=ft.Border.all(3, "#EF82A2"),
        )

        return ft.Container(
            content=ft.Column(
                controls=[titulo, tarjeta, construir_tabla_historial()],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=30,
            expand=True,
        )

    #? ===================== HAY TURNO ABIERTO: mostrar info + opción de cerrar =====================
    id_corte, fecha, hora_apertura, hora_cierre, monto_inicial, monto_final, _ = corte_abierto

    num_ventas, total_ventas = corte_caja_dao.ventas_del_dia_empleado(id_empleado)
    monto_inicial = float(monto_inicial)
    total_ventas = float(total_ventas)
    total_esperado = monto_inicial + total_ventas

    mensaje = ft.Text("", color=ft.Colors.RED)

    efectivo_contado = ft.TextField(
        label="Efectivo contado en caja",
        hint_text="$0.00",
        width=250,
        color="#000000",
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    def limpiar_mensaje(e=None):
        if mensaje.value:
            mensaje.value = ""
            page.update()

    efectivo_contado.on_change = limpiar_mensaje

    #? Se muestra solo después de dar clic en "Cerrar turno"
    seccion_cierre = ft.Column(controls=[], spacing=16, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def mostrar_captura_cierre(e):
        seccion_cierre.controls = [
            efectivo_contado,
            ft.ElevatedButton(
                "Confirmar cierre",
                icon=ft.Icons.LOCK,
                bgcolor="#EF82A2",
                color="#000000",
                height=45,
                width=250,
                on_click=confirmar_cierre,
            ),
            mensaje,
        ]
        page.update()

    def confirmar_cierre(e):
        if not es_decimal_valido(efectivo_contado.value):
            mensaje.value = "Ingresa un monto válido"
            mensaje.color = ft.Colors.RED
            page.update()
            return

        contado = float(efectivo_contado.value)
        corte_caja_dao.cerrar_turno(id_corte, contado)

        diferencia = contado - total_esperado

        if abs(diferencia) < 0.01:
            texto_resultado = "Turno cerrado. La caja cuadra perfectamente."
            color_resultado = ft.Colors.GREEN
        elif diferencia > 0:
            texto_resultado = f"Turno cerrado. Sobran ${diferencia:,.2f} en caja."
            color_resultado = "#C62828"
        else:
            texto_resultado = f"Turno cerrado. Faltan ${abs(diferencia):,.2f} en caja."
            color_resultado = "#C62828"

        mensaje.value = texto_resultado
        mensaje.color = color_resultado
        seccion_cierre.controls = [mensaje]
        page.update()

    tarjeta = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Turno abierto", size=20, weight=ft.FontWeight.BOLD, color="#000000"),
                ft.Divider(color="#E5A1B4"),
                ft.Text(f"Fecha: {fecha}", size=16, color="#000000"),
                ft.Text(f"Hora de apertura: {hora_apertura}", size=16, color="#000000"),
                ft.Text(f"Monto inicial: ${monto_inicial:,.2f}", size=16, color="#000000"),
                ft.Text(f"Ventas del día: {num_ventas} (${total_ventas:,.2f})", size=16, color="#000000"),
                ft.Text(f"Efectivo esperado en caja: ${total_esperado:,.2f}", size=18, weight=ft.FontWeight.BOLD, color="#5A1026"),
                ft.Divider(color="#E5A1B4"),
                ft.ElevatedButton(
                    "Cerrar turno",
                    icon=ft.Icons.LOCK_OUTLINE,
                    bgcolor="#EF82A2",
                    color="#000000",
                    height=45,
                    width=250,
                    on_click=mostrar_captura_cierre,
                ),
                seccion_cierre,
            ],
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=450,
        padding=30,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        border=ft.Border.all(3, "#EF82A2"),
    )

    return ft.Container(
        content=ft.Column(
            controls=[titulo, tarjeta, construir_tabla_historial()],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=30,
        expand=True,
    )