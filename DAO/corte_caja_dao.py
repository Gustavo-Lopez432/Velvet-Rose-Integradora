from database.conexion import Conexion
from models.corte_caja import CorteCaja


class CorteCajaDAO:

    def obtener(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM "CorteCaja"')
        registros = cursor.fetchall()

        cortes = []

        for registro in registros:
            corte = CorteCaja(
                id=registro[0],
                fecha=registro[1],
                horaApertura=registro[2],
                horaCierre=registro[3],
                montoInicial=registro[4],
                montoFinal=registro[5],
                idEmpleado=registro[6]
            )

            cortes.append(corte)

        cursor.close()
        conexion.close()

        return cortes

    def insert(self, corte):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO "CorteCaja"
            (id, fecha, horaApertura, horaCierre, montoInicial, montoFinal, idEmpleado)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            corte.id,
            corte.fecha,
            corte.horaApertura,
            corte.horaCierre,
            corte.montoInicial,
            corte.montoFinal,
            corte.idEmpleado
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def update(self, corte):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            UPDATE "CorteCaja"
            SET fecha = %s,
                horaApertura = %s,
                horaCierre = %s,
                montoInicial = %s,
                montoFinal = %s,
                idEmpleado = %s
            WHERE id = %s
        """

        cursor.execute(sql, (
            corte.fecha,
            corte.horaApertura,
            corte.horaCierre,
            corte.montoInicial,
            corte.montoFinal,
            corte.idEmpleado,
            corte.id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def delete(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('DELETE FROM "CorteCaja" WHERE id = %s', (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT MAX(id) FROM "CorteCaja"')
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0

        return resultado[0]