import flet as ft
from datetime import datetime
from DAO.producto_dao import ProductoDAO
from DAO.venta_dao import VentaDAO
from DAO.detalle_venta_dao import DetalleVentaDAO
from models.venta import Venta
from models.detalle_venta import DetalleVenta


def agregar_venta_formulario(page: ft.Page, cancelar):
    page.title = "Registrar venta"
    page.bgcolor = "#F9F3F4"
    page.padding = 0

    #? TODO: reemplazar por el id del empleado en sesión cuando exista login
    id_empleado_actual = 1

    #? Instancias de los DAO
    producto_dao = ProductoDAO()
    venta_dao = VentaDAO()
    detalle_venta_dao = DetalleVentaDAO()

    #? Cargar productos reales desde la base de datos
    productos_bd = producto_dao.cargar_datos()

    #? Diccionario id -> {nombre, precio} para acceso rápido
    productos_dict = {
        str(p[0]): {"nombre": p[2], "precio": float(p[7])}
        for p in productos_bd
    }

    #? Carrito en memoria (aún no toca la base de datos)
    carrito = []

    ancho_campo = 170

    producto = ft.Dropdown(
        label="Producto",
        hint_text="Selecciona un producto",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        options=[
            ft.dropdown.Option(key=str(p[0]), text=p[2])
            for p in productos_bd
        ]
    )

    cantidad = ft.TextField(
        label="Cantidad",
        hint_text="0",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    precio = ft.TextField(
        label="Precio unitario",
        hint_text="$0.00",
        height=60,
        width=ancho_campo,
        text_size=13,
        color="#000000",
        label_style=ft.TextStyle(color="#66727C", size=16),
        hint_style=ft.TextStyle(color="#A8B7C4"),
        border_color="#AEBCC8",
        focused_border_color="#C2355F",
        read_only=True
    )

    #? Autocompletar precio al elegir el producto
    def producto_seleccionado(e):
        datos = productos_dict.get(producto.value)
        precio.value = f"{datos['precio']:.2f}" if datos else ""
        page.update()

    producto.on_change = producto_seleccionado

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
        heading_row_color="#C2355F",
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
            producto.error_text = "Selecciona un producto"
            producto.update()
            return

        if not cantidad.value or not cantidad.value.isdigit() or int(cantidad.value) <= 0:
            cantidad.error_text = "Ingresa una cantidad válida"
            cantidad.update()
            return

        producto.error_text = None
        cantidad.error_text = None

        datos = productos_dict.get(producto.value)
        if not datos:
            return

        cant = int(cantidad.value)
        precio_unit = datos["precio"]

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
        precio.value = ""

        page.update()

    #? Cancelar formulario
    def cancelar_formulario(e):
        cancelar()

    #? Finalizar venta: guarda la venta y su detalle en la base de datos
    def finalizar_venta(e):

        if not carrito:
            return

        subtotal = sum(item["subtotal"] for item in carrito)
        iva = subtotal * 0.16
        total = subtotal + iva

        venta = Venta(
            id=None,
            fecha=datetime.now(),
            folio=f"V-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            idEmpleado=id_empleado_actual,
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

        print("Venta registrada correctamente")

        cancelar()

    titulo = ft.Text("Registre una venta", size=30, weight=ft.FontWeight.BOLD, color="#5A1026")

    btn_agregar = ft.ElevatedButton(
        "Agregar",
        icon=ft.Icons.ADD_CIRCLE_OUTLINE,
        width=130,
        height=40,
        bgcolor="#E96791",
        color="#FFFFFF",
        on_click=agregar_producto,
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

    btn_finalizar = ft.ElevatedButton(
        "Finalizar venta",
        icon=ft.Icons.POINT_OF_SALE,
        width=180,
        height=40,
        bgcolor="#5A1026",
        color="#FFFFFF",
        on_click=finalizar_venta
    )

    fila_1 = ft.Row(
        controls=[producto, cantidad, precio],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=550
    )

    botones_agregar = ft.Row(
        controls=[btn_agregar],
        alignment=ft.MainAxisAlignment.END,
        width=550
    )

    carrito_scroll = ft.Column(
        controls=[tabla_carrito],
        scroll=ft.ScrollMode.AUTO,
        height=180,
    )

    totales = ft.Column(
        controls=[subtotal_txt, iva_txt, total_txt],
        horizontal_alignment=ft.CrossAxisAlignment.END,
        spacing=4,
    )

    botones = ft.Row(
        controls=[btn_finalizar, btn_cancelar],
        alignment=ft.MainAxisAlignment.END,
        spacing=22,
        width=550
    )

    formulario = ft.Container(
        width=650,
        height=650,
        border=ft.Border.all(1, "#E5A1B4"),
        bgcolor="#FDF5F6",
        padding=25,
        content=ft.Column(
            controls=[
                titulo,
                fila_1,
                botones_agregar,
                carrito_scroll,
                ft.Divider(color="#E5A1B4"),
                totales,
                ft.Container(expand=True),
                botones
            ],
            spacing=14,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    layout = ft.Container(
        content=formulario,
        expand=True,
        alignment=ft.Alignment.CENTER
    )

    return layout