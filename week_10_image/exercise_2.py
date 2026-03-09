import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r'C:\lap_trinh\laptrinhpython\Tuan10_Anh\yellowlily.jpg')
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
R,G,B=cv2.split(image_rgb)
gray = 0.299 * R + 0.587 * G + 0.114 * B
gray = gray.astype(np.uint8)

# Hiển thị ảnh xám
plt.imshow(gray, cmap='gray')
plt.axis("off")
plt.title("Ảnh xám (tự tính)")
plt.show()