import os
from checa import posicao
from tela import *
from jogo import *
from jogadores import *


def main():

    app: App = App()
    app.setup()
    
    cores = Cores()
    tela = Tela(cores)
    menu = Menu(tela, cores)
    jogo = Jogo(tela, cores)
    
    fonteInput = pygame.font.SysFont('Courier', 20)
    pygame.mixer.music.load('media/CornettaPiano.ogg')
    pygame.mixer.music.set_volume(0.5)
    inputTexto = ''
    
    while app.rodando == True:
        for event in pygame.event.get():
            pygame.display.update()
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                app.rodando = False
                pygame.quit()
                quit()
            
            ### Menu principal
            elif event.type == pygame.MOUSEBUTTONUP and  menu.ativo == 1:
                pygame.display.update()
                posMouse = pygame.mouse.get_pos()
                jogo.numero_jogada = 0
                if ( menu.listaOpcoes[0].collidepoint( posMouse ) ): # OPCAO JOGADOR HUMANO
                    
                    jogo.opcao = 1
                    jogo.numero_jogada += 1 
                    menu.ativo = 0
                    
                    tela.display.fill(cores.preto)
                    tela.renderiza_tabuleiro( tela.Largura, tela.Altura, tela.display, cores )
                    
                    pygame.display.update()
                    jogo.jogo_ativo = 1
                    jogo.quem_joga = quem_joga(jogo.numero_jogada)
                    tela.display.blit(tela.fonteJogo.render('Jogador %i:'%jogo.quem_joga, True, cores.branco), (tela.Largura/7, tela.Altura/1.1))
                    pygame.display.update()
                    continue
                elif ( menu.listaOpcoes[1].collidepoint( posMouse ) ): # OPCAO JOGADOR ESTABANADO 
                    jogo.opcao = 2
                    jogo.numero_jogada += 1
                    menu.ativo = 0

                    tela.display.fill(cores.preto)
                    tela.renderiza_tabuleiro( tela.Largura, tela.Altura, tela.display, cores )
                    
                    pygame.display.update()
                    jogo.jogo_ativo = 1
                    
                    jogadorEstabanado = JogadorAleatorio( jogo.tabuleiro, 'O' )
                    
                    jogo.quem_joga = quem_joga(jogo.numero_jogada)
                    tela.display.blit(tela.fonteJogo.render('Jogador %i:'%jogo.quem_joga, True, cores.branco), (tela.Largura/7, tela.Altura/1.1))
                    pygame.display.update()
                    continue
                elif (menu.listaOpcoes[2].collidepoint( posMouse ) ):
                    jogo.opcao = 3
                    jogo.numero_jogada += 1
                    menu.ativo = 0

                    tela.display.fill(cores.preto)
                    tela.renderiza_tabuleiro( tela.Largura, tela.Altura, tela.display, cores )
                    
                    pygame.display.update()
                    jogo.jogo_ativo = 1
                    
                    jogadorComeCru = JogadorSequencial( jogo.tabuleiro, 'O' )

                    jogo.quem_joga = quem_joga(jogo.numero_jogada)
                    tela.display.blit(tela.fonteJogo.render('Jogador %i:'%jogo.quem_joga, True, cores.branco), (tela.Largura/7, tela.Altura/1.1))
                    pygame.display.update()
                    continue

                elif (menu.listaOpcoes[3].collidepoint( posMouse ) ):
                    jogo.opcao = 4
                    jogo.numero_jogada += 1
                    menu.ativo = 0

                    tela.display.fill(cores.preto)
                    tela.renderiza_tabuleiro( tela.Largura, tela.Altura, tela.display, cores )
                    
                    pygame.display.update()
                    jogo.jogo_ativo = 1
                    
                    jogadorInteligente = JogadorEsperto( jogo.tabuleiro, 'O' )
                    jogadorInteligente.definir_dificuldade(0)

                    jogo.quem_joga = quem_joga(jogo.numero_jogada)
                    tela.display.blit(tela.fonteJogo.render('Jogador %i:'%jogo.quem_joga, True, cores.branco), (tela.Largura/7, tela.Altura/1.1))
                    pygame.display.update()
                    continue

            ### Trata inputs de usuário
            if (jogo.jogo_ativo == 1) and ((jogo.opcao == 1) or (jogo.opcao != 1 and jogo.quem_joga == 1)):
                # Define se o jogo está ativo, e o input baseado no modo de jogo/de quem é a vez
                if event.type == pygame.KEYDOWN:
                    inputTexto += event.unicode
            
            elif (jogo.jogo_ativo == 1 and jogo.opcao == 2 and jogo.quem_joga == 2):
                jogada = jogadorEstabanado.joga_aleatoriamente()
                inputTexto = str(jogada)
                if int(inputTexto) < 10:
                    inputTexto = '0' + inputTexto
            elif (jogo.jogo_ativo == 1 and jogo.opcao == 3 and jogo.quem_joga == 2):
                jogada = jogadorComeCru.joga_sequencialmente()
                inputTexto = str(jogada)
                if int(inputTexto) < 10:
                    inputTexto = '0' + inputTexto
            elif (jogo.jogo_ativo == 1 and jogo.opcao == 4 and jogo.quem_joga == 2):
                jogada = jogadorInteligente.joga_esperto( False )
                inputTexto = str(jogada)
                if int(inputTexto) < 10:
                    inputTexto = '0' + inputTexto

            # Desenha a jogada e joga no tabuleiro de backend    
            if len(inputTexto) == 2 and jogo.jogo_ativo == 1:
                posi, posj, posk = posicao(int(inputTexto))
                if int(inputTexto)*(int(inputTexto) - 65) < 0 and jogo.tabuleiro.tab[posi][posj][posk] == '': # 0 < jogada_atual <= 64 e posição não ocupada
     
                    jogo.jogada_atual =  int(inputTexto)
                    tela.retanguloTexto = pygame.draw.rect( tela.display, cores.preto, (5, tela.Altura - tela.Altura//6, tela.Largura-20, tela.Altura/7 ))
                    tela.display.blit(tela.fonteJogo.render('Jogador %i:'%jogo.quem_joga, True, cores.branco), (tela.Largura/7, tela.Altura/1.1))
                    jogo.imprime_input(inputTexto, fonteInput) 
                    jogo.atualiza_tabuleiro()
                    pygame.time.wait(150)
     
                    if jogo.tabuleiro.checaTab() != None:
                        tela.desenha_item(marcador(jogo.numero_jogada-1), jogo.jogada_atual)
                        tela.retanguloTexto = pygame.draw.rect( tela.display, cores.preto, (5, tela.Altura - tela.Altura//6, tela.Largura-20, tela.Altura/7 ))
                        tela.display.blit(tela.fonteJogo.render('FIM', True, cores.branco), (tela.Largura/7, tela.Altura/1.1))
                        pygame.display.update()
                        pygame.mixer.music.play(0)
                        pygame.time.wait(4800)
                        app.rodando = False
                        pygame.quit()
                        quit()
                    jogo.quem_joga = quem_joga(jogo.numero_jogada)
                    inputTexto = ''
                else:
                    tela.retanguloTexto = pygame.draw.rect( tela.display, cores.preto, (5, tela.Altura - tela.Altura//6, tela.Largura-20, tela.Altura/7))
                    tela.display.blit( tela.fonteJogo.render("Jogada inválida!", True, cores.branco),(tela.Largura/4, tela.Altura/1.1) )
                    inputTexto = ''

                pygame.display.update()

        

if __name__=="__main__":
    main()

