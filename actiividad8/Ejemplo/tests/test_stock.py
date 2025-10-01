import pytest
from src.carrito import Carrito, Producto

def test_agregar_producto_excede_stock():
    producto = Producto("ProductoStock", 100.00,stock=5)
    producto.stock = 5
    carrito = Carrito()
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto, cantidad=6)