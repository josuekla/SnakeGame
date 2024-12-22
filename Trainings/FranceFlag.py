import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()

BLUE = (0,0,255)
WHITE = (255,255,255)
RED = (255,0,0)

b = pygame.Surface((200, 500))
w = pygame.Surface((200, 500))
r = pygame.Surface((200, 500))
b.fill((BLUE))
w.fill((WHITE))
r.fill((RED))



while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill((125, 200, 75))
    screen.blit(b, (0,0))
    screen.blit(w, (200,0))
    screen.blit(r, (400,0))
    pygame.display.update()
    clock.tick(60)