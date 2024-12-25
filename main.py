import pygame, sys, random
from pygame.math import Vector2

class Snake():
    def __init__(self):
        self.body = [Vector2(3, 10), Vector2(4, 10), Vector2(5, 10)]

        self.direction = Vector2(1,0)
    
    def draw_snake(self):
        for block in self.body:
            x_position = block.x * cells_size
            y_position = block.y * cells_size
            snake_rect = pygame.Rect( x_position, y_position, cells_size, cells_size)
            pygame.draw.rect(screen, (77, 200, 10), snake_rect)

    def move_snake(self):
        snake_copy = self.body[:-1]
        snake_copy.insert(0, snake_copy[0] + self.direction)
        self.body = snake_copy[:] 
    
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
snake = Snake()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, +1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(+1, 0)
    screen.fill((180, 225, 75))
    fruit.draw_apple()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)