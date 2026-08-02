from database.conexion import Conexion

class DashboardDAO:

    #? obtener todas las ventas de hoy
    def ventas_hoy(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT COALESCE(SUM(total_venta), 0)
            FROM "Ventas"
            WHERE DATE(fecha_venta) = CURRENT_DATE
        """

        cursor.execute(sql)
        total = cursor.fetchone()[0]
        cursor.close()
        conexion.close()

        return total

    #? obtener total de productos en inventario
    def total_productos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT COUNT(*)
            FROM "Productos"
        """

        cursor.execute(sql)
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total

    #? obtener productos en stock bajo
    def stock_bajo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT COUNT (*)
            FROM "Productos"
            WHERE existencia_producto <= minstock_producto
        """

        cursor.execute(sql)
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total

    #? obtener total en caja
    def tota_caja(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT COALESCE(SUM(total_venta), 0)
            FROM "Ventas"
        """

        cursor.execute(sql)
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total

    #? tabla de productos mas vendidos 
    def productos_mas_vendidos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT 
                p.nombre_producto,
                p.imagen_producto,
                SUM(d.cantidad) AS Ventas
            FROM "DetalleVenta" d
            JOIN "Productos" p
                ON p.id_producto = d.id_detalleventa
            GROUP BY p.id_producto, p.nombre_producto, p.imagen_producto
            ORDER BY ventas DESC
            LIMIT 5
        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos