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
    def resumen_ventas(self, filtro="Semana"):
    
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
    
        if filtro == "Semana":
        
            sql = """
                SELECT
                    DATE(fecha) AS periodo,
                    COALESCE(SUM(total), 0) AS ventas
                FROM ventas
                WHERE fecha >= CURRENT_DATE - INTERVAL '6 days'
                GROUP BY DATE(fecha)
                ORDER BY periodo
            """
    
        elif filtro == "Mes":
        
            sql = """
                SELECT
                    DATE(fecha) AS periodo,
                    COALESCE(SUM(total), 0) AS ventas
                FROM ventas
                WHERE fecha >= CURRENT_DATE - INTERVAL '29 days'
                GROUP BY DATE(fecha)
                ORDER BY periodo
            """
    
        elif filtro == "Año":
        
            sql = """
                SELECT
                    DATE_TRUNC('month', fecha) AS periodo,
                    COALESCE(SUM(total), 0) AS ventas
                FROM ventas
                WHERE fecha >= CURRENT_DATE - INTERVAL '11 months'
                GROUP BY DATE_TRUNC('month', fecha)
                ORDER BY periodo
            """
    
        else:
        
            sql = """
                SELECT
                    DATE(fecha) AS periodo,
                    COALESCE(SUM(total), 0) AS ventas
                FROM ventas
                GROUP BY DATE(fecha)
                ORDER BY periodo
            """
    
        cursor.execute(sql)
    
        datos = cursor.fetchall()
    
        cursor.close()
        conexion.close()
    
        return datos