import flet as ft
from DAO.producto_dao import ProductoDAO
from models.producto import Producto

def productos_window_formulario(page: ft.Page, cancelar, id_producto=None):

    #? instancias
    producto_dao = ProductoDAO()

    #? si hay id, buscamos el producto para precargar sus datos (modo edición)
    producto_actual = None
    if id_producto is not None:
        todos = producto_dao.cargar_datos()
        for p in todos:
            if p[0] == id_producto:
                producto_actual = p
                break

    #? configuracion de la ventana
    page.title = "Editar producto" if producto_actual else "Registrar producto"
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
        border_color="#000000",
        value=producto_actual[1] if producto_actual else ""
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
        border_color="#000000",
        value=producto_actual[2] if producto_actual else ""
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
        keyboard_type=ft.KeyboardType.NUMBER,
        value=str(producto_actual[7]) if producto_actual else ""
    )

    #? En modo agregar: cuántas piezas entran ahora.
    #? En modo editar: la existencia actual, editable directamente.
    cantidad = ft.TextField(
        label="Existencia" if producto_actual else "Cantidad",
        hint_text="0" if producto_actual else "Piezas a ingresar",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        focused_border_color="#C2355F",
        border_color="#000000",
        keyboard_type=ft.KeyboardType.NUMBER,
        value=str(producto_actual[9]) if producto_actual else ""
    )

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
        keyboard_type=ft.KeyboardType.NUMBER,
        value=str(producto_actual[10]) if producto_actual else ""
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
        keyboard_type=ft.KeyboardType.NUMBER,
        value=str(producto_actual[11]) if producto_actual else ""
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
        value=producto_actual[6] if producto_actual and producto_actual[6] else ""
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
        options=[ft.dropdown.Option(m) for m in marcas],
        value=producto_actual[3] if producto_actual else None
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
        options=[ft.dropdown.Option(t) for t in tallas],
        value=producto_actual[4] if producto_actual else None
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
        options=[ft.dropdown.Option(c) for c in colores],
        value=producto_actual[5] if producto_actual else None
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
        options=[ft.dropdown.Option(p) for p in proveedores],
        value=producto_actual[8] if producto_actual and producto_actual[8] else None
    )

    #? Validaciones en tiempo real
    def validar_codigo_barras(e):
        codigo_barras.error = None
        codigo_barras.update()

    def validar_nombre(e):
        nombre.error = None
        nombre.update()

    def validar_precio(e):
        valor = precio.value
        if valor:
            try:
                num = float(valor)
                precio.error = "Debe ser mayor a 0" if num <= 0 else None
            except ValueError:
                precio.error = "Precio inválido"
        else:
            precio.error = None
        precio.update()

    def validar_cantidad(e):
        valor = cantidad.value
        if valor and not valor.isdigit():
            cantidad.error = "Solo números"
        else:
            cantidad.error = None
        cantidad.update()

    def validar_max_stock(e):
        valor = max_stock.value
        if valor and not valor.isdigit():
            max_stock.error = "Solo números"
        else:
            max_stock.error = None
        max_stock.update()

    def validar_min_stock(e):
        valor = min_stock.value
        if valor and not valor.isdigit():
            min_stock.error = "Solo números"
        else:
            min_stock.error = None
        min_stock.update()

    def validar_marca(e):
        marca.error = None
        marca.update()

    def validar_talla(e):
        talla.error = None
        talla.update()

    def validar_color(e):
        color.error = None
        color.update()

    codigo_barras.on_change = validar_codigo_barras
    nombre.on_change = validar_nombre
    precio.on_change = validar_precio
    cantidad.on_change = validar_cantidad
    max_stock.on_change = validar_max_stock
    min_stock.on_change = validar_min_stock
    marca.on_change = validar_marca
    talla.on_change = validar_talla
    color.on_change = validar_color

    titulo = ft.Text(
        "Editar producto" if producto_actual else "Registre un producto",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#5A1026"
    )

    #? funciones para agregar/editar producto y cancelar
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

    def guardar_producto(e):

        if not codigo_barras.value:
            codigo_barras.error = "Ingresa el código de barras"
            codigo_barras.update()
            return

        if not cantidad.value or not cantidad.value.isdigit():
            cantidad.error = "Ingresa un valor válido"
            cantidad.update()
            return

        #? ===================== MODO EDITAR =====================
        if producto_actual:

            if not nombre.value:
                nombre.error = "Ingresa el nombre"
                nombre.update()
                return

            if not marca.value:
                marca.error = "Selecciona una marca"
                marca.update()
                return

            if not talla.value:
                talla.error = "Selecciona una talla"
                talla.update()
                return

            if not color.value:
                color.error = "Selecciona un color"
                color.update()
                return

            if not precio.value:
                precio.error = "Ingresa el precio"
                precio.update()
                return

            max_stock_valor = int(max_stock.value) if max_stock.value else 50
            min_stock_valor = int(min_stock.value) if min_stock.value else 5
            proveedor_valor = proveedor.value if proveedor.value else None
            imagen_valor = imagen.value if imagen.value else None

            producto = Producto(
                id=id_producto,
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

            producto_dao.update(producto)
            mostrar_mensaje(f"Producto '{nombre.value}' actualizado correctamente.")
            cancelar()
            return

        #? ===================== MODO AGREGAR =====================
        if int(cantidad.value) <= 0:
            cantidad.error = "Ingresa una cantidad válida"
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
            id_existente = producto_existente[0]
            nombre_producto = producto_existente[2]

            producto_dao.sumar_existencia(id_existente, int(cantidad.value))

            mostrar_mensaje(
                f"Se sumaron {cantidad.value} piezas a '{nombre_producto}'. Existencia actualizada."
            )
            cancelar()
            return

        #? CASO 2: producto nuevo -> validamos el resto de los campos obligatorios
        if not nombre.value:
            nombre.error = "Ingresa el nombre"
            nombre.update()
            return

        if not marca.value:
            marca.error = "Selecciona una marca"
            marca.update()
            return

        if not talla.value:
            talla.error = "Selecciona una talla"
            talla.update()
            return

        if not color.value:
            color.error = "Selecciona un color"
            color.update()
            return

        if not precio.value:
            precio.error = "Ingresa el precio"
            precio.update()
            return

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

    #? botones de guardar y cancelar
    btn_agregar = ft.ElevatedButton(
        "Guardar cambios" if producto_actual else "Agregar",
        icon=ft.Icons.SAVE if producto_actual else ft.Icons.ADD_CIRCLE_OUTLINE,
        width=150,
        height=40,
        bgcolor="#E96791",
        color="#FFFFFF",
        on_click=guardar_producto
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