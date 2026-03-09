import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r'C:\lap_trinh\laptrinhpython\Tuan10_Anh\yellowlily.jpg')
image_hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
H,S,V=cv2.split(image_hsv)
gray = 0.299 * H + 0.587 * S + 0.114 * V
gray = gray.astype(np.uint8)

# Hiển thị ảnh hsv
plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.axis("off")
plt.title("Ảnh hsv (tự tính)")

image_YCbCr=cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
Y,Cr,Cb=cv2.split(image_YCbCr)
gray = 0.299 * Y + 0.587 * Cb + 0.114 * Cr
gray = gray.astype(np.uint8)

# Hiển thị ảnh Ycbcr
plt.subplot(1,2,2)
plt.imshow(gray, cmap='gray')
plt.axis("off")
plt.title("Ảnh hsv (tự tính)")


plt.show()

