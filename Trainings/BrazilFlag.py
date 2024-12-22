import pygame
import sys

pygame.init()
WEIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WEIDTH, HEIGHT))
clock = pygame.time.Clock()

BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOM = (255,250,0)


x_pos, y_pos = 500, 300
vertice_top = (x_pos, y_pos - HEIGHT // 2)
vertice_down = (x_pos, y_pos + HEIGHT // 2)
vertice_left = (x_pos - WEIDTH // 2, y_pos)
vertice_right = (x_pos + WEIDTH //2, y_pos)
losango_points = [vertice_top, vertice_right, vertice_down, vertice_left]



while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill((10, 200, 75))
    pygame.draw.polygon(screen, YELLOM, losango_points)
    pygame.draw.circle(screen, pygame.Color("blue"), (500, 300), radius=150)
    pygame.display.update()
    clock.tick(60)