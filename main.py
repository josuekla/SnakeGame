import pygame

pygame.init()
screen = pygame.display.set_mode((500, 600))

while True:
    #draw all elements from game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()