# Importa a biblioteca pygame e inicializa o motor de jogo
import pygame
pygame.init()

# Define o tamanho da janela onde vamos desenhar
screen = pygame.display.set_mode((400, 400))

# Desenhar linha (ecrã, (cor em rgb), origem (x,y), destino (x,y), espessura)
pygame.draw.line(screen, (0,0,255), (50, 50), (350, 50), 3)

# Desenhar retangulos (ecrã, (cor em rgb),(esquerda, topo, largura, altura), bordadura)
pygame.draw.rect(screen, (255, 0, 0), (100, 50, 40, 80))

# Desenhar circulos (ecrã, (cor em rgb),centro, raio, bordadura)
pygame.draw.circle(screen,(0,255,0),(200,200),30)

# Ciclo infinito que mantém a janela aberta até ser fechada no X
while True:
    if pygame.event.get(pygame.QUIT):
        break
    pygame.display.update()

pygame.quit()