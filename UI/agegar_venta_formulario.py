import flet as ft
from datetime import datetime
from DAO.producto_dao import ProductoDAO
from DAO.venta_dao import VentaDAO
from DAO.detalle_venta_dao import DetalleVentaDAO
from models.venta import Venta
from models.detalle_venta import DetalleVenta


def agregar_venta_formulario(page: ft.Page, cancelar, id_empleado):
    page.title = "Registrar venta"
    page.bgcolor = "#F9F3F4"
    page.padding = 0

    #? Instancias de los DAO
    producto_dao = ProductoDAO()
    venta_dao = VentaDAO()
    detalle_venta_dao = DetalleVentaDAO()

    #? Cargar productos reales desde la base de datos
    productos_bd = producto_dao.cargar_datos()

    #? Diccionario id -> {nombre, precio, existencia} para acceso rápido
    productos_dict = {
        str(p[0]): {"nombre": p[2], "precio": float(p[7]), "existencia": p[9]}
        for p in productos_bd
    }

    #? Carrito en memoria (aún no toca la base de datos)
    carrito = []

    #? Mensaje único de validación (mismo patrón que login/empleados)
    mensaje = ft.Text("", color=ft.Colors.RED)

    def mostrar_mensaje(texto, color=ft.Colors.RED):
        mensaje.value = texto
        mensaje.color = color
        page.update()

    ancho_campo = 250

    producto = ft.Dropdown(
        label="Producto",
        hint_text="Selecciona un producto",
        width=ancho_campo,
        options=[
            ft.dropdown.Option(key=str(p[0]), text=p[2])
            for p in productos_bd
        ]
    )

    cantidad = ft.TextField(
        label="Cantidad",
        hint_text="0",
        width=ancho_campo,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    #? Limpia el mensaje al interactuar, igual que en login
    def limpiar_mensaje(e=None):
        if mensaje.value:
            mensaje.value = ""
            page.update()

    producto.on_change = limpiar_mensaje
    cantidad.on_change = limpiar_mensaje

    #? Tabla del carrito
    tabla_carrito = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Producto", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Cant.", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Precio", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Subtotal", color="#FFFFFF", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("", color="#FFFFFF")),
        ],
        rows=[],
        heading_row_color="#EF82A2",
        heading_row_height=40,
    )

    subtotal_txt = ft.Text("Subtotal: $0.00", size=16, color="#000000")
    iva_txt = ft.Text("IVA: $0.00", size=16, color="#000000")
    total_txt = ft.Text("Total: $0.00", size=20, weight=ft.FontWeight.BOLD, color="#5A1026")

    #? Recalcula subtotal, iva y total en base al carrito actual
    def actualizar_totales():
        subtotal = sum(item["subtotal"] for item in carrito)
        iva = subtotal * 0.16
        total = subtotal + iva

        subtotal_txt.value = f"Subtotal: ${subtotal:,.2f}"
        iva_txt.value = f"IVA: ${iva:,.2f}"
        total_txt.value = f"Total: ${total:,.2f}"

    #? Reconstruye las filas visibles del carrito
    def construir_filas_carrito():
        filas = []
        for idx, item in enumerate(carrito):
            filas.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(item["nombre"], color="#000000")),
                        ft.DataCell(ft.Text(str(item["cantidad"]), color="#000000")),
                        ft.DataCell(ft.Text(f"${item['precio_unitario']:.2f}", color="#000000")),
                        ft.DataCell(ft.Text(f"${item['subtotal']:.2f}", color="#000000")),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_color="#C2355F",
                                tooltip="Quitar",
                                on_click=lambda e, i=idx: quitar_producto(i),
                            )
                        ),
                    ]
                )
            )
        tabla_carrito.rows = filas

    def quitar_producto(indice):
        carrito.pop(indice)
        construir_filas_carrito()
        actualizar_totales()
        page.update()

    #? Agrega el producto seleccionado al carrito
    def agregar_producto(e):
        if not producto.value:
            mostrar_mensaje("Selecciona un producto")
            return

        if not cantidad.value or not cantidad.value.isdigit() or int(cantidad.value) <= 0:
            mostrar_mensaje("Ingresa una cantidad válida")
            return

        datos = productos_dict.get(producto.value)
        if not datos:
            mostrar_mensaje("Producto no encontrado")
            return

        cant = int(cantidad.value)
        precio_unit = datos["precio"]

        cantidad_en_carrito = sum(
            item["cantidad"] for item in carrito
            if item["id_producto"] == producto.value
        )

        cantidad_disponible = datos["existencia"] - cantidad_en_carrito

        if cant > cantidad_disponible:
            mostrar_mensaje(f"Solo hay {cantidad_disponible} piezas disponibles")
            return

        carrito.append({
            "id_producto": producto.value,
            "nombre": datos["nombre"],
            "cantidad": cant,
            "precio_unitario": precio_unit,
            "subtotal": cant * precio_unit,
        })

        construir_filas_carrito()
        actualizar_totales()

        producto.value = None
        cantidad.value = ""
        mensaje.value = ""

        page.update()

    #? Cancelar formulario
    def cancelar_formulario(e):
        cancelar()

    #? Finalizar venta: guarda la venta y su detalle en la base de datos
    def finalizar_venta(e):
        if not carrito:
            mostrar_mensaje("Agrega al menos un producto al carrito")
            return

        subtotal = sum(item["subtotal"] for item in carrito)
        iva = subtotal * 0.16
        total = subtotal + iva
        folio = f"V-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        venta = Venta(
            id=None,
            fecha=datetime.now(),
            folio=folio,
            idEmpleado=id_empleado,
            subtotal=subtotal,
            iva=iva,
            total=total
        )

        #? Insertamos la venta y obtenemos su id recién generado
        venta_dao.insert(venta)
        id_venta = venta_dao.obtener_ultimo_id()

        for item in carrito:
            detalle = DetalleVenta(
                id=None,
                idVenta=id_venta,
                idProducto=item["id_producto"],
                cantidad=item["cantidad"],
                precioUnitario=item["precio_unitario"],
                subtotal=item["subtotal"]
            )
            detalle_venta_dao.insert(detalle)

            #? Descontamos del inventario lo que se acaba de vender
            producto_dao.sumar_existencia(item["id_producto"], -item["cantidad"])

        mostrar_mensaje(f"Venta {folio} registrada correctamente. Total: ${total:,.2f}", ft.Colors.GREEN)

        cancelar()

    #? Mismo estilo de botón que el login: bgcolor "#EF82A2", texto negro
    btn_agregar = ft.ElevatedButton(
        "Agregar",
        icon=ft.Icons.ADD_CIRCLE_OUTLINE,
        width=300,
        height=45,
        bgcolor="#EF82A2",
        color="#000000",
        on_click=agregar_producto,
    )

    btn_finalizar = ft.ElevatedButton(
        "Finalizar venta",
        icon=ft.Icons.POINT_OF_SALE,
        width=300,
        height=50,
        bgcolor="#EF82A2",
        color="#000000",
        on_click=finalizar_venta
    )

    btn_cancelar = ft.ElevatedButton(
        "Cancelar",
        icon=ft.Icons.CANCEL_OUTLINED,
        width=300,
        height=45,
        bgcolor="#EF82A2",
        color="#000000",
        on_click=cancelar_formulario
    )

    #? La tabla del carrito, centrada dentro de la tarjeta
    carrito_scroll = ft.Row(
        controls=[tabla_carrito],
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
    )

    totales = ft.Column(
        controls=[subtotal_txt, iva_txt, total_txt],
        horizontal_alignment=ft.CrossAxisAlignment.END,
        spacing=4,
    )

    #? Fila superior: producto + cantidad + botón agregar, aprovechando el ancho extra
    fila_agregar = ft.Row(
        controls=[producto, cantidad, btn_agregar],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    fila_botones = ft.Row(
        controls=[btn_finalizar, btn_cancelar],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        wrap=True,
    )

    #? Tarjeta al estilo login: blanca, borde rosa, radio 15, pero más ancha
    #? para que las 5 columnas de la tabla del carrito se vean sin recortarse
    formulario = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Registrar venta",
                    size=20,
                    color="#000000",
                    weight=ft.FontWeight.BOLD,
                ),
                fila_agregar,
                ft.Divider(color="#E5A1B4"),
                carrito_scroll,
                ft.Divider(color="#E5A1B4"),
                totales,
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