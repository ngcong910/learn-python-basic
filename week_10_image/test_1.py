# doc anh 
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

image=cv2.imread('C:\lap_trinh\laptrinhpython\Tuan10_Anh\yellowlily.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Ngoc_Cong_Hoi_Nho")
 # tat truc tao do
plt.show()

#tach kenh cac mau-------------------------------------------
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
img_array=np.array(image_rgb)

#cach_1
#R=img_array[:,:,0]
#G=img_array[:,:,1]
#B=img_array[:,:,2]

#cach_2
R,G,B=cv2.split(image_rgb)
plt.subplot(4,4,1)
plt.imshow(R,cmap='Reds')
plt.title('R channel')
plt.axis('off')

plt.subplot(4,4,2)
plt.imshow(G,cmap="Greens")
plt.title("G channel")
plt.axis('off')

plt.subplot(4,4,3)
plt.imshow(B, cmap='Blues')
plt.title('B channel')
plt.axis("off")# tat truc tao do


#gop kenh cac mau lai--------------------------------
#cach_1
merged_image=np.stack((R,G,B),axis=2)
plt.subplot(4,4,4)
plt.imshow(merged_image)
plt.title('RGB imnage')
plt.axis("off")


#cach_2
merged_image=cv2.merge([R,G,B])
plt.subplot(4,4,5)
plt.imshow(merged_image)
plt.title("Gray Imege")
plt.axis("off")


# chuyen anh mau sanh anh den trang--------------------
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.subplot(4,4,6)
plt.imshow(gray,cmap='gray')
plt.title("Gray Image")
plt.axis("off")


#Cat_anh--------------------
cropped=image[400:1200,250:1000] # (y,x)
plt.subplot(4,4,7)
plt.imshow(cv2.cvtColor(cropped,cv2.COLOR_BGR2RGB))
plt.title("Cropped image")
plt.axis("off")

#cv2.imwrite("Save cropped image",cropped) # luu anh 

# thay doi kich thuoc anh--------

##resized=cv2.resize(image,(200,200))
#plt.imshow(cv2.cvtColor(resized),cv2.COLOR_BGR2RGB)
#plt.title("Resized image")
#plt.axis("off")
#

# lam mo hinh anh--------------
blurred=cv2.GaussianBlur(image,(51,51),51)
plt.subplot(4,4,8)
plt.imshow(cv2.cvtColor(blurred,cv2.COLOR_BGR2RGB))
plt.title("Blurred image")
plt.axis("off")


#tang cuong do sang cua anh 
#factor=1.5
#brightened=np.clip(image*factor,0,255).astype(np.uint8)
#plt.imshow(cv2.cvtColor(brightened,cv2.COLOR_BGR2RGB))
#plt.title("Enhanced image")
#plt.axis("off")
#plt.show

# them nhieu vao anh
plt.subplot(4,4,9)
resized=cv2.resize(gray,(200,200))
noise=np.random.randint(50,100,(200,200))
noisy_image=resized+noise
noisy_image=np.clip(noisy_image,0,255).astype(np.uint8)
plt.imshow(cv2.cvtColor(noisy_image,cv2.COLOR_BGR2RGB))
plt.title("Noisy image")
plt.axis("off")


# xoa nhieu
plt.subplot(4,4,10)
denoised_gaussian=cv2.GaussianBlur(noisy_image,(5,5),0)
denoised_blur=cv2.blur(noisy_image,(5,5))
plt.imshow(cv2.cvtColor(denoised_blur,cv2.COLOR_BGR2RGB))
plt.title("Dinoisef iamge")
plt.axis("off")

#hien thi toan bo 
plt.show()

# ve histogram cua anh 
gray_array=np.array(gray).flatten() # doi anh 2 chieu sang 1 chieu
plt.hist(gray_array,bins=256,color="Red")
plt.title("Histogram anh den trang")
plt.xlabel("Gia tri diem anh (0-255)")
plt.ylabel("Tan Xuat")
plt.grid(True)
plt.tight_layout()
plt.show()

