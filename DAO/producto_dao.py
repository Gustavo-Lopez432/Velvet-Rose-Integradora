from database.conexion import Conexion
from models.producto import Producto


class ProductoDAO:

    def obtener(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM "Productos"')
        registros = cursor.fetchall()

        productos = []

        for registro in registros:
            producto = Producto(
                id=registro[0],
                codigoBarras=registro[1],
                nombre=registro[2],
                marca=registro[3],
                talla=registro[4],
                color=registro[5],
                imagen=registro[6],
                precio=registro[7],
                proveedor=registro[8],
                existencia=registro[9],
                maxStock=registro[10],
                minStock=registro[11]
            )

            productos.append(producto)

        cursor.close()
        conexion.close()

        return productos

    def insert(self, producto):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO "Productos"
            (id, codigoBarras, nombre, marca, talla, color, imagen, precio, proveedor, existencia, maxStock, minStock)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            producto.id,
            producto.codigoBarras,
            producto.nombre,
            producto.marca,
            producto.talla,
            producto.color,
            producto.imagen,
            producto.precio,
            producto.proveedor,
            producto.existencia,
            producto.maxStock,
            producto.minStock
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def update(self, producto):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            UPDATE "Productos"
            SET codigoBarras = %s,
                nombre = %s,
                marca = %s,
                talla = %s,
                color = %s,
                imagen = %s,
                precio = %s,
                proveedor = %s,
                existencia = %s,
                maxStock = %s,
                minStock = %s
            WHERE id = %s
        """

        cursor.execute(sql, (
            producto.codigoBarras,
            producto.nombre,
            producto.marca,
            producto.talla,
            producto.color,
            producto.imagen,
            producto.precio,
            producto.proveedor,
            producto.existencia,
            producto.maxStock,
            producto.minStock,
            producto.id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def delete(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('DELETE FROM "Productos" WHERE id = %s', (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT MAX(id) FROM "Productos"')
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0

        return resultado[0]