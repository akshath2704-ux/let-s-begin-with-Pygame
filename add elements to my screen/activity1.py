import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (100, 100, 200, 100))
        font = pygame.font.Font(None, 36)
        text = font.render("Hello, Game!", True, BLACK)
        screen.blit(text, (150, 150))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()