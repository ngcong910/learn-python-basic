import pygame
from random import randint

# Khởi tạo Pygame
pygame.init()

# Màu sắc
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED=(255,0,0)

# Thiết lập cửa sổ
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Di chuyển hình vuông")

# Thiết lập đồng hồ
clock = pygame.time.Clock()



# Tọa độ ban đầu và tốc độ
rect_x = 100
rect_y = 100
speed = 50

red_x=200
red_y=200

# Nền
background = WHITE

font=pygame.font.SysFont(None,48)

# Vòng lặp chính
running = True
while running:
    clock.tick(60)
    screen.fill(background)

    # Vẽ hình vuông
    red_rect=pygame.draw.rect(screen,RED,(red_x,red_y,50,50))
    blue_rect=pygame.draw.rect(screen, BLUE, (rect_x, rect_y, 50, 50))

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect_x += speed
            if event.key == pygame.K_LEFT:
                rect_x -= speed
            if event.key == pygame.K_UP:
                rect_y -= speed
            if event.key == pygame.K_DOWN:
                rect_y += speed

        if event.type == pygame.QUIT:
            running = False

    if blue_rect.colliderect(red_rect):
        text = font.render("Defeat", True, (255, 0, 0))
        print("Nguu")
        screen.blit(text, (200, 50))

    pygame.display.flip()

pygame.quit()
