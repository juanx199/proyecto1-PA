from producto import Producto

class ProductoCongelado(Producto):
    def __init__(self, fecha_caducidad, numero_lote, temperatura_congelacion):
        super().__init__(fecha_caducidad, numero_lote)
        self.temperatura_congelacion = temperatura_congelacion

    def set_temperatura_congelacion(self, temperatura_congelacion):
        self.temperatura_congelacion = temperatura_congelacion

    def get_temperatura_congelacion(self):
        return self.temperatura_congelacion

    def mostrar_info(self):
        base_info = super().mostrar_info()
        return f"{base_info}, Temperatura de Congelación Recomendada: {self.temperatura_congelacion}"