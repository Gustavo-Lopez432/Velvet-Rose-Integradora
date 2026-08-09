from database.conexion import Conexion

class InicioSesionDAO:

    def validar_usuario(self, usuario, contrasena):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        try:
            cursor.execute(
                '''
                SELECT id, nombre, apellidos, usuario, puesto, estado
                FROM empleados
                WHERE usuario = %s AND contrasena = %s
                ''',
                (usuario, contrasena)
            )

            registro = cursor.fetchone()

            if registro is None:
                return None

            if registro[5] != "Activo":
                return "INACTIVO"

            return registro

        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()