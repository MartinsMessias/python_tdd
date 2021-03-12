from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui', 500)
        self.yuri = Usuario('Yuri', 500)

        self.lance_yuri = Lance(self.yuri, 200.0)
        self.lance_gui = Lance(self.gui, 100.0)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propor(self.lance_gui)
        self.leilao.propor(self.lance_yuri)

        menor_valor_esperado = 100
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propor(self.lance_yuri)
            self.leilao.propor(self.lance_gui)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_tiver_um_lance(self):
        self.leilao.propor(self.lance_gui)

        quantidade_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(1, quantidade_lances_recebidos)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_o_leilao_tiver_tres_lances(self):
        vini = Usuario('Vini', 500)
        lance_vini = Lance(vini, 300.0)

        self.leilao.propor(self.lance_gui)
        self.leilao.propor(self.lance_yuri)
        self.leilao.propor(lance_vini)

        menor_valor_esperado = 100
        maior_valor_esperado = 300

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tiver_lances(self):
        self.leilao.propor(self.lance_gui)

        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500)
        lance_yuri = Lance(yuri, 300.0)

        self.leilao.propor(self.lance_gui)
        self.leilao.propor(lance_yuri)

        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances_recebido)

    def test_nao_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_o_mesmo(self):
        segundo_lance_gui = Lance(self.gui, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propor(self.lance_gui)
            self.leilao.propor(segundo_lance_gui)