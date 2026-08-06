import flet as ft
from DAO.producto_dao import ProductoDAO
from models.producto import Producto

def productos_window_formulario(page: ft.Page, cancelar):

    producto_dao = ProductoDAO()

    page.title = "Registrar producto"
    page.bgcolor = "#F9F3F4"
    page.padding = 0

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

    ancho_campo = 170

    codigo_barras = ft.TextField(
        label="Código de barras",
        hint_text="Cod. Barras",
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

    nombre = ft.TextField(
        label="Nombre",
        hint_text="Nombre producto",
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
        focused_border_color="#C2355F",
        border_color="#000000",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    max_stock = ft.TextField(
        label="Máximo en stock",
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
        focused_border_color="#C2355F",
        border_color="#000000",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    min_stock = ft.TextField(
        label="Mínimo en stock",
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
        focused_border_color="#C2355F",
        border_color="#000000",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    imagen = ft.TextField(
        label="Imagen",
        hint_text="Seleccione imagen",
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
    )

    marca = ft.Dropdown(
        label="Marca",
        hint_text="Selecciona una marca",
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
            ft.dropdown.Option(marca)
            for marca in marcas
        ]
    )

    talla = ft.Dropdown(
        label="Talla",
        hint_text="Selecciona una talla",
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
            ft.dropdown.Option(talla)
            for talla in tallas
        ]
    )

    color = ft.Dropdown(
        label="Color",
        hint_text="Selecciona un color",
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
            ft.dropdown.Option(color)
            for color in colores
        ]
    )

    proveedor = ft.Dropdown(
        label="Proveedor",
        hint_text="Selecciona un proveedor",
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
            ft.dropdown.Option(proveedor)
            for proveedor in proveedores
        ]
    )

    titulo = ft.Text(
        "Registre un producto",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#5A1026"
    )

    def cancelar_formulario(e):
        cancelar()

    def agregar_producto(e):

        if not codigo_barras.value:
            codigo_barras.error_text = "Ingresa el código de barras"
            codigo_barras.update()
            return

        if not nombre.value:
            nombre.error_text = "Ingresa el nombre"
            nombre.update()
            return

        if not marca.value:
            marca.error_text = "Selecciona una marca"
            marca.update()
            return

        if not talla.value:
            talla.error_text = "Selecciona una talla"
            talla.update()
            return

        if not color.value:
            color.error_text = "Selecciona un color"
            color.update()
            return

        if not proveedor.value:
            proveedor.error_text = "Selecciona un proveedor"
            proveedor.update()
            return

        if not precio.value:
            precio.error_text = "Ingresa el precio"
            precio.update()
            return

        if not max_stock.value:
            max_stock.error_text = "Ingresa el stock máximo"
            max_stock.update()
            return

        if not min_stock.value:
            min_stock.error_text = "Ingresa el stock mínimo"
            min_stock.update()
            return

        producto = Producto(
            id=None,
            codigoBarras=codigo_barras.value,
            nombre=nombre.value,
            marca=marca.value,
            talla=talla.value,
            color=color.value,
            imagen=imagen.value,
            precio=float(precio.value),
            proveedor=proveedor.value,
            existencia=0,
            maxStock=int(max_stock.value),
            minStock=int(min_stock.value)
        )

        if producto_dao.existe_codigo_barras(codigo_barras.value):
            codigo_barras.error_text = "Este código de barras ya está registrado"
            codigo_barras.update()
            return

        producto_dao.insert(producto)

        print("Producto agregado correctamente")

    btn_agregar = ft.ElevatedButton(
        "Agregar",
        icon=ft.Icons.ADD_CIRCLE_OUTLINE,
        width=130,
        height=40,
        bgcolor="#E96791",
        color="#FFFFFF",
        on_click=agregar_producto
    )

    btn_cancelar = ft.ElevatedButton(
        "Cancelar",
        icon=ft.Icons.CANCEL_OUTLINED,
        width=130,
        height=40,
        bgcolor="#E96791",
        color="#FFFFFF",
        on_click=lambda e: cancelar()
    )

    fila_1 = ft.Row(
        controls=[
            codigo_barras,
            nombre,
            precio
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=550
    )

    fila_2 = ft.Row(
        controls=[
            max_stock,
            min_stock,
            imagen
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=550
    )

    fila_dropdowns = ft.Row(
        controls=[
            marca,
            talla,
            color
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=550
    )

    fila_proveedor = ft.Row(
        controls=[
            ft.Container(
                width=ancho_campo
            ),

            proveedor,

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
        height=600,

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

                # Campos normales
                fila_1,
                fila_2,

                # Separación
                ft.Container(
                    height=5
                ),

                # Dropdowns
                fila_dropdowns,
                fila_proveedor,

                # Espacio antes de los botones
                ft.Container(
                    expand=True
                ),

                # Botones
                botones
            ],

            spacing=13,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    layout = ft.Container(
        content=formulario,
        expand=True,
        alignment=ft.Alignment.CENTER
    )

    return layout