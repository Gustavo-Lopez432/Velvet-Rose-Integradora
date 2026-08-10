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

    #? Mensaje único de validación, mismo patrón que login y ventas
    mensaje = ft.Text("", color=ft.Colors.RED)

    def mostrar_mensaje(texto, color=ft.Colors.RED):
        mensaje.value = texto
        mensaje.color = color
        page.update()

    def limpiar_mensaje(e=None):
        if mensaje.value:
            mensaje.value = ""
            page.update()

    #? Helpers de validación numérica — nada llega a int()/float() sin pasar por aquí
    def es_entero_valido(valor):
        return valor is not None and valor.strip().isdigit()

    def es_decimal_valido(valor):
        if valor is None or not valor.strip():
            return False
        try:
            float(valor)
            return True
        except ValueError:
            return False

    #? inputs del formulario
    ancho_campo = 250

    codigo_barras = ft.TextField(
        label="Código de barras",
        hint_text="Cod. Barras",
        width=ancho_campo,
        value=producto_actual[1] if producto_actual else "",
        on_change=limpiar_mensaje,
    )

    nombre = ft.TextField(
        label="Nombre",
        hint_text="Nombre producto",
        width=ancho_campo,
        value=producto_actual[2] if producto_actual else "",
        on_change=limpiar_mensaje,
    )

    precio = ft.TextField(
        label="Precio",
        hint_text="$0.00",
        width=ancho_campo,
        keyboard_type=ft.KeyboardType.NUMBER,
        value=str(producto_actual[7]) if producto_actual else "",
        on_change=limpiar_mensaje,
    )

    #? En modo agregar: cuántas piezas entran ahora.
    #? En modo editar: la existencia actual, editable directamente.
    cantidad = ft.TextField(
        label="Existencia" if producto_actual else "Cantidad",
        hint_text="0" if producto_actual else "Piezas a ingresar",
        width=ancho_campo,
        keyboard_type=ft.KeyboardType.NUMBER,
        value=str(producto_actual[9]) if producto_actual else "",
        on_change=limpiar_mensaje,
    )

    max_stock = ft.TextField(
        label="Máximo en stock (opcional)",
        hint_text="Default: 50",
        width=ancho_campo,
        keyboard_type=ft.KeyboardType.NUMBER,
        value=str(producto_actual[10]) if producto_actual else "",
        on_change=limpiar_mensaje,
    )

    min_stock = ft.TextField(
        label="Mínimo en stock (opcional)",
        hint_text="Default: 5",
        width=ancho_campo,
        keyboard_type=ft.KeyboardType.NUMBER,
        value=str(producto_actual[11]) if producto_actual else "",
        on_change=limpiar_mensaje,
    )

    imagen = ft.TextField(
        label="Imagen (opcional)",
        hint_text="Ninguna imagen seleccionada",
        width=ancho_campo,
        value=producto_actual[6] if producto_actual and producto_actual[6] else "",
        read_only=True,
        on_change=limpiar_mensaje,
    )

    imagen_preview = ft.Image(
        src=producto_actual[6] if producto_actual and producto_actual[6] else "",
        width=80,
        height=80,
        fit=ft.BoxFit.COVER,
        border_radius=8,
        visible=bool(producto_actual and producto_actual[6]),
    )

    file_picker = ft.FilePicker()
    page.services.append(file_picker)   # ✅ ahora es un "service"

    async def al_seleccionar_imagen(e):
        files = await file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["png", "jpg", "jpeg", "webp"],
        )
        if files:
            ruta = files[0].path
            imagen.value = ruta
            imagen_preview.src = ruta
            imagen_preview.visible = True
            limpiar_mensaje()
            page.update()

    btn_seleccionar_imagen = ft.ElevatedButton(
        "Seleccionar imagen",
        icon=ft.Icons.IMAGE_OUTLINED,
        bgcolor="#EF82A2",
        color="#000000",
        on_click=al_seleccionar_imagen,
    )

    marca = ft.Dropdown(
        label="Marca",
        hint_text="Selecciona una marca",
        width=ancho_campo,
        options=[ft.dropdown.Option(m) for m in marcas],
        value=producto_actual[3] if producto_actual else None,
    )
    marca.on_change = limpiar_mensaje

    talla = ft.Dropdown(
        label="Talla",
        hint_text="Selecciona una talla",
        width=ancho_campo,
        options=[ft.dropdown.Option(t) for t in tallas],
        value=producto_actual[4] if producto_actual else None,
    )
    talla.on_change = limpiar_mensaje

    color = ft.Dropdown(
        label="Color",
        hint_text="Selecciona un color",
        width=ancho_campo,
        options=[ft.dropdown.Option(c) for c in colores],
        value=producto_actual[5] if producto_actual else None,
    )
    color.on_change = limpiar_mensaje

    proveedor = ft.Dropdown(
        label="Proveedor (opcional)",
        hint_text="Selecciona un proveedor",
        width=ancho_campo,
        options=[ft.dropdown.Option(p) for p in proveedores],
        value=producto_actual[8] if producto_actual and producto_actual[8] else None,
    )
    proveedor.on_change = limpiar_mensaje

    titulo = ft.Text(
        "Editar producto" if producto_actual else "Registre un producto",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="#000000"
    )

    #? funciones para agregar/editar producto y cancelar
    def cancelar_formulario(e):
        cancelar()

    def guardar_producto(e):

        errores = []

        #? --- Validaciones comunes a ambos modos ---
        if not codigo_barras.value or not codigo_barras.value.strip():
            errores.append("Código de barras")

        if not es_entero_valido(cantidad.value):
            errores.append("Cantidad" if not producto_actual else "Existencia")

        if not nombre.value or not nombre.value.strip():
            errores.append("Nombre")

        if not marca.value:
            errores.append("Marca")

        if not talla.value:
            errores.append("Talla")

        if not color.value:
            errores.append("Color")

        if not es_decimal_valido(precio.value):
            errores.append("Precio")
        elif float(precio.value) <= 0:
            errores.append("Precio (debe ser mayor a 0)")

        #? Opcionales: solo se validan si el usuario escribió algo
        if max_stock.value and not es_entero_valido(max_stock.value):
            errores.append("Máximo en stock (solo números)")

        if min_stock.value and not es_entero_valido(min_stock.value):
            errores.append("Mínimo en stock (solo números)")

        if errores:
            mostrar_mensaje(f"Faltan campos por completar: {', '.join(errores)}")
            return

        if int(cantidad.value) <= 0 and not producto_actual:
            mostrar_mensaje("La cantidad debe ser mayor a 0")
            return

        max_stock_valor = int(max_stock.value) if max_stock.value else 50
        min_stock_valor = int(min_stock.value) if min_stock.value else 5
        proveedor_valor = proveedor.value if proveedor.value else None
        imagen_valor = imagen.value if imagen.value else None

        #? ===================== MODO EDITAR =====================
        if producto_actual:
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
            mostrar_mensaje(f"Producto '{nombre.value}' actualizado correctamente.", ft.Colors.GREEN)
            cancelar()
            return

        #? ===================== MODO AGREGAR =====================
        productos_bd = producto_dao.cargar_datos()
        producto_existente = None
        for p in productos_bd:
            if p[1] == codigo_barras.value:
                producto_existente = p
                break

        if producto_existente:
            id_existente = producto_existente[0]
            nombre_producto = producto_existente[2]

            producto_dao.sumar_existencia(id_existente, int(cantidad.value))

            mostrar_mensaje(
                f"Se sumaron {cantidad.value} piezas a '{nombre_producto}'. Existencia actualizada.",
                ft.Colors.GREEN
            )
            cancelar()
            return

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
        mostrar_mensaje(f"Producto '{nombre.value}' registrado correctamente.", ft.Colors.GREEN)
        cancelar()

    #? botones — mismos colores que el botón de login
    btn_agregar = ft.ElevatedButton(
        "Guardar cambios" if producto_actual else "Agregar",
        icon=ft.Icons.SAVE if producto_actual else ft.Icons.ADD_CIRCLE_OUTLINE,
        width=ancho_campo,
        height=45,
        bgcolor="#EF82A2",
        color="#000000",
        on_click=guardar_producto
    )

    btn_cancelar = ft.ElevatedButton(
        "Cancelar",
        icon=ft.Icons.CANCEL_OUTLINED,
        width=ancho_campo,
        height=45,
        bgcolor="#EF82A2",
        color="#000000",
        on_click=cancelar_formulario
    )

    #? filas de los campos, aprovechando el ancho extra de la tarjeta
    fila_1 = ft.Row(
        controls=[codigo_barras, nombre, precio],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    fila_2 = ft.Row(
        controls=[cantidad, max_stock, min_stock],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    fila_dropdowns = ft.Row(
        controls=[marca, talla, color],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    fila_imagen = ft.Row(
        controls=[imagen, btn_seleccionar_imagen, imagen_preview],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    fila_proveedor = ft.Row(
        controls=[proveedor],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    fila_botones = ft.Row(
        controls=[btn_agregar, btn_cancelar],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    #? Tarjeta al estilo login: blanca, borde rosa, radio 15, ancha para
    #? que los campos entren de a 3 por fila sin sentirse amontonados
    formulario = ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                fila_1,
                fila_2,
                fila_dropdowns,
                fila_imagen,
                fila_proveedor,
                fila_botones,
                mensaje,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
        ),
        width=850,
        padding=30,
        alignment=ft.Alignment.CENTER,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        border=ft.Border.all(3, "#EF82A2"),
    )

    return ft.Container(
        content=ft.Column(
            controls=[formulario],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=True,
        alignment=ft.Alignment.CENTER,
        padding=30,
    )