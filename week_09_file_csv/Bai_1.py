import csv 

headline=["Name","Sex","Age","Point","Average"] # tao tieu de

with open("file.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file) # ghi file
    writer.writerow(headline) # ghi tieu de
    while True: # cho true
        name=input("Vui long nhap tên: ") # nhap ten
        if name=="stop": # neu dung stop thi out 
            break
        sex=input("Vui long nhap gioi tinh: ").lower()
        age=input("Vui long nhap tuoi: ")
        point=input("Vui long nhap diem: ")
        aver=input("Vui long nhap diem trung binh: ")
        writer.writerow([name,sex,age,point,aver])
        print("\n")
        print("Da nhap xong \n")

