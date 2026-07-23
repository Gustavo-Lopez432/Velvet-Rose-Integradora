
class Empleado:

    def __init__(self, id, nombre, aPaterno, aMaterno, telefono, rol, correo, estado, municipio, calle, numero):
        self.id = id
        self.nombre = nombre
        self.aPaterno = aPaterno
        self.aMaterno = aMaterno
        self.telefono = telefono
        self.rol = rol
        self.correo = correo
        self.estado = estado
        self.municipio = municipio
        self.calle = calle
        self.numero = numero

    def info(self):
        return f"ID: {self.id} \n Nombre: {self.nombre} \n Apellido paterno: {self.aPaterno} \n Apellido materno: {self.aMaterno} \n Telefono: {self.telefono} \n Rol: {self.rol} \n Correo: {self.correo} \n Estado: {self.estado} \n Municipio: {self.municipio} \n Calle: {self.calle} \n Numero: {self.numero}"