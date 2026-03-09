# phạm ngọc công 24119116
import numpy as np
import matplotlib.pyplot as plt

a=float(input("Nhập hệ số a: "))
b=float(input("Nhập hệ số b: "))
c=float(input("Nhập hệ số c: "))
denta=b**2-4*a*c
if denta<0:
    print("Phương trình vô nghiệm")
elif denta>0:
    print("Phương trình có 2 nghiệm")
    x=np.linspace(-50,50,1000)
    y=(a*(x**2)+b*x+c)

    plt.plot(x,y,label="a*(x**2)+b*x+c", color="red")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Biểu đồ phương trình bậc 2 có 2 nghiệm ")
    plt.legend()
    plt.show()
else:
    print("Phương trình có nghiệm kép")

