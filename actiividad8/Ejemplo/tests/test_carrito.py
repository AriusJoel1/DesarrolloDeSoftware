## Ejemplo de prueba
# tests/test_carrito.py

import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory

def test_agregar_producto_nuevo():
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)
    
    # Act
    carrito.agregar_producto(producto)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act
    carrito.agregar_producto(producto, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Teclado", precio=75.00)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.remover_producto(producto, cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Monitor", precio=300.00)
    carrito.agregar_producto(producto, cantidad=2)
    
    # Act
    carrito.remover_producto(producto, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Auriculares", precio=150.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=5)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto():
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Cargador", precio=25.00, stock=3)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=0)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total():
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150
    
    # Act
    total = carrito.calcular_total()
    
    # Assert
    assert total == 550.00


def test_aplicar_descuento():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Tablet", precio=500.00)
    carrito.agregar_producto(producto, cantidad=2)  # Total 1000
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(10)
    
    # Assert
    assert total_con_descuento == 900.00


def test_aplicar_descuento_limites():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)


def test_vaciar_carrito():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos.
    Act:    Se invoca vaciar() en el carrito.
    Assert: obtener_items() retorna [], calcular_total() retorna 0.
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Libro", precio=20.0)
    producto2 = ProductoFactory(nombre="Bolígrafo", precio=2.5)
    carrito.agregar_producto(producto1, cantidad=2)
    carrito.agregar_producto(producto2, cantidad=3)

    # Act
    carrito.vaciar()

    # Assert
    assert carrito.obtener_items() == []
    assert carrito.calcular_total() == 0


def test_descuento_condicional_aplicado_si_supera_minimo():
    """
    AAA:
    Arrange: Se crea un carrito con total mayor al mínimo requerido.
    Act: Se aplica un descuento condicional.
    Assert: Se verifica que el descuento se aplica correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=600.00)
    carrito.agregar_producto(producto, cantidad=1)
    # Act
    total_con_descuento = carrito.aplicar_descuento_condicional(15, minimo=500)
    # Assert
    assert total_con_descuento == 510.00  # 600 - 15%


def test_descuento_condicional_no_aplicado_si_no_supera_minimo():
    """
    AAA:
    Arrange: Se crea un carrito con total menor al mínimo requerido.
    Act: Se aplica un descuento condicional.
    Assert: Se verifica que el total permanece sin descuento.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Mouse", precio=100.00)
    carrito.agregar_producto(producto, cantidad=1)
    # Act
    total_con_descuento = carrito.aplicar_descuento_condicional(15, minimo=500)
    # Assert
    assert total_con_descuento == 100.00

def test_agregar_producto_respetando_stock():
    """
    AAA:
    Arrange: Se crea un carrito y un producto con stock suficiente.
    Act: Se agrega una cantidad menor o igual al stock.
    Assert: Se verifica que se agrega correctamente.
    """
    # Arrange
    producto = ProductoFactory(nombre="Tablet", precio=250.00, stock=5)
    carrito = Carrito()

    # Act
    carrito.agregar_producto(producto, cantidad=3)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_agregar_producto_superando_stock_lanza_excepcion():
    """
    AAA:
    Arrange: Se crea un carrito y un producto con stock limitado.
    Act: Se intenta agregar una cantidad superior al stock.
    Assert: Se lanza una excepción por falta de stock.
    """
    # Arrange
    producto = ProductoFactory(nombre="Smartwatch", precio=180.00, stock=2)
    carrito = Carrito()
    carrito.agregar_producto(producto, cantidad=2)  # Llenamos el stock

    # Act & Assert
    with pytest.raises(ValueError, match="Cantidad a agregar excede el stock disponible"):
        carrito.agregar_producto(producto, cantidad=1)

def test_obtener_items_ordenados_por_precio():
    """
    AAA:
    Arrange: Se agregan varios productos con precios distintos al carrito.
    Act: Se obtiene la lista ordenada por precio.
    Assert: Se verifica el orden correcto.
    """
    carrito = Carrito()
    p1 = ProductoFactory(nombre="Producto A", precio=30.0, stock=10)
    p2 = ProductoFactory(nombre="Producto B", precio=10.0, stock=10)
    p3 = ProductoFactory(nombre="Producto C", precio=20.0, stock=10)

    carrito.agregar_producto(p1)
    carrito.agregar_producto(p2)
    carrito.agregar_producto(p3)

    items_ordenados = carrito.obtener_items_ordenados("precio")
    precios = [item.producto.precio for item in items_ordenados]
    
    assert precios == sorted(precios)


def test_obtener_items_ordenados_por_nombre():
    """
    AAA:
    Arrange: Se agregan varios productos con nombres distintos al carrito.
    Act: Se obtiene la lista ordenada por nombre.
    Assert: Se verifica el orden alfabético.
    """
    carrito = Carrito()
    p1 = ProductoFactory(nombre="Zanahoria", precio=10.0, stock=10)
    p2 = ProductoFactory(nombre="Manzana", precio=10.0, stock=10)
    p3 = ProductoFactory(nombre="Banana", precio=10.0, stock=10)

    carrito.agregar_producto(p1)
    carrito.agregar_producto(p2)
    carrito.agregar_producto(p3)

    items_ordenados = carrito.obtener_items_ordenados("nombre")
    nombres = [item.producto.nombre for item in items_ordenados]

    assert nombres == sorted(nombres)


def test_obtener_items_ordenados_con_criterio_invalido():
    """
    AAA:
    Arrange: Se crea un carrito vacío.
    Act & Assert: Se intenta ordenar con un criterio inválido.
    """
    carrito = Carrito()
    with pytest.raises(ValueError, match="Criterio inválido"):
        carrito.obtener_items_ordenados("peso")

# 
def test_agregar_producto_al_carrito(carrito, producto_generico):
    carrito.agregar_producto(producto_generico, cantidad=2)
    assert len(carrito.items) == 1
    assert carrito.items[0].cantidad == 2


def test_no_agregar_mas_del_stock_disponible(carrito):
    producto = ProductoFactory(nombre="Limitado", precio=50.0, stock=3)
    carrito.agregar_producto(producto, cantidad=3)
    with pytest.raises(ValueError, match="Cantidad a agregar excede el stock disponible"):
        carrito.agregar_producto(producto, cantidad=1)


def test_aplicar_descuento_condicional(carrito):
    producto = ProductoFactory(precio=300.0, stock=10)
    carrito.agregar_producto(producto, cantidad=2)
    total_con_descuento = carrito.aplicar_descuento_condicional(15, minimo=500)
    assert total_con_descuento == pytest.approx(510.0)


def test_aplicar_descuento_condicional_no_aplica(carrito):
    producto = ProductoFactory(precio=100.0, stock=10)
    carrito.agregar_producto(producto, cantidad=2)
    total = carrito.aplicar_descuento_condicional(15, minimo=500)
    assert total == 200.0


def test_obtener_items_ordenados_por_precio(carrito):
    p1 = ProductoFactory(nombre="A", precio=30.0, stock=10)
    p2 = ProductoFactory(nombre="B", precio=10.0, stock=10)
    p3 = ProductoFactory(nombre="C", precio=20.0, stock=10)

    carrito.agregar_producto(p1)
    carrito.agregar_producto(p2)
    carrito.agregar_producto(p3)

    items = carrito.obtener_items_ordenados("precio")
    precios = [item.producto.precio for item in items]
    assert precios == sorted(precios)


def test_obtener_items_ordenados_por_nombre(carrito):
    p1 = ProductoFactory(nombre="Zanahoria", precio=10.0, stock=10)
    p2 = ProductoFactory(nombre="Manzana", precio=10.0, stock=10)
    p3 = ProductoFactory(nombre="Banana", precio=10.0, stock=10)

    carrito.agregar_producto(p1)
    carrito.agregar_producto(p2)
    carrito.agregar_producto(p3)

    items = carrito.obtener_items_ordenados("nombre")
    nombres = [item.producto.nombre for item in items]
    assert nombres == sorted(nombres)


def test_obtener_items_ordenados_con_criterio_invalido(carrito):
    with pytest.raises(ValueError, match="Criterio inválido"):
        carrito.obtener_items_ordenados("peso")

