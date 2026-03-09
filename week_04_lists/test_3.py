#file=open("data.txt","w")
#file.write("welcom to Pham Ngoc Cong\n")
#file.close()

#file=open("data.txt","w")
#file.write("Pham Ngoc Cong\n")
#file.close()
# cach 2
#with open ("data.txt","a") as file:
#    file.write("Yeu thu huyen qua ta\n")
#    file.write("Thu huyen la daucute\n")
##copy 
#with open("data.txt","r") as file:
#    data=file.read()
#    print(data)#

#with open("data.txt","r") as file1:
#    content=file1.read()#

#with open("copy.txt","w") as file2:
#    file2.write(content)
#print("DONE")

with open("data.txt","w",encoding="utf-8") as file:
    while True:
        line=input("Nhap dong ( hoac go STOP de dung): ")
        if line=="STOP":
            break
        file.write(line+"\n")# ghi vao file va xuong dong
print("Du lieu da ghi vao file data.txt")
#with open("data.txt","r") as file: # coi có bao nhiêu dòng 
#    lines=file.readlines()
#print(lines)

keyword=input("Nhập từ cần tìm: ")
with open("data.txt","r",encoding="utf-8") as file: # encoding="utf-8" cho phep go tieng viet
    content=file.read()
if keyword in content:
    print(f"Tu '{keyword}' co trong file.")
else:
    print(f"Tu '{keyword}' khong co trong file")