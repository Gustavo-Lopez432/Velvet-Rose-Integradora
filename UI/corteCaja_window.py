import flet as ft
from DAO.corte_caja_dao import CorteCajaDAO


def corte_caja_window(page: ft.Page, actualizar_vista=None):

    corte_caja_dao = CorteCajaDAO()

    titulo = ft.Text(
        "Corte de caja",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#5A1026",
    )

    #? Área donde se pinta el resultado, vacía hasta que se genere el corte
    resultado = ft.Column(
        controls=[],
        spacing=10,
    )

    def generar_corte(e):
        num_ventas, subtotal, iva, total = corte_caja_dao.obtener_corte_dia()

        tarjeta = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Corte del día de hoy", size=20, weight=ft.FontWeight.BOLD, color="#000000"),
                    ft.Divider(color="#E5A1B4"),
                    ft.Text(f"Ventas realizadas: {num_ventas}", size=16, color="#000000"),
                    ft.Text(f"Subtotal: ${float(subtotal):,.2f}", size=16, color="#000000"),
                    ft.Text(f"IVA: ${float(iva):,.2f}", size=16, color="#000000"),
                    ft.Text(f"Total: ${float(total):,.2f}", size=22, weight=ft.FontWeight.BOLD, color="#5A1026"),
                ],
                spacing=8,
            ),
            width=400,
            padding=25,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            border=ft.Border.all(3, "#EF82A2"),
        )

        resultado.controls = [tarjeta]
        page.update()

    boton_generar = ft.ElevatedButton(
        "Generar corte de caja",
        icon=ft.Icons.POINT_OF_SALE,
        bgcolor="#EF82A2",
        color="#000000",
        height=45,
        on_click=generar_corte,
    )

    contenido = ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                boton_generar,
                resultado,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=30,
        expand=True,
    )

    return contenido