import flet as ft
from DAO.empleado_dao import EmpleadoDAO
from models.empleado import Empleado

def empleados_window_formulario(page: ft.Page, cancelar):

    #? instancias
    empleado_dao = EmpleadoDAO()

    #? configuracion de la ventana
    page.title = "Registrar empleado"
    page.bgcolor = "#F9F3F4"
    page.padding = 0

    #? opciones del dropdown
    puestos = [
        "Vendedor",
        "Administrador",
    ]

    #? inputs del formulario
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
        focused_border_color="#C2355F",
        border_color="#000000"
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
        focused_border_color="#C2355F",
        border_color="#000000"
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
        focused_border_color="#C2355F",
        border_color="#000000",
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
        focused_border_color="#C2355F",
        border_color="#000000",
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
        focused_border_color="#C2355F",
        border_color="#000000"
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
        focused_border_color="#C2355F",
        border_color="#000000",
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
        focused_border_color="#C2355F",
        border_color="#000000",
        options=[
            ft.dropdown.Option(puesto)
            for puesto in puestos
        ]
    )

    #? titulo
    titulo = ft.Text(
        "Registre un empleado",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#5A1026"
    )

    #? funciones para agregar empleado y cancelar
    def cancelar_formulario(e):
        cancelar()

    def agregar_empleado(e):

        #? validaciones de los campos
        if not nombre.value:
            nombre.error_text = "Ingresa el nombre"
            nombre.update()
            return

        if not apellidos.value:
            apellidos.error_text = "Ingresa los apellidos"
            apellidos.update()
            return

        if not telefono.value:
            telefono.error_text = "Ingresa el teléfono"
            telefono.update()
            return

        if not correo.value:
            correo.error_text = "Ingresa el correo electrónico"
            correo.update()
            return

        if not usuario.value:
            usuario.error_text = "Ingresa el usuario"
            usuario.update()
            return

        if not contrasena.value:
            contrasena.error_text = "Ingresa la contraseña"
            contrasena.update()
            return

        if not puesto.value:
            puesto.error_text = "Selecciona un puesto"
            puesto.update()
            return

        #? creamos el objeto empleado
        empleado = Empleado(
            id=None,
            nombre=nombre.value,
            apellidos=apellidos.value,
            telefono=telefono.value,
            correo=correo.value,
            usuario=usuario.value,
            contrasena=contrasena.value,
            puesto=puesto.value
        )

        #? insertamos el empleado
        empleado_dao.insert(empleado)

        print("Empleado agregado correctamente")

        #? regresamos a la ventana anterior
        cancelar()

    #? botones de agregar empleado y cancelar
    btn_agregar = ft.ElevatedButton(
        "Agregar",
        icon=ft.Icons.ADD_CIRCLE_OUTLINE,
        width=130,
        height=40,
        bgcolor="#E96791",
        color="#FFFFFF",
        on_click=agregar_empleado
    )

    btn_cancelar = ft.ElevatedButton(
        "Cancelar",
        icon=ft.Icons.CANCEL_OUTLINED,
        width=130,
        height=40,
        bgcolor="#E96791",
        color="#FFFFFF",
        on_click=cancelar_formulario
    )

    #? filas de los campos
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
        spacing=22,
        width=550
    )

    #? contenedor principal
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
                titulo,
                fila_1,
                fila_2,

                ft.Container(
                    height=5
                ),

                fila_puesto,

                ft.Container(
                    expand=True
                ),

                botones
            ],

            spacing=18,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    #? agregamos al layout
    layout = ft.Container(
        content=formulario,
        expand=True,
        alignment=ft.Alignment.CENTER
    )

    return layout