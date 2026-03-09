import matplotlib.pyplot as plt
labels=["A","B","C","D"]
values=[10,20,15,25]

plt.bar(labels,values,color=["red","blue","green","purple"])
plt.xlabel("Class")
plt.ylabel("Value")
plt.title("Bar chart")
plt.show()