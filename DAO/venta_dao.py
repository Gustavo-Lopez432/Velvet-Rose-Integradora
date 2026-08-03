from database.conexion import Conexion
from models.venta import Venta


class VentaDAO:

    def obtener(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM ventas')
        registros = cursor.fetchall()

        ventas = []

        for registro in registros:
            venta = Venta(
                id=registro[0],
                fecha=registro[1],
                folio=registro[2],
                idEmpleado=registro[3],
                subtotal=registro[4],
                iva=registro[5],
                total=registro[6]
            )

            ventas.append(venta)

        cursor.close()
        conexion.close()

        return ventas

    def insert(self, venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO ventas
            (fecha, folio, id_empleado, subtotal, iva, total)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            venta.fecha,
            venta.folio,
            venta.idEmpleado,
            venta.subtotal,
            venta.iva,
            venta.total
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def update(self, venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            UPDATE ventas
            SET fecha = %s,
                folio = %s,
                id_empleado = %s,
                subtotal = %s,
                iva = %s,
                total = %s
            WHERE id = %s
        """

        cursor.execute(sql, (
            venta.fecha,
            venta.folio,
            venta.idEmpleado,
            venta.subtotal,
            venta.iva,
            venta.total,
            venta.id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def delete(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('DELETE FROM ventas WHERE id = %s', (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT MAX(id) FROM ventas')
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0

        return resultado[0]
