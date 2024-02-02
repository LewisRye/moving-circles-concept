# Example file showing a circle moving on screen
import pygame
import os
from pygame import mixer;

# pygame setup
pygame.init()

# screen setup
display_info = pygame.display.Info()
display_width = display_info.current_w
display_height = display_info.current_h

#choose here whether to start in resizable or fullscreen
screen = pygame.display.set_mode((700, 500), pygame.RESIZABLE)
# screen = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN) # use to begin in fs

#change this value based on the starting screen
fullscreen = False
#change which key activates the fullscreen and resizable screen
fullscreen_key = pygame.K_f

# file system setup
current_path = os.path.dirname(__file__)
icon = pygame.image.load(current_path + '/assets/appIcon.png')
pygame.display.set_caption('Moving Circles Concept App')
pygame.display.set_icon(icon)
background = pygame.image.load(current_path + '/assets/background.jpg')
btnPlay = pygame.image.load(current_path + '/assets/btnPlay.png')
btnPlayHover = pygame.image.load(current_path + '/assets/btnPlayHover.png')
btnExit = pygame.image.load(current_path + '/assets/btnExit.png')
btnExitHover = pygame.image.load(current_path + '/assets/btnExitHover.png')
btnSettings = pygame.image.load(current_path + '/assets/btnSettings.png')
btnSettingsHover = pygame.image.load(current_path + '/assets/btnSettingsHover.png')

mixer.music.load(current_path +'/assets/background.mp3')
mixer.music.play(-1)
pygame.mixer.music.set_volume(0.03)

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
        self.text = self.font.render('ESC to QUIT', True, (255, 255, 255))
        self.text_width = self.text.get_width()
        screen.blit(self.text, (screen.get_width() - self.text_width, 0))
        self.icon = pygame.transform.scale(icon, (50, 50))
        screen.blit(self.icon, (5, screen.get_height() - 55)) # offset by 5px so it is not stuck in the bottom left

fps = FPS()
ui = UI()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

runningGame = False
runningMenu = True
runningSettings = False

running = True

while running:
    # opening the menu UI
    if runningMenu and not runningSettings:
        screen.fill("black")
        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
        screen.blit(background, (0, 0))

        areaPlayBtn = pygame.Rect(screen.get_width() / 2 - 152.5, screen.get_height() / 2 - 47.5, 305, 95)
        screen.blit(btnPlay, (screen.get_width() / 2 - 152.5, screen.get_height() / 2 - 47.5))

        areaExitBtn = pygame.Rect(screen.get_width() / 2 - 152.5, screen.get_height() / 2 + 47.5, 305, 95)
        screen.blit(btnExit, (screen.get_width() / 2 - 152.5, screen.get_height() / 2 + 47.5))

        areaSettingsBtn = pygame.Rect(screen.get_width() - 144 - 10, 10, 144, 122) # offset 10px from the edge of the screen
        screen.blit(btnSettings, (screen.get_width() - 144 - 10, 10))

        cursor_pos = pygame.mouse.get_pos()
        if areaPlayBtn.collidepoint(cursor_pos):
            screen.blit(btnPlayHover, (screen.get_width() / 2 - 152.5, screen.get_height() / 2 - 47.5))
        elif areaExitBtn.collidepoint(cursor_pos):
            screen.blit(btnExitHover, (screen.get_width() / 2 - 152.5, screen.get_height() / 2 + 47.5))
        elif areaSettingsBtn.collidepoint(cursor_pos):
            screen.blit(btnSettingsHover, (screen.get_width() - 144 - 10, 10))

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_f]):
            runningGame = True
            runningMenu = False
        
        pygame.display.flip()

    # opening the settings UI
    if runningSettings:
        # implement settings UI here
        None

    # opening the game UI
    if runningGame:
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
        if (keys[pygame.K_ESCAPE]):
            running = False

        # flip() the display to put your work on screen
        fps.render(screen)
        ui.render(screen)
        pygame.display.flip()

        # dt is delta time in seconds since last frame, loosely caps FPS
        dt = clock.tick(240) / 1000

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if runningSettings:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                runningSettings = False

        if runningMenu:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if areaPlayBtn.collidepoint(event.pos):
                    runningGame = True
                    runningMenu = False
                if areaExitBtn.collidepoint(event.pos):
                    running = False
                if areaSettingsBtn.collidepoint(event.pos):
                    runningSettings = True

        if event.type == pygame.KEYDOWN and event.key == fullscreen_key:
            if fullscreen: 
                screen = pygame.display.set_mode((700, 500), pygame.RESIZABLE)
                fullscreen = False
            else: 
                screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                fullscreen = True

pygame.quit()