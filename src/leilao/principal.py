from src.leilao.dominio import Avaliador, Leilao, Lance, Usuario


gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_gui = Lance(gui, 150.0)
lance_yuri = Lance(yuri, 100.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_gui)
leilao.lances.append(lance_yuri)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de R$ {lance.valor}')

avaliador = Avaliador()
avaliador.avaliar(leilao)
print(
    f'O menor lance foi de {avaliador.menor_lance} e o maior de {avaliador.maior_lance}')
