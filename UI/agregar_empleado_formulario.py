import flet as ft


def empleados_window_formulario(page: ft.Page):

    page.title = "Registrar empleado"
    page.bgcolor = "#F9F3F4"
    page.padding = 0

    puestos = [
        "Vendedor",
        "Administrador",
    ]

    ancho_campo = 170

    nombre = ft.TextField(
        label="Nombre",
        hint_text="Ingresa el nombre",
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
        focused_border_color="#C2355F"
    )

    apellidos = ft.TextField(
        label="Apellidos",
        hint_text="Ingresa los apellidos",
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
        focused_border_color="#C2355F"
    )

    telefono = ft.TextField(
        label="Teléfono",
        hint_text="Ingresa el teléfono",
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

        keyboard_type=ft.KeyboardType.PHONE
    )

    correo = ft.TextField(
        label="Correo electrónico",
        hint_text="ejemplo@correo.com",
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

        keyboard_type=ft.KeyboardType.EMAIL
    )

    usuario = ft.TextField(
        label="Usuario",
        hint_text="Ingresa el nombre de usuario",
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
        focused_border_color="#C2355F"
    )

    contrasena = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa la contraseña",
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

        password=True,
        can_reveal_password=True
    )

    puesto = ft.Dropdown(
        label="Puesto",
        hint_text="Selecciona un puesto",
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
            ft.dropdown.Option(puesto)
            for puesto in puestos
        ]
    )

    titulo = ft.Text(
        "Registre un empleado",
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
            nombre,
            apellidos,
            telefono
        ],

        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

        width=550
    )

    fila_2 = ft.Row(
        controls=[
            correo,
            usuario,
            contrasena
        ],

        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

        width=550
    )

    fila_puesto = ft.Row(
        controls=[
            ft.Container(
                width=ancho_campo
            ),

            puesto,

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

        spacing=15,

        width=550
    )

    formulario = ft.Container(
        width=650,
        height=500,

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

                # Nombre / Apellidos / Teléfono
                fila_1,

                # Correo / Usuario / Contraseña
                fila_2,

                # Separación
                ft.Container(
                    height=5
                ),

                # Puesto
                fila_puesto,

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