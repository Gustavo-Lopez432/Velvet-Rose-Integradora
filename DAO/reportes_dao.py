from database.conexion import Conexion


class ReportesDAO:

    #? Ventas agrupadas por día, últimos 30 días
    def ventas_por_rango(self, dias=30):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = f"""
            SELECT
                TO_CHAR(v.fecha, 'DD/MM/YY') AS dia,
                COUNT(*) AS num_ventas,
                COALESCE(SUM(v.total), 0) AS total
            FROM ventas v
            WHERE v.fecha >= CURRENT_DATE - INTERVAL '{dias} days'
            GROUP BY TO_CHAR(v.fecha, 'DD/MM/YY'), DATE(v.fecha)
            ORDER BY DATE(v.fecha) DESC
        """

        cursor.execute(sql)
        registros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return registros

    #? Top 10 productos más vendidos (por cantidad, histórico)
    def productos_mas_vendidos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT
                p.nombre,
                SUM(d.cantidad) AS total_vendido
            FROM detalle_venta d
            JOIN productos p ON p.id = d.id_producto
            GROUP BY p.nombre
            ORDER BY total_vendido DESC
            LIMIT 10
        """

        cursor.execute(sql)
        registros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return registros

    #? Ventas totales por empleado (histórico)
    def ventas_por_empleado(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT
                e.nombre || ' ' || e.apellidos AS empleado,
                COUNT(v.id) AS num_ventas,
                COALESCE(SUM(v.total), 0) AS total
            FROM empleados e
            LEFT JOIN ventas v ON v.id_empleado = e.id
            GROUP BY e.id, e.nombre, e.apellidos
            ORDER BY total DESC
        """

        cursor.execute(sql)
        registros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return registros