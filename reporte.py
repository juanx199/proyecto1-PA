from fresco import ProductoFresco
from refrigerado import ProductoRefrigerado
from congelado import ProductoCongelado

def ingresar_producto_fresco():
    fecha_caducidad = input("Ingrese la fecha de caducidad (YYYY-MM-DD): ")
    numero_lote = input("Ingrese el número de lote: ")
    fecha_envasado = input("Ingrese la fecha de envasado (YYYY-MM-DD): ")
    pais_origen = input("Ingrese el país de origen: ")
    return ProductoFresco(fecha_caducidad, numero_lote, fecha_envasado, pais_origen)

def ingresar_producto_refrigerado():
    fecha_caducidad = input("Ingrese la fecha de caducidad (YYYY-MM-DD): ")
    numero_lote = input("Ingrese el número de lote: ")
    codigo_supervision = input("Ingrese el código del organismo de supervisión alimentaria: ")
    return ProductoRefrigerado(fecha_caducidad, numero_lote, codigo_supervision)

def ingresar_producto_congelado():
    fecha_caducidad = input("Ingrese la fecha de caducidad (YYYY-MM-DD): ")
    numero_lote = input("Ingrese el número de lote: ")
    temperatura_congelacion = input("Ingrese la temperatura de congelación recomendada: ")
    return ProductoCongelado(fecha_caducidad, numero_lote, temperatura_congelacion)

def mostrar_reporte(productos):
    for producto in productos:
        print(producto.mostrar_info())

def main():
    productos = []

    while True:
        tipo_producto = input("¿Qué tipo de producto desea ingresar? (fresco/refrigerado/congelado) o 'salir' para terminar: ").strip().lower()

        if tipo_producto == 'fresco':
            producto = ingresar_producto_fresco()
        elif tipo_producto == 'refrigerado':
            producto = ingresar_producto_refrigerado()
        elif tipo_producto == 'congelado':
            producto = ingresar_producto_congelado()
        elif tipo_producto == 'salir':
            break
        else:
            print("Tipo de producto no reconocido. Inténtelo de nuevo.")
            continue

        productos.append(producto)

    print("\nReporte de Productos:")
    mostrar_reporte(productos)

if __name__ == "__main__":
    main()