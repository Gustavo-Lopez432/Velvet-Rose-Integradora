import flet as ft


def agregar_venta_formulario(page: ft.Page):

    #? Configuración
    page.title = "Registrar venta"

    #? Datos de ejemplo
    productos = [
        "Producto 1",
        "Producto 2",
        "Producto 3",
        "Producto 4",
    ]


    #? Campos

    producto = ft.Dropdown(
        hint_text="Producto",
        height=38,
        width=180,
        text_size=13,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        options=[
            ft.dropdown.Option(producto)
            for producto in productos
        ]
    )

    cantidad = ft.TextField(
        hint_text="0",
        height=38,
        width=134,
        text_size=13,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        hint_style=ft.TextStyle(
            color="#A8B7C4"
        )
    )

    precio = ft.TextField(
        hint_text="$0.00",
        height=38,
        width=134,
        text_size=13,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        hint_style=ft.TextStyle(
            color="#A8B7C4"
        )
    )

    total = ft.TextField(
        hint_text="$0.00",
        height=38,
        width=134,
        text_size=13,
        read_only=True,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        hint_style=ft.TextStyle(
            color="#A8B7C4"
        )
    )


    #? Botones

    btn_agregar = ft.ElevatedButton(
        "Agregar",
        icon=ft.Icons.ADD_CIRCLE_OUTLINE,
        width=84,
        height=28,
        bgcolor="#E96791",
        color="#FFFFFF"
    )

    btn_cancelar = ft.ElevatedButton(
        "Cancelar",
        icon=ft.Icons.CANCEL_OUTLINED,
        width=87,
        height=28,
        bgcolor="#E96791",
        color="#FFFFFF"
    )


    #? Título

    titulo = ft.Text(
        "Registre una venta",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#5A1026"
    )


    #? Primera fila

    fila_1 = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Producto",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    producto
                ],
                spacing=5
            ),

            ft.Column(
                controls=[
                    ft.Text(
                        "Cantidad",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    cantidad
                ],
                spacing=5
            ),

            ft.Column(
                controls=[
                    ft.Text(
                        "Precio",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    precio
                ],
                spacing=5
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )


    #? Segunda fila

    fila_2 = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Total",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    total
                ],
                spacing=5
            )
        ],
        alignment=ft.MainAxisAlignment.START
    )


    #? Botones

    botones = ft.Row(
        controls=[
            btn_agregar,
            btn_cancelar
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing=22
    )


    #? Cuadro principal

    formulario = ft.Container(
        width=604,
        height=300,
        border=ft.Border.all(
            1,
            "#E5A1B4"
        ),
        bgcolor="#FDF5F6",
        padding=25,

        content=ft.Column(
            controls=[
                titulo,

                fila_1,
                fila_2,

                ft.Container(
                    content=botones,
                    expand=True,
                    alignment=ft.Alignment.BOTTOM_RIGHT
                )
            ],

            spacing=18,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


    #? Contenido principal

    layout = ft.Container(
        content=formulario,
        expand=True,
        alignment=ft.Alignment.CENTER
    )

    return layout