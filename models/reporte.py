
class Reporte:

    def __init__(self, id, tipoReporte, fechaInicio, fechaFin, numeroVentas, productosVendidos, productoMasVendido):
        self.id = id
        self.tipoReporte = tipoReporte
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.numeroVentas = numeroVentas
        self.productosVendidos = productosVendidos
        self.productoMasVendido = productoMasVendido

    def info(self):
        return f"ID: {self.id} \n Tipo de reporte: {self.tipoReporte} \n Fecha de inicio: {self.fechaInicio} \n Fecha de fin: {self.fechaFin} \n Numero de ventas: {self.numeroVentas} \n Productos vendidos: {self.productosVendidos}"