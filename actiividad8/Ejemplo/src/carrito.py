# src/carrito.py

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio}, stock={self.stock})"


class ItemCarrito:
    def __init__(self, producto, cantidad=1):
        self.producto = producto
        self.cantidad = cantidad

    def total(self):
        return self.producto.precio * self.cantidad

    def __repr__(self):
        return f"ItemCarrito({self.producto}, cantidad={self.cantidad})"


class Carrito:
    def __init__(self):
        self.items = []

    def vaciar(self):
        self.items = []

    def _buscar_item(self, producto):
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                return item
        return None

    def agregar_producto(self, producto, cantidad=1):
        """
        Agrega un producto al carrito, validando stock.
        """
        item = self._buscar_item(producto)
        cantidad_actual = item.cantidad if item else 0
        if cantidad_actual + cantidad > producto.stock:
            raise ValueError("Cantidad a agregar excede el stock disponible")
        if item:
            item.cantidad += cantidad
        else:
            self.items.append(ItemCarrito(producto, cantidad))

    def remover_producto(self, producto, cantidad=1):
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if item.cantidad > cantidad:
                    item.cantidad -= cantidad
                elif item.cantidad == cantidad:
                    self.items.remove(item)
                else:
                    raise ValueError("Cantidad a remover es mayor que la cantidad en el carrito")
                return
        raise ValueError("Producto no encontrado en el carrito")

    def actualizar_cantidad(self, producto, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if nueva_cantidad == 0:
                    self.items.remove(item)
                else:
                    item.cantidad = nueva_cantidad
                return
        raise ValueError("Producto no encontrado en el carrito")

    def calcular_total(self):
        return sum(item.total() for item in self.items)

    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        return total * (1 - porcentaje / 100)

    def aplicar_descuento_condicional(self, porcentaje, minimo):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        return total * (1 - porcentaje / 100) if total >= minimo else total

    def calcular_impuestos(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        return self.calcular_total() * (porcentaje / 100)

    def aplicar_cupon(self, descuento_porcentaje, descuento_maximo):
        if descuento_porcentaje < 0 or descuento_maximo < 0:
            raise ValueError("Los valores de descuento deben ser positivos")
        total = self.calcular_total()
        descuento = min(total * (descuento_porcentaje / 100), descuento_maximo)
        return total - descuento

    def contar_items(self):
        return sum(item.cantidad for item in self.items)

    def obtener_items(self):
        return self.items

    def obtener_items_ordenados(self, criterio: str):
        if criterio == "precio":
            return sorted(self.items, key=lambda item: item.producto.precio)
        elif criterio == "nombre":
            return sorted(self.items, key=lambda item: item.producto.nombre)
        else:
            raise ValueError("Criterio inválido. Usa 'precio' o 'nombre'.")