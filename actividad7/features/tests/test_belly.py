# tests/test_belly.py


import pytest
from src.belly import Belly

@pytest.fixture
def belly():
    # Esta función de fijación crea una instancia de Belly antes de cada prueba
    return Belly()

def test_comer_pepinos(belly):
    belly.comer(10)
    assert belly.pepinos_comidos == 10

def test_esperar(belly):
    belly.comer(10)
    belly.esperar(1.5)  # Esperamos 1.5 horas
    assert belly.tiempo_esperado == 1.5

def test_esta_gruñendo(belly):
    belly.comer(15)
    belly.esperar(2)  # Esperamos 2 horas
    assert belly.esta_gruñendo()  # Debería gruñir, porque tiene más de 10 pepinos y 1.5 horas

def test_no_esta_gruñendo(belly):
    belly.comer(5)
    belly.esperar(2)  # Esperamos 2 horas
    assert not belly.esta_gruñendo()  # No debería gruñir, porque tiene menos de 10 pepinos

def test_esperar_menos_de_una_hora(belly):
    belly.comer(20)
    belly.esperar(0.5)  # Esperamos 30 minutos
    assert not belly.esta_gruñendo()  # No debería gruñir, porque no ha pasado suficiente tiempo


def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True

def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15

def test_estomago_gruñendo():
    belly = Belly()
    belly.comer(20)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True