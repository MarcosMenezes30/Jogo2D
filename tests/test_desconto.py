import pytest
from src.desconto import DescontoNormal, DescontoVIP, DescontoPremium

@pytest.mark.parametrize("valor, esperado", [
    (100, 30),
    (200, 60),
    (300, 90)
])
def test_desconto_premium(valor, esperado):
    desconto = DescontoPremium()
    resultado = desconto.calcular(valor)

    assert resultado == esperado
