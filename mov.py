# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos1 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos2 = pygame.Vector2(screen.get_width() / 2 + 80, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkblue")

    pygame.draw.circle(screen, "pink", player_pos1, 40)
    pygame.draw.circle(screen, "pink", player_pos2, 40)

    mov_multiplyer=1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        mov_multiplyer=2.5
    if keys[pygame.K_w]:
        player_pos1.y -= 400 * dt * mov_multiplyer
        player_pos2.y -= 400 * dt * mov_multiplyer
    if keys[pygame.K_s]:
        player_pos1.y += 400 * dt * mov_multiplyer
        player_pos2.y += 400 * dt * mov_multiplyer
    if keys[pygame.K_a]:
        player_pos1.x -= 400 * dt * mov_multiplyer
        player_pos2.x -= 400 * dt * mov_multiplyer
    if keys[pygame.K_d]:
        player_pos1.x += 400 * dt * mov_multiplyer
        player_pos2.x += 400 * dt * mov_multiplyer
    if keys[pygame.K_SPACE]:
        for i in range(0, 10, 1):
            player_pos1.y += 100
            player_pos2.y += 100
            pygame.time.delay(1)

        for i in range(0, 10, 1):
            player_pos1.y -= 100
            player_pos2.y -= 100
            pygame.time.delay(1)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(80) / 1000

pygame.quit()