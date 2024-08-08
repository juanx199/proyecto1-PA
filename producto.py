class Producto:
    def __init__(self, fecha_caducidad, numero_lote):
        self.fecha_caducidad = fecha_caducidad
        self.numero_lote = numero_lote

    def set_fecha_caducidad(self, fecha_caducidad):
        self.fecha_caducidad = fecha_caducidad

    def get_fecha_caducidad(self):
        return self.fecha_caducidad

    def set_numero_lote(self, numero_lote):
        self.numero_lote = numero_lote

    def get_numero_lote(self):
        return self.numero_lote

    def mostrar_info(self):
        return f"Fecha de Caducidad: {self.fecha_caducidad}, Número de Lote: {self.numero_lote}"