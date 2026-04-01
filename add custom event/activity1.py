import pygame
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Custom event to change sprite color
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color
    def change_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    sprite1 = Sprite(RED, 200, 300)
    sprite2 = Sprite(BLUE, 400, 300)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(sprite1, sprite2)
    pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == CHANGE_COLOR_EVENT:
                sprite1.change_color()
                sprite2.change_color()

        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
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