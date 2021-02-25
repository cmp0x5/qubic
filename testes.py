import pytest
import tab
import checa
import jogadores

def testa_checa_tabuleiro1():
	#Aqui, o X ganhou numa diagonal entre andares
	tab1=[[['O','','','X'],['X','','',''],['','X','O','X'],['O','','','']],[['','','',''],['','X','','X'],['','','',''],['','','','']],[['O','O','','O'],['','','X',''],['O','','X',''],['','','','']],[['','X','X','O'],['','','','X'],['','X','',''],['','','','X']]]
	
	assert checa.checa_tabuleiro(tab1) == ('X', [5, 22, 39, 56])


def testa_checa_tabuleiro2():
	#Aqui, nenhum jogador ainda ganhou
	tab1=[[['O','','','X'],['X','','',''],['','X','O','X'],['O','','','']],[['','','',''],['','X','','X'],['','','',''],['','','','']],[['O','O','','O'],['','','X',''],['O','','X',''],['','','','']],[['','X','X','O'],['','','',''],['','X','',''],['','','','X']]]
	
	assert checa.checa_tabuleiro(tab1) == None


def testa_checa_tabuleiro3():
	#Aqui, o jogador ganhou em uma horizontal dentro de um andar
	tab1=[[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['X','','',''],['X','','',''],['X','','',''],['X','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
	
	assert checa.checa_tabuleiro(tab1) == ('X', [33, 37, 41, 45])


def testa_insereItem():
	testeTab = tab.Tabuleiro()
	
	testeTab.insereItem('X',1)
	testeTab.insereItem('X',2)
	testeTab.insereItem('X',3)
	testeTab.insereItem('X',4)
	
	assert checa.checa_tabuleiro(testeTab.tab) == ('X', [1, 2, 3, 4])


def testa_reiniciaTab():
	testeTab = tab.Tabuleiro()
	
	testeTab.insereItem('X',11)
	testeTab.insereItem('X',22)
	testeTab.insereItem('X',33)
	testeTab.insereItem('X',44)
	
	testeTab.reiniciaTab()
	
	tabuleiro_vazio=[[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
	
	assert testeTab.tab == tabuleiro_vazio


def testa_JogadorAleatorio1():
	# Aqui, apenas testaremos se o jogador está realizando jogadas válidas,
	# uma vez que ele joga aleatoriamente.
	
	testeTab = tab.Tabuleiro()
	testeTab.tab=[[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
	jogador_aleatorio = jogadores.JogadorAleatorio(testeTab, "X")

	for i in range(8000):
		jogada = jogador_aleatorio.joga_aleatoriamente()
		x, y, z = checa.posicao(jogada)
		assert jogador_aleatorio.tabuleiro[x][y][z] == ""


def testa_JogadorAleatorio2():
	# Aqui, apenas testaremos se o jogador está realizando jogadas válidas,
	# uma vez que ele joga aleatoriamente.
	
	testeTab = tab.Tabuleiro()
	testeTab.tab=[[['O','','','X'],['X','','',''],['','X','O','X'],['O','','','']],[['','','',''],['','X','','X'],['','','',''],['','','','']],[['O','O','','O'],['','','X',''],['O','','X',''],['','','','']],[['','X','X','O'],['','','',''],['','X','',''],['','','','X']]]
	jogador_aleatorio = jogadores.JogadorAleatorio(testeTab, "X")

	for i in range(8000):
		jogada = jogador_aleatorio.joga_aleatoriamente()
		x, y, z = checa.posicao(jogada)
		assert jogador_aleatorio.tabuleiro[x][y][z] == ""


def testa_JogadorSequencial1():
	# Como jogador_sequencial é deterministico, 
	# não precisamos o testar mais de uma vez

	testeTab = tab.Tabuleiro()
	testeTab.tab=[[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
	jogador_sequencial = jogadores.JogadorSequencial(testeTab, "X")
	
	jogada = jogador_sequencial.joga_sequencialmente()
	assert jogada == 1


def testa_JogadorSequencial2():
	# Como jogador_sequencial é deterministico, 
	# não precisamos o testar mais de uma vez

	testeTab = tab.Tabuleiro()
	testeTab.tab=[[['O','','','X'],['X','','',''],['','X','O','X'],['O','','','']],[['','','',''],['','X','','X'],['','','',''],['','','','']],[['O','O','','O'],['','','X',''],['O','','X',''],['','','','']],[['','X','X','O'],['','','',''],['','X','',''],['','','','X']]]
	jogador_sequencial = jogadores.JogadorSequencial(testeTab, "X")
	
	jogada = jogador_sequencial.joga_sequencialmente()
	assert jogada == 2


def testa_JogadorEsperto1():
	# Como jogador_esperto é deterministico, 
	# não precisamos o testar mais de uma vez
	#
	# Aqui utilizaremos a dificuldade 0 para tornarmos o teste menos
	# computacionalmente intenso, mas manteremos o parâmetro calculaMetade = 0
	
	testeTab = tab.Tabuleiro()
	testeTab.tab=[[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
	jogador_esperto = jogadores.JogadorEsperto(testeTab, "X")
	jogador_esperto.definir_dificuldade(0)
	
	jogada = jogador_esperto.joga_esperto(0)
	x, y, z = checa.posicao(jogada)
	assert jogador_esperto.tabuleiro[x][y][z] == ""


def testa_JogadorEsperto2():
	# Como jogador_esperto é deterministico, 
	# não precisamos o testar mais de uma vez
	#
	# Aqui utilizaremos a dificuldade 1 para tornarmos 
	# o teste menos computacionalmente intenso
	
	testeTab = tab.Tabuleiro()
	testeTab.tab=[[['O','','','X'],['X','','',''],['','X','O','X'],['O','','','']],[['','','',''],['','X','','X'],['','','',''],['','','','']],[['O','O','','O'],['','','X',''],['O','','X',''],['','','','']],[['','X','X','O'],['','','',''],['','X','',''],['','','','X']]]
	jogador_esperto = jogadores.JogadorEsperto(testeTab, "X")
	jogador_esperto.definir_dificuldade(0)
	
	jogada = jogador_esperto.joga_esperto(0)
	x, y, z = checa.posicao(jogada)
	assert jogador_esperto.tabuleiro[x][y][z] == ""


if __name__=="__main__":
	
	testa_checa_tabuleiro1()
	testa_checa_tabuleiro2()
	testa_checa_tabuleiro3()
	
	testa_JogadorAleatorio1()
	testa_JogadorAleatorio2()
	
	testa_JogadorSequencial1()
	testa_JogadorSequencial2()
	
	testa_JogadorEsperto1()
	testa_JogadorEsperto2()
		
	testa_insereItem()
	testa_reiniciaTab()
	
	print("Passou nos testes!")
