import flet as ft

def main(page: ft.Page):
    page.title = "Formulario de Empleados"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 600
    page.window_height = 700
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # Opciones para el dropdown de puesto
    puestos = [
        "Vendedor",
        "Administrador",
    ]

    # Campos del formulario
    nombre = ft.TextField(
        label="Nombre",
        hint_text="Ingresa el nombre",
        width=400,
    )

    apellidos = ft.TextField(
        label="Apellidos",
        hint_text="Ingresa los apellidos",
        width=400,
    )

    telefono = ft.TextField(
        label="Teléfono",
        hint_text="Ingresa el teléfono",
        width=400,
        keyboard_type=ft.KeyboardType.PHONE,
    )

    correo = ft.TextField(
        label="Correo Electrónico",
        hint_text="ejemplo@correo.com",
        width=400,
        keyboard_type=ft.KeyboardType.EMAIL,
    )

    usuario = ft.TextField(
        label="Usuario",
        hint_text="Ingresa el nombre de usuario",
        width=400,
    )

    contrasena = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa la contraseña",
        width=400,
        password=True,
        can_reveal_password=True,
    )

    puesto = ft.Dropdown(
        label="Puesto",
        hint_text="Selecciona un puesto",
        width=400,
        options=[ft.dropdown.Option(puesto) for puesto in puestos],
        value=puestos[0] if puestos else None,
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
                ft.Text("👤 Registro de Empleados", size=28, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20),
                nombre,
                apellidos,
                telefono,
                correo,
                usuario,
                contrasena,
                puesto,
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