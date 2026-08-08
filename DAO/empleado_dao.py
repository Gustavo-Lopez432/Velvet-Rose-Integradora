from database.conexion import Conexion
from models.empleado import Empleado


class EmpleadoDAO:

    def obtener(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM empleados')
        registros = cursor.fetchall()

        empleados = []

        for registro in registros:
            empleado = Empleado(
                id=registro[0],
                nombre=registro[1],
                apellidos=registro[2],
                telefono=registro[3],
                correo=registro[4],
                usuario=registro[5],
                contrasena=registro[6],
                puesto=registro[7],
                estado=registro[8]
            )

            empleados.append(empleado)

        cursor.close()
        conexion.close()

        return empleados

    def insert(self, empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO empleados
            (nombre, apellidos, telefono, correo, usuario, contrasena, puesto)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            empleado.nombre,
            empleado.apellidos,
            empleado.telefono,
            empleado.correo,
            empleado.usuario,
            empleado.contrasena,
            empleado.puesto
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def update(self, empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            UPDATE empleados
            SET nombre = %s,
                apellidos = %s,
                telefono = %s,
                correo = %s,
                usuario = %s,
                contrasena = %s,
                puesto = %s
            WHERE id = %s
        """

        cursor.execute(sql, (
            empleado.nombre,
            empleado.apellidos,
            empleado.telefono,
            empleado.correo,
            empleado.usuario,
            empleado.contrasena,
            empleado.puesto,
            empleado.id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def delete(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('DELETE FROM empleados WHERE id = %s', (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def cambiar_estado(self, id, nuevo_estado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = "UPDATE empleados SET estado = %s WHERE id = %s"

        cursor.execute(sql, (nuevo_estado, id))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute('SELECT MAX(id) FROM empleados')
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0

        return resultado[0]

    #? carga los datos de la tabla empleado
    def cargar_datos(self, filtro="TODO"):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT 
                id,
                nombre,
                apellidos,
                telefono,
                correo,
                usuario,
                contrasena,
                puesto,
                estado
            FROM empleados
        """

        if filtro == "VENDEDORES":
            sql += " WHERE puesto = 'Vendedor'"
        elif filtro == "ADMINISTRADORES":
            sql += " WHERE puesto = 'Administrador'"

        sql += " ORDER BY nombre ASC, apellidos ASC"

        cursor.execute(sql)
        registros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return registros
