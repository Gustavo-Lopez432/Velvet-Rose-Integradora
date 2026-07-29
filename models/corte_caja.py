class CorteCaja:

    def __init__(self, id, fecha, horaApertura, horaCierre, montoInicial, montoFinal, idEmpleado):
        self.id = id
        self.fecha = fecha
        self.horaApertura = horaApertura
        self.horaCierre = horaCierre
        self.montoInicial = montoInicial
        self.montoFinal = montoFinal
        self.idEmpleado = idEmpleado

    def info(self):
        return f"ID: {self.id} \nFecha: {self.fecha} \nHora de Apertura: {self.horaApertura} \nHora de Cierre: {self.horaCierre} \nMonto Inicial: {self.montoInicial} \nMonto Final: {self.montoFinal} \nID Empleado: {self.idEmpleado}"