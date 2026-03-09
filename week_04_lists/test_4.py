##file=open("data.txt","r")
#data=file.read()
#print(data)

#words=text.split(" ",3)
#print(words)
colors = ["red", "blue", "red", "green", "red", "yellow"]
red_index=[]
for i in range(len(colors)):
    if colors[i]=="red":
        red_index.append(colors[i])
print((red_index))