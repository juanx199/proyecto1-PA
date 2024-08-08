from producto import Producto

class ProductoRefrigerado(Producto):
    def __init__(self, fecha_caducidad, numero_lote, codigo_supervision):
        super().__init__(fecha_caducidad, numero_lote)
        self.codigo_supervision = codigo_supervision

    def set_codigo_supervision(self, codigo_supervision):
        self.codigo_supervision = codigo_supervision

    def get_codigo_supervision(self):
        return self.codigo_supervision

    def mostrar_info(self):
        base_info = super().mostrar_info()
        return f"{base_info}, Código de Supervisión: {self.codigo_supervision}"