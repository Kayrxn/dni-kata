from test.dni_correctos import CASOS_TEST_CORRECTOS
from test.dni_incorrectos import CASOS_TEST_LETRA_PROHIBIDA
from test.dni_formato_incorrecto import CASOS_TEST_FORMATO_INCORRECTO
import pytest
from src.dni import Dni


@pytest.fixture(name="dni")
def inyector():
    return Dni()


def test_constructor_default(dni):
    assert dni.obtener_dni() == ""
    assert not dni.obtener_numero_sano()
    assert not dni.obtener_letra_sana()


def test_setters_getters(dni):
    dni.establecer_dni("12345678Z")
    assert dni.obtener_dni() == "12345678Z"


@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_check_cif_correcto(dni, dni_test):
    dni.establecer_dni(dni_test)
    assert dni.comprobar_formato()


@pytest.mark.parametrize("dni_test", CASOS_TEST_LETRA_PROHIBIDA)
def test_check_cif_incorrecto(dni, dni_test):
    dni.establecer_dni(dni_test)
    assert not dni.comprobar_formato()


@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_check_dni_correcto(dni, dni_test):
    dni.establecer_dni(dni_test)
    assert dni.comprobar_validez()


@pytest.mark.parametrize("dni_test", CASOS_TEST_FORMATO_INCORRECTO)
def test_check_dni_incorrecto(dni, dni_test):
    dni.establecer_dni(dni_test)
    assert not dni.comprobar_validez()


@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_check_letra_correcta(dni, dni_test):
    dni.establecer_dni(dni_test)
    dni.comprobar_validez()  # Necesario para establecer numeroSano
    assert dni.comprobar_letra()


@pytest.mark.parametrize("dni_test", CASOS_TEST_LETRA_PROHIBIDA)
def test_check_letra_incorrecta(dni, dni_test):
    dni.establecer_dni(dni_test)
    dni.comprobar_validez()  # Necesario para establecer numeroSano
    assert not dni.comprobar_letra()


@pytest.mark.parametrize("dni_test", CASOS_TEST_FORMATO_INCORRECTO)
def test_check_letra_numero_mal_formateado(dni, dni_test):
    dni.establecer_dni(dni_test)
    dni.comprobar_validez()  # Necesario para establecer numeroSano
    assert not dni.comprobar_letra()


@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_obtener_letra_correcta(dni, dni_test):
    dni.establecer_dni(dni_test)
    dni.comprobar_validez()  # Necesario para establecer numeroSano
    assert dni.obtener_letra() == dni_test[-1]


def test_obtener_letra_sin_numero_sano(dni):
    dni.establecer_dni("1234567X")  # DNI con longitud incorrecta
    assert dni.obtener_letra() is None


def test_parte_alfabetica_dni(dni):
    dni.establecer_dni("12345678Z")
    assert dni.obtener_parte_alfabetica() == "Z"


def test_parte_numerica_dni(dni):
    dni.establecer_dni("12345678Z")
    dni.comprobar_validez()  # Necesario para establecer numeroSano
    assert dni.obtener_parte_numerica() == "12345678"


def test_parte_numerica_dni_sin_numero_sano(dni):
    dni.establecer_dni("1234567")  # DNI incompleto
    assert not dni.obtener_parte_numerica()
