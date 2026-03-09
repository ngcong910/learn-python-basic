import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100,1000)
y=np.cos(x)

plt.plot(x,y,label="cos(x)",color="black",linestyle="-.") # muốn nét liền thì bỏ linestyle
plt.xlabel("X-axis") # hiển thị đường x
plt.ylabel("Y-axis") # hiển thị đường y
plt.title("Biêu đồ đường cos") 
plt.legend() # đọc tên đường của hình gì 
plt.show() # hiển thị ảnh
