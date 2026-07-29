class Empleado:

    def __init__(self, id, nombre, apellidos, telefono, correo, usuario, contrasena, puesto):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.correo = correo
        self.usuario = usuario
        self.contrasena = contrasena
        self.puesto = puesto

    def info(self):
        return f"ID: {self.id} \nNombre: {self.nombre} {self.apellidos} \nTelefono: {self.telefono} \nCorreo: {self.correo} \nUsuario: {self.usuario} \nPuesto: {self.puesto}"