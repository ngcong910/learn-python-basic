import pygame

# Khởi tạo
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Hình vuông di chuyển")
clock = pygame.time.Clock()

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Hình vuông
square_size = 50
square_x = 100
square_y = 175
square_rect = pygame.Rect(square_x, square_y, square_size, square_size)

# Cờ trạng thái
moving = False
speed = 5

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # Vẽ hình vuông
    pygame.draw.rect(screen, RED, square_rect)

    # Di chuyển nếu được kích hoạt
    if moving:
        square_rect.x += speed
        if square_rect.x > 600:  # Ra khỏi màn hình thì quay lại
            square_rect.x = -square_size

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if square_rect.collidepoint(event.pos):
                moving = True  # Bắt đầu chạy khi nhấn vào hình vuông

    pygame.display.flip()

pygame.quit()
