import csv   # tao thu vien file csv
fields=["Name","point","Score"] # tao ten 
rows=[{"Name":"Ngoc Cong","point":18,"Score":9},
      {"Name":"Tai","point":8,"Score":90}]

with open("output.csv",mode="w",newline="",encoding="utf-8")as file: # viet file
    writer=csv.DictWriter(file,fieldnames=fields) 
    writer.writeheader()
    writer.writerows(rows)

with open("output.csv","r",encoding="utf-8")as file:
    reader=csv.DictReader(file)
    count=0 # cho bien dem bang khong
    for row in reader:
        count+=1 # moi lan qua 1 dong thi dem tăng 1    
        if float(row["Score"])>=85: # nếu Score>85 thì in ra điều kiện
            print("Dong có 'Score' lớn hơn 85 là: ",count)