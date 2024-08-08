from producto import Producto

class ProductoFresco(Producto):
    def __init__(self, fecha_caducidad, numero_lote, fecha_envasado, pais_origen):
        super().__init__(fecha_caducidad, numero_lote)
        self.fecha_envasado = fecha_envasado
        self.pais_origen = pais_origen

    def set_fecha_envasado(self, fecha_envasado):
        self.fecha_envasado = fecha_envasado

    def get_fecha_envasado(self):
        return self.fecha_envasado

    def set_pais_origen(self, pais_origen):
        self.pais_origen = pais_origen

    def get_pais_origen(self):
        return self.pais_origen

    def mostrar_info(self):
        base_info = super().mostrar_info()
        return f"{base_info}, Fecha de Envasado: {self.fecha_envasado}, País de Origen: {self.pais_origen}"