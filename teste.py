import pygame
import math


pygame.init()

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

display = pygame.display.set_mode((800,600))
display.fill(preto)

#pixAr = pygame.PixelArray(display)
#pixAr[10][20] = verde

pygame.draw.line(display, azul, (100,200), (300,450), 5)

rect = pygame.draw.rect(display, vermelho, (400,400,200,150))

pygame.draw.circle(display, branco, (150,150), 75) 

#rectRotacionado = pygame.transform.rotate(rect, self.

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()
    pygame.display.update()

