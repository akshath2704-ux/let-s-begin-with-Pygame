import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Level Up")
background = pygame.image.load('background.jpg')  
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pygame.mixer.init()
background_music = pygame.mixer.Sound('background_music.mp3')  
shoot_sound = pygame.mixer.Sound('shoot.wav') 
background_music.play(-1)
def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
game_loop()