import pygame
BLACK = (0,0,0)
 
class Jogador(pygame.sprite.Sprite):
    #Esta classe representa um jogador. Deriva da classe sprite do Pygame.
    
    def __init__(self, color, width, height):
        # Iniciar o construtor da classe (Sprite)
        super().__init__()
        
        # Definir a cor, largura e altura do jogador
        # Definir a cor do fundo e a sua transparencia.
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Desenhar o jogador (um retangulo!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Obtém o objeto rectangulo que contém as medidas da imagem.
        self.rect = self.image.get_rect()
        

    # Mover jogador para a esquerda 
    def moveEsq(self, pixels):
        self.rect.x -= pixels
		# Verificar se o jogador não sai pelo lado esquerdo do ecrã
        if self.rect.x < 0:
          self.rect.x = 0
    # Mover jogador para a direita          
    def moveDir(self, pixels):
        self.rect.x += pixels
	    # Verificar se o jogador não sai pelo lado direito do ecrã
        if self.rect.x > 650:
          self.rect.x = 650