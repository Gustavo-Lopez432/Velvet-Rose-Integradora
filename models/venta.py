class Venta:

    def __init__(self, id, fecha, folio, idEmpleado, subtotal, iva, total):
        self.id = id
        self.fecha = fecha
        self.folio = folio
        self.idEmpleado = idEmpleado
        self.subtotal = subtotal
        self.iva = iva
        self.total = total

    def info(self):
        return f"ID: {self.id} \nFecha: {self.fecha} \nFolio: {self.folio} \nID Empleado: {self.idEmpleado} \nSubtotal: {self.subtotal} \nIVA: {self.iva} \nTotal: {self.total}"