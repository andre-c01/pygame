# Importa a biblioteca pygame e inicializa o motor de jogo
import pygame
# Importar a classe jogador
from jogador import Jogador
# Importar a classe bola
from bola import Bola
from random import randint

pygame.init()

# Definir cores
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Criar uma janela com x altura por y largura
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Apanh'á Bola")

# Definir a cor, largura e altura do jogador
jogadorA = Jogador(WHITE, 50, 10)
jogadorA.rect.x = 325
jogadorA.rect.y = 470

# Definir a cor, largura e altura do jogador
jogadorB = Jogador(WHITE, 50, 10)
jogadorB.rect.x = 325
jogadorB.rect.y = 30

# Definir a cor, largura e altura da bola
bola = Bola(WHITE,10,10)
bola.rect.x = 345
bola.rect.y = 250

# Cria uma lista que contem todos os sprites que serão utilizados
all_sprites_list = pygame.sprite.Group()
 
# Adiciona o jogador à lista de sprites
all_sprites_list.add(jogadorA)
all_sprites_list.add(jogadorB)
all_sprites_list.add(bola)
 
# Controlo de loop infinito ou até o utilizador sair do jogo (fecha a janela).
emJogo = True
 
# Cria um clock que será utilizado para controlar a velocidade de refresh
clock = pygame.time.Clock()

scoreA = 0
scoreB = 0
 
# -------- Ciclo Principal do programa -----------
while emJogo:
    # --- Ciclo principal
    for event in pygame.event.get(): # O utilizador fez alguma coisa
        if event.type == pygame.QUIT: # O utilizador fechou a janela
              emJogo = False # Muda o controlo para assinalar que o jogo terminou
    
    # Move o jogador quando o utilizador pressiona as teclas direccionais esquerda e direita 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jogadorA.moveEsq(5)
    if keys[pygame.K_RIGHT]:
        jogadorA.moveDir(5)

    # Move o jogador quando o utilizador pressiona as teclas direccionais esquerda e direita 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        jogadorB.moveEsq(5)
    if keys[pygame.K_d]:
        jogadorB.moveDir(5)

    # --- Lógica do jogo AQUI
    all_sprites_list.update()
    # Deteta colisão entre a bola e o jogador
    if pygame.sprite.collide_mask(bola, jogadorA):
        scoreA += 1
        bola.catch()
    
    if pygame.sprite.collide_mask(bola, jogadorB):
        scoreB += 1
        bola.catch()

    # Verifica se a bola saiu do ecrã
    if bola.rect.y > 500:
        scoreB += 2
        bola.rect.x = randint(100,600)
        bola.rect.y = 250
    
    if bola.rect.y < 0:
        scoreA += 2
        bola.rect.x = randint(100,600)
        bola.rect.y = 250
 
    # --- Desenho do jogo AQUI
    
    # Limpar o ecrã (ecrã a preto)
    screen.fill(BLACK)
    
    # Desenhar todas as sprites de uma só vez.
    all_sprites_list.draw(screen)
    
    # Mostra pontuação:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (625,10))

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (25,10))
 
    # Atualizar o ecrã com o que foi desenhado.
    pygame.display.flip()
     
    # --- Limitar a 60 frames por segundo
    clock.tick(60)
 
# Para o motor de jogo (após terminar o ciclo principal do programa)

pygame.quit()