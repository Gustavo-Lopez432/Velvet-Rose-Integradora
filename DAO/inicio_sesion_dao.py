from database.conexion import Conexion
from models.empleado import Empleado

class InicioSesionDAO:
    
    def validar_usuario(self, usuario, contrasena):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            '''
            SELECT usuario, contrasena
            FROM empleados
            WHERE usuario = %s AND contrasena = %s
            ''',
            (usuario, contrasena)
        )

        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        return registro