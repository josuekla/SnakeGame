import pygame, sys, random
from pygame.math import Vector2

class Snake():
    def __init__(self):
        self.body = [Vector2(3, 10), Vector2(2, 10), Vector2(1, 10)]
        self.direction = Vector2(1,0)
        self.add_block = False
    
    def draw_snake(self):
        for block in self.body:
            x_position = block.x * cells_size
            y_position = block.y * cells_size
            snake_rect = pygame.Rect( x_position, y_position, cells_size, cells_size)
            pygame.draw.rect(screen, (77, 200, 10), snake_rect)

    def move_snake(self):
        if self.add_block == True:
            snake_copy = self.body[:]
            snake_copy.insert(0, snake_copy[0] + self.direction)
            self.body = snake_copy[:]
            self.add_block = False
        
        else:
            snake_copy = self.body[:-1]
            snake_copy.insert(0, snake_copy[0] + self.direction)
            self.body = snake_copy[:] 
    
    def block_add(self):
        self.add_block = True
    
class Apple():
    def __init__(self):
        self.randomize()

    def draw_apple(self):
        apple_rect = pygame.Rect(self.position.x * cells_size, self.position.y * cells_size, cells_size, cells_size)
        pygame.draw.rect(screen, (5, 85, 240), apple_rect)

    def randomize(self):
        self.x = random.randint(0, cells_number - 1)
        self.y = random.randint(0, cells_number - 1)
        self.position = Vector2(self.x, self.y)

class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Apple()
    
    def update(self):
        self.snake.move_snake()
        self.check_colisition()
        self.check_fail()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_apple()

    def check_colisition(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.block_add()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cells_number or not 0 <= self.snake.body[0].y < cells_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
        

pygame.init()
cells_size = 35
cells_number = 15
screen = pygame.display.set_mode((cells_size * cells_number, cells_size * cells_number))
clock = pygame.time.Clock()

main_game = Main()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, +1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                     main_game.snake.direction = Vector2(+1, 0)
    screen.fill((180, 225, 75))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)