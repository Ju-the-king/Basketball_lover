# Example file showing a circle moving on screen
import pygame
import numpy as np

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
delay = 0

print(screen)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    legs = 5000
    mvt_sec = 200

    pygame.draw.circle(screen, "yellow", player_pos, 40)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player_pos.y -= legs * dt
        #print(player_pos)
    if keys[pygame.K_DOWN]:
        player_pos.y += legs * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= legs * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += legs * dt

    mvt_behavior = np.random.random()

    delay += clock.tick(60)

    if delay >= mvt_sec :

        delay = 0

        if mvt_behavior < 0.25 :

            player_pos.y -= legs * dt

        elif mvt_behavior > 0.25 and mvt_behavior < 0.50 :

            player_pos.y += legs * dt

        elif mvt_behavior > 0.50 and mvt_behavior < 0.75 :

            player_pos.x -= legs * dt

        elif mvt_behavior > 0.75 :

            player_pos.x += legs * dt

    #boundaries :

    if player_pos.y < 0 :

        player_pos.y = 0

    elif player_pos.y > 720 :

        player_pos.y = 720

    elif player_pos.x < 0 :

        player_pos.x = 0

    elif player_pos.x > 1280 :

        player_pos.x = 1280


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()