from random import randint
from checa import posicao, checa_tabuleiro

# Funções auxiliares, que definem as jogadas do computador num jogo
# usuário vs computador.

class Jogador:
	
	def __init__(
		self,
		tabuleiro,
		marcador
		):
	
		self.tabuleiro = tabuleiro.tab
		self.marcador = marcador
	
class JogadorAleatorio(Jogador):
	
	def joga_aleatoriamente(
		self
		):
		"""
		Recebe o tabuleiro, e o marcador usado pelo computador, e escolhe
		e retorna uma jogada válida aleatoriamente, sem levar em consideração
		nenhuma jogada futura.
		"""
		
		jogada = randint(1, 64)
		i, j, k = posicao(jogada)
		
		while self.tabuleiro[i][j][k] != '':
			jogada = randint(1, 64)
			i, j, k = posicao(jogada)
			
		return jogada
		
			
class JogadorSequencial(Jogador):
	
	def joga_sequencialmente(
		self
		):
		"""
		Recebe o tabuleiro, e o marcador usado pelo computador, e escolhe
		e retorna a jogada de menor número que é considerada válida.
		"""
		for jogada in range(1, 65):
			i, j, k = posicao(jogada);
			if self.tabuleiro[i][j][k] == '':
				return jogada

class JogadorEsperto(Jogador):
	
	def definir_dificuldade(
		self,
		dificuldade
		):
		self.dificuldade = dificuldade
	
	def joga_esperto(
		self,
		calculaMetade
		):
		"""
		Recebe o tabuleiro, e o marcador usado pelo computador, e escolhe
		e retorna a "melhor" jogada possivel para aquela dificuldade.
		
		Essa função é baseada no algortmo minmax, todavia dada a complexidade do jogo,
		para que ela possa calcular duas jogadas no futuro, ela toma em média entre 1 e 2
		minutos para ser executada.
		"""
		
		for jogada in range(1, 65):
			melhorPontuação = -999999999
			i, j, k = posicao(jogada)
			if self.tabuleiro[i][j][k] == "":
				self.tabuleiro[i][j][k] = self.marcador
				if self.marcador == "X": pontuação = self.minmax(0, False, "O", calculaMetade)
				else: pontuação = self.minmax(0, False, "X", calculaMetade)
				
				self.tabuleiro[i][j][k] = ""
				if pontuação > melhorPontuação:
					melhorPontuação = pontuação
					movimento = jogada
		
		return movimento
	
	def minmax(
		self,
		profundidade,
		estaMaximizando,
		marcador,
		calculaMetade
		):
		"""
		Função auxiliar de joga_esperto()
		"""
		
		#Checamos se o jogo acabou
		resultado = checa_tabuleiro(self.tabuleiro);
		if resultado != None:
			if resultado[0] == marcador: return 10
			elif resultado[0] != marcador: return -10
		
		if profundidade > self.dificuldade: return 0
		
		if estaMaximizando:
			melhorPontuação = -999999999
			passo = 1
			if calculaMetade: passo = 2
			for jogada in range(1, 65, passo):
				i, j, k = posicao(jogada)
				if self.tabuleiro[i][j][k] == "":
					self.tabuleiro[i][j][k] = marcador
					if marcador == "X": pontuação = self.minmax(profundidade + 1, False, "O", calculaMetade)
					else: pontuação = self.minmax(profundidade + 1, False, "X", calculaMetade)
					self.tabuleiro[i][j][k] = ""
					melhorPontuação = max(pontuação, melhorPontuação)
			
			return melhorPontuação
		
		elif not estaMaximizando:
			melhorPontuação = 999999999
			passo = 1
			if calculaMetade: passo = 2
			for jogada in range(1, 65, passo):
				i, j, k = posicao(jogada)
				if self.tabuleiro[i][j][k] == "":
					self.tabuleiro[i][j][k] = marcador
					if marcador == "X": pontuação = self.minmax(profundidade + 1, True, "O", calculaMetade)
					else: pontuação = self.minmax(profundidade + 1, True, "X", calculaMetade)
					self.tabuleiro[i][j][k] = ""
					melhorPontuação = min(pontuação, melhorPontuação)
			
			return melhorPontuação
