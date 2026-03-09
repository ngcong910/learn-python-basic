# a
import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r'C:\lap_trinh\laptrinhpython\Tuan10_Anh\yellowlily.jpg')
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.subplot(2,2,1)
plt.imshow(image_rgb)
plt.axis("off")
plt.title("Anh goc")

R,G,B=cv2.split(image_rgb)

# channel R
plt.subplot(2,2,2)
plt.imshow(R,cmap="Reds")
plt.axis("off")
plt.title("Channel R ")

# channel G
plt.subplot(2,2,3)
plt.imshow(G,cmap="Greens")
plt.axis("off")
plt.title("Channel G ")

# channel B
plt.subplot(2,2,4)
plt.imshow(B,cmap="Blues")
plt.axis("off")
plt.title("Channel B ")

plt.show()

#b

# chuyen anh xam
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_gray=np.array(gray_image).flatten()
plt.subplot(2,2,1)
plt.hist(image_gray)
plt.xlabel("Anh xam")
plt.ylabel("Tan xuat")
plt.title("Gray_image")

channel_R=np.array(R).flatten()
plt.subplot(2,2,2)
plt.hist(channel_R)
plt.xlabel("Anh xam")
plt.ylabel("Tan xuat")
plt.title("R_image")

channel_G=np.array(G).flatten()
plt.subplot(2,2,3)
plt.hist(channel_G)
plt.xlabel("Anh xam")
plt.ylabel("Tan xuat")
plt.title("G_image")

channel_B=np.array(B).flatten()
plt.subplot(2,2,4)
plt.hist(channel_B)
plt.xlabel("Anh xam")
plt.ylabel("Tan xuat")
plt.title("B_image")

plt.show()
