import pygame, sys, random
from pygame.math import Vector2

class Snake():
    def __init__(self):
        self.body = [Vector2(3, 10), Vector2(2, 10), Vector2(1, 10)]
        self.direction = Vector2(1,0)
        self.add_block = False


        self.head_up = pygame.image.load('img/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('img/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('img/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('img/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('img/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('img/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('img/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('img/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('img/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('img/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('img/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('img/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('img/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('img/body_bl.png').convert_alpha()

    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            print(index, block)
            x_pos = int(block.x * cells_size)
            y_pos = int(block.y * cells_size)
            block_rect = pygame.Rect(x_pos, y_pos, cells_size, cells_size)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
            
        
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down

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
        screen.blit(apple, apple_rect)
        # pygame.draw.rect(screen, (5, 85, 240), apple_rect)

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
cells_size = 40
cells_number = 16   
screen = pygame.display.set_mode((cells_size * cells_number, cells_size * cells_number))
clock = pygame.time.Clock()
apple = pygame.image.load('img/apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (cells_size, cells_size))

main_game = Main()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 50)

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