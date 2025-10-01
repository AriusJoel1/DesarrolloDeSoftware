import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

def test_aplicar_cupon_con_limite():
    carrito = Carrito()
    producto = ProductoFactory(nombre="Producto", precio=200.00)
    carrito.agregar_producto(producto, cantidad=2)  # Total = 400
    total_con_cupon = carrito.aplicar_cupon(20, 50)
    assert total_con_cupon == 350.00