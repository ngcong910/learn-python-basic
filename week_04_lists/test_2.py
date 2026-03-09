colors=["green","red","blue","red"]
print(colors)
try:
    print(colors.index("red"))
except:
    print("not exist")
#tra ve 2 la vi tri dau tien cua "red"

colors=["green","red","blue","red"]
print(colors)
try:
    print(colors.count("red"))
except:
    print("not exist")
#dem coi "red" xuat hien bao nhieu lan

# dem red khong can count
colors=["green","red","blue","red"]
print(colors)
k=0
for i in range(len(colors)):
    if colors[i]=="red":
        print("Tai vi tri ",i)
        k+=1
print("So lan suat hien (red)",k)
# cach 1
colors=["green","red","blue","red"]
red_index=[]
for i in range(len(colors)):
    if colors[i]=="red":
        red_index.append(i)
print(len(red_index))
#cach 2 