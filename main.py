# Example file showing a circle moving on screen
import pygame
import os

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
current_path = os.path.dirname(__file__)
icon = pygame.image.load(current_path + '/icon.png')
pygame.display.set_caption('Moving Circles')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and player_pos.y > 0:
        player_pos.y -= 300 * dt
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player_pos.y < screen.get_height():
        player_pos.y += 300 * dt
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_pos.x > 0:
        player_pos.x -= 300 * dt
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_pos.x < screen.get_width():
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
