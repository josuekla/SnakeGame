import pygame, sys, random
from pygame.math import Vector2

class Apple():
    def __init__(self):
        self.x = random.randint(0, cells_number - 1)
        self.y = random.randint(0, cells_number - 1)    
        self.position = Vector2(self.x, self.y)

    def draw_apple(self):
        apple_rect = pygame.Rect(self.position.x * cells_size, self.position.y * cells_size, cells_size, cells_size)
        pygame.draw.rect(screen, (5, 85, 240), apple_rect)

pygame.init()
cells_size = 35
cells_number = 15
screen = pygame.display.set_mode((cells_size * cells_number, cells_size * cells_number))
clock = pygame.time.Clock()

fruit = Apple()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    screen.fill((180, 225, 75))
    fruit.draw_apple()
    pygame.display.update()
    clock.tick(60)