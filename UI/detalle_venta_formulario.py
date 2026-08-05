import flet as ft

def main(page: ft.Page):
    page.title = "Formulario de Detalle de Venta"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 600
    page.window_height = 650
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # Campos del formulario
    id_venta = ft.TextField(
        label="ID de Venta",
        hint_text="Ingresa el ID de la venta",
        width=400,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    id_producto = ft.TextField(
        label="ID del Producto",
        hint_text="Ingresa el ID del producto",
        width=400,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    cantidad = ft.TextField(
        label="Cantidad",
        hint_text="Ingresa la cantidad",
        width=400,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    precio_unitario = ft.TextField(
        label="Precio Unitario",
        hint_text="0.00",
        width=400,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    subtotal = ft.TextField(
        label="Subtotal",
        hint_text="0.00",
        width=400,
        keyboard_type=ft.KeyboardType.NUMBER,
        read_only=True,
    )

    # Botones
    btn_guardar = ft.ElevatedButton(
        "Guardar",
        icon=ft.Icons.SAVE,
        width=150,
    )

    btn_limpiar = ft.OutlinedButton(
        "Limpiar",
        icon=ft.Icons.CLEAR,
        width=150,
    )

    btn_cancelar = ft.OutlinedButton(
        "Cancelar",
        icon=ft.Icons.CLOSE,
        width=150,
    )

    # Contenedor del formulario
    formulario = ft.Container(
        content=ft.Column(
            [
                ft.Text("Detalle de Venta", size=28, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20),
                id_venta,
                id_producto,
                cantidad,
                precio_unitario,
                subtotal,
                ft.Divider(height=20),
                ft.Row(
                    [btn_guardar, btn_limpiar, btn_cancelar],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,
                ),
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=30,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.Colors.GREY_400,
        ),
    )

    page.add(formulario)

ft.app(target=main)