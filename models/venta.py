
class Venta:

    def __init__(self, id, fecha, folio, producto_id, producto_nombre, producto_color, producto_precio, producto_cantidad, subtotal, iva, total):
        self.id = id
        self.fecha = fecha
        self.folio = folio
        self.producto_id = producto_id
        self.producto_nombre = producto_nombre
        self.producto_color = producto_color
        self.producto_precio = producto_precio
        self.producto_cantidad = producto_cantidad
        self.subtota = subtotal
        self.iva = iva
        self.total = total

    def info(self):
        return f"ID: {self.id} \n Fecha: {self.fecha} \n Folio: {self.folio} \n ID del producto: {self.producto_id} \n Nombre del producto: {self.producto_nombre} \n Color del producto: {self.producto_color} \n Precio del producto: {self.producto_precio} \n Cantidad del producto: {self.producto_cantidad} \n Subtotal: {self.subtota} \n IVA: {self.iva} \n Total: {self.total}"
