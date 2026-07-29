import flet as ft
from UI.dashboard import *

ft.app (target=dashboard)




























#from DAO.producto_dao import *

# producto_dao= ProductoDAO()
# productos = producto_dao.obtener()

# if len(productos) == 0:
#     print ("no hay")
# else:
#     for producto in productos:
#         print (f"ID: {producto.id} \n Codigo de Barras: {producto.codigoBarras} \n Nombre: {producto.nombre} \n Marca: {producto.marca} \n Talla: {producto.talla} \n Color: {producto.color} \n Imagen: {producto.imagen} \n Precio: {producto.precio} \n Proveedor: {producto.proveedor} \n Existencia: {producto.existencia} \n Stock Maximo: {producto.maxStock} \n Stock Minimo: {producto.minStock}")