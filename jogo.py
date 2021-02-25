import pygame
from tab import *
from tela import *

def quem_joga(jogada):
    return int(2 - (jogada%2))

def marcador(jogada):
    if quem_joga(jogada) == 1:
        return 'X'
    return 'O'

class Jogo: 
    def __init__(self, tela, cores):
        self.tabuleiro = Tabuleiro()
        self.tela = tela
        self.cores = cores
        self.tab = Tabuleiro()
        self.opcao = 0
        self.jogo_ativo = 0
        self.numero_jogada = 0
        self.jogada_atual = 1
        self.quem_joga = None

    def atualiza_jogo(self):
        self.atualiza_tabuleiro(self.jogada_atual)

    def atualiza_tabuleiro(self):
        self.tabuleiro.insereItem(marcador(self.numero_jogada), self.jogada_atual)
        self.tela.desenha_item(marcador(self.numero_jogada), self.jogada_atual)
        self.numero_jogada += 1
        
    def imprime_input(self, inputTexto, fonte):
        self.tela.display.blit( fonte.render(inputTexto, True, self.cores.branco),(self.tela.Largura/4, self.tela.Altura/1.1))

    
    # DISPLAY MOSTRAR QUEM JOGA A PARTIR DA VAR JOGADA, esperar input
    
    # #checa se o input é válido (1 a 64) -> caso não avise, caso sim:
    #checa se a posição está disponível -> caso não avise, caso sim:
    #insereItem no tab (Objeto) e desenha o item ('Tipo' ~ quem_joga(jogada)) na interface
    #checa_tabuleiro() pra ver se o jogo foi vencido com a jogada -> caso sim SAIA DO JOGO E FINALIZE, caso não:
    #jogada += 1
    



