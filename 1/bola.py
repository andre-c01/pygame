import pygame
from random import randint
BLACK = (0,0,0)
WHITE = (255,255,255)

class Bola(pygame.sprite.Sprite):
    # Esta classe representa uma bola. Deriva da classe sprite do Pygame.
    
    def __init__(self, color, width, height):
        # Iniciar o construtor da classe (Sprite)
        super().__init__()
        
        # Definir a cor, largura e altura da bola
        # Definir a cor do fundo e a sua transparencia.
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Desenhar a bola (um retangulo!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Definir a velocidade da bola (Random)
        self.velocity_y = randint(-5,5)
        while (self.velocity_y == 0):
            self.velocity_y = randint(-5,5)
        self.velocity_x = randint(-1,1)
        while (self.velocity_x == 0):
            self.velocity_x = randint(-1,1)
        print(self.velocity_x)
        
        # Obter o objeto rectangulo que contém as medidas da imagem.
        self.rect = self.image.get_rect()
    

    def update(self):
        self.rect.x += self.velocity_x
        if (self.velocity_y < 0):
            self.rect.y -= abs(self.velocity_y)

        else:
            self.rect.y += abs(self.velocity_y)

    
    def catch(self):
        if (self.velocity_y < 0):
            self.velocity_y = +abs(self.velocity_y)
        else:
            self.velocity_y = -abs(self.velocity_y)
        
