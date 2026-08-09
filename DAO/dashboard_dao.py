from database.conexion import Conexion

class DashboardDAO:

    #? Obtener todas las ventas de hoy
    def ventas_hoy(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT COALESCE(SUM(total), 0)
            FROM ventas
            WHERE DATE(fecha) = CURRENT_DATE
        """

        cursor.execute(sql)
        total = cursor.fetchone()[0]
        cursor.close()
        conexion.close()

        return total

    #? Obtener total de productos en inventario
    def total_productos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT COUNT(*)
            FROM productos
        """

        cursor.execute(sql)
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total

    #? Obtener productos en stock bajo
    def stock_bajo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT COUNT(*)
            FROM productos
            WHERE existencia <= min_stock
        """

        cursor.execute(sql)
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total

    #? Obtener total en caja (todas las ventas)
    def total_caja(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT COALESCE(SUM(total), 0)
            FROM ventas
        """

        cursor.execute(sql)
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total

    #? Tabla de productos más vendidos
    def productos_mas_vendidos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT 
                p.nombre AS nombre_producto,
                p.imagen AS imagen_producto,
                SUM(dv.cantidad) AS ventas
            FROM detalle_venta dv
            JOIN productos p ON p.id = dv.id_producto
            GROUP BY p.id, p.nombre, p.imagen
            ORDER BY ventas DESC
            LIMIT 5
        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos

    #? Resumen de ventas
    def resumen_ventas_hoy(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
    
        sql = """
            SELECT
                fecha,
                total
            FROM ventas
            WHERE DATE(fecha) = CURRENT_DATE
            ORDER BY fecha
        """
    
        cursor.execute(sql)
    
        datos = cursor.fetchall()
    
        cursor.close()
        conexion.close()
    
        return datos

    #? Ventas de hoy de un empleado específico
    def ventas_hoy_empleado(self, id_empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT COALESCE(SUM(total), 0)
            FROM ventas
            WHERE DATE(fecha) = CURRENT_DATE
            AND id_empleado = %s
        """

        cursor.execute(sql, (id_empleado,))
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total

    #? Número de ventas (tickets) que hizo un empleado hoy
    def numero_ventas_hoy_empleado(self, id_empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT COUNT(*)
            FROM ventas
            WHERE DATE(fecha) = CURRENT_DATE
            AND id_empleado = %s
        """

        cursor.execute(sql, (id_empleado,))
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total

    #? Resumen de ventas de hoy de un empleado específico (para la gráfica)
    def resumen_ventas_hoy_empleado(self, id_empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT
                fecha,
                total
            FROM ventas
            WHERE DATE(fecha) = CURRENT_DATE
            AND id_empleado = %s
            ORDER BY fecha
        """

        cursor.execute(sql, (id_empleado,))

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos