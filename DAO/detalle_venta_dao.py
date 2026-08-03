from database.conexion import Conexion
from models.detalle_venta import DetalleVenta


class DetalleVentaDAO:

    def obtener(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM detalle_venta')
        registros = cursor.fetchall()

        detalles = []

        for registro in registros:
            detalle = DetalleVenta(
                id=registro[0],
                idVenta=registro[1],
                idProducto=registro[2],
                cantidad=registro[3],
                precioUnitario=registro[4],
                subtotal=registro[5]
            )

            detalles.append(detalle)

        cursor.close()
        conexion.close()

        return detalles

    def insert(self, detalle):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO detalle_venta
            (id_venta, id_producto, cantidad, precio_unitario, subtotal)
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            detalle.idVenta,
            detalle.idProducto,
            detalle.cantidad,
            detalle.precioUnitario,
            detalle.subtotal
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def update(self, detalle):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            UPDATE detalle_venta
            SET id_venta = %s,
                id_producto = %s,
                cantidad = %s,
                precio_unitario = %s,
                subtotal = %s
            WHERE id = %s
        """

        cursor.execute(sql, (
            detalle.idVenta,
            detalle.idProducto,
            detalle.cantidad,
            detalle.precioUnitario,
            detalle.subtotal,
            detalle.id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def delete(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('DELETE FROM detalle_venta WHERE id = %s', (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT MAX(id) FROM detalle_venta')
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0

        return resultado[0]

    #? carga los datos de la tabla detalle venta
    def cargar_datos(self, id_venta=None):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT 
                dv.id,
                dv.id_venta,
                dv.id_producto,
                p.nombre AS producto,
                dv.cantidad,
                dv.precio_unitario,
                dv.subtotal
            FROM detalle_venta dv
            JOIN productos p ON p.id = dv.id_producto
        """

        if id_venta:
            sql += f" WHERE dv.id_venta = {id_venta}"

        sql += " ORDER BY dv.id ASC"

        cursor.execute(sql)
        registros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return registros