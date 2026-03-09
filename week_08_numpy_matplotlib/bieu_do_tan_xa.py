import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(50)
y=np.random.rand(50)

plt.scatter(x,y,color="blue", marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter chart")
plt.legend()
plt.show()