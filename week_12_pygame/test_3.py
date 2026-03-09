import pygame
from random import randint

# Khởi tạo Pygame
pygame.init()

# Thiết lập cửa sổ
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

# Màu sắc
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Nhạc nền
pygame.mixer.music.load(r"C:\lap_trinh\laptrinhpython\Tuan_12_Pygame\SieuNhanCuongPhong-Takeshi-4341647.mp3")
pygame.mixer.music.play()

# Tải ảnh và font
img = pygame.image.load(r"C:\lap_trinh\laptrinhpython\Tuan_12_Pygame\anh.jpg")
font = pygame.font.SysFont("sans", 30)

# Tạo text
text = font.render("NGUUU", True, BLACK)
text_box = text.get_rect()
random_pos = (100, 100)

# Bắt đầu vòng lặp game
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # Hiển thị ảnh
    screen.blit(img, (0, 0))

    # Vẽ chữ "NGUUU"
    pygame.draw.rect(screen, GREEN, (random_pos[0], random_pos[1], text_box.width, text_box.height))
    screen.blit(text, random_pos)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left")
            elif event.button == 3:
                print("Right")
            elif event.button == 2:
                print("Middle")
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == 1074741904:
                print("Key press Left")
    # Cập nhật màn hình
    pygame.display.flip()

# Thoát game
pygame.quit()
