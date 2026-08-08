import flet as ft
from DAO.producto_dao import ProductoDAO
from models.producto import Producto

def productos_window_formulario(page: ft.Page, cancelar):

    #? instancias
    producto_dao = ProductoDAO()

    #? configuracion de la ventana
    page.title = "Registrar producto"
    page.bgcolor = "#F9F3F4"
    page.padding = 0

    #? opciones de los dropdowns
    marcas = ["Nike", "Adidas", "New Balance", "Converse", "Vans"]
    tallas = ["XS", "S", "M", "L", "XL"]
    colores = [
        "Negro", "Blanco", "Rojo", "Azul", "Verde", "Amarillo",
        "Naranja", "Morado", "Rosa", "Café", "Gris", "Azul Marino"
    ]
    proveedores = [
        "Distribuidora Nacional S.A.",
        "Importadora Global",
        "Proveedores Unidos"
    ]

    #? inputs del formulario
    ancho_campo = 170

    codigo_barras = ft.TextField(
        label="Código de barras",
        hint_text="Cod. Barras",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
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
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
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
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        focused_border_color="#C2355F",
        border_color="#000000",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    #? Nuevo campo: cantidad que se está ingresando ahora
    cantidad = ft.TextField(
        label="Cantidad",
        hint_text="Piezas a ingresar",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        focused_border_color="#C2355F",
        border_color="#000000",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    #? Ahora opcionales, con hint indicándolo
    max_stock = ft.TextField(
        label="Máximo en stock (opcional)",
        hint_text="Default: 50",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        focused_border_color="#C2355F",
        border_color="#000000",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    min_stock = ft.TextField(
        label="Mínimo en stock (opcional)",
        hint_text="Default: 5",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        focused_border_color="#C2355F",
        border_color="#000000",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    imagen = ft.TextField(
        label="Imagen (opcional)",
        hint_text="Seleccione imagen",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
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
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        focused_border_color="#C2355F",
        border_color="#000000",
        options=[ft.dropdown.Option(m) for m in marcas]
    )

    talla = ft.Dropdown(
        label="Talla",
        hint_text="Selecciona una talla",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        focused_border_color="#C2355F",
        border_color="#000000",
        options=[ft.dropdown.Option(t) for t in tallas]
    )

    color = ft.Dropdown(
        label="Color",
        hint_text="Selecciona un color",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        focused_border_color="#C2355F",
        border_color="#000000",
        options=[ft.dropdown.Option(c) for c in colores]
    )

    proveedor = ft.Dropdown(
        label="Proveedor (opcional)",
        hint_text="Selecciona un proveedor",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        focused_border_color="#C2355F",
        border_color="#000000",
        options=[ft.dropdown.Option(p) for p in proveedores]
    )

    titulo = ft.Text(
        "Registre un producto",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#5A1026"
    )

    #? funciones para agregar producto y cancelar
    def cancelar_formulario(e):
        cancelar()

    def mostrar_mensaje(texto, color="#2E7D32"):
        snack = ft.SnackBar(
            content=ft.Text(texto),
            bgcolor=color,
        )
        page.overlay.append(snack)
        snack.open = True
        page.update()

    def agregar_producto(e):

        #? el código de barras y la cantidad siempre son obligatorios
        if not codigo_barras.value:
            codigo_barras.error_text = "Ingresa el código de barras"
            codigo_barras.update()
            return

        if not cantidad.value or not cantidad.value.isdigit() or int(cantidad.value) <= 0:
            cantidad.error_text = "Ingresa una cantidad válida"
            cantidad.update()
            return

        #? buscamos si el código de barras ya existe
        productos_bd = producto_dao.cargar_datos()
        producto_existente = None
        for p in productos_bd:
            if p[1] == codigo_barras.value:
                producto_existente = p
                break

        #? CASO 1: el producto ya existe -> solo sumamos la cantidad a su existencia
        if producto_existente:
            id_producto = producto_existente[0]
            nombre_producto = producto_existente[2]

            producto_dao.sumar_existencia(id_producto, int(cantidad.value))

            mostrar_mensaje(
                f"Se sumaron {cantidad.value} piezas a '{nombre_producto}'. Existencia actualizada."
            )
            cancelar()
            return

        #? CASO 2: producto nuevo -> validamos el resto de los campos obligatorios
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

        if not precio.value:
            precio.error_text = "Ingresa el precio"
            precio.update()
            return

        #? campos opcionales con default
        max_stock_valor = int(max_stock.value) if max_stock.value else 50
        min_stock_valor = int(min_stock.value) if min_stock.value else 5
        proveedor_valor = proveedor.value if proveedor.value else None
        imagen_valor = imagen.value if imagen.value else None

        producto = Producto(
            id=None,
            codigoBarras=codigo_barras.value,
            nombre=nombre.value,
            marca=marca.value,
            talla=talla.value,
            color=color.value,
            imagen=imagen_valor,
            precio=float(precio.value),
            proveedor=proveedor_valor,
            existencia=int(cantidad.value),
            maxStock=max_stock_valor,
            minStock=min_stock_valor
        )

        producto_dao.insert(producto)

        mostrar_mensaje(f"Producto '{nombre.value}' registrado correctamente.")
        cancelar()

    #? botones de agregar producto y cancelar
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
        on_click=cancelar_formulario
    )

    #? filas de los campos
    fila_1 = ft.Row(
        controls=[codigo_barras, nombre, precio],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=550
    )

    fila_2 = ft.Row(
        controls=[cantidad, max_stock, min_stock],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=550
    )

    fila_dropdowns = ft.Row(
        controls=[marca, talla, color],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=550
    )

    fila_proveedor = ft.Row(
        controls=[
            imagen,
            proveedor,
            ft.Container(width=ancho_campo)
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=550
    )

    botones = ft.Row(
        controls=[btn_agregar, btn_cancelar],
        alignment=ft.MainAxisAlignment.END,
        spacing=22,
        width=550
    )

    #? contenedor principal
    formulario = ft.Container(
        width=650,
        height=620,
        border=ft.Border.all(1, "#E5A1B4"),
        bgcolor="#FDF5F6",
        padding=25,
        content=ft.Column(
            controls=[
                titulo,
                fila_1,
                fila_2,
                ft.Container(height=5),
                fila_dropdowns,
                fila_proveedor,
                ft.Container(expand=True),
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