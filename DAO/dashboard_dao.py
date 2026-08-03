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