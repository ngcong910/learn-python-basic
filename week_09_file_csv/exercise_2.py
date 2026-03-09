import csv # tao thu vien csv

headline=["Name","Age"]
body=[{"Name": "Ngoc_Cong", "Age": 18},
    {"Name": "Tan_Tai", "Age": 31},
    {"Name": "Gia_Huy", "Age": 35}]

with open ("data.csv","w",newline="",encoding="utf-8") as file:
    write=csv.DictWriter(file,fieldnames=headline)
    write.writeheader()
    write.writerows(body)

with open("data.csv","r",encoding="utf-8") as file:
    reader=csv.DictReader(file)
    count=0 # cho đếm bằng 0    
    people=[] # tạo list rỗng   
    for row in body:
        if float(row["Age"])>30: # nếu age lớn hơn 30   
            count+=1 # count tăng 1
            people.append(row["Name"]) # thêm tên vào danh sách
    print(f"Co {count}  lon hon 30.  ")        
    print("Nhung nguoi do ten la:" )
    print(people)
        
