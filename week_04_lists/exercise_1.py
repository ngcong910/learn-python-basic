#Pham Ngoc Cong_24119116
with open("data.txt","w") as file:
    a=int(input("Nhap 1 so nguyen N: "))
    for i in range(a,0,-1):
        file.write(str(i)+"\n")
with open("data.txt","r") as file:
    line=file.readlines()
    for i in range(len(line)):
        print(f"Dong {i+1}: {line[i].strip()}")
