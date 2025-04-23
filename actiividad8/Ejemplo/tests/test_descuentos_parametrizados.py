import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

@pytest.mark.parametrize("porcentaje, total_esperado", [
    (10, 100.0),
    (20, 200.0),
    (0, 0.0),
    (100, 1000.0),
])
def test_aplicar_descuento_parametrizado(porcentaje, total_esperado):
    carrito = Carrito()
    producto = ProductoFactory(precio=1000.0)
    carrito.agregar_producto(producto)
    total_con_descuento = carrito.calcular_total() * (porcentaje / 100)
    assert total_con_descuento == total_esperado

@pytest.mark.parametrize("cantidad, stock, deberia_fallar", [
    (3, 5, False),
    (5, 5, False),
    (6, 5, True),
    (0, 5, False),
])
def test_actualizar_cantidad_parametrizado(cantidad, stock, deberia_fallar):
    carrito = Carrito()
    producto = ProductoFactory(stock=stock)
    if deberia_fallar:
        with pytest.raises(ValueError):
            carrito.agregar_producto(producto, cantidad=cantidad)
    else:
        carrito.agregar_producto(producto, cantidad=cantidad)
        assert True
