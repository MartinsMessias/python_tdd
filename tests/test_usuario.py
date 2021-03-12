from src.leilao.dominio import Usuario, Leilao

import pytest

from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def vini():
    return Usuario('Vini', 100)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):
    vini.propor_lance(leilao, 50)
    assert vini.carteira == 50

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_valor_da_carteira(vini, leilao):
    vini.propor_lance(leilao, 1)
    assert vini.carteira == 99

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(vini, leilao):
    vini.propor_lance(leilao, 100)
    assert vini.carteira == 0

def test_nao_deve_permitir_propor_lance_quando_o_valor_e_maior_ao_valor_da_carteira(vini, leilao):
    with pytest.raises(LanceInvalido):
        vini.propor_lance(leilao, 200)
