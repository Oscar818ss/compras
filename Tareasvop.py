# Clase base para los productos
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.__nombre = nombre  # Encapsulación
        self.__precio = precio  # Encapsulación
        self.__categoria = categoria  # Encapsulación

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_categoria(self):
        return self.__categoria

    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Precio: ${self.__precio:.2f}, Categoría: {self.__categoria}"


# Herencia: Clase para camisas que hereda de Producto
class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio, "Camisa")  # Llama al constructor de la clase base
        self.__talla = talla  # Atributo específico de Camisa

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self.__talla}"


# Herencia: Clase para pantalones
class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio, "Pantalón")
        self.__talla = talla

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self.__talla}"


# Herencia: Clase para zapatos
class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio, "Zapato")
        self.__talla = talla

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self.__talla}"


# Clase carrito que gestiona los productos seleccionados para la compra
class Carrito:
    def __init__(self):
        self.__items = []  # Lista de productos en el carrito

    def agregar_al_carrito(self, producto):
        self.__items.append(producto)
        print(f"{producto.get_nombre()} ha sido agregado al carrito.")

    def mostrar_carrito(self):
        if not self.__items:
            print("El carrito está vacío.")
            return
        print("Productos en el carrito:")
        for item in self.__items:
            print(item.mostrar_info())

    def calcular_total(self):
        total = sum(item.get_precio() for item in self.__items)
        print(f"Total a pagar: ${total:.2f}")


# Clase tienda que gestiona los productos
class Tienda:
    def __init__(self):
        self.__productos = []  # Lista de productos en la tienda

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_productos(self):
        if not self.__productos:
            print("No hay productos disponibles.")
            return
        for idx, producto in enumerate(self.__productos, 1):
            print(f"{idx}. {producto.mostrar_info()}")


# Clase principal para manejar la lógica de compra
class SistemaCompras:
    def __init__(self):
        self.__tienda = Tienda()
        self.__carrito = Carrito()

    def iniciar(self):
        # Agregar productos a la tienda
        self.__tienda.agregar_producto(Camisa("Camisa Casual", 20.0, "M"))
        self.__tienda.agregar_producto(Pantalon("Pantalón Jeans", 30.0, "L"))
        self.__tienda.agregar_producto(Zapato("Zapatos de Cuero", 50.0, "42"))

        # Mostrar productos
        print("Productos disponibles:")
        self.__tienda.mostrar_productos()

        # Interacción básica para agregar productos al carrito
        while True:
            try:
                opcion = int(input("Selecciona el número del producto a agregar al carrito (0 para salir): "))
                if opcion == 0:
                    break
                if 1 <= opcion <= len(self.__tienda._Tienda__productos):
                    producto = self.__tienda._Tienda__productos[opcion - 1]
                    self.__carrito.agregar_al_carrito(producto)
                else:
                    print("Opción no válida. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número.")

        # Mostrar el carrito y calcular total
        self.__carrito.mostrar_carrito()
        self.__carrito.calcular_total()


# Ejecutar el sistema de compras
if __name__ == "__main__":
    sistema = SistemaCompras()
    sistema.iniciar()
