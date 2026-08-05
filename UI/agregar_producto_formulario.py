import flet as ft


def productos_window_formulario(page: ft.Page):

    #? configuracion de la pagina
    page.title = "Registrar producto"
    page.bgcolor = "#F9F3F4"
    page.padding = 0


    #? datos para los dropdowns

    marcas = [
        "Nike",
        "Adidas",
        "New Balance",
        "Converse",
        "Vans",
    ]

    tallas = [
        "XS",
        "S",
        "M",
        "L",
        "XL",
    ]

    colores = [
        "Negro",
        "Blanco",
        "Rojo",
        "Azul",
        "Verde",
        "Amarillo",
        "Naranja",
        "Morado",
        "Rosa",
        "Café",
        "Gris",
        "Azul Marino"
    ]

    proveedores = [
        "Distribuidora Nacional S.A.",
        "Importadora Global",
        "Proveedores Unidos"
    ]


    #? campos del formulario

    codigo_barras = ft.TextField(
        hint_text="Cod. Barras",
        height=38,
        width=134,
        text_size=13,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        hint_style=ft.TextStyle(
            color="#A8B7C4"
        )
    )

    nombre = ft.TextField(
        hint_text="Nombre producto",
        height=38,
        width=134,
        text_size=13,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        hint_style=ft.TextStyle(
            color="#A8B7C4"
        )
    )

    marca = ft.Dropdown(
        hint_text="Marca",
        height=38,
        width=134,
        text_size=13,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        options=[
            ft.dropdown.Option(marca)
            for marca in marcas
        ]
    )

    talla = ft.Dropdown(
        hint_text="Talla",
        height=38,
        width=134,
        text_size=13,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        options=[
            ft.dropdown.Option(talla)
            for talla in tallas
        ]
    )

    color = ft.Dropdown(
        hint_text="Color",
        height=38,
        width=134,
        text_size=13,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        options=[
            ft.dropdown.Option(color)
            for color in colores
        ]
    )

    proveedor = ft.Dropdown(
        hint_text="Proveedor",
        height=38,
        width=134,
        text_size=13,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        options=[
            ft.dropdown.Option(proveedor)
            for proveedor in proveedores
        ]
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

    max_stock = ft.TextField(
        hint_text="0",
        height=38,
        width=134,
        text_size=13,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        hint_style=ft.TextStyle(
            color="#A8B7C4"
        )
    )

    min_stock = ft.TextField(
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

    imagen = ft.TextField(
        hint_text="Seleccione imagen",
        height=38,
        width=146,
        text_size=13,
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        hint_style=ft.TextStyle(
            color="#A8B7C4"
        ),
        read_only=True
    )


    #? botones

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


    #? titulo

    titulo = ft.Text(
        "Registre un producto",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#5A1026"
    )


    #? filas del formulario

    fila_1 = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Código de barras",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    codigo_barras
                ],
                spacing=5
            ),

            ft.Column(
                controls=[
                    ft.Text(
                        "Talla",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    talla
                ],
                spacing=5
            ),

            ft.Column(
                controls=[
                    ft.Text(
                        "Proveedor",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    proveedor
                ],
                spacing=5
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )


    fila_2 = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Nombre",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    nombre
                ],
                spacing=5
            ),

            ft.Column(
                controls=[
                    ft.Text(
                        "Color",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    color
                ],
                spacing=5
            ),

            ft.Column(
                controls=[
                    ft.Text(
                        "Máximo en stock",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    max_stock
                ],
                spacing=5
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )


    fila_3 = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Marca",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    marca
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
            ),

            ft.Column(
                controls=[
                    ft.Text(
                        "Mínimo en stock",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#66727C"
                    ),
                    min_stock
                ],
                spacing=5
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )


    #? campo de imagen

    campo_imagen = ft.Column(
        controls=[
            ft.Text(
                "Imagen",
                size=9,
                weight=ft.FontWeight.BOLD,
                color="#66727C"
            ),
            imagen
        ],
        spacing=5
    )


    #? botones

    botones = ft.Row(
        controls=[
            btn_agregar,
            btn_cancelar
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing=22
    )


    #? cuadro principal

    formulario = ft.Container(
        width=604,
        height=443,
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
                fila_3,

                ft.Container(
                    content=campo_imagen,
                    alignment=ft.Alignment.CENTER
                ),

                ft.Container(
                    content=botones,
                    expand=True,
                    alignment=ft.Alignment.BOTTOM_RIGHT
                )
            ],

            spacing=13,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


    #? contenido principal

    layout = ft.Container(
        content=formulario,
        expand=True,
        alignment=ft.Alignment.CENTER
    )

    return layout