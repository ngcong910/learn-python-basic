import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Mouse Event")
ruuning = True
BLUE= (0, 0, 200)
RED=(200, 0, 0)
rect = pygame.Rect(150, 70, 100, 100)
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(60)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), rect)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                if event.button == 1:
                    rect.x -= 10
                elif event.button == 3:
                    rect.x += 10
                elif event.button == 2:
                    rect.y -= 10
                elif event.button == 4:
                    rect.y += 10
                elif event.button == 5:
                    rect.y -= 5
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
