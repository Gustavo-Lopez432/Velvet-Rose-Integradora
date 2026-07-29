from database.conexion import Conexion
from models.venta import Venta


class VentaDAO:

    def obtener(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM "Ventas"')
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
            INSERT INTO "Ventas"
            (id, fecha, folio, idEmpleado, subtotal, iva, total)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            venta.id,
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
            UPDATE "Ventas"
            SET fecha = %s,
                idEmpleado = %s
            WHERE id = %s
        """

        cursor.execute(sql, (
            venta.fecha,
            venta.idEmpleado,
            venta.id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def delete(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('DELETE FROM "Ventas" WHERE id = %s', (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT MAX(id) FROM "Ventas"')
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0

        return resultado[0]