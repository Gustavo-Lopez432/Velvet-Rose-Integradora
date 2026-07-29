class DetalleVenta:

    def __init__(self, id, idVenta, idProducto, cantidad, precioUnitario, subtotal):
        self.id = id
        self.idVenta = idVenta
        self.idProducto = idProducto
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario
        self.subtotal = subtotal

    def info(self):
        return f"ID: {self.id} \nID Venta: {self.idVenta} \nID Producto: {self.idProducto} \nCantidad: {self.cantidad} \nPrecio Unitario: {self.precioUnitario} \nSubtotal: {self.subtotal}"