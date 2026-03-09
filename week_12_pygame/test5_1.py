import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Click để đổi màu")

# Màu ban đầu
background_color = (200, 200, 200)
rect_color = (255, 0, 0)

# Tọa độ và kích thước hình chữ nhật
rect_x = 50
rect_y = 100
rect_w = 250
rect_h = 100
rect = pygame.Rect(rect_x, rect_y, rect_w, rect_h)

running = True
while running:
    screen.fill(background_color)
    pygame.draw.rect(screen, rect_color, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect.collidepoint((mouse_x, mouse_y)):
                # Đổi màu nền và màu hình chữ nhật ngẫu nhiên
                background_color = (randint(0,255), randint(0,255), randint(0,255))
                rect_color = (randint(0,255), randint(0,255), randint(0,255))

    pygame.display.flip()

pygame.quit()
