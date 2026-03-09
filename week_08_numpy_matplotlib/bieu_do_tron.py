import matplotlib.pyplot as plt

labels=['Apple','Samsung','Xiaomi','Oppo']
sizes=[40,30,20,10]

plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("Phones market")
plt.show()