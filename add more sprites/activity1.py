import pygame
import random

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

class Player(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH // 2, HEIGHT // 2, 50, 50)
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.x = max(0, min(WIDTH - self.width, self.x))
        self.y = max(0, min(HEIGHT - self.height, self.y))

class Enemy(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH-40), random.randint(0, HEIGHT-40), 40, 40)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player()
    enemies = [Enemy() for _ in range(7)]
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        player.move(dx, dy)

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)
        for enemy in enemies:
            if player.colliderect(enemy):
                score += 1
                enemy.x = random.randint(0, WIDTH-40)
                enemy.y = random.randint(0, HEIGHT-40)
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()