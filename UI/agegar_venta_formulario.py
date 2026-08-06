import flet as ft


def agregar_venta_formulario(page: ft.Page):

    page.title = "Registrar venta"
    page.bgcolor = "#F9F3F4"
    page.padding = 0

    productos = [
        "Producto 1",
        "Producto 2",
        "Producto 3",
        "Producto 4",
    ]

    ancho_campo = 170

    producto = ft.Dropdown(
        label="Producto",
        hint_text="Selecciona un producto",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",

        label_style=ft.TextStyle(
            color="#66727C",
            size=16
        ),

        hint_style=ft.TextStyle(
            color="#A8B7C4"
        ),

        border_color="#AEBCC8",
        focused_border_color="#C2355F",

        options=[
            ft.dropdown.Option(producto)
            for producto in productos
        ]
    )

    cantidad = ft.TextField(
        label="Cantidad",
        hint_text="0",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",

        label_style=ft.TextStyle(
            color="#66727C",
            size=16
        ),

        hint_style=ft.TextStyle(
            color="#A8B7C4"
        ),

        border_color="#AEBCC8",
        focused_border_color="#C2355F",

        keyboard_type=ft.KeyboardType.NUMBER
    )

    precio = ft.TextField(
        label="Precio",
        hint_text="$0.00",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",

        label_style=ft.TextStyle(
            color="#66727C",
            size=16
        ),

        hint_style=ft.TextStyle(
            color="#A8B7C4"
        ),

        border_color="#AEBCC8",
        focused_border_color="#C2355F",

        keyboard_type=ft.KeyboardType.NUMBER
    )

    total = ft.TextField(
        label="Total",
        hint_text="$0.00",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",

        label_style=ft.TextStyle(
            color="#66727C",
            size=16
        ),

        hint_style=ft.TextStyle(
            color="#A8B7C4"
        ),

        border_color="#AEBCC8",
        focused_border_color="#C2355F",

        read_only=True
    )

    titulo = ft.Text(
        "Registre una venta",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#5A1026"
    )

    btn_agregar = ft.ElevatedButton(
        "Agregar",
        icon=ft.Icons.ADD_CIRCLE_OUTLINE,
        width=130,
        height=40,
        bgcolor="#E96791",
        color="#FFFFFF"
    )

    btn_cancelar = ft.ElevatedButton(
        "Cancelar",
        icon=ft.Icons.CANCEL_OUTLINED,
        width=130,
        height=40,
        bgcolor="#E96791",
        color="#FFFFFF"
    )

    fila_1 = ft.Row(
        controls=[
            producto,
            cantidad,
            precio
        ],

        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

        width=550
    )

    fila_2 = ft.Row(
        controls=[
            ft.Container(
                width=ancho_campo
            ),

            total,

            ft.Container(
                width=ancho_campo
            )
        ],

        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

        width=550
    )

    botones = ft.Row(
        controls=[
            btn_agregar,
            btn_cancelar
        ],

        alignment=ft.MainAxisAlignment.END,

        spacing=22,

        width=550
    )

    formulario = ft.Container(
        width=650,
        height=430,

        border=ft.Border.all(
            1,
            "#E5A1B4"
        ),

        bgcolor="#FDF5F6",

        padding=25,

        content=ft.Column(
            controls=[

                # Título
                titulo,

                # Producto / Cantidad / Precio
                fila_1,

                # Total
                fila_2,

                # Espacio
                ft.Container(
                    expand=True
                ),

                # Botones
                botones
            ],

            spacing=18,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    layout = ft.Container(
        content=formulario,
        expand=True,
        alignment=ft.Alignment.CENTER
    )

    return layout