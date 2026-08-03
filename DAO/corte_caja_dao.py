from database.conexion import Conexion
from models.corte_caja import CorteCaja


class CorteCajaDAO:

    def obtener(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM corte_caja')
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
            INSERT INTO corte_caja
            (fecha, hora_apertura, hora_cierre, monto_inicial, monto_final, id_empleado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
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
            UPDATE corte_caja
            SET fecha = %s,
                hora_apertura = %s,
                hora_cierre = %s,
                monto_inicial = %s,
                monto_final = %s,
                id_empleado = %s
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

        cursor.execute('DELETE FROM corte_caja WHERE id = %s', (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT MAX(id) FROM corte_caja')
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0

        return resultado[0]

    #? carga los datos de la tabla corte de caja
    def cargar_datos(self, filtro="TODO"):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT 
                cc.id,
                cc.fecha,
                cc.hora_apertura,
                cc.hora_cierre,
                cc.monto_inicial,
                cc.monto_final,
                e.nombre || ' ' || e.apellidos AS empleado,
                (cc.monto_final - cc.monto_inicial) AS total_ventas
            FROM corte_caja cc
            JOIN empleados e ON e.id = cc.id_empleado
        """

        if filtro == "ABIERTOS":
            sql += " WHERE cc.hora_cierre IS NULL"
        elif filtro == "CERRADOS":
            sql += " WHERE cc.hora_cierre IS NOT NULL"
        elif filtro == "DIA":
            sql += " WHERE cc.fecha = CURRENT_DATE"

        sql += " ORDER BY cc.fecha DESC, cc.hora_apertura DESC"

        cursor.execute(sql)
        registros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return registros