from math import sin, radians
from checa import posicao
import pygame


### Geometria
def x(Xo, theta, i, j): # x e y usados para calcular funções para desenhar os polígonos referentes ao tabuleiro. Olhar comentários da função renderiza_tabuleiro
	return j * (Xo/2) * pow(sin(theta), i)


def y(Xo, theta, i):
	y = 0
	for j in range(i):
		y += (Xo/2 * (0.5 * pow(sin(theta), j)))
	return y - (Xo/2)

def x_item(Xo, theta, i, j): #j = 0, 1, 2, 3 / i = 0,1,2,3  # x_item e y_item usados para calcular o ponto central dos círculos a serem desenhados
	Xo = 0.74 * Xo
	return (2*j - 3)*(Xo/3)*pow(sin(theta), i)

def y_item(Xo, theta, i): # i = 0,1,2,3
	Xo = 0.74 * Xo
	#y = Xo * sin(theta)/6
	y=0
	for j in range(i):
		y += (Xo/3 * (0.9 * pow(sin(theta), j)))
	return y - (Xo/3)

# Definir cores a serem usadas
class Cores:
	def __init__(self):
		self.branco = (255,255,255)
		self.preto = (0,0,0)
		self.vermelho = (255,0,0)
		self.verde = (0,255,0)
		self.azul = (0,0,255)
		self.dourado = (255,215,0)
		self.prata = (192,192,192)
		self.ciano = (0,255,255)


# Código driver da aplicação
class App:
	def __init__(self):
		self.rodando = False
	def setup(self):
		pygame.init()
		self.rodando = True

# Define a tela e seus elementos

class Tela:
	#menu: Menu = Menu(self, cores)
	def __init__(self, cores):
		self.Largura = 1280
		self.Altura = 960
		self.fonteJogo = pygame.font.SysFont('Courier', 20)
		self.cores = cores        
		self.display = pygame.display.set_mode((self.Largura, self.Altura)) 
		self.display.fill(cores.preto)
			   
		pygame.display.set_caption("EP4 - Jogo da Velha 3D (PyGame) - J.Renner, L.Cornetta, V.Campos")
		

	def renderiza_tabuleiro(self, larguraTabuleiro, alturaTabuleiro, display, cores):
		
		# Tabuleiro consistirá de 4 andares, cada qual em formato de losango (desenhados com pygame.draw.polygon)
		
		tamanhoCasinha = 40.0
		tamanhoTabuleiro = 4.0
		larguraTabuleiro = tamanhoCasinha * tamanhoTabuleiro
		self.larguraTabuleiro = larguraTabuleiro
 
		theta = radians(65)
		Xo = larguraTabuleiro/1.4
		self.theta = theta
		self.Xo = Xo 
		pontos = []
		
		offsetX = self.Largura/2
		offsetY = self.Altura/6
		vetorCores = [ cores.branco, cores.ciano, cores.verde, cores.vermelho ]
		
		for z in range(4):
			pontos.append([])
			for i in range(5):
				for j in range(-2,3):
					pontos[z].append( ( x(Xo, theta, i, j) + offsetX, y(Xo, theta, 4) - y(Xo, theta, i) + offsetY ) )

		

			# Nota: Imaginar um tabuleiro 4x4 observado em perspectiva. Agora denote todos os 4 pontos que farão parte para cada um dos 16
			# quadradinhos desse tabuleiro. As funções x e y tratam de calcular os 25 pontos no espaço necessários para desenhar cada um dos
			# quadrados observados em perspectiva para definir esse tabuleiro. O processo é repetido para cada um dos 4 tabuleiros
			# por meio do loop z, que incrementa o offset vertical offsetY.

			# Pontos estão armazenados em um vetor. Desenhamos polígonos a partir dos pontos guardados no vetor, e incrementamos de acordo.
			# Mais uma vez imaginando os pontos de um tabuleiro observado em perspectiva, como um losango -> Contar os pontos a partir da aresta de baixo.
			# O sétimo ponto contado será o ponto de topo para o primeiro quadradinho, por isso o indice 6 em indiceTopo.  

			indiceTopo = 6
			indiceEsquerda = 5
			indiceChao = 0
			indiceDireita = 1
			

			#pygame.gfxdraw.filled_polygon(display, (pontos[z][indiceTopo], pontos[z][indiceEsquerda], pontos[z][indiceChao], pontos[z][indiceDireita]), cores.branco)
			
			for i in range(1,17):
				pygame.draw.polygon(display, vetorCores[z], (pontos[z][indiceTopo], pontos[z][indiceEsquerda], pontos[z][indiceChao], pontos[z][indiceDireita]), 2) 
				
				indiceTopo += 1
				indiceEsquerda += 1
				indiceChao += 1
				indiceDireita += 1
				
				# A cada 4ª iteração, incrementamos em dois para ajustar à nova linha                
				if i % 4 == 0:
					indiceTopo += 1
					indiceEsquerda += 1
					indiceChao += 1
					indiceDireita += 1
			offsetY += larguraTabuleiro/2 + 35 # Avança pro próximo tabuleiro
		self.retanguloTexto = pygame.draw.rect( display, cores.branco, (1, self.Altura - self.Altura//5, self.Largura-1, self.Altura/5), 2 )
	def cor_do_marcador(self,marcador):
		if marcador == 'X':
			return self.cores.azul
		if marcador == 'O':
			return self.cores.dourado
	
	def desenha_item(self, marcador, pos):
		posi, posj, posk = posicao(pos)
		coordx = self.Largura/2 + x_item(self.Xo, self.theta, 3 - posj, posk)
		coordy = self.Altura/6 + posi*(self.larguraTabuleiro/2 + 35) +y(self.Xo, self.theta, 4) - y_item(self.Xo, self.theta, 3 - posj) + 10
		cor = self.cor_do_marcador(marcador)
		raio = 0.15*self.Xo*pow(sin(self.theta),3 - posj)
		pygame.draw.circle(self.display, cor, (coordx, coordy), 10)             

	
class Menu:
	def __init__(self, tela, cores):
		self.ativo = 1
		self.fontePrincipal = pygame.font.SysFont('Courier', 60) 
		self.fonteBotoes = pygame.font.SysFont('Courier', 28)
		offsetAltura = 0
		texto_titulo = self.fontePrincipal.render('Jogo da Velha 3D', True, cores.branco)
		text_retangulo = texto_titulo.get_rect(center=(tela.Largura/2, tela.Altura/7))
		tela.display.blit(texto_titulo, text_retangulo)
		pygame.display.update()
		self.listaOpcoes = []

		for i in range(4, 8):
			self.listaOpcoes.append( pygame.draw.rect(tela.display, cores.ciano, (tela.Largura/4, i*tela.Altura/10 - (tela.Altura/20), 2*tela.Largura/4,tela.Altura/10), 2) )

		
		texto_1 = self.fonteBotoes.render('Oponente Humano (2 jogadores)', True, cores.branco)
		texto_2 = self.fonteBotoes.render('Oponente Estabanado', True, cores.branco)
		texto_3 = self.fonteBotoes.render('Oponente Come-Crú', True, cores.branco)
		texto_4 = self.fonteBotoes.render('Oponente Inteligente', True, cores.branco)
		
		texto_1_rect = texto_1.get_rect(center=(tela.Largura/2, 4*tela.Altura/10))
		texto_2_rect = texto_2.get_rect(center=(tela.Largura/2, 5*tela.Altura/10))
		texto_3_rect = texto_3.get_rect(center=(tela.Largura/2, 6*tela.Altura/10))
		texto_4_rect = texto_4.get_rect(center=(tela.Largura/2, 7*tela.Altura/10))

		tela.display.blit(texto_1, texto_1_rect)
		tela.display.blit(texto_2, texto_2_rect)
		tela.display.blit(texto_3, texto_3_rect)
		tela.display.blit(texto_4, texto_4_rect)
		pygame.display.update() 
