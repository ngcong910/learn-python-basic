import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2*np.pi,2*np.pi,100)

y_sin=np.sin(x)
y_cos=np.cos(x)

# vẽ đồ thị 
plt.plot(x,y_sin,label="y=sin(x)",color="red")
plt.plot(x,y_cos,label="y=cos(x)",color="blue")
plt.title("Biểu đồ hình sin và cos")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()