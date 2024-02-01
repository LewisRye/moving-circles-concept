# Example file showing a circle moving on screen
import pygame
import os

# pygame setup
pygame.init()

# screen setup
display_info = pygame.display.Info()
display_width = display_info.current_w
display_height = display_info.current_h
screen = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)

# file system setup
current_path = os.path.dirname(__file__)
icon = pygame.image.load(current_path + '/icon.png')
pygame.display.set_caption('Moving Circles Concept')
pygame.display.set_icon(icon)


clock = pygame.time.Clock()
dt = 0

class FPS:
    def __init__(self):
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
    
    def render(self, screen):
        self.text = self.font.render('FPS: ' + str(round(clock.get_fps(), 1)), True, (255, 255, 255))
        screen.blit(self.text, (0, 0))

class UI:
    def __init__(self):
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
    
    def render(self, screen):
        self.text = self.font.render('F11: fullscreen | ESC: quit', True, (255, 255, 255))
        self.text_width = self.text.get_width()
        screen.blit(self.text, (screen.get_width() - self.text_width, 0))
        self.icon = pygame.transform.scale(icon, (50, 50))
        screen.blit(self.icon, (5, screen.get_height() - 55)) # offset by 5px so it is not stuck in the bottom left

fps = FPS()
ui = UI()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.display.toggle_fullscreen()
running = True

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "red", player_pos, 33)

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and player_pos.y > 0:
        player_pos.y -= 500 * dt
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player_pos.y < screen.get_height():
        player_pos.y += 500 * dt
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_pos.x > 0:
        player_pos.x -= 500 * dt
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_pos.x < screen.get_width():
        player_pos.x += 500 * dt
    if (keys[pygame.K_F11]):
        pygame.display.toggle_fullscreen()
        pygame.time.delay(250)
    if (keys[pygame.K_ESCAPE]):
        running = False

    # flip() the display to put your work on screen
    fps.render(screen)
    ui.render(screen)
    pygame.display.flip()

    # limits FPS
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(240) / 1000

pygame.quit()
