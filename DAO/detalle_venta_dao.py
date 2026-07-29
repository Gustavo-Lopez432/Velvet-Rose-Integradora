from database.conexion import Conexion
from models.detalle_venta import DetalleVenta


class DetalleVentaDAO:

    def obtener(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM "DetalleVenta"')
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
            INSERT INTO "DetalleVenta"
            (id, idVenta, idProducto, cantidad, precioUnitario, subtotal)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            detalle.id,
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
            UPDATE "DetalleVenta"
            SET idVenta = %s,
                idProducto = %s,
                cantidad = %s,
                precioUnitario = %s,
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

        cursor.execute('DELETE FROM "DetalleVenta" WHERE id = %s', (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT MAX(id) FROM "DetalleVenta"')
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0

        return resultado[0]