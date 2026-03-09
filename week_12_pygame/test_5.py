import pygame
from random import randint

# Khởi tạo
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Click ngoài để đổi màu")

# Màu ban đầu
background_color = (200, 200, 200)
rect_color = (255, 0, 0)

# Hình chữ nhật
rect = pygame.Rect(50, 100, 250, 100)  # (x, y, width, height)

running = True
while running:
    screen.fill(background_color)
    pygame.draw.rect(screen, rect_color, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not rect.collidepoint(event.pos):
                # Chỉ đổi màu nếu click ngoài hình
                background_color = (randint(0,255), randint(0,255), randint(0,255))
                rect_color = (randint(0,255), randint(0,255), randint(0,255))

    pygame.display.flip()

pygame.quit()
