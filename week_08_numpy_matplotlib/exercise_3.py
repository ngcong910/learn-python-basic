import numpy as np
import matplotlib.pyplot as plt

arr=np.random.randint(0,226,size=(20,30))
dieu_kien=arr<200
result=np.sum(dieu_kien) # nếu dieu kien đúng thì True+1
location=np.argwhere(dieu_kien) # nếu thỏa điều kiện thì lấy vị trí

# vẽ hình 
plt.hist(arr.ravel(),bins=30,color="black",edgecolor="blue",label=("Biểu đồ theo điều kiện"))
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Biểu đồ histogram")
plt.legend()
plt.show()
