import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 500, 500
CAPTION = "My first game screen"
IMAGE_SIZE = (300, 300)
BG_COLOR = (58, 58, 58)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
try:
    image = pygame.image.load('image.png')
    image = pygame.transform.scale(image, IMAGE_SIZE)
except FileNotFoundError:
    print("Error: Image file 'image.png' not found.")
    sys.exit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BG_COLOR)
    image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(image, image_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)