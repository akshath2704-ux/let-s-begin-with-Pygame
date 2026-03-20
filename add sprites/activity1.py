import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Sprite:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
sprite1 = Sprite(100, 100, 50, 50, RED)
sprite2 = Sprite(300, 300, 50, 50, BLUE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        sprite1.rect.y -= 5
    if keys[pygame.K_DOWN]:
        sprite1.rect.y += 5
    if keys[pygame.K_LEFT]:
        sprite1.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        sprite1.rect.x += 5
    sprite1.rect.clamp_ip(screen.get_rect())
    screen.fill(WHITE)
    sprite1.draw()
    sprite2.draw()
    pygame.display.flip()
    pygame.time.Clock().tick(60)