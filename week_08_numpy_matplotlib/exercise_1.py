import numpy as np
import matplotlib.pyplot as plt

a=int(input("Nhập hệ số a: "))
b=int(input("Nhập hệ số b: "))
x=np.linspace(-20,20,100)
y=a*x+b

# vẽ biểu đồ 
plt.plot(x,y,color="blue",label="y=a*x+b")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Phương trình bậc nhất")
plt.show()