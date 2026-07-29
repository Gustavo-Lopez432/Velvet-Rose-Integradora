
class Producto:

    def __init__(self, id, codigoBarras, nombre, marca, talla, color, imagen, precio, proveedor, existencia, maxStock, minStock):
        self.id = id
        self.codigoBarras = codigoBarras
        self.nombre = nombre
        self.marca = marca
        self.talla = talla
        self.color = color
        self.imagen = imagen
        self.precio = precio
        self.proveedor = proveedor
        self.existencia = existencia
        self.maxStock = maxStock
        self.minStock = minStock

    def info(self):
        return f"ID: {self.id} \n Codigo de Barras: {self.codigoBarras} \n Nombre: {self.nombre} \n Marca: {self.marca} \n Talla: {self.talla} \n Color: {self.color} \n Imagen: {self.imagen} \n Precio: {self.precio} \n Proveedor: {self.proveedor} \n Existencia: {self.existencia} \n Stock Maximo: {self.maxStock} \n Stock Minimo: {self.minStock}"
