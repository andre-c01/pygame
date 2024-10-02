# Importa a biblioteca pygame e inicializa o motor de jogo
import pygame,sys
pygame.init()

# Define um tamanho largura por altura
size = width, height = 1024, 600
# Define uma velocidade (eixo x e y)
speed = [10, 10]
# Define a cor preta
black = 0, 0, 0
# Inicializa um clock
clock = pygame.time.Clock()

# Cria a janela com o tamanho definido e um título
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Olá Bola")

# Atribui uma imagem a uma variável
ball = pygame.image.load("sexy_400x400.jpeg")
# Atribui a um retangulo a dimensão da imagem (frame)
ballrect = ball.get_rect

ballrect.y += 100

while True:
    # Se a janela for fechada encerra o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move a frame (com a imagem) à velocidade estabelecida
    ballrect = ballrect.move(speed)

    # Se o lado esquerdo da frame for menor que 0 ou 
    # o lado direito for maior que a largura move a bola a -1*velocidade
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # Se o topo da frame for menor que 0 ou 
    # a base for maior que a altura move a bola a -1*velocidade
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    # Limpa o ecrã
    screen.fill(black)
    # Framerate a 60 fps
    clock.tick(60)
    # Associa a imagem à frame e faz o seu display
    screen.blit(ball, ballrect)
    pygame.display.flip()